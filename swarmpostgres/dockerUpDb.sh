#!/bin/bash
docker build -t swarmpostgres .
docker run -d --name swarmpostgres --restart always  \
    -p 5432:5432 \
    --env-file ./env.list \
    --network swarm-net\
    swarmpostgres:latest
