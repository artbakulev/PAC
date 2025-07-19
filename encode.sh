#!/usr/bin/env bash

set -e

./to_base64
python to_shadowrocket.py

echo "Конвертация завершена: ${OUTPUT}"
