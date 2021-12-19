#!/bin/bash

docker build --tag stat_server .
docker run --name stat_server_container -p 50002:50002 stat_server

