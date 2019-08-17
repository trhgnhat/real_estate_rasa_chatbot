To create train/test data for evaluation

rasa data split nlu -u data/data.md --out data/ --training-fraction=0.8

python utils/mdtojson.py

python train_nlu_core.py

ngrok http 5000

python slack_bot.py

python -m rasa_sdk.endpoint --actions actions --cors "*" --debug

docker run -p 8000:8000 rasa/duckling

docker build . -t housebot:lastest

docker run -v models:/housebot/models -v configs:/housebot/configs housebot:lastest python3.7 train_nlu_core.py

