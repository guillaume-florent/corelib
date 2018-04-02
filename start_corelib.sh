#!/usr/bin/env bash

xhost +local:corelib
docker start corelib
docker exec -it corelib /bin/bash