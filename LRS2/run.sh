#!/bin/bash

if [ "$1" == "1" ]; then
    sudo chmod -R 777 /dev 
else 
    python3 -m lasdai_ula.ejemplos.$1
fi
