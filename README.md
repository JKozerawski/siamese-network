# siamese-network
Caffe implementation of the Siamese Neural Network for image data


## Description
This is an implementation of the Inception V1 [GoogleNet](https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet) Siamese Neural Network (inspired by the work of [Koch et al.](https://pdfs.semanticscholar.org/f216/444d4f2959b4520c61d20003fa30a199670a.pdf)).

Network was trained using categories coming from the ILSVRC 2012 challange.

Used net surgery to duplicate the Inception Network and copy its pretrained weights to its Siamese version.

## Pretrained model:
You can download the pretrained Caffe model files in here: [Drive](https://drive.google.com/open?id=1KhKtjOOYhI38tyhjRH2GjolpuHgq0vcO)

## Training data
Training data is coming from the ILSVRC 2012. For every category there is 100 positive pairs (same category - labeled "1") and 100 negative pairs (different categories - labeled "0"). That gives 200 000 pairs split 70-30 to train and val sets.

## Training
If you want to train your own Siamese Network - you can download the caffemodel file in here [Drive](https://drive.google.com/open?id=1xFCv3cj-MIr3nKU6CoTmWIazb6bMSmqz). Both arms of the Siamese have copied weights from the Inception V1, so it's not training from scratch.

To be completed

## Testing
To be completed
