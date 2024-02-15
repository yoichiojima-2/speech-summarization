#!/bin/bash

mkdir -p ./logs

input_directory="./data/input"

for file in $input_directory/*; do
  filename=$(basename $file)
  filename_wo_ext="${filename%.*}"
  echo "Processing $file"
  poetry run python \
    ./speech_summarization/pipeline.py SummarizeText \
    --target "${file}" \
    > "./logs/${filename_wo_ext}.log" 2>&1
done
