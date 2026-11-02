# Orinvex 1.0 syntax

Programs are text files with the `.ovx` extension, run top to bottom.

## Comments

A line that starts with `#` is ignored. Comments must be on their own line.

```
# this is a comment
```

## Values

| Type | Examples |
|---|---|
| Text | `"hello"`, `'hello'` |
| Integer | `5`, `-3` |
| Decimal | `3.14`, `-0.5` |
| Boolean | `<true>`, `<false>` |
| Variable | `data:Get.name` |

There are no escape sequences in text, and text cannot contain the
sequence ` - ` (space, dash, space) because it separates commands.

## Commands

Most commands end with the word `end` glued to the closing bracket:

```
print.ConsoleText("Hi")end
define.x = 5.end
```

## Several commands on one line

Separate them with ` - ` (a dash with spaces on both sides):

```
define.a = 1.end - print.Number(data:Get.a)end
```

## Variables

```
define.score = 10.end
print.Number(data:Get.score)end
```

- A name starts with a letter or `_`, then letters, digits or `_`.
- A variable can be defined only once; defining it again is an error.
- Reading an undefined variable is an error.
- There is no assignment to an existing variable in 1.0.

## Loops

```
loop -- <true>.Repeat(3)
    print.ConsoleText("Hi")end
end
```

- The body is closed with a line that contains only `end`.
- Loops can be nested; each needs its own `end`.
- `<false>` loops never run.
- The repeat count must be a plain non-negative integer written in the
  source (not a variable).

## Libraries

Libraries are loaded with `import`. Version 1.0 has one library:

```
import rest
```

## Not in 1.0

User input, if/else, functions and math expressions.
