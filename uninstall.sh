#!/usr/bin/env bash
# Orinvex uninstaller: removes what install.sh created.
set -e

INSTALL_DIR="${HOME}/.local/share/orinvex"
LAUNCHER="${HOME}/.local/bin/orinvex"

removed=0

if [ -f "${LAUNCHER}" ]; then
    rm -f "${LAUNCHER}"
    echo "Removed ${LAUNCHER}"
    removed=1
fi

if [ -d "${INSTALL_DIR}" ]; then
    rm -rf "${INSTALL_DIR}"
    echo "Removed ${INSTALL_DIR}"
    removed=1
fi

if [ "${removed}" -eq 0 ]; then
    echo "Orinvex is not installed."
else
    echo "Orinvex uninstalled."
fi
