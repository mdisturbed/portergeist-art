#!/bin/bash
# Quick preview server for Portergeist Art site

echo "🎨 Starting Portergeist Art preview server..."
echo ""
echo "📍 Opening browser at http://localhost:8000"
echo "⚡ Press Ctrl+C to stop"
echo ""

# Open browser after a brief delay
(sleep 2 && open http://localhost:8000) &

# Start Python HTTP server
cd "$(dirname "$0")"
python3 -m http.server 8000
