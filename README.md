## Objective
1. Build a model to classify the sentiments of IMDB Reviews. Following the tensorflow [tutorial](https://www.tensorflow.org/hub/tutorials/tf2_text_classification).
2. Modify the base model to create a second version of the model.
3. Deploy / serve both versions using [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving).
4. Enable users to switch between both versions.


## Run Locally
1. Clone repo and go into project directory:
```
git clone 
cd text_classification
```
2. Ensure you have Docker installed. One way to confirm is by running the following in your terminal:
```
docker info
```
 If you get errors, it means you don't have Docker on your local machine. Follow the instructions [here](https://docs.docker.com/docker-for-mac/install/) to install Docker.
3. Activate a virtual environment to isolate dependencies: 
```
source bin/venv_activate.sh
```
4. Install the requirements / dependencies:
```
source bin/requirements.sh
```
5. Serve the model on port 8501:
```
source bin/serve_model.sh
```
6. Test the model in another terminal using cURL or the python3 cli:
```
curl -d '{"instances": ["this is such a horrible movie"]}' \
    -X POST http://localhost:8501/v1/models/text_classifier/versions/2:predict
```
**OR**
```
python3 app/main.py
```

## Shut Down
1. Deactivate virtual environment: 
```
source bin/venv_deactivate.sh
```
2. Stop docker container:
```
docker-compose down
```
