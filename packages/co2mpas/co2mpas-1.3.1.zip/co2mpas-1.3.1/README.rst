.. image:: doc/_static/CO2MPAS_banner.png
   :align: left
.. _start-opening:

######################################################################
|co2mpas|: Vehicle simulator predicting NEDC |CO2| emissions from WLTP
######################################################################

:Release:       1.3.1
:Date:          2016-07-18 20:37:01
:Home:          http://co2mpas.io/
:Releases:      http://files.co2mpas.io/
:Sources:       https://github.com/JRCSTU/co2mpas
:pypi-repo:     https://pypi.python.org/pypi/co2mpas
:Keywords:      CO2, fuel-consumption, WLTP, NEDC, vehicle, automotive,
                EU, JRC, IET, STU, back-translation, policy, monitoring, M1, N1,
                simulator, engineering, scientific
:Developers:    .. include:: AUTHORS.rst
:Copyright:     2015-2016 European Commission (`JRC-IET
                <https://ec.europa.eu/jrc/en/institutes/iet>`_)
:License:       `EUPL 1.1+ <https://joinup.ec.europa.eu/software/page/eupl>`_

|co2mpas| is backward-looking longitudinal-dynamics |CO2| and
fuel-consumption simulator for light-duty M1 & N1 vehicles (cars and vans),
specially crafted to back-translate consumption figures from WLTP cycles
into NEDC ones, according to the *EU* legislation.

It is an open-source project developed with Python-3.4+,
using Anaconda & WinPython under Windows 7, Anaconda under MacOS, and
Linux's standard python environment.
It runs as a *console command* consuming (mostly) excel-files with input-data.

History
=======
The *European Commission* is supporting the introduction of the *WLTP cycle*
for Light-duty vehicles developed at the *United Nations (UN/ECE)*
level, in the shortest possible time-frame. Its introduction requires
the adaptation of |CO2| certification and monitoring procedures set
by European regulations. European Commission's *Joint Research Centre (JRC)*
has been assigned the development of this vehicle simulator to facilitate this
adaptation.

For recent activity, check the :doc:`changes`.


Quickstart
==========
.. Tip::
    **About console-commands appearing in the examples of the documentation:**

    - Console-commands beginning with ``$`` symbol are for the ``bash`` shell
      (UNIX).
      You can install it on *Windows* with **cygwin**: https://www.cygwin.com/
      along with these useful utilities::

        * git, git-completion
        * make, zip, unzip, bzip2, 7z, dos2unix
        * openssh, curl, wget

    - Console-commands beginning with ``>`` symbol are for *Windows* ``cmd.exe``
      command-prompt.
      You can augment it with bash-like capabilities using **Clink**:
      http://mridgers.github.io/clink/

    - You can adapt commands between the two shells with minor modifications
      (i.e. ``ls <--> dir``, ``rm -r <--> rmdir /s/q``).

    - You may download and install the *all-in-one* archive which contains
      both shells configured in a console supporting decent copy-paste and
      resizing capabilities (see :ref:`all-in-one`).

IF you are familiar with python, AND
IF you already have a full-blown *python-3 environment*
(i.e. *Linux* or the *all-in-one* archive), AND
IF you have familiarity with v1 release, THEN
you can immediately start working with the following *bash* commands;
otherwise follow the detailed instructions under sections :ref:`install` and
:ref:`usage`.

.. code-block:: console

    ## Install co2mpas.
    ## NOTE: If behind proxy, specify additionally this option:
    ##    --proxy http://user:password@yourProxyUrl:yourProxyPort
    ##
    $ pip install co2mpas

    ## Where to store input and output files.
    ## In *Windows* cmd-prompt use `md` command instead.
    $ mkdir input output

    ## Create a template excel-file for inputs.
    $ co2mpas template input/vehicle_1.xlsx

    ###################################################
    ## Edit generated `./input/vehicle_1.xlsx` file. ##
    ###################################################

    ## Run simulator.
    $ co2mpas batch  input -O output

    ###################################################
    ## Inspect generated results inside `./output/`. ##
    ###################################################


.. _end-opening:
.. contents:: Table of Contents
  :backlinks: top
  :depth: 4


.. _install:

Install
=======
These are the installation options:

A. On *Windows* you may install the latest *all-In-One* archive and
   ensure it contains (or upgrade to) the latest ``co2mpas`` python package;
   alternatively, you may perform the following 2 steps.

   .. Tip::
      **This is the easiest procedure for all non-technical users.**

B. Manually install everything needed:
   1. Install (or Upgrade) Python (2 choices under *Windows*), then proceed to
   2. install the ``co2mpas`` python package:

     a. Install (or Upgrade) executable.
     b. (optional) Install documents.
     c. (optional) Install sources.



.. _all-in-one:

*All-In-One* Installation under Windows
---------------------------------------
- Download **all-in-one archive** from http://files.co2mpas.io/
  (it only runs on **64bit PCs**).

  .. Tip::
     Search in older releases if the latest does not contain an ALLINONE archive,
     ansd remember to upgrade |co2mpas| afterwords.


- Use the original `"7z" extraxtor <http://portableapps.com/apps/utilities/7-zip_portable>`_,
  since "plain-zip" produces out-of-memory errors when expanding long
  directories.

  .. Note::
     Prefer to **extract it in a folder without any spaces in its path.**
  .. image:: _static/Co2mpasALLINONE-Extract.gif
   :scale: 75%
   :alt: Extract Co2mpas-ALLINONE into Desktop
   :align: center

- Run ``INSTALL.bat`` script contained in the root of the unzipped folder.
  It will install links for commons |co2mpas| tasks under your *Windows*
  Start-Menu.

  .. image:: _static/Co2mpasALLINONE-InstallShortcuts.gif
   :scale: 75%
   :alt: Install Co2mpas-ALLINONE shortcupts into Window Start-menu.
   :align: center

- Use *Windows start-menu* to launch |co2mpas| CONSOLE or the GUI dialog-boxes.

  .. image:: _static/Co2mpasALLINONE-LaunchConsoleShortcut.gif
   :scale: 75%
   :alt: Launch CO2MPAS from Window Start-menu.
   :align: center


- Visit the guidelines for its usage: :doc:`allinone`
  (also contained within the archive).

