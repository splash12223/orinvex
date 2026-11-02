# Installing Orinvex 1.0

## Requirements

- Python 3.8 or newer (`python3 --version`)
- Linux or macOS for `install.sh`

## Run without installing

```bash
python3 orinvex.py examples/hello.ovx
```

## Install

```bash
chmod +x install.sh uninstall.sh
./install.sh
```

This copies the interpreter and examples to `~/.local/share/orinvex` and
creates the `orinvex` command in `~/.local/bin`.

```bash
orinvex examples/hello.ovx
```

## Uninstall

```bash
./uninstall.sh
```

## Troubleshooting

**`orinvex: command not found`**
`~/.local/bin` is not in your PATH. Add this to `~/.bashrc` or `~/.zshrc`
and restart the terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

**`python3 is required but was not found`**
Install Python 3 (for example `sudo apt install python3`).

**`Permission denied` when running `./install.sh`**
Run `chmod +x install.sh` first.

**Windows**
`install.sh` does not support Windows, but `python orinvex.py file.ovx`
works there.
