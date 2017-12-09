#!/usr/bin/env sh
set -e
TOOLS=/home/jedrzej/work/caffe/tools
python $TOOLS/extra/parse_log.py ./log/model.log ./log
python ./save_loss.py
