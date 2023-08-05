# -*- coding: utf-8 -*-
#
# Copyright 2015 European Commission (JRC);
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl

"""
It provides CO2MPAS schema parse/validator.
"""

import logging
from collections import Iterable, OrderedDict
import numpy as np
import pandas as pd
from lmfit import Parameters, Parameter
from schema import Schema, Use, And, Or, Optional, SchemaError
from sklearn.tree import DecisionTreeClassifier
from pprint import pformat
import co2mpas.dispatcher.utils as dsp_utl
import co2mpas.utils as co2_utl
from .validations import hard_validation
from co2mpas.model.physical.gear_box.at_gear import CMV, MVL, GSPV
from co2mpas.model.physical.electrics import Alternator_status_model

log = logging.getLogger(__name__)


def validate_data(data, soft_validation, read_schema=None):
    plan = validate_plan(data.get('plan', pd.DataFrame([])), read_schema)

    inputs = validate_inputs(data.get('base', {}), soft_validation, read_schema)
    inputs = {'.'.join(k): v
              for k, v in co2_utl.stack_nested_keys(inputs, depth=3)}

    return inputs, plan


def validate_inputs(data, soft_validation=False, read_schema=None):
    res, errors, validate = {}, {}, read_schema.validate
    for k, v in sorted(co2_utl.stack_nested_keys(data, depth=4)):
        d = co2_utl.get_nested_dicts(res, *k[:-1])
        _add_validated_input(d, validate, k, v, errors)

    if not soft_validation:
        for k, v in co2_utl.stack_nested_keys(res, depth=3):
            for c, msg in hard_validation(v):
                co2_utl.get_nested_dicts(errors, *k)[c] = SchemaError([], [msg])

    if _log_errors_msg(errors):
        return {}

    return res


def _add_validated_input(data, validate, keys, value, errors):
    try:
        k, v = next(iter(validate({keys[-1]: value}).items()))
        if v is not dsp_utl.NONE:
            data[k] = v
    except SchemaError as ex:
        co2_utl.get_nested_dicts(errors, *keys[:-1])[keys[-1]] = ex


def _log_errors_msg(errors):
    if errors:
        msg = ['\nInput cannot be parsed, due to:']
        for k, v in co2_utl.stack_nested_keys(errors, depth=4):
            msg.append('{} in {}: {}'.format(k[-1], '/'.join(k[:-1]), v))
        log.error('\n  '.join(msg))
        return True
    return False


def validate_plan(plan, read_schema=None):
    validated_plan, errors, validate = [], {}, read_schema.validate
    for i, data in plan.iterrows():
        inputs = {}
        data.dropna(how='all', inplace=True)
        plan_id = 'plan id:{}'.format(i[0])
        for k, v in data.items():
            k = (plan_id,) + tuple(k.split('.'))
            d = co2_utl.get_nested_dicts(inputs, '.'.join(k[1:-1]))
            _add_validated_input(d, validate, k, v, errors)

        validated_plan.append((i, inputs))

    if _log_errors_msg(errors):
        return []

    return validated_plan


class Empty(object):
    def __repr__(self):
        return '%s' % self.__class__.__name__

    @staticmethod
    def validate(data):
        if isinstance(data, str) and data == 'EMPTY':
            return dsp_utl.EMPTY

        try:
            empty = not (data or data == 0)
        except ValueError:
            empty = np.isnan(data).all()

        if empty:
            return dsp_utl.NONE
        else:
            raise SchemaError('%r is not empty' % data, None)


# noinspection PyUnusedLocal
def _function(error=None, read=True, **kwargs):
    def _check_function(f):
        assert callable(f)
        return f
    if read:
        error = error or 'should be a function!'
        return Use(_check_function, error=error)
    return _eval(And(_function(), Use(lambda x: dsp_utl.NONE), error=error))


# noinspection PyUnusedLocal
def _string(error=None, **kwargs):
    error = error or 'should be a string!'
    return Use(str, error=error)


# noinspection PyUnusedLocal
def _select(types=(), error=None, **kwargs):
    error = error or 'should be one of {}!'.format(types)
    types = {k.lower(): k for k in types}
    return And(str, Use(lambda x: types[x.lower()]), error=error)


def _check_positive(x):
    return x >= 0


# noinspection PyUnusedLocal
def _positive(type=float, error=None, **kwargs):
    error = error or 'should be as {} and positive!'.format(type)
    return And(Use(type), _check_positive, error=error)


# noinspection PyUnusedLocal
def _limits(limits=(0, 100), error=None, **kwargs):
    error = error or 'should be {} <= x <= {}!'.format(*limits)

    def _check_limits(x):
        return limits[0] <= x <= limits[1]

    return And(Use(float), _check_limits, error=error)


