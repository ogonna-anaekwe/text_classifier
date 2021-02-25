#!/bin/bash

# CONTAINER_NAME='text_classifier_text_classifier_1'
CONTAINER_NAME=`docker ps --format "{{.Names}}"`

MODEL_FOLDER='/models/text_classifier'

echo "running container named ${CONTAINER_NAME} in your current terminal session"
echo "copying model config file into container named ${CONTAINER_NAME} in your current terminal session"
echo "copied model config file into container named ${CONTAINER_NAME} into ${MODEL_FOLDER}"

# copy model.config file into the model folder in the container so that it's visible to the container
docker cp ./model.config ${CONTAINER_NAME}:${MODEL_FOLDER}

# stop container and rebuild with the recently copied model config file
docker stop ${CONTAINER_NAME}

docker-compose up --build