# Orinvex 1.0

![Version](https://img.shields.io/badge/version-1.0-blue)
![Written in](https://img.shields.io/badge/written%20in-Python-3776AB?logo=python&logoColor=white)
![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

**Orinvex** is a small, easy-to-learn scripting language with an interpreter written in pure Python.
Programs are plain text files with the `.ovx` extension. There are no dependencies: if you have
Python 3, you can run Orinvex.

```
import rest

define.name = "world".end
print.ConsoleText("Hello, world!")end

loop -- <true>.Repeat(3)
    print.ConsoleText("Tick")end
    rest.wait -- milliseconds(500)end
end
```

Output:

```
Hello, world!
Tick
Tick
Tick
```

---

## Table of contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running programs](#running-programs)
- [Language tour](#language-tour)
  - [Comments](#comments)
  - [Values](#values)
  - [Variables](#variables)
  - [Output](#output)
  - [Loops](#loops)
  - [Waiting](#waiting)
  - [Several commands on one line](#several-commands-on-one-line)
- [Examples](#examples)
- [Error messages](#error-messages)
- [Limitations of version 1.0](#limitations-of-version-10)
- [Roadmap](#roadmap)
- [Project layout](#project-layout)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Features

| Feature | Syntax |
|---|---|
| Comments | `# comment` (on its own line) |
| Variables | `define.x = 5.end` and `data:Get.x` |
| Console output | `print.ConsoleText(...)end` |
| Number output | `print.Number(...)end` |
| Waiting | `import rest`, then `rest.wait -- time(1)end` |
| Loops (nestable) | `loop -- <true>.Repeat(5)` ... `end` |
| Several commands per line | `cmd1 - cmd2 - cmd3` |

## Requirements

- Python 3.8 or newer
- Linux or macOS to use `install.sh`
- The interpreter itself (`orinvex.py`) runs anywhere Python runs, including Windows

## Installation

### Option 1: run without installing

```bash
git clone https://github.com/YOUR_NAME/Orinvex.git
cd Orinvex
python3 orinvex.py examples/hello.ovx
```

### Option 2: install the `orinvex` command

```bash
chmod +x install.sh uninstall.sh
./install.sh
```

The installer copies the interpreter and the examples to `~/.local/share/orinvex` and creates the
`orinvex` command in `~/.local/bin`. If that folder is not in your `PATH`, add this line to
`~/.bashrc` or `~/.zshrc` and restart the terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Check that it works:

```bash
orinvex examples/hello.ovx
```

### Uninstall

```bash
./uninstall.sh
```

More details and troubleshooting: [docs/installation.md](docs/installation.md).

## Running programs

```bash
# without installing
python3 orinvex.py program.ovx

# after install.sh
orinvex program.ovx
```

Run the interpreter with no arguments to see its usage message. If a program contains an error,
Orinvex prints `Orinvex error: ...` to stderr and exits with code 1.

---

## Language tour

### Comments

A line that starts with `#` is ignored. Comments must be on their own line.

```
# this is a comment
print.ConsoleText("Hi")end
```

### Values

| Type | Examples |
|---|---|
| Text | `"hello"` or `'hello'` |
| Integer | `5`, `-3` |
| Decimal | `3.14`, `-0.5` |
| Boolean | `<true>`, `<false>` |
| Variable | `data:Get.name` |

Text has no escape sequences, and it cannot contain the sequence ` - ` (space, dash, space),
because that sequence separates commands on one line.

### Variables

Create a variable with `define`, read it with `data:Get`:

```
define.score = 10.end
define.player = "Ana".end

print.ConsoleText(data:Get.player)end
print.Number(data:Get.score)end
```

Rules:

- A name starts with a letter or `_` and then contains letters, digits or `_`.
- A variable can be defined only once. Defining it again is an error.
- Reading a variable that does not exist is an error.
- Version 1.0 has no assignment to an existing variable.

### Output

Most commands end with the word `end` glued to the closing bracket.

| Command | What it does |
|---|---|
| `print.ConsoleText(VALUE)end` | Prints any value to the terminal |
| `print.Number(VALUE)end` | Prints a number; text and booleans are an error |
| `print.Text(VALUE)end` | Reserved for game integrations; always an error in the terminal |

```
print.ConsoleText("Hello")end
print.ConsoleText(<true>)end
print.Number(3.14)end
```

Booleans are printed the way Python prints them: `True` and `False`.

### Loops

```
loop -- <true>.Repeat(3)
    print.ConsoleText("Hello")end
end
```

- The body is closed by a line that contains only `end`.
- Loops can be nested, and every loop needs its own `end`.
- A loop with `<false>` never runs its body.
- The repeat count must be a whole number written directly in the source. A variable cannot be
  used there in 1.0.

Nested loops:

```
loop -- <true>.Repeat(2)
    print.ConsoleText("Outer")end
    loop -- <true>.Repeat(2)
        print.ConsoleText("  Inner")end
    end
end
```

### Waiting

The `rest` library provides pauses. It must be imported first:

```
import rest

rest.wait -- time(1.5)end
rest.wait -- milliseconds(250)end
```

- `time(...)` is in seconds and may be a decimal.
- `milliseconds(...)` is in milliseconds.
- The duration must be a number and cannot be negative.
- Using `rest.wait` without `import rest` is an error.

### Several commands on one line

Separate commands with ` - ` (a dash with a space on each side):

```
define.a = 1.end - define.b = 2.end - print.Number(data:Get.b)end
```

---

## Examples

The `examples/` folder contains one program per topic:

| File | Topic | Status |
|---|---|---|
| `hello.ovx` | Output | Works |
| `variables.ovx` | Variables | Works |
| `loops.ovx` | Loops | Works |
| `wait.ovx` | Waiting with `rest` | Works |
| `input.ovx` | User input | Placeholder |
| `conditions.ovx` | if/else | Placeholder |
| `functions.ovx` | Functions | Placeholder |
| `math.ovx` | Arithmetic | Placeholder |

Run any of them:

```bash
python3 orinvex.py examples/loops.ovx
```

## Error messages

| Message | Cause |
|---|---|
| `File not found: ...` | The `.ovx` file does not exist |
| `Unknown command: ...` | The line is not a valid command |
| `Unknown value: ...` | A value is not text, number, boolean or `data:Get.name` |
| `Variable 'x' does not exist` | `data:Get.x` is used before `define.x` |
| `Variable 'x' is already defined` | `define.x` was written twice |
| `print.Number() requires a number` | Text or a boolean was given to `print.Number` |
| `print.Text() requires a game integration` | `print.Text` used in the terminal |
| `Library 'rest' is not imported` | `rest.wait` without `import rest` |
| `Wait duration must be a number` | A non-number was given to `rest.wait` |
| `Wait duration cannot be negative` | A negative duration was given |
| `Loop is missing its closing 'end'` | A `loop` has no matching `end` |

## Limitations of version 1.0

Orinvex 1.0 is intentionally small. It does **not** have yet:

- user input
- if/else conditions
- arithmetic and other expressions
- user-defined functions
- changing the value of an existing variable
- variables as a loop repeat count

The files `input.ovx`, `conditions.ovx`, `functions.ovx` and `math.ovx` in `examples/` are
placeholders that describe this.

## Roadmap

Ideas for the next versions (not promised, not final):

- [ ] Arithmetic: add, subtract, multiply, divide
- [ ] Changing variables
- [ ] Conditions (if/else)
- [ ] User input
- [ ] Functions
- [ ] Loop counts from variables
- [ ] More libraries

## Project layout

```
Orinvex-1.0/
├── orinvex.py        the interpreter
├── install.sh        installs the `orinvex` command
├── uninstall.sh      removes it
├── README.md         this file
├── LICENSE           MIT license
├── examples/         example programs (.ovx)
└── docs/
    ├── syntax.md         how the language is written
    ├── commands.md       every command in detail
    └── installation.md   installing and troubleshooting
```

## Documentation

- [docs/syntax.md](docs/syntax.md): how the language is written
- [docs/commands.md](docs/commands.md): every command in detail
- [docs/installation.md](docs/installation.md): installing and troubleshooting

## Contributing

Ideas, bug reports and pull requests are welcome. To report a problem, open an issue with the
program you ran and the full error text. For a new feature, describe the syntax you would like
and add an example `.ovx` file.

## License

Released under the MIT License. See [LICENSE](LICENSE).
