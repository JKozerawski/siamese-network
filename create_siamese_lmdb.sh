#!/usr/bin/env sh
# Create the data lmdb inputs
# N.B. set the path to the dataset train + val data dirs
set -e

EXAMPLE=/home/jedrzej/siamese_data	
DATA=/media/jedrzej/SAMSUNG/DATA/ILSVRC2012
TOOLS=/home/jedrzej/work/caffe/tools


TRAIN_DATA_ROOT=/media/jedrzej/SAMSUNG/DATA/ILSVRC2012/TRAIN/
VAL_DATA_ROOT=/media/jedrzej/SAMSUNG/DATA/ILSVRC2012/TRAIN/
RESIZE=true
if $RESIZE; then
 RESIZE_HEIGHT=224
 RESIZE_WIDTH=224	
else	
 RESIZE_HEIGHT=0
 RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi


echo "Creating train lmdb right..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle=false \
    $TRAIN_DATA_ROOT \
    $DATA/train_right.txt \
    $EXAMPLE/siamese_train_right_lmdb

echo "Creating val lmdb right..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle=false \
    $VAL_DATA_ROOT \
    $DATA/val_right.txt \
    $EXAMPLE/siamese_val_right_lmdb

echo "Creating train lmdb left..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle=false \
    $TRAIN_DATA_ROOT \
    $DATA/train_left.txt \
    $EXAMPLE/siamese_train_left_lmdb

echo "Creating val lmdb left..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle=false \
    $VAL_DATA_ROOT \
    $DATA/val_left.txt \
    $EXAMPLE/siamese_val_left_lmdb

echo "Done."
