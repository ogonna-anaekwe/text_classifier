### Objective
1. Build a model to classify the sentiment of IMDB Reviews, following the Tensorflow [tutorial](https://www.tensorflow.org/hub/tutorials/tf2_text_classification).
2. Modify the base model to create a second version of the model.
3. Deploy / serve both versions using [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving).
4. Enable users to switch between both versions.

### Requirements
To run this application locally, you need to have / do the following:
1. macOS (you could use Windows as well, however, the instructions here were tested on Mac).
2. [python3](https://programwithus.com/learn/python/install-python3-mac).
3. Docker.
4. Run the [notebook](https://colab.research.google.com/github/ogonna-anaekwe/text_classifier/blob/master/Text_Classification_with_Movie_Reviews_(Data_Eng_).ipynb) and unzip the downloaded files in the `Downloads` folder of your Mac.

### Run Locally
1. Clone repo and go into project directory:
```sh
git clone git@github.com:ogonna-anaekwe/text_classifier.git
cd text_classifier
```

2. Ensure you have Docker installed. One way to confirm is by running the following in your terminal:
```sh
docker info --format "{{.OperatingSystem}}"
```
 If you get errors, it means you don't have Docker on your Mac. Follow the instructions [here](https://docs.docker.com/docker-for-mac/install/) to install Docker.

3. Serve the model on port 8501:
```sh
source bin/start_server_error.sh
```
In another terminal window, enter:
```sh
source bin/start_server.sh
```

4. In another terminal window, activate a virtual environment to isolate dependencies and install dependencies: 
```sh
source bin/requirements.sh
```

5. Run unit tests:
```sh
cd app
python3 tests/main_test.py <version>
```

6. Test the model using `cURL` or the `python3 cli`:
```sh
curl -d '{"instances": ["this is such a horrible movie", "this is such a great movie", "this is such a horrible and great movie"]}' \
    -X POST http://localhost:8501/v1/models/text_classifier/versions/<version>:predict
```
**OR**
```sh
python3 main.py <version>
```

**Note:** `<version>` could be `1` or `2` since we currently have only versions 1 and 2 of the model. Update the placeholders accordingly before running commands.

### Shut Down
To shut down the application, use:
```sh
source ../bin/stop_server.sh
```