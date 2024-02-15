#!/bin/bash

mkdir -p ./logs

input_directory="./tests/data/input"

for file in $input_directory/*; do
  echo "Processing $file"
  filename=$(basename $file)
  filename_wo_ext="${filename%.*}"
  poetry run python \
    ./speech_summarization/pipeline.py SplitText \
    --target $file \
    > "./logs/${filename_wo_ext}.log" 2>&1
done