.. Note::
    If you have downloaded an *all-in-one* from previous version of |co2mpas|
    you may upgrade |co2mpas| contained within.
    Follow the instructions in the "Upgrade" section, below.


Python Installation
-------------------
If you already have a suitable python-3 installation with all scientific
packages updated to their latest versions, you may skip this 1st stage.

.. Note::
    **Installing Python under Windows:**

    The program requires CPython-3, and depends on *numpy*, *scipy*, *pandas*,
    *sklearn* and *matplotlib* packages, which depend on C-native backends
    and need a C-compiler to install from sources.

    In *Windows* it is strongly suggested **NOT to install the standard CPython
    distribution that comes up first(!) when you google for "python windows"**,
    unless you are an experienced python-developer, and you know how to
    hunt down pre-compiled dependencies from the *PyPi* repository and/or
    from the `Unofficial Windows Binaries for Python Extension Packages
    <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.

    Therefore we suggest that you download one of the following two
    *scientific-python* distributions:

      #. `WinPython <https://winpython.github.io/>`_ **python-3** (64 bit)
      #. `Anaconda <http://continuum.io/downloads>`_ **python-3** (64 bit)



Install WinPython
~~~~~~~~~~~~~~~~~
The *WinPython* distribution is just a collection of the standard pre-compiled
binaries for *Windows* containing all the scientific packages, and much more.
It is not update-able, and has a quasi-regular release-cycle of 3 months.


1. Install the latest **python-3.4+  64 bit** from https://winpython.github.io/.
   Prefer an **installation-folder without any spaces leading to it**.

2. Open the WinPython's command-prompt console, by locating the folder where
   you just installed it and run (double-click) the following file::

        <winpython-folder>\"WinPython Command Prompt.exe"


3. In the console-window check that you have the correct version of
   WinPython installed, and expect a similar response:

   .. code-block:: console

        > python -V
        Python 3.4.3

        REM Check your python is indeed where you installed it.
        > where python
        ....


4. Use this console and follow :ref:`install-co2mpas-package` instructions, below.



Install Anaconda
~~~~~~~~~~~~~~~~
The *Anaconda* distribution is a non-standard Python environment that
for *Windows* containing all the scientific packages we need, and much more.
It is not update-able, and has a semi-regular release-cycle of 3 months.

1. Install Anaconda **python-3.4+ 64 bit** from http://continuum.io/downloads.
   Prefer an **installation-folder without any spaces leading to it**.

   .. Note::
        When asked by the installation wizard, ensure that *Anaconda* gets to be
        registered as the default python-environment for the user's account.

2. Open a *Windows* command-prompt console::

        "windows start button" --> `cmd.exe`

3. In the console-window check that you have the correct version of
   Anaconda-python installed, by typing:

   .. code-block:: console

        > python -V
        Python 3.4.3 :: Anaconda 2.3.0 (64-bit)

        REM Check your python is indeed where you installed it.
        > where python
        ....

4. Use this console and follow :ref:`install-co2mpas-package` instructions, below.


.. _install-co2mpas-package:

Install ``co2mpas`` package
---------------------------
1. Install |co2mpas| executable internally into your python-environment with
   the following console-commands (there is no prob if the 1st `uninstall`
   command fails):

   .. code-block:: console

        > pip uninstall co2mpas
        > pip install co2mpas
        Collecting co2mpas
        Downloading http://pypi.co2mpas.io/packages/co2mpas-...
        ...
        Installing collected packages: co2mpas
        Successfully installed co2mpas-1.3.1

   .. Warning::
        **Installation failures:**

        The previous step require http-connectivity for ``pip`` command to
        Python's "standard" repository (https://pypi.python.org/) and to
        co2mpas-site (http://files.co2mpas.io).
        In case you are behind a **corporate proxy**, you may try one of the methods
        described in section `Alternative installation methods`_, below.

        If all methods to install |co2mpas| fail, re-run ``pip`` command adding
        extra *verbose* flags ``-vv``, copy-paste the console-output, and report it
        to JRC.

2. Check that when you run ``co2mpas``, the version executed is indeed the one
   installed above (check both version-identifiers and paths):

   .. code-block:: console

       > co2mpas -vV
       co2mpas_version: 1.3.1
       co2mpas_rel_date: 2016-07-18 20:37:01
       co2mpas_path: d:\co2mpas_ALLINONE-64bit-v1.3.1\Apps\WinPython\python-3.4.3\lib\site-packages\co2mpas
       python_path: D:\co2mpas_ALLINONE-64bit-v1.3.1\WinPython\python-3.4.3
       python_version: 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 XXX]
       PATH: D:\co2mpas_ALLINONE-64bit-v1.3.1\WinPython...


   .. Note::
       The above procedure installs the *latest* |co2mpas|, which
       **might be more up-to-date than the version described here!**

       In that case you can either:

       a) Visit the documents for the newer version actually installed.
       b) "Pin" the exact version you wish to install with a ``pip`` command
          (see section below).


Install extras
~~~~~~~~~~~~~~
Internally |co2mpas| uses an algorithmic scheduler to execute model functions.
In order to visualize the *design-time models* and *run-time workflows*
you need to install the **Graphviz** visualization library  from:
http://www.graphviz.org/.

If you skip this step, the ``modelgraph`` sub-command and the ``--plot-workflow``
option would both fail to run (see :ref:`debug`).



Upgrade |co2mpas| (with internet connectivity)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Uninstall (see below) and re-install it.


Uninstall |co2mpas|
~~~~~~~~~~~~~~~~~~~
To uninstall |co2mpas| type the following command, and confirm it with ``y``:

.. code-block:: console

    > pip uninstall co2mpas
    Uninstalling co2mpas-<installed-version>
    ...
    Proceed (y/n)?


Re-run the command *again*, to make sure that no dangling installations are left
over; disregard any errors this time.


Alternative installation methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You may get multiple versions of |co2mpas|, from various places, but all
require the use of ``pip`` command from a *console* to install:

..  Warning::
    In all cases below, remember to uninstall |co2mpas| if it's already installed.

- **Latest STABLE:**
  use the default ``pip`` described command above.

