#!/usr/bin/env bash
# Orinvex installer: puts the interpreter in ~/.local/share/orinvex
# and creates an `orinvex` command in ~/.local/bin.
set -e

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="${HOME}/.local/share/orinvex"
BIN_DIR="${HOME}/.local/bin"
LAUNCHER="${BIN_DIR}/orinvex"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 is required but was not found." >&2
    exit 1
fi

if [ ! -f "${SRC_DIR}/orinvex.py" ]; then
    echo "Error: orinvex.py not found next to install.sh." >&2
    exit 1
fi

mkdir -p "${INSTALL_DIR}" "${BIN_DIR}"
cp "${SRC_DIR}/orinvex.py" "${INSTALL_DIR}/orinvex.py"

if [ -d "${SRC_DIR}/examples" ]; then
    rm -rf "${INSTALL_DIR}/examples"
    cp -r "${SRC_DIR}/examples" "${INSTALL_DIR}/examples"
fi

cat > "${LAUNCHER}" <<EOF
#!/usr/bin/env bash
exec python3 "${INSTALL_DIR}/orinvex.py" "\$@"
EOF
chmod +x "${LAUNCHER}"

echo "Orinvex installed."
echo "  Interpreter: ${INSTALL_DIR}/orinvex.py"
echo "  Command:     ${LAUNCHER}"

case ":${PATH}:" in
    *":${BIN_DIR}:"*) ;;
    *)
        echo
        echo "Note: ${BIN_DIR} is not in your PATH."
        echo "Add this line to ~/.bashrc or ~/.zshrc:"
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
        ;;
esac

echo
echo "Try it: orinvex ${INSTALL_DIR}/examples/hello.ovx"
