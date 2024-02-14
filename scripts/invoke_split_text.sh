#!/bin/bash

mkdir -p ./logs

poetry run \
    python speech_summarization/pipeline.py SplitText \
    --target ~/Developer/repo/speech_summarization/data/input/ad_tech_1.mp3 \
    > ./logs/split_text_ad_tech_1.log 2>&1 &

poetry run \
    python speech_summarization/pipeline.py SplitText \
    --target ~/Developer/repo/speech_summarization/data/input/ad_tech_2.mp3 \
    > ./logs/split_text_ad_tech_2.log 2>&1 &

poetry run \
    python speech_summarization/pipeline.py SplitText \
    --target ~/Developer/repo/speech_summarization/data/input/dmp_1.mp3 \
    > ./logs/split_text_dmp_1.log 2>&1 &

poetry run \
    python speech_summarization/pipeline.py SplitText \
    --target ~/Developer/repo/speech_summarization/data/input/web_ad_1.mp3 \
    > ./logs/split_text_web_ad_1.log 2>&1 