# noinspection PyUnusedLocal
def _eval(s, error=None, **kwargs):
    error = error or 'cannot be eval!'
    return Or(And(str, Use(lambda x: eval(x)), s), s, error=error)


# noinspection PyUnusedLocal
def _dict(format=None, error=None, read=True, **kwargs):
    format = format or {int: float}
    error = error or 'should be a dict with this format {}!'.format(format)
    c = Use(lambda x: {k: v for k, v in dict(x).items() if v is not None})
    if read:
        return _eval(Or(Empty(), And(c, Or(Empty(), format))), error=error)
    else:
        return And(_dict(format=format, error=error), Use(pformat))


# noinspection PyUnusedLocal
def _ordict(format=None, error=None, read=True, **kwargs):
    format = format or {int: float}
    msg = 'should be a OrderedDict with this format {}!'
    error = error or msg.format(format)
    c = Use(OrderedDict)
    if read:
        return _eval(Or(Empty(), And(c, Or(Empty(), format))), error=error)
    else:
        return And(_dict(format=format, error=error), Use(pformat))


def _check_length(length):
    if not isinstance(length, Iterable):
        length = (length,)

    def check_length(data):
        ld = len(data)
        return any(ld == l for l in length)

    return check_length


# noinspection PyUnusedLocal
def _type(type=None, error=None, length=None, **kwargs):
    type = type or tuple

    if length is not None:
        error = error or 'should be as {} and ' \
                         'with a length of {}!'.format(type, length)
        return And(_type(type=type), _check_length(length), error=error)
    if not isinstance(type, (Use, Schema, And, Or)):
        type = Or(type, Use(type))
    error = error or 'should be as {}!'.format(type)
    return _eval(type, error=error)


# noinspection PyUnusedLocal
def _index_dict(error=None, **kwargs):
    error = error or 'cannot be parsed as {}!'.format({int: float})
    c = {int: Use(float)}

    def f(x):
        return {k: v for k, v in enumerate(x, start=1)}

    return Or(c, And(_dict(), c), And(_type(), Use(f), c), error=error)


# noinspection PyUnusedLocal
def _np_array(dtype=None, error=None, read=True, **kwargs):
    dtype = dtype or float
    error = error or 'cannot be parsed as np.array dtype={}!'.format(dtype)
    if read:
        c = Use(lambda x: np.asarray(x, dtype=dtype))
        return Or(And(str, _eval(c)), c, And(_type(), c), Empty(), error=error)
    else:
        return And(_np_array(dtype=dtype), Use(lambda x: x.tolist()),
                   error=error)


# noinspection PyUnusedLocal
def _cmv(error=None, **kwargs):
    return _type(type=CMV, error=error)


# noinspection PyUnusedLocal
def _mvl(error=None, **kwargs):
    return _type(type=MVL, error=error)


# noinspection PyUnusedLocal
def _gspv(error=None, **kwargs):
    return _type(type=GSPV, error=error)


# noinspection PyUnusedLocal
def _dtc(error=None, read=True, **kwargs):
    if read:
        return _type(type=DecisionTreeClassifier, error=error)
    return And(_dtc(), Use(lambda x: dsp_utl.NONE), error=error)


def _parameters2str(data):
    if isinstance(data, Parameters):
        s = []
        for k, v in data.items():
            s.append("('%s', %s)" % (k, _parameters2str(v)))
        return 'Parameters(None, OrderedDict([%s]))' % ', '.join(s)
    elif isinstance(data, Parameter):
        d = [
            ('name', "'%s'" % data.name),
            ('vary', data.vary),
            ('max', data.max),
            ('min', data.min),
            ('expr', "'%s'" % data._expr if data._expr else 'None'),
            ('value', data._val)
        ]
        return 'Parameter(%s)' % ', '.join('%s=%s' % v for v in d)


def _parameters(error=None, read=True):
    if read:
        return _type(type=Parameters, error=error)
    else:
        return And(_parameters(), Use(_parameters2str), error=error)


# noinspection PyUnusedLocal
def _compare_str(s, **kwargs):
    return And(Use(str.lower), s.lower(), Use(lambda x: s))


def _convert_str(old_str, new_str, **kwargs):
    return And(Use(str), Or(old_str, new_str), Use(lambda x: new_str))


def _tyre_code(error=None, **kwargs):
    error = error or 'invalid tyre code!'
    from ..model.physical.wheels import _re_tyre_code_iso, _re_tyre_code_numeric
    c = Or(_re_tyre_code_iso.match, _re_tyre_code_numeric.match)
    return And(str, c, error=error)


def _tyre_dimensions(error=None, **kwargs):
    error = error or 'invalid format for tyre dimensions!'
    from ..model.physical.wheels import _format_tyre_dimensions
    return And(_dict(format=dict), Use(_format_tyre_dimensions), error=error)