- **Latest PRE-RELEASE:**
  append the ``--pre`` option in the ``pip`` command.

- **Specific version:**
  modify the ``pip`` command like that, with optionally appending ``--pre``:

  .. code-block:: console

      pip install co2mpas==1.0.1 ... # Other options, like above.

- **Specific branch** from the GitHub-sources:

  .. code-block:: console

      pip install git+https://github.com/JRCSTU/co2mpas.git@dev

- **Specific commit** from the GitHub-sources:

  .. code-block:: console

      pip install git+https://github.com/JRCSTU/co2mpas.git@2927346f4c513a

- **Speed-up download**:
  append  the ``--use-mirrors`` option in the ``pip`` command.

- (for all of the above) When you are **behind an http-proxy**:
  append an appropriately adapted option
  ``--proxy http://user:password@yourProxyUrl:yourProxyPort``.

  .. Important::
      To avert any security deliberations for this http-proxy "tunnel",
      JRC *cryptographically signs* all *final releases* with one of those
      keys:
      - ``GPG key ID: 9CF277C40A8A1B08`` form @ankostis
      - ``GPG key ID: 1831F9C2294A33CC`` for @vinci1it2000

      Your IT staff may `validate their authenticity
      <https://www.davidfischer.name/2012/05/signing-and-verifying-python-packages-with-pgp/>`_
      and detect *man-in-the-middle* attacks, however impossible.

