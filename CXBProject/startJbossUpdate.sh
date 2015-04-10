#!/bin/bash
basepath=$(pwd)
echo $basepath
export PYTHONPATH=${PYTHONPATH}:$basepath/CX/Library
echo "The folder passed from command"
if [ $# -gt 0 ]; then
user=$1
echo "$user"
output=/Users/"$user"/Documents/chromereport/
if [ -d "$output" ]; then
    echo "file is existed"
    rm -R "$output"
    mkdir "$output"
    echo "delete and create $ouput"
else
    mkdir "$output"
    echo "create $output"
fi
pybot --suite Jboss_Update_Smoke_Test  --outputdir "$output" "$basepath/CX"
else
echo "please insert you account name"
fi
