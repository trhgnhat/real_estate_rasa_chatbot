#!/usr/bin/env bash
cd..

ngrok http 5000

python train_nlu_core.py

python multi_channels_bot.py

python -m rasa_sdk.endpoint --actions actions --cors "*" --debug

docker run -p 8000:8000 rasa/duckling