#!/bin/bash
# CONTAINER_NAME=`docker ps --format '{{.Names}}'`
docker-compose up --build
CONTAINER_NAME='text_classification_text_classifier_1'
MODEL_FOLDER='/models/text_classifier'

echo "running container named ${CONTAINER_NAME} in your current terminal session"
echo "copying model config file into container named ${CONTAINER_NAME} in your current terminal session"

docker cp ./model.config ${CONTAINER_NAME}:${MODEL_FOLDER}

echo "copied model config file into container named ${CONTAINER_NAME} into ${MODEL_FOLDER}"

docker-compose up --build