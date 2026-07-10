#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "⛏ Installing MCCRAFT..."

# Check Termux
if [ -z "$PREFIX" ]; then
    echo "❌ This is not Termux."
    exit 1
fi

# Install requirements
echo "📦 Installing requirements..."
pkg install -y git python

# Download MCCRAFT
echo "📥 Downloading MCCRAFT..."

rm -rf "$PREFIX/share/mccraft"

git clone https://github.com/ransombiyato/mccraft.git \
"$PREFIX/share/mccraft"

# Create command
echo "🔧 Creating command..."

cat > "$PREFIX/bin/mccraft" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
python "$PREFIX/share/mccraft/main.py" "$@"
EOF

chmod +x "$PREFIX/bin/mccraft"

echo
echo "✅ MCCRAFT installed!"
echo
echo "Try:"
echo "  mccraft help"
