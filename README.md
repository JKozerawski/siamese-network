# Siamese Network using Inception V1
Caffe implementation of the Siamese Neural Network for image data

## Requirements:
- Caffe
- Numpy

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

1. Create training data pairs using:
	```
	python training_paris_generation.py --dir pathToImages --examples numOfExamplesPerCategory
	```
2. Previous step will create 4 text files (train_left, train_rigth, val_left and val_right) in the directory pointed by the --txt_dir flag ("./txtFiles/" as a default). Copy those files to your ILSVRC folder. Now you can use those text files to create lmdb files to use for training the network. To do this you have to change the following paths in the create_siamese_lmdb.sh:
- EXAMPLE=/home/jedrzej/siamese_data	
- DATA=/media/jedrzej/SAMSUNG/DATA/ILSVRC2012
- TOOLS=/home/jedrzej/work/caffe/tools
- TRAIN_DATA_ROOT=/media/jedrzej/SAMSUNG/DATA/ILSVRC2012/TRAIN/
- VAL_DATA_ROOT=/media/jedrzej/SAMSUNG/DATA/ILSVRC2012/TRAIN/

3. Run the script:
	```
	./create_siamese_lmdb.sh
	```

4. Now you can download train_val.prototxt file from link above. Remember to modify paths to your lmdb paths in the file.
5. Perform either training from scratch or finetune (either from the copied [Inception V1](https://drive.google.com/open?id=1xFCv3cj-MIr3nKU6CoTmWIazb6bMSmqz) or from our [model](https://drive.google.com/open?id=1KhKtjOOYhI38tyhjRH2GjolpuHgq0vcO) trained on ILSVRC2012.

## Testing
In the test.py file we use feature extraction script (using Inception V1 network) to do preprocessing of images.
If you want to use our test.py file - please download the Inception V1 .caffemodel and deploy file from [here](https://drive.google.com/file/d/1WctmdPPkMCu7XFuAFixruG_a55grGiFP/view?usp=sharing). Make sure to point to the directory where the model is with the --inception_model_dir flag when using the test.py

To test the network just run our example:
```
python test.py --model_dir pathToTheSiameseNetwork --inception_model_dir pathToTheInceptionNetwork --imageL pathToTheLeftImage --imageR pathToTheRightImage
```