- (for all of the above) **Without internet connectivity** or when the above
  proxy cmd fails:

  1. With with a "regular" browser and when connected to the Internet,
     pre-download locally all files present in the ``packages`` folder
     located in the desired |co2mpas| version in the *|co2mpas| site*
     (e.g. http://files.co2mpas.io/CO2MPAS-1.3.1/packages/).

  2. Install *co2mpas*, referencing the above folder.
     Assuming that you downloaded the packages in the folder ``path/to/co2mpas_packages``,
     use a console-command like this:

     .. code-block:: console

        pip install co2mpas  --no-index  -f path/to/co2mpas_packages


Install Multiple versions in parallel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In order to run and compare results from different |co2mpas| versions,
you may use `virtualenv <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_
command.

The `virtualenv` command creates isolated python-environments ("children-venvs")
where in each one you can install a different versions of |co2mpas|.

.. Note::
    The `virtualenv` command does NOT run under the "conda" python-environment.
    Use the `conda command <http://conda.pydata.org/docs/using/envs.html>`_
    in similar manner to create child *conda-environments* instead.


1. Ensure `virtualenv` command installed in your "parent" python-environment,
   i.e the "WinPython" you use:

   .. code-block:: console

       > pip install virtualenv

   .. Note::
      The ``pip`` command above has to run only once for each parent python-env.
      If `virtualenv` is already installed, ``pip`` will exit gracefully.



2. Ensure co2mpas uninstalled in your parent-env:

   .. code-block:: console

       > pip uninstall co2mpas

   .. Warning::
     It is important for the "parent" python-env NOT to have |co2mpas| installed!
     The reason is that you must set "children venvs" to inherit all packages
     installed on their "parent" (i.e. `numpy` and `pandas`), and you cannot
     update any inherited package from within a child-env.


3. Move to the folder where you want your "venvs" to reside and create
   the "venv" with this command:

   .. code-block:: console

       > virtualenv --system-site-packages co2mpas_v1.0.1.venv.venv

   The ``--system-site-packages`` option instructs the child-venv to inherit
   all "parent" packages (numpy, pandas).

   Select a venv's  name to signify the version it will contains,
   e.g. ``co2mpas_v1.0.1.venv``.  The ``.venv`` at the end is not required,
   it is just for tagging the *venv* folders.

4. "Activate" the new "venv" by running the following command
   (notice the dot(``.``) at the begining of the command):

   .. code-block:: console

        > .\co2mpas_v1.0.1.venv.venv\Scripts\activate.bat

   Or type this in *bash*:

   .. code-block:: console

        $ source co2mpas_v1.0.1.venv.venv\Scripts\activate.bat

   You must now see that your prompt has been prefixed with the venv's name.


6. Install the co2mpas version you want inside the activated venv.
   See the :ref:`install-co2mpas-package` section, above.

   Don't forget to check that what you get when running co2mpas is what you
   installed.

7. To "deactivate" the active venv, type:

   .. code-block:: console

       > deactivate

   The prompt-prefix with the venv-name should now dissappear.  And if you
   try to invoke ``co2mpas``, it should fail.



.. Tip::
    - Repeat steps 2-->5 to create venvs for different versions of co2mpas.
    - Use steps (6: Activate) and (9: Deactivate) to switch between different
      venvs.


Autocompletion
--------------
In order to press ``[Tab]`` and get completions, do the following in your
environment (ALLINONE is pre-configured with them):

- For the |clink|_ environment, on `cmd.exe`, add the following *lua* script
  inside clink's profile folder: ``clink/profile/co2mpas_autocompletion.lua``

  .. code-block:: lua

    --[[ clink-autocompletion for CO2MPAS
    --]]
    local handle = io.popen('co2mpas-autocompletions')
    words_str = handle:read("*a")
    handle:close()

    function words_generator(prefix, first, last)
        local cmd = 'co2mpas'
        local prefix_len = #prefix

        --print('P:'..prefix..', F:'..first..', L:'..last..', l:'..rl_state.line_buffer)
        if prefix_len == 0 or rl_state.line_buffer:sub(1, cmd:len()) ~= cmd then
            return false
        end

        for w in string.gmatch(words_str, "%S+") do
            -- Add matching app-words.
            --
            if w:sub(1, prefix_len) == prefix then
                clink.add_match(w)
            end

            -- Add matching files & dirs.
            --
            full_path = true
            nf = clink.match_files(prefix..'*', full_path)
            if nf > 0 then
                clink.matches_are_files()
            end
        end
        return clink.match_count() > 0
    end

    sort_id = 100
    clink.register_match_generator(words_generator)


- For the *bash* shell just add this command in your :file:`~/.bashrc`
  (or type it every time you open a new console):

  .. code-block:: console

      complete -fdev -W "`co2mpas-autocompletions`" co2mpas


.. _usage:

Usage
=====
.. Note::
    The following commands are for the **bash console**, specifically tailored
    for the **all-in-one** archive.  In `cmd.exe` the commands are rougly similar,
    but remember to substitute the slashes (`/`) in paths with backslashes(`\\`).

    The :doc:`allinone` contains additionally batch-files
    (e.g. :file:`RUN_CO2MPAS.bat`, :file:`NEW_TEMPLATE.bat`, etc)
    that offer roughly the same capabillities described below.
    When you double-click them, the output from these commands gets to be
    written in the :file:`ALLINONE/CO2MPAS/co2mpas.log` file.



First ensure that the latest version of |co2mpas| is properly installed, and that
its version match the version declared on this file.

The main entry for the simulator is the ``co2mpas`` console-command,
which **is not visible, but it is installed in your PATH**.
To get the syntax of the ``co2mpas`` console-command, open a console where
you have installed |co2mpas| (see :ref:`install` above) and type::

    Predict NEDC CO2 emissions from WLTP.

    :Home:         http://co2mpas.io/
    :Copyright:    2015-2016 European Commission (JRC-IET <https://ec.europa.eu/jrc/en/institutes/iet>
    :License:       EUPL 1.1+ <https://joinup.ec.europa.eu/software/page/eupl>

    Use the `batch` sub-command to simulate a vehicle contained in an excel-file.


    USAGE:
      co2mpas batch       [-v | --logconf=<conf-file>] [--gui] [-f]
                          [--overwrite-cache] [--out-template=<xlsx-file>]
                          [--plot-workflow] [-O=<output-folder>]
                          [--only-summary] [--soft-validation]
                          [<input-path>]...
      co2mpas demo        [-v | --logconf=<conf-file>] [--gui] [-f]
                          [<output-folder>]
      co2mpas template    [-v | --logconf=<conf-file>] [--gui] [-f]
                          [<excel-file-path> ...]
      co2mpas ipynb       [-v | --logconf=<conf-file>] [--gui] [-f]
                          [<output-folder>]
      co2mpas modelgraph  [-v | --logconf=<conf-file>] [-O=<output-folder>]
                          (--list | [--graph-depth=<levels>] [<models> ...])
      co2mpas             [--verbose | -v]  (--version | -V)
      co2mpas             --help

    Syntax tip:
      The brackets `[ ]`, parens `( )`, pipes `|` and ellipsis `...` signify
      "optional", "required", "mutually exclusive", and "repeating elements";
      for more syntax-help see: http://docopt.org/


    OPTIONS:
      <input-path>                Input xlsx-file or folder. Assumes current-dir if
                                  missing.
      -O=<output-folder>          Output folder or file [default: .].
      <excel-file-path>           Output file.
      --gui                       Launches GUI dialog-boxes to choose Input, Output
                                  and Options. [default: False].
      --only-summary              Do not save vehicle outputs, just the summary.
      --overwrite-cache           Overwrite the cached file.
      --soft-validation           Validate only partially input-data (no schema).
      --out-template=<xlsx-file>  Clone the given excel-file and appends results into it.
                                  By default, results are appended into an empty excel-file.
                                  Use `--out-template=-` to use input-file as template.
      --plot-workflow             Open workflow-plot in browser, after run finished.
      -l, --list                  List available models.
      --graph-depth=<levels>      An integer to Limit the levels of sub-models plotted.
      -f, --force                 Overwrite output/template/demo excel-file(s).

    Miscellaneous:
      -h, --help                  Show this help message and exit.
      -V, --version               Print version of the program, with --verbose
                                  list release-date and installation details.
      -v, --verbose               Print more verbosely messages - overridden by --logconf.
      --logconf=<conf-file>       Path to a logging-configuration file, according to:
                                    https://docs.python.org/3/library/logging.config.html#configuration-file-format
                                  If the file-extension is '.yaml' or '.yml', it reads a dict-schema from YAML:
                                    https://docs.python.org/3.5/library/logging.config.html#logging-config-dictschema


    SUB-COMMANDS:
        batch           Simulate vehicle for all <input-path> excel-files & folder.
                        If no <input-path> given, reads all excel-files from current-dir.
                        Read this for explanations of the param names:
                          http://co2mpas.io/explanation.html#excel-input-data-naming-conventions
        demo            Generate demo input-files for the `batch` cmd inside <output-folder>.
        template        Generate "empty" input-file for the `batch` cmd as <excel-file-path>.
        ipynb           Generate IPython notebooks inside <output-folder>; view them with cmd:
                          jupyter --notebook-dir=<output-folder>
        modelgraph      List or plot available models. If no model(s) specified, all assumed.


    EXAMPLES::

        # Don't enter lines starting with `#`.

        # Create work folders and then fill `input` with sample-vehicles:
        md input output
        co2mpas  demo  input

        # Launch GUI dialog-boxes on the sample-vehicles just created:
        co2mpas  batch  --gui  input

        # or specify them with output-charts and workflow plots:
        co2mpas  batch  input  -O output  --plot-workflow

        # Create an empty vehicle-file inside `input` folder:
        co2mpas  template  input/vehicle_1.xlsx

        # View a specific submodel on your browser:
        co2mpas  modelgraph  co2mpas.model.physical.wheels.wheels

        # View full version specs:
        co2mpas -vV


The default sub-command (``batch``) accepts either a single **input-excel-file**
or a folder with multiple input-files for each vehicle, and generates a
**summary-excel-file** aggregating the major result-values from these vehicles,
and (optionally) multiple **output-excel-files** for each vehicle run.


Demo files
----------
The simulator contains input-files for demo-vehicles that are a nice
starting point to try out:

======= == ========== ========== === ==== ========== ========== ======== ====
id      AT cal WLTP-H cal WLTP-L S/S BERS trg NEDC-H trg NEDC-L pre WLTP plan
======= == ========== ========== === ==== ========== ========== ======== ====
   0           X          X                  X
   1           X          X      X    X      X
   2    X      X          X                             X
   3           X          X      X           X                    X
   4    X                 X           X                 X
   5           X          X           X      X
   6    X      X          X      X           X                    X
   7    X      X                 X    X      X
   8           X          X                  X          X
   9    X      X          X      X    X      X
simplan          X          X                  X                           X
======= == ========== ========== === ==== ========== ========== ======== ====

To run them, do the following:

1. Choose a folder where you will store the *input* and *output* files:

   .. code-block:: console

        ## Skip this if ``tutorial`` folder already exists.
        $ mkdir tutorial
        $ cd tutorial

        ## Skip also this if folders exist.
        $ mkdir input output

  .. Note::
    The input & output folders do not have to reside in the same parent,
    neither to have these names.
    It is only for demonstration purposes that we decided to group them both
    under a hypothetical ``some-folder``.

2. Create the demo vehicles inside the *input-folder* with the ``demo``
   sub-command:


   .. code-block:: console

        $ co2mpas demo input
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-0.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-1.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-10.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-2.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-3.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-4.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-5.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-6.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-7.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-8.xlsx'...
        INFO:co2mpas.__main__:Creating INPUT-DEMO file 't\co2mpas_demo-9.xlsx'...
        INFO:co2mpas.__main__:You may run DEMOS with:
            co2mpas batch input

3. Run the simulator on all demo-files (note, it might take considerable time):

   .. code-block:: console

       $ co2mpas batch input -O output
       Processing ['input'] --> 'output'...
       Processing: co2mpas_demo-0
       ...
       ...
       Done! [499.579 sec]

   .. Note::
      The last demo-file, the "simulation-plan" will take longer to complete,
      and, for demonstration purposes, some some of the actual models will fail;
      check the *summary file*.

4. Inspect the results (explained in the next section):

   .. code-block:: console

       $ start output/*summary.xlsx       ## More summaries might exist in the folder from previous runs.
       $ start output                     ## View the folder with all files generated.


Output files
------------
The output-files produced on each run are the following:

- One file per vehicle, named as `<timestamp>-<inp-fname>.xls`:
  This file contains all the inputs and calculation results for each vehicle
  contained in the batch-run: scalar-parameters and time series for target,
  calibration and prediction phases, for all cycles.
  In addition, the file contains all the specific submodel-functions that
  generated the results, a comparison summary, and information on the python
  libraries installed on the system (for investigating reproducibility issues).

- A Summary-file named as `<timestamp>-summary.xls`:
  Major |CO2| emissions values, optimized |CO2| parameters values and
  success/fail flags of |co2mpas| submodels for all vehicles in the batch-run.

.. tip::

    Additionally, a sample output file is provide here:
    http://files.co2mpas.io/CO2MPAS-1.3.1/co2mpas-empty_output-2.2.xlsx


Entering new vehicles
---------------------
You may modify the samples vehicles and run again the model.
But to be sure that your vehicle does not contain by accident any of
the sample-data, use the ``template`` sub-command to make an *empty* input
excel-file:

1. Decide the *input/output* folders.  Assuming we are still in the ``tutorial``
   folder and we wish to re-use the ``input/output`` folders from the example
   above, we may clear all their contents with this:

   .. code-block:: console

        $ rm -r ./input/* ./output/*      ## Replace `rm` with `del` in *Windows* (`cmd.exe`)


2. Create an empty vehicle template-file (eg. ``vehicle_1.xlsx``) inside
   the *input-folder* with the ``template`` sub-command:

   .. code-block:: console

        $ co2mpas template input/vehicle_1.xlsx  ## Note that here we specify the filename, not the folder!
        Creating TEMPLATE INPUT file 'input/vehicle_1.xlsx'...


3. Open the template excel-file to fill-in your vehicle data
   (and save it afterwards):

   .. code-block:: console

        $ start input/vehicle_1.xlsx      ## Opens the excel-file. Use `start` in *cmd.exe*.

   The generated file contains help descriptions to help you populate it
   with vehicle data.  For items where an array of values is required
   (i.e. gear-box ratios) you may reference different parts of
   the spreadsheet following the syntax of the `"xlref" mini-language
   <https://pandalone.readthedocs.org/en/latest/reference.html#module-pandalone.xleash>`_.

   .. tip::
       You may also read the `"annotated" input excel-file
       <http://files.co2mpas.io/CO2MPAS-1.3.1/co2mpas-annotated_input-2.2.xls>`_
       to get an understanding of each scalar paramet and series required,
       but **DO NOT USE THIS "fatty" xl-file (~10Mb) when running the model.**

       For an explanation of the naming of the fields, read below the
       :ref:`excel-model` section

   You may repeat these last 2 steps if you want to add more vehicles in
   the *batch-run*.

4. Run the simulator.  Specify the single excel-file as input:

   .. code-block:: console

        $ co2mpas batch ./input/vehicle_1.xlsx -O output
        Processing './input/vehicle_1.xlsx' --> 'output'...
        Processing: vehicle_1
        ...
        Done! [12.938986 sec]

5. Assuming you do receive any error, you may now inspect the results:

   .. code-block:: console

        $ start output/*summary.xlsx      ## More summaries might open from previous runs.
        $ start output                    ## View all files generated (see below).


6. In the case of errors, or if the results are not satisfactory, repeat the
   above procedure from step 3 to modify the vehicle and re-run the model.
   See also :ref:`debug`, below.


Simulation plan
---------------
It is possible to launch co2mpas once, and have it run the model multiple times,
with variations on the input-data, all contained in a single
(or more) input file(s).

The data for **base model** are contained in the regular sheets, and any
variations are provided in additional sheets which names starting with
the ``plan.`` prefix.
These sheets must contain a table where each row is a single simulation,
while the columns names are the parameters that the user want to vary.
The columns of these tables must contain the following special names:

- **id**: Identifies the variation id.
- **base**: this is a file path of a CO2MPAS excel input, this model will be
  used as new base vehicle.
- **defaults**: this is a a list of file paths. The calibrated models of these
  files are used as default models of the **base** model. This behavior is
  needed to simulate, for example, a manual car (**base**) as A/T, because
  the A/T strategy and the torque converter are not in the **base** model.


Using custom output xl-files as templates
-----------------------------------------
You may have defined customized xl-files for summarizing time-series and
scalar parameters.  To have |co2mpas| fill those "output-template" files with
its results, execute it with the ``--out-template`` option.


To create/modify one output-template yourself, do the following:

1. Open a typical |co2mpas| output-file for some vehicle.

2. Add one or more sheets and specify/referring |co2mpas| result-data using
   `named-ranges <https://www.google.it/search?q=excel+named-ranges>`_.

   .. Warning::
   		Do not use simple/absolute excel references (e.g. "=B2").
   		Use excel functions (indirect, lookup, offset, etc.) and array-functions
   		together with string references to the named ranges
   		(e.g. "=indirect("nedc_predictions_time_series!_fuel_consumptions")").

3. (Optional) Delete the old sheets and save your file.

4. Use that file together with the ``--out-template`` argument.


Launch |co2mpas| from Jupyter(aka IPython)
------------------------------------------
You may enter the data for a single vehicle and run its simulation, plot its
results and experiment in your browser using `IPython <http://ipython.org/>`_.

The usage pattern is similar to "demos" but requires to have **ipython**
installed:

1. Ensure *ipython* with *notebook* "extra" is installed:

   .. Warning::
        This step requires too many libraries to provide as standalone files,
        so unless you have it already installed, you will need a proper
        *http-connectivity* to the standard python-repo.

   .. code-block:: console

        $ pip install ipython[notebook]
        Installing collected packages: ipython[notebook]
        ...
        Successfully installed ipython-x.x.x notebook-x.x.x


2. Then create the demo ipython-notebook(s) into some folder
   (i.e. assuming the same setup from above, ``tutorial/input``):

   .. code-block:: console

        $ pwd                     ## Check our current folder (``cd`` alone for Windows).
        .../tutorial

        $ co2mpas ipynb ./input

3. Start-up the server and open a browser page to run the vehicle-simulation:

   .. code-block:: console

        $ ipython notebook ./input

4. A new window should open to your default browser (AVOID IEXPLORER) listing
   the ``simVehicle.ipynb`` notebook (and all the demo xls-files).
   Click on the ``*.ipynb`` file to "load" the notebook in a new tab.

   The results are of a simulation run already pre-generated for this notebook
   but you may run it yourself again, by clicking the menu::

        "menu" --> `Cell` --> `Run All`

   And watch it as it re-calculates *cell* by cell.

5. You may edit the python code on the cells by selecting them and clicking
   ``Enter`` (the frame should become green), and then re-run them,
   with ``Ctrl + Enter``.

   Navigate your self around by taking the tutorial at::

        "menu" --> `Help` --> `User Interface Tour`

   And study the example code and diagrams.

6. When you have finished, return to the console and issue twice ``Ctrl + C``
   to shutdown the *ipython-server*.


Synchronizing time-series
-------------------------
The model might fail in case your time-series signals are time-shifted and/or
with different sampling rates.  Even if the run succeeds, the results will not
be accurate enough.

As an aid tool, you may use the ``datasync`` command-line tool to "synchronize"
your *data-tables*. This command reads one or more tables from excel-files and
synchronizes their columns.  The syntax of this utility command is given
by typing ``datasync --help`` in the command line
(listing below just the main fields)::

    Shift and resample excel-tables; see http://co2mpas.io/usage.html#Synchronizing-time-series.

    Usage:
      datasync          [(-v | --verbose) | --logconf <conf-file>] [--force | -f]
                        [--interp <method>] [--no-clone] [--prefix-cols]
                        [-O <output>] <x-label> <y-label> <ref-table>
                        [<sync-table> ...]
      datasync          [--verbose | -v]  (--version | -V)
      datasync          [--interp-methods | -l]
      datasync          --help
      datasync template [-f] [--cycle <cycle>] [<excel-file-path> ...]

    Options:
      <x-label>              Column-name of the common x-axis (e.g. 'times') to be
                             re-sampled if needed.
      <y-label>              Column-name of y-axis cross-correlated between all
                             <sync-table> and <ref-table>.
      <ref-table>            The reference table, in *xl-ref* notation (usually
                             given as `file#sheet!`); synced columns will be
                             appended into this table.
                             The captured table must contain <x_label> & <y_label>
                             as column labels.
                             If hash(`#`) symbol missing, assumed as file-path and
                             the table is read from its 1st sheet .
      <sync-table>           Sheets to be synced in relation to <ref-table>, also in
                             *xl-ref* notation.
                             All tables must contain <x_label> & <y_label> as column
                             labels.
                             Each xlref may omit file or sheet-name parts; in that
                             case, those from the previous xlref(s) are reused.
                             If hash(`#`) symbol missing, assumed as sheet-name.
                             If none given, all non-empty sheets of <ref-table> are
                             synced against the 1st one.
      -O <output>            Output folder or file path to write the results:
                             - Non-existent path: taken as the new file-path; fails
                               if intermediate folders do not exist, unless --force.
                             - Existent file: file-path to overwrite if --force,
                               fails otherwise.
                             - Existent folder: writes a new file
                               `<ref-file>.sync<.ext>` in that folder; --force
                               required if that file exists.
                             [default: .].
      -f, --force            Overwrite excel-file(s) and create any missing
                             intermediate folders.
      --prefix-cols          Prefix all synced column names with their source
                             sheet-names. By default, only clashing column-names are
                             prefixed.
      --no-clone             Do not clone excel-sheets contained in <ref-table>
                             workbook into output.
      --interp <method>      Interpolation method used in the resampling
                             [default: linear]: 'linear', 'nearest', 'zero',
                             'slinear', 'quadratic', 'cubic', 'barycentric',
                             'polynomial', 'spline' is passed to
                             scipy.interpolate.interp1d. Both 'polynomial' and
                             'spline' require that you also specify an order (int),
                             e.g. df.interpolate(--interp=polynomial4).
                             'krogh', 'piecewise_polynomial', 'pchip' and 'akima'
                             are all wrappers around the scipy interpolation methods
                             of similar names. 'integral'
      -l, --interp-methods   List of all interpolation methods that can be used in
                             the resampling.
      --cycle <cycle>        If set (e.g., --cycle=nedc.manual), the <ref-table> is
                             populated with the theoretical velocity profile.
                             Options: 'nedc.manual', 'nedc.automatic',
                             'wltp.class1', 'wltp.class2', 'wltp.class3a', and
                             'wltp.class3b'.
      <excel-file-path>      Output file.


All input tables must share 2 common columns: ``<x-label>`` and ``<y-label>``, as if
those tables describe 2D cartesian data, with a common *X-axis* and multiple
data-series on the *Y-Axis*.

.. Tip:: The ``<x-label>`` usually refers to the "time" dimension.

The 1st table given (`<ref-table>`) is considered to contain the "reference"
X/Y values;  the data-columns to shift-and-resample are contained in one
or more tables (``<sync-table>``) specified subsequently in the command line,
that are possibly read from different excel work-books.

- *Shifting* is based on the *cross-correlation* of ``<y-label>`` columns;
- *resampling* is based on the values of ``<x-label>`` columns among the
  different tables.

All tables are read from excel-sheets using the `xl-ref syntax
<https://pandalone.readthedocs.org/en/latest/reference.html#module-pandalone.xleash>`_,
which is best explained with some examples.


Examples
~~~~~~~~
- Read the full contents from all `wbook.xlsx` sheets as tables and
  sync their columns using the table from the 1st sheet as reference::

    datasync times  velocity  folder/Book.xlsx

- Sync `Sheet1` using `Sheet3` as reference::

    datasync times  velocity  wbook.xlsx#Sheet3!  Sheet1!

- The same as above but with integeres used to index excel-sheets::

    datasync times  velocity  wbook.xlsx#2!  0

  .. Note:: Sheet-indices are zero based!

- A more complex *xlr-ref* example which reads the synce-table from sheet2
  of wbook-2 starting at D5 cell, or more Down 'n Right if that was empty,
  till the first empty cell Down n Right, and synchronizes that  based on
  1st sheet of wbook-1::

    datasync times  velocity wbook-1.xlsx  wbook-2.xlsx#0!D5(DR):..(DR)

- Typical usage for |co2mpas| velocity time-series from Dyno and OBD:

  1. Create a template pre-populated with the theoretical velocity profile::

       datasync template --cycle wltp.class3b template.xlsx

  .. note:: the ref sheet contains the theoretical velocity profile.

  2. Fill the dyno and obd sheet with the raw data. Synchronize the data::

       datasync -O ./output times velocities template.xlsx#ref dyno obd

  3. Copy paste the synchronized signal into the CO2MPAS template.


.. _debug:

Debugging and investigating results
-----------------------------------

- Make sure that you have installed `graphviz`, and when running the simulation,
  append also the ``--plot-workflow`` option.

  .. code-block:: console

        $ co2mpas batch --plot-workflow bad-file.xlsx

  A browser tab will open at the end with the nodes processed.

- Use the ``modelgraph`` sub-command to plot the offending model (or just
  out of curiosity).  For instance:

  .. code-block:: console

        $ co2mpas modelgraph co2mpas.model.physical.wheels.wheels

  .. image:: _static/Wheel%20model/Wheel_model.gv.svg
    :alt: Flow-diagram Wheel-to-Engine speed ratio calculations.
    :height: 240
    :width: 320

- Inspect the functions mentioned in the workflow and models and search them
  in `CO2MPAS documentation <http://files.co2mpas.io/>`_ ensuring you are
  visiting the documents for the actual version you are using.


.. _explanation:

Model
=====
Execution Model
---------------
The execution of CO2MPAS model for a single vehicle is a stepwise procedure
of 3 stages: ``precondition``, ``calibration``, and ``prediction``.
These are invoked repeatedly, and subsequently combined, for the various cycles,
as shown in the "active" flow-diagram of the execution, below:

.. image:: _static/CO2MPAS%20model/CO2MPAS_model.gv.svg
    :alt: Flow-diagram of the execution of various Stages and Cycles sub-models.
    :width: 640

.. Tip:: The models in the diagram are nested; explore by clicking on them.

1. **Precondition:** identifies the initial state of the vehicle by running
   a preconditioning *WLTP* cycle, before running the *WLTP-H* and *WLTP-L*
   cycles.
   The inputs are defined by the ``input.precondition.wltp_p`` node,
   while the outputs are stored in ``output.precondition.wltp_p``.

2. **Calibration:** the scope of the stage is to identify, calibrate and select
   (see next sections) the best physical models from the WLTP-H and WLTP-L
   inputs (``input.calibration.wltp_x``).
   If some of the inputs needed to calibrate the physical models are not
   provided (e.g. ``initial_state_of_charge``), the model will select the
   missing ones from precondition-stage's outputs
   (``output.precondition.wltp_p``).
   Note that all data provided in ``input.calibration.wltp_x`` overwrite those
   in ``output.precondition.wltp_p``.

3. **Prediction:** executed for the NEDC and as well as for the WLTP-H and
   WLTP-L cycles. All predictions use the ``calibrated_models``. The inputs to
   predict the cycles are defined by the user in ``input.prediction.xxx`` nodes.
   If some or all inputs for the prediction of WLTP-H and WLTP-L cycles are not
   provided, the model will select from ```output.calibration.wltp_x`` nodes a
   minimum set required to predict |CO2| emissions.

.. _excel-model:

Excel input: data naming conventions
------------------------------------
This section describes the data naming convention used in the |co2mpas| template
(``.xlsx`` file). In it, the names used as **sheet-names**, **parameter-names**
and **column-names** are "sensitive", in the sense that they construct a
*data-values tree* which is then fed into into the simulation model as input.
These names are split in "parts", as explained below with examples:

- **sheet-names** parts::

                  base.input.precondition.WLTP-H.ts
                  └┬─┘ └─┬─┘ └────┬─────┘ └─┬──┘ └┬┘
      scope────────┘     │        │         │     │
      usage──────────────┘        │         │     │
      stage───────────────────────┘         │     │
      cycle─────────────────────────────────┘     │
      sheet_type──────────────────────────────────┘


  First 4 parts above are optional, but at least one of them must be present on
  a **sheet-name**; those parts are then used as defaults for all
  **parameter-names** contained in that sheet. **type** is optional and specify
  the type of sheet.

- **parameter-names**/**columns-names** parts::

                     plan.target.prediction.initial_state_of_charge.WLTP-H
                     └┬─┘ └─┬─┘ └────┬────┘ └──────────┬──────────┘ └──┬─┘
      scope(optional)─┘     │        │                 │               │
      usage(optional)───────┘        │                 │               │
      stage(optional)────────────────┘                 │               │
      parameter────────────────────────────────────────┘               │
      cycle(optional)──────────────────────────────────────────────────┘

  OR with the last 2 parts reversed::

                    plan.target.prediction.WLTP-H.initial_state_of_charge
                                           └──┬─┘ └──────────┬──────────┘
      cycle(optional)─────────────────────────┘              │
      parameter──────────────────────────────────────────────┘

.. note::
   - The dot(``.``) may be replaced by space.
   - The **usage** and **stage** parts may end with an ``s``, denoting plural,
     and are not case-insensitive, e.g. ``Inputs``.


Description of the name-parts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. **scope:**

   - ``base`` [default]: values provided by the user as input to |co2mpas|.
   - ``plan``: values selected (see previous section) to calibrate the models
     and to predict the |CO2| emission.

2. **usage:**

   - ``input`` [default]: values provided by the user as input to |co2mpas|.
   - ``data``: values selected (see previous section) to calibrate the models
     and to predict the |CO2| emission.
   - ``output``: |co2mpas| precondition, calibration, and prediction results.
   - ``target``: reference-values (**NOT USED IN CALIBRATION OR PREDICTION**) to
     be compared with the |co2mpas| results. This comparison is performed in the
     *report* sub-model by ``compare_outputs_vs_targets()`` function.

3. **stage:**

   - ``precondition`` [imposed when: ``wltp-p`` is specified as **cycle**]:
     data related to the precondition stage.
   - ``calibration`` [default]: data related to the calibration stage.
   - ``prediction`` [imposed when: ``nedc`` is specified as **cycle**]:
     data related to the prediction stage.

4. **cycle:**

   - ``nedc-h``: data related to the *NEDC High* cycle.
   - ``nedc-l``: data related to the *NEDC Low* cycle.
   - ``wltp-h``: data related to the *WLTP High* cycle.
   - ``wltp-l``: data related to the *WLTP Low* cycle.
   - ``wltp-precon``: data related to the preconditioning *WLTP* cycle.
   - ``wltp-p``: is a shortcut of ``wltp-precon``.
   - ``nedc``: is a shortcut to set values for both ``nedc-h`` and ``nedc-l``
     cycles.
   - ``wltp``: is a shortcut to set values for both ``wltp-h`` and ``wltp-l``
     cycles.
   - ``all`` [default]: is a shortcut to set values for ``nedc``, ``wltp``,
     and ``wltp-p`` cycles.

5. **param:** any data node name (e.g. ``vehicle_mass``) used in the physical
   model.

6. **sheet_type:** there are three sheet types, which are parsed according to
   their contained data:

   - **pl** [parsed range is ``#A1:__``]: table of scalar and time-depended
     values used into the simulation plan as variation from the base model.
   - **pa** [parsed range is ``#B2:C_``]: scalar or not time-depended
     values (e.g. ``r_dynamic``, ``gear_box_ratios``, ``full_load_speeds``).
   - **ts** [parsed range is ``#A2:__``]: time-depended values (e.g.
     ``times``, ``velocities``, ``gears``). Columns without values are skipped.
     **COLUMNS MUST HAVE THE SAME LENGTH!**

   ..note:: If it is not defined, the default value follows these rules:
     When **scope** is ``plan``, the sheet is parsed as **pl**.
     If **scope** is ``base`` and **cycle** is missing in the **sheet-name**,
     the sheet is parsed as **pa**, otherwise it is parsed as **ts**.

Calibrated Physical Models
--------------------------
There are potentially eight models calibrated from input scalar-values and
time-series (see :doc:`reference`):

1. *AT_model*,
2. *electric_model*,
3. *clutch_torque_converter_model*,
4. *co2_params*,
5. *engine_cold_start_speed_model*,
6. *engine_coolant_temperature_model*,
7. *engine_speed_model*, and
8. *start_stop_model*.

Each model is calibrated separately over *WLTP_H* and *WLTP_L*.
A model can contain one or several functions predicting different quantities.
For example, the electric_model contains the following functions/data:

- *alternator_current_model*,
- *alternator_status_model*,
- *electric_load*,
- *max_battery_charging_current*,
- *start_demand*.

These functions/data are calibrated/estimated based on the provided input
(in the particular case: *alternator current*, *battery current*, and
*initial SOC*) over both cycles, assuming that data for both WLTP_H and WLTP_L
are provided.

.. Note::
    The ``co2_params`` model has a third possible calibration configuration
    (so called `ALL`) using data from both WLTP_H and WLTP_L combined
    (when both are present).


Model selection
---------------
To select which is the best calibration (from *WLTP_H* or *WLTP_L* or *ALL*)
to be used in the prediction phase, the results of each stage are compared
against the provided input data (used in the calibration).
The calibrated models are THEN used to recalculate (predict) the inputs of the
*WLTP_H* and *WLTP_L* cycles. A **score** (weighted average of all computed
metrics) is attributed to each calibration of each model as a result of this
comparison.

.. Note::
    The overall score attributed to a specific calibration of a model is
    the average score achieved when compared against each one of the input
    cycles (*WLTP_H* and *WLTP_L*).

    For example, the score of `electric_model` calibrated based on *WLTP_H*
    when predicting *WLTP_H* is 20, and when predicting *WLTP_L* is 14.
    In this case the overall score of the the `electric_model` calibrated
    based on *WLTP_H* is 17. Assuming that the calibration of the same model
    over *WLTP_L* was 18 and 12 respectively, this would give an overall score
    of 15.

    In this case the second calibration (*WLTP_L*) would be chosen for
    predicting the NEDC.

In addition to the above, a success flag is defined according to
upper or lower limits of scores which have been defined empirically by the JRC.
If a model fails these limits, priority is then given to a model that succeeds,
even if it has achieved a worse score.

The following table describes the scores, targets, and metrics for each model:

.. image:: _static/CO2MPAS_model_score_targets_limits.png
   :width: 600 px
   :align: center

.. _substs:

.. |co2mpas| replace:: CO\ :sub:`2`\ MPAS
.. |CO2| replace:: CO\ :sub:`2`
.. |clink| replace:: *Clink*
.. _clink: http://mridgers.github.io/clink/

