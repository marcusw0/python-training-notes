# File Operations

This course section introduces reading, writing, appending, CSV handling, and
JSON serialization. The notebooks use the supporting files in this folder and
show output directly below each file operation.

## Recommended Order

1. `file_operations.ipynb`
2. `python_csv.ipynb`
3. `json_in_python.ipynb`

## Topic Map

| Topic | Files | Main ideas |
| --- | --- | --- |
| Text files | `file_operations.ipynb`, `sample.txt` | `open`, `read`, `readline`, `seek`, `tell` |
| Writing files | `file_operations.ipynb` | Write mode, append mode, truncate, rename, remove |
| CSV files | `python_csv.ipynb`, `record.csv`, `record_pipe.csv`, `record_tab.csv` | `csv.reader`, delimiters, `DictReader`, `DictWriter` |
| JSON files | `json_in_python.ipynb`, `currency.json`, `eat.txt` | `json.loads`, `json.load`, `json.dumps`, `json.dump` |

## Practice Labs

1. Read only the first line of `sample.txt`.
2. Write three new lines to a temporary text file and read them back.
3. Add a new row to `names.csv` with `csv.writer`.
4. Read `record_pipe.csv` with the correct delimiter.
5. Add another key to the JSON dessert object and write it to `eat.txt`.

## Quick Reference

| Pattern | Example |
| --- | --- |
| Open file | `open("sample.txt")` |
| Context manager | `with open("sample.txt") as f:` |
| Read all text | `f.read()` |
| Read lines | `f.readlines()` |
| Write text | `f.write("text")` |
| CSV reader | `csv.reader(file)` |
| JSON load | `json.load(file)` |
| JSON dump | `json.dump(data, file)` |

