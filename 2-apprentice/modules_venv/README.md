# Modules and Virtual Environments

This course section introduces importing modules, creating virtual
environments, and packaging a small custom module. Some files remain as `.py`
because they are importable package/support files rather than notebook lessons.

## Recommended Order

1. `importing_modules.ipynb`
2. `create_venv/virtualenv.txt`
3. `custom_modules/packaging_custom_modules.txt`
4. `custom_modules/calculator/custom_calculator.py`
5. `custom_modules/calculator/setup.py`

## Topic Map

| Topic | Files | Main ideas |
| --- | --- | --- |
| Standard imports | `importing_modules.ipynb` | `math`, `sys`, `time`, `datetime`, `random` |
| Virtual environments | `create_venv/virtualenv.txt` | Environment creation, activation, isolation |
| Custom module packaging | `custom_modules/packaging_custom_modules.txt` | Package layout and build notes |
| Calculator module | `custom_modules/calculator/custom_calculator.py` | Reusable arithmetic functions |
| Package setup | `custom_modules/calculator/setup.py` | Package metadata and setup configuration |

## Use Cases

- Use standard-library modules instead of rewriting common functionality.
- Use virtual environments to isolate dependencies for each project.
- Use custom modules to share reusable functions across scripts.
- Use packaging files when code needs to be installed or distributed.

## Practice Labs

1. Import another standard-library module and print one useful value.
2. Inspect `sys.path` and identify where Python looks for imports.
3. Add a new function to `custom_calculator.py`.
4. Update package metadata in `setup.py`.
5. Create a fresh virtual environment and install the calculator package into
   it.

## Challenge Extensions

- Add docstrings to each calculator function.
- Add a small test file that imports and calls the calculator functions.
- Build a wheel distribution in addition to the source archive.
- Compare imports from the current directory with imports from an installed
  package.

## Quick Reference

| Pattern | Example |
| --- | --- |
| Import module | `import math` |
| Import alias | `import math as m` |
| Import name | `from time import asctime` |
| Module search path | `sys.path` |
| Create venv | `python3 -m venv .venv` |
| Activate venv | `source .venv/bin/activate` |
| Install package | `python3 -m pip install .` |

