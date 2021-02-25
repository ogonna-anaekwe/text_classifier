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


# the only required piece is the model name in order to differentiate endpoints
ENV MODEL_NAME=text_classifier

# this script runs the model server so we can use environment variables
# while also passing in arguments from the docker command line
RUN echo '#!/bin/bash \n\n\
tensorflow_model_server --port=8500 --rest_api_port=8501 \
--model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME}/ \
--model_config_file_poll_wait_seconds=60 \
--model_config_file=${MODEL_BASE_PATH}/${MODEL_NAME}/model.config \
"$@"' > /usr/bin/serve_text_classifier.sh \
&& chmod +x /usr/bin/serve_text_classifier.sh

ENTRYPOINT ["/usr/bin/serve_text_classifier.sh"]