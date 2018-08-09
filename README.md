# Siamese Network using Inception V1
Caffe implementation of the Siamese Neural Network for image data


## Description
This is an implementation of the Inception V1 [GoogleNet](https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet) Siamese Neural Network (inspired by the work of [Koch et al.](https://pdfs.semanticscholar.org/f216/444d4f2959b4520c61d20003fa30a199670a.pdf)).

Network was trained using categories coming from the ILSVRC 2012 challange.

Used net surgery to duplicate the Inception Network and copy its pretrained weights to its Siamese version.

## Pretrained model:
You can download the pretrained Caffe model files in here: [Drive](https://drive.google.com/open?id=1KhKtjOOYhI38tyhjRH2GjolpuHgq0vcO).
Unpack the files to the directory of your choosing (we suggest the "./model/") - remember to point to this directory with the --model_dir flag if you would like to use our test.py script.

## Training data
Training data is coming from the ILSVRC 2012. For every category there is 100 positive pairs (same category - labeled "1") and 100 negative pairs (different categories - labeled "0"). That gives 200 000 pairs split 70-30 to train and val sets.

## Training
If you want to train your own Siamese Network - you can download the caffemodel file in here [Drive](https://drive.google.com/open?id=1xFCv3cj-MIr3nKU6CoTmWIazb6bMSmqz). Both arms of the Siamese have copied weights from the Inception V1, so it's not training from scratch.

To be completed

## Testing
In the test.py file we use feature extraction script (using Inception V1 network) to do preprocessing of images.
If you want to use our test.py file - please download the Inception V1 .caffemodel and deploy file from [here](https://drive.google.com/file/d/1WctmdPPkMCu7XFuAFixruG_a55grGiFP/view?usp=sharing). Make sure to point to the directory where the model is with the --inception_model_dir flag when using the test.py 
To be completed
