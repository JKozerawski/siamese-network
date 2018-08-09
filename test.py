import argparse
import caffe
from caffe_feature_extractor import CaffeFeatureExtractor

def preprocess(image_path):
	image = caffe.io.load(image_path, extractionNet)	# load the image
	return np.asarray(extractionNet.transformer.preprocess("data",image)/255.)	# preprocess the image
	
def run_siamese(net, extractionNet, imageL_path, imageR_path):
	# read and preprocess images:
	imageL = preprocess(imageL_path, extractionNet)
	imageR = preprocess(imageR_path, extractionNet)
	
	# prepare network input:
	network_input = np.zeros((1,6,224,224))
	network_input[0,:3,...] = imageL
	network_input[0,3:,...] = imageR

	# run the network:
	net.blobs['data'].reshape(1,6,224,224)	# reshape input to make sure it matches size of the batch (in this example batch of size 1)
	similarity_score = net.forward(data = network_input))["prob"].copy()[0][0]	# run the network and extract "prob" layer output
	return similarity_score


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--imageL',
		type=str,
		default="",
		help="Path to the left image"
		)
	parser.add_argument(
		'--imageR',
		type=str,
		default="",
		help="Path to the right image"
		)
	parser.add_argument(
		'--model_dir',
		type=str,
		default="./model/",
		help="Directory where the caffe model files are"
		)
	parser.add_argument(
		'--inception_model_dir',
		type=str,
		default="./model_inception/",
		help="Directory where the caffe model files are for the Inception V1 network"
		)

	FLAGS = parser.parse_args()
	extractionNet = CaffeFeatureExtractor(
		model_path = FLAGS.inception_model_dir+"googlenet_deploy.prototxt",
		pretrained_path = FLAGS.inception_model_dir+"bvlc_googlenet.caffemodel",
		blob = "pool/7x7_s1",
		crop_size = 224,
		mean_values = [104.0, 117.0, 123.0]		
		)
	siameseNet = caffe.Net(FLAGS.model_dir+"deploy.prototxt", FLAGS.model_dir+"siamese_iter_10000.caffemodel", caffe.TEST)
    	score = run_siamese(siameseNet, extractionNet, FLAGS.imageL, FLAGS.imageR)
	print "Calculated similarity score between the images:", score
