#!/bin/bash

clear


if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

    pkg install -y git python3
elif [ "$(uname)" = "Darwin" ]; then
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false
else
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false
    sudo apt-get install -y git python3
fi

