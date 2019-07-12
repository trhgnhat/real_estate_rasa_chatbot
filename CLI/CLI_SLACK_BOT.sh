#!/usr/bin/env bash
cd..

ngrok http 5000

python train_nlu_core.py

python slack_bot.py

python -m rasa_core_sdk.endpoint --actions form_action
