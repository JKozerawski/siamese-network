import sys
CAFFE_ROOT = '/home/jedrzej/work/caffe/python'
sys.path.insert(0, CAFFE_ROOT) 
import caffe

googlenet = caffe.Net('./model/googlenet_deploy.prototxt', './model/bvlc_googlenet.caffemodel', caffe.TEST)
siamesenet = caffe.Net('./model/deploy.prototxt', './model/siamese.caffemodel', caffe.TEST)

for layerName in googlenet._layer_names:
    	print "Copying parameters for layer:",layerName
	try:
		W = googlenet.params[str(layerName)][0].data[...]
		b = googlenet.params[str(layerName)][1].data[...]

		siamesenet.params[str(layerName)+"_left"][0].data[...] = W
		siamesenet.params[str(layerName)+"_left"][1].data[...] = b
		siamesenet.params[str(layerName)+"_right"][0].data[...] = W
		siamesenet.params[str(layerName)+"_right"][1].data[...] = b
		print siamesenet.params[str(layerName)+"_left"][0].data[...]
		print "Layer",layerName,"parameters copied"
		
	except:
		print "Layer",layerName,"with no weights"
siamesenet.save('./model/siamese.caffemodel')