def define_data_schema(read=True):
    cmv = _cmv(read=read)
    dtc = _dtc(read=read)
    gspv = _gspv(read=read)
    string = _string(read=read)
    positive = _positive(read=read)
    positive_int = _positive(type=int, read=read)
    limits = _limits(read=read)
    index_dict = _index_dict(read=read)
    np_array = _np_array(read=read)
    np_array_bool = _np_array(dtype=bool, read=read)
    np_array_int = _np_array(dtype=int, read=read)
    _bool = _type(type=bool, read=read)
    function = _function(read=read)
    tuplefloat2 = _type(
            type=And(Use(tuple), (_type(float),)),
            length=2,
            read=read
    )
    tuplefloat = _type(type=And(Use(tuple), (_type(float),)), read=read)
    dictstrdict = _dict(format={str: dict}, read=read)
    ordictstrdict = _ordict(format={str: dict}, read=read)
    parameters = _parameters(read=read)
    dictstrfloat = _dict(format={str: Use(float)}, read=read)
    dictstrtuple = _dict(format={str: tuple}, read=read)
    tyre_code = _tyre_code(read=read)
    tyre_dimensions = _tyre_dimensions(read=read)

    schema = {
        _compare_str('CVT'): function,
        _compare_str('CMV'): cmv,
        _compare_str('CMV_Cold_Hot'): _dict(format={'hot': cmv, 'cold': cmv},
                                            read=read),
        _compare_str('DT_VA'): dtc,
        _compare_str('DT_VAP'): dtc,
        _compare_str('DT_VAT'): dtc,
        _compare_str('DT_VATP'): dtc,
        _compare_str('GSPV'): gspv,
        _compare_str('GSPV_Cold_Hot'): _dict(format={'hot': gspv, 'cold': gspv},
                                             read=read),
        _compare_str('MVL'): _mvl(read=read),

        _compare_str('VERSION'): string,
        'lock_up_tc_limits': tuplefloat2,
        'tyre_dimensions': tyre_dimensions,
        'tyre_code': tyre_code,
        'wltp_base_model': _dict(format=dict, read=read),
        'fuel_type': _select(types=('gasoline', 'diesel', 'LPG', 'NG',
                                    'ethanol', 'biodiesel'), read=read),
        'engine_fuel_lower_heating_value': positive,
        'fuel_carbon_content': positive,
        'engine_capacity': positive,
        'engine_stroke': positive,
        'engine_max_power': positive,
        'engine_max_speed_at_max_power': positive,
        'engine_max_speed': positive,
        'engine_max_torque': positive,
        'idle_engine_speed_median': positive,
        'engine_idle_fuel_consumption': positive,
        'final_drive_ratio': positive,
        'r_dynamic': positive,
        'wltp_class': _select(types=('class1', 'class2', 'class3a', 'class3b'),
                              read=read),
        'downscale_phases': tuplefloat,
        'gear_box_type': _select(types=('manual', 'automatic', 'cvt'),
                                 read=read),
        'ignition_type': _select(types=('positive', 'compression'), read=read),
        'start_stop_activation_time': positive,
        'alternator_nominal_voltage': positive,
        'battery_capacity': positive,
        'state_of_charge_balance': limits,
        'state_of_charge_balance_window': limits,
        'initial_state_of_charge ': limits,
        'idle_engine_speed_std': positive,
        'alternator_nominal_power': positive,
        'alternator_efficiency': _limits(limits=(0, 1), read=read),
        'time_cold_hot_transition': positive,
        'co2_params': dictstrfloat,
        'willans_factors': dictstrfloat,
        'phases_willans_factors': _type(
            type=And(Use(tuple), (dictstrfloat,)), read=read),
        'optimal_efficiency': dictstrtuple,
        'velocity_speed_ratios': index_dict,
        'gear_box_ratios': index_dict,
        'speed_velocity_ratios': index_dict,
        'full_load_speeds': np_array,
        'full_load_torques': np_array,
        'full_load_powers': np_array,

        'vehicle_mass': positive,
        'f0_uncorrected': positive,
        'f2': positive,
        'f0': positive,
        'correct_f0': _bool,

        'co2_emission_low': positive,
        'co2_emission_medium': positive,
        'co2_emission_high': positive,
        'co2_emission_extra_high': positive,

        _compare_str('co2_emission_UDC'): positive,
        _compare_str('co2_emission_EUDC'): positive,
        'co2_emission_value': positive,
        'n_dyno_axes': positive_int,
        'n_wheel_drive': positive_int,

        'engine_is_turbo': _bool,
        'has_start_stop': _bool,
        'has_energy_recuperation': _bool,
        'use_basic_start_stop': _bool,
        'is_hybrid': _bool,
        'engine_has_variable_valve_actuation': _bool,
        'has_thermal_management': _bool,
        'engine_has_direct_injection': _bool,
        'has_lean_burn': _bool,
        'has_sufficient_power': _bool,
        'engine_has_cylinder_deactivation': _bool,
        'has_exhausted_gas_recirculation': _bool,
        'has_particle_filter': _bool,
        'has_selective_catalytic_reduction': _bool,
        'has_nox_storage_catalyst': _bool,
        'has_torque_converter': _bool,
        'is_cycle_hot': _bool,
        'use_dt_gear_shifting': _bool,
        _convert_str('eco_mode', 'fuel_saving_at_strategy'): _bool,
        'correct_start_stop_with_gears': _bool,
        'enable_phases_willans': _bool,
        'enable_willans': _bool,

        'alternator_charging_currents': tuplefloat2,
        'alternator_current_model': function,
        'alternator_status_model': function,
        'clutch_model': function,
        'co2_emissions_model': function,
        'co2_error_function_on_emissions': function,
        'co2_error_function_on_phases': function,
        'cold_start_speed_model': function,
        'clutch_window': tuplefloat2,
        'co2_params_calibrated': parameters,
        'co2_params_initial_guess': parameters,
        'cycle_type': string,
        'cycle_name': string,
        'specific_gear_shifting': string,
        'calibration_status': _type(type=And(Use(list),
                                             [(bool, Or(parameters, None))]),
                                    length=4,
                                    read=read),
        'electric_load': tuplefloat2,
        'engine_thermostat_temperature_window': tuplefloat2,
        'engine_temperature_regression_model': function,
        'electrics_model': function,
        'engine_type': string,
        'full_load_curve': function,
        'gear_box_efficiency_constants': dictstrdict,
        'gear_box_efficiency_parameters_cold_hot': dictstrdict,
        'model_scores': dictstrdict,
        'scores': dictstrdict,
        'at_scores': ordictstrdict,

        'fuel_density': positive,
        'idle_engine_speed': tuplefloat2,
        'k1': positive_int,
        'k2': positive_int,
        'k5': positive_int,
        'max_gear': positive_int,

        'road_loads': _type(type=And(Use(tuple), (_type(float),)),
                            length=3,
                            read=read),
        'start_stop_model': function,
        'gear_box_temperature_references': tuplefloat2,
        'torque_converter_model': function,
        'phases_co2_emissions': tuplefloat,
        'phases_integration_times':
            _type(type=And(Use(tuple), (And(Use(tuple), (_type(float),)),)),
                  read=read),
        'extended_phases_co2_emissions': tuplefloat,
        'extended_phases_integration_times':
            _type(type=And(Use(tuple), (And(Use(tuple), (_type(float),)),)),
                  read=read),
        'extended_integration_times': tuplefloat,
        'phases_fuel_consumptions': tuplefloat,

        'accelerations': np_array,
        'alternator_currents': np_array,
        'alternator_powers_demand': np_array,
        'alternator_statuses': np_array_int,
        'auxiliaries_power_losses': np_array,
        'auxiliaries_torque_loss': positive,
        'auxiliaries_torque_losses': np_array,
        'battery_currents': np_array,
        'clutch_tc_powers': np_array,
        'clutch_tc_speeds_delta': np_array,
        'co2_emissions': np_array,
        'cold_start_speeds_delta': np_array,
        'engine_coolant_temperatures': np_array,
        'engine_powers_out': np_array,
        'engine_speeds_out': np_array,
        'engine_speeds_out_hot': np_array,
        'engine_starts': np_array_bool,
        'co2_normalization_references': np_array,
        'final_drive_powers_in': np_array,
        'final_drive_speeds_in': np_array,
        'final_drive_torques_in': np_array,
        'fuel_consumptions': np_array,
        'gear_box_efficiencies': np_array,
        'gear_box_powers_in': np_array,
        'gear_box_speeds_in': np_array,
        'gear_box_temperatures': np_array,
        'gear_box_torque_losses': np_array,
        'gear_box_torques_in': np_array,
        'gear_shifts': np_array_bool,
        'gears': np_array_int,
        'identified_co2_emissions': np_array,
        'motive_powers': np_array,
        'on_engine': np_array_bool,
        'on_idle': np_array_bool,
        'state_of_charges': np_array,
        'times': np_array,
        'velocities': np_array,
        _compare_str('obd_velocities'): np_array,
        'wheel_powers': np_array,
        'wheel_speeds': np_array,
        'wheel_torques': np_array,
    }

    schema = {Optional(k): Or(Empty(), v) for k, v in schema.items()}
    schema[Optional(str)] = Or(_type(type=float, read=read), np_array)

    if not read:

        def f(x):
            return x is dsp_utl.NONE

        schema = {k: And(v, Or(f, Use(str))) for k, v in schema.items()}

    return Schema(schema)
