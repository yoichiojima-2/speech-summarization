#!/bin/bash

poetry run \
    python speech_summarization/pipeline.py SplitText \
    --target ~/Developer/repo/speech_summarization/tests/data/input/test.mp3
