#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"

./scripts/to_base64
python scripts/to_shadowrocket.py

echo "Конвертация завершена: pac.txt, pac_shadowrocket.txt"
