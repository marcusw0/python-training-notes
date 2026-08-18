# Command Line Arguments

This course section demonstrates how Python scripts receive values from the
command line. The notebooks simulate command-line input with `sys.argv` or
`argparse` so each example can run inside Jupyter without needing a terminal.

## Recommended Order

1. `sysargv.ipynb`
2. `helloworld.ipynb`
3. `addition.ipynb`
4. `display.ipynb`
5. `calculator_argparse.ipynb`

## Topic Map

| Topic | Files | Main ideas |
| --- | --- | --- |
| Raw arguments | `sysargv.ipynb` | `sys.argv`, script name, argument count |
| Repeated output | `helloworld.ipynb` | Parsing one numeric argument |
| Positional values | `addition.ipynb` | Converting string arguments to integers |
| Named argument | `display.ipynb` | `argparse.ArgumentParser`, simple options |
| Calculator CLI | `calculator_argparse.ipynb` | Required options, help output, arithmetic |

## Quick Reference

| Pattern | Example |
| --- | --- |
| Raw argument list | `sys.argv` |
| First user argument | `sys.argv[1]` |
| Parser object | `argparse.ArgumentParser()` |
| Add option | `parser.add_argument("-a")` |
| Parse arguments | `parser.parse_args()` |
| Help flag | `--help` |

## Notes for Learners

Command-line arguments arrive as strings. Convert them to `int`, `float`, or
another type before doing arithmetic.
