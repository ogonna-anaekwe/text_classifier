#!/bin/bash

# build image and run container for text classifier
# this will fail the first time, 
# but we hide the error (Failed to start server. Error: Not found: /models/text_classifier/model.config; No such file or directory) in /dev/null
# it fails because the model.config file doesn't exist in the container as yet
# we'll be adding this when we start the server through start_server.sh
# there will be no more errors at that point
docker-compose up --build > /dev/null