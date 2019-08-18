#Required services/applications:
* Docker & Docker-compose
    * Download Docker Desktop: [download](https://docs.docker.com/docker-for-windows/install/)
    * Setup the recommended memory for Docker: ![image]() 
    * Setup the shared drive for volume usage: ![image]() 
* ngrok
    * Download ngrok: [download](https://ngrok.com/download)
    * Inside of the unzipped folder containing `ngrok`, run the following command
    to setup the path environment for ngrok: 
    
        `setx path "%path%;<PATH>"`
    * Check ngrok: `ngrok --version`
    
>To convert `.md` file into `.json` file:
>    `python utils/mdtojson.py`


#Building project locally:
* Train model:

        `python train_nlu_core.py`
* Run ngrok webhook service:

        `ngrok http 5000`
* Run action server to handle custom actions:

        `python -m rasa_sdk.endpoint --actions actions --cors "*" --debug`
* Run Duckling (NER extractor) service via docker:

        `docker run -p 8000:8000 rasa/duckling`
* Run the bot:
    * On Slack:

            `python slack_bot.py`
    * On RestAPI server:
    
            `python slack cmd.py`

#Building project via Docker:
* Build all necessary images via Docker-compose:

        `docker-compose build`
* Build housebot image only:
        
        `docker build . -t housebot:latest`
* Training model
    * On Linux/MacOS:
    
            `docker run -v $(pwd):/housebot housebot:latest python3.7 train_nlu_core.py`

    * On Window 10:
         
           `docker run -v cwd:/housebot housebot:latest python3.7 train_nlu_core.py`
* Run all services via Docker-compose:
    
        `docker-compose up`
            
To setup constants (paths, information, api-keys, etc.), you must create a `constant.py` 
file inside the `utils` folder based on `constant_template.py`

Bot are communicated via RestAPI, with the following format:
* URL:
    
    `<url>/webhooks/rest/webhook`
    
    Example: `http://localhost:5000/webhooks/rest/webhook`

* body json:

    ```
    {
        "sender": "<sender_id>",
        "message": "<message_content>"
    }
    ```
    
> Created by
>
> Nhat Hoang Truong