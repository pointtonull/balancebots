# Concurrent Balance Bots

This is a toy implementation to [Balance Bots Problem][BalanceBots] with a
concurrent aproach. It includes good practices structure for:

    - predictable development enviroment setup with GNU Make
    - testing and coverage enabled
    - local dependences
    - sub-modules

## Overview

Mean the problem could be resolved faster and easier with a pure Finite-stame
machines implementation, the idea is to provide an example of simple
implementation of concurrent threats.

## Dependencies

- It should run with Python2.+ and Python3+ (use Python3, please)
- It doesn't have external dependences

## How to build/run

To clone a local copy:

```sh
git clone git@github.com:pointtonull/balancebots.git
cd balancebots
```

To install dependences:

```sh
make deps
```

After this step you should have a `_buld` directory where all the relevant
libraries are stored. The mechanism used by this command should work in any
Posix enviroment but I was not able to test on legacy systems, if you find a
problem please issue a bug.

To run tests and coverage you can use the respective targets:

```sh
make test
make coverage
```

This should output current status of the project:

```sh
% make coverage
Pulling in dependencies...
================================== test session starts ==================================
platform darwin -- Python 3.6.1, pytest-3.1.3, py-1.4.34, pluggy-0.4.0
rootdir: /Users/ccabrera/programacion/github/neu, inifile:
plugins: cov-2.5.1
collected 1 item s

../tests/test__example.py .

---------- coverage: platform darwin, python 3.6.1-final-0 -----------
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
lib/__init__.py       0      0   100%
lib/matrix.py        77      3    96%   6-7, 102
main.py              13     13     0%   3-18
-----------------------------------------------
TOTAL                90     16    82%


=============================== 1 passed in 0.27 seconds ================================
```

The tests includes given example.

### Running

To run you can execute simply execute `make run`:

```sh
$ make run
Pulling in dependencies...
Intruction: bot 75 gives low to bot 145 and high to bot 95
  > bot 75 had been created
Intruction: bot 116 gives low to bot 157 and high to bot 197
  > bot 116 had been created
Intruction: bot 185 gives low to bot 57 and high to bot 139
  > bot 185 had been created

(...)

bot 1 is shuting down
bot 113 is shuting down
bot 136 is shuting down
bot 192 is shuting down
bot 98 is shuting down
===
The result is bot 38
```

### Debuging

To run a Interactive shell in the enviroment of the program you can run:

```sh
make shell
```

Like me, do you love IPython?, you can use it with:

```sh
make PYTHON_VERSION=ipython shell
```

And even use it to run the main routine with PDB:

```sh
make PYTHON_VERSION="ipython --pdb" run
```

And the same trick can be used to test specific python versions:

```sh
make PYTHON_VERSION=python2.6 run
```

```sh
make PYTHON_VERSION=python3.6 run
```

(you should be using Python3 tough)



[BalanceBots]: http://adventofcode.com/2016/day/10

<!--- vim: sw=4 et ts=4 -->
