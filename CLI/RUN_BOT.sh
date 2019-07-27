cd ..
python -m rasa_core.run --enable_api -d models/official -u models/nlu/default/official -o out.log --port 5000 --endpoints endpoints.yml --cors "*" --debug