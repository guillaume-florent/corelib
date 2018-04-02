#!/usr/bin/env bash

home="${1:-$HOME}"

imageName="guillaume-florent/corelib:latest"
containerName="corelib"
displayVar="$DISPLAY"

docker build --tag ${imageName} .

docker run  -it -d --name ${containerName}                  \
    -e DISPLAY=${displayVar}                                \
    --workdir="${home}"                                     \
    --volume="${home}:${home}"                              \
     -v=/tmp/.X11-unix:/tmp/.X11-unix ${imageName}          \
     /bin/bash
