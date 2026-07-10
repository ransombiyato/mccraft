#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "⛏ Installing MCCRAFT..."

if ! command -v curl >/dev/null 2>&1; then
    pkg install -y curl
fi

TMP=$(mktemp)

curl -L \
https://github.com/ransombiyato/mccraft/releases/latest/download/mccraft.deb \
-o "$TMP"

dpkg -i "$TMP"

rm "$TMP"

echo
echo "✅ MCCRAFT installed successfully!"
echo "Run: mccraft"
