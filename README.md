# Happy Kostadin

If you have files with CRLF line endings it can create problems. 

## Install

```bash
pip install happy-kostadin
```

## Use as check

Happy_kostadin is a CLI tool. Navigate to the project you want to check and run the following:

```bash
happy_kostadin
```

If you want to specify a path you can specify it

```bash
happy_kostadin your\path\here
```

For legacy reasons you can also do this with the `-p` and `--path` flag.

```bash
happy_kostadin -p your\path\here
happy_kostadin --path your\path\here
```

## Use as formatter

Happy_kostadin can also be used as formatter with the flag `-f` or `--fix`

```bash
happy_kostadin your\path\here --fix
```

### Select what files to include

happy_kostadin uses the `pyproject.toml` in the folder it ran from.
If in there there is the following it will only look for files ending the allowed post-fixes.

```toml
[tool.happy_kostadin]
allowed-post-fixes = [
  ".py",
  ".md",
  ".gitignore",
]
```

If this not present all files will scanned.

# Credits

- Tom Nijhof
