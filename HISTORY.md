# History

## 0.1.0 (2025-03-27)
- Add the flag `--fix` for allowing happy_kostadin to change the files
- Increase testing of functions by separating and unit testing them
- Remove test argument `return_checked_files` from `main()`
- Reduce Cyclomatic Complexity from 3.25 to 2.19

## 0.0.6 (2025-02-20)
- Update minimum python requirement to =>3.9, <=3.13
- Make it possible to add path with flag. So `happy_kostadin path/to/code` will now work
- Improve readability of error for multiple files
- Technical change: if CRLF files are detect it will no longer raise a value error but only system exit code 1
- bugfix: Some systems have trouble with emoticon so they are removed from the print statement

## 0.0.5 (2024-01-25)
- Stop printing all files

## 0.0.4 (2024-01-19)
- Add check if pyproject exist

## 0.0.3 (2024-01-18)
- Add setting to pick your postfix

## 0.0.2 (2024-01-18)
- Add submodules

## 0.0.1 (2024-01-18)
- Add a check for /r/n (crlf) in the files

## 0.0.0 (2024-01-18)
- Copied basic package a start of happy_kostadin
