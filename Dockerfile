# pull the lastest tensorflow/serving image from docker hub
FROM tensorflow/serving:latest

# gRPC port
EXPOSE 8500
# REST port
EXPOSE 8501

# set where models should be stored in the container
# we'll mount this base path in the volume
ENV MODEL_BASE_PATH=/models

RUN mkdir -p ${MODEL_BASE_PATH}

# the name of the model
# helps differentiate different models
ENV MODEL_NAME=text_classifier

# start the model server. this serves the model
# also pass the path to the model.config file
# we'll be checking this file every 60 seconds for updates to 
# the servable model versions
RUN echo '#!/bin/bash \n\n\
tensorflow_model_server --port=8500 --rest_api_port=8501 \
--model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME}/ \
--model_config_file_poll_wait_seconds=60 \
--model_config_file=${MODEL_BASE_PATH}/${MODEL_NAME}/model.config \
"$@"' > /usr/bin/serve_${MODEL_NAME}.sh \
&& chmod +x /usr/bin/serve_${MODEL_NAME}.sh

ENTRYPOINT ["/usr/bin/serve_text_classifier.sh"]