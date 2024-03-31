#!/bin/bash

mkdir -p ./logs

input_directory="./data/input"

while read -r file; do
  filename_wo_ext="${file%.*}"
  echo "Processing ${input_directory}/${file}"
  echo "${input_directory}/${file}"
  poetry run python \
    ./speech_summarization/pipeline.py RefineOutput \
    --target "${input_directory}/${file}" \
    | tee "./logs/${filename_wo_ext}.log" 2>&1
done < "./scripts/target.txt"
