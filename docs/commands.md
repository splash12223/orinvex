# Orinvex 1.0 command reference

## import rest

Loads the `rest` library. Required before any `rest.wait` command.

## define.NAME = VALUE.end

Creates a variable.

```
define.name = "Ana".end
```

Errors: the variable already exists; the value is not valid.

## data:Get.NAME

Not a command but a value: it gives the content of a variable. Use it
wherever a value is expected.

```
print.ConsoleText(data:Get.name)end
```

Error: the variable does not exist.

## print.ConsoleText(VALUE)end

Prints any value to the terminal followed by a newline.
Booleans are printed as Python prints them: `True` / `False`.

## print.Number(VALUE)end

Prints a number (integer or decimal). Text and booleans are an error.

## print.Text(VALUE)end

Reserved for game integrations. In the terminal it always fails with an
error; use `print.ConsoleText` instead.

## rest.wait -- time(SECONDS)end

Pauses the program. The value is in seconds and may be a decimal.

```
rest.wait -- time(1.5)end
```

## rest.wait -- milliseconds(MS)end

Same, but in milliseconds.

```
rest.wait -- milliseconds(250)end
```

Errors: `rest` is not imported; the duration is not a number or is negative.

## loop -- <true>.Repeat(N)

Repeats the lines up to the matching `end` N times. With `<false>` the
body is skipped.

## Errors

Any error stops the program and prints `Orinvex error: ...` to stderr
with exit code 1.
