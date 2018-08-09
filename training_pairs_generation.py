from glob import glob
import numpy as np
import random
import argparse
import os

class pairs():
	def __init__(self, imagesPath, noOfPositiveExamples, noOfNegativeExamples, imgExtension = "JPEG"):
		self.imagesPath = imagesPath				# path of a directory where are folders with images (each folder - different category)
		self.noOfPositiveExamples = noOfPositiveExamples	# number of positive ("same") examples per category
		self.noOfNegativeExamples = noOfNegativeExamples	# number of negative ("different") examples per category
		self.imgExtension = imgExtension			# image extension format (.jpg, .JPEG etc)

	def get_all_images_in_lists(self):
		self.images = []
		folderList = glob(self.imagesPath+'*/')
		for folder_i, folder in enumerate(folderList):
			imgPathList = glob(folder+'*'+self.imgExtension)
			self.images.append(imgPathList)
		self.noOfCategories = len(self.images)

	def get_random_two_images(self, listA, listB):
		imageA = np.random.choice(listA)
		imageB = np.random.choice(listB)
		# make sure they are not the same image:
		while(imageA==imageB):
			imageB = np.random.choice(listB)

		return "/".join(imageA.split("/")[-2:]), "/".join(imageB.split("/")[-2:])

	def create_pairs(self):
		# returns 2D list of the format "[pathToImageA, pathToImageB, label]"
		
		pairsList = []	# empty list for all the information
		# iterate through all the categories in the dataset:
		for i in xrange(self.noOfCategories):
			print "Class", i+1,"out of", self.noOfCategories
			negativeCategoriesList = np.delete(np.arange(0,self.noOfCategories),i)

			# get "noOfPositiveExamples" of pairs with label "1":
			for k in xrange(self.noOfPositiveExamples):
				imageA, imageB = self.get_random_two_images(self.images[i], self.images[i])
				pairsList.append([imageA,imageB,"1"])

			# get "noOfNegativeExamples" of pairs with label "0":
			for k in xrange(self.noOfNegativeExamples):
				j = np.random.choice(negativeCategoriesList)
				imageA, imageB = self.get_random_two_images(self.images[i], self.images[j])
				pairsList.append([imageA,imageB,"0"])
		return pairsList

	def split_list_into_four_textfiles(self, pairsList, txtFilesDir = "./txtFiles/"):
		trainFileLeft = ""
		trainFileRight = ""
		valFileLeft = ""
		valFileRight = ""
		random.shuffle(pairsList)	# shuffle list of pairs
		for line in pairsList:
			# choose randomly if it's a val or train case (split 70/30):
			if(random.random()>0.3):
				trainFileLeft+= line[0]+" "+line[2]+"\n"	# first image path + label
				trainFileRight+= line[1]+" "+line[2]+"\n"	# second image path + label
			else:
				valFileLeft+= line[0]+" "+line[2]+"\n"		# first image path + label
				valFileRight+= line[1]+" "+line[2]+"\n"		# second image path + label

		# Save all four files:
		if(not os.path.exists(txtFilesDir)):
			os.makedirs(txtFilesDir)		# create the folder if one does not exist
		f = open(txtFilesDir+"train_left.txt","w")
		f.write(trainFileLeft)
		f.close()
		f = open(txtFilesDir+"train_right.txt","w")
		f.write(trainFileRight)
		f.close()
		f = open(txtFilesDir+"val_left.txt","w")
		f.write(valFileLeft)
		f.close()
		f = open(txtFilesDir+"val_right.txt","w")
		f.write(valFileRight)
		f.close()
			

#------------------------------------------------------------------

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--dir',
		type=str,
		default="",
		help="Directory where are stored images (folders of images)"
		)
	parser.add_argument(
		'--examples',
		type=int,
		default=100,
		help="Number of positive examples per category"
		)
	parser.add_argument(
		'--txt_dir',
		type=str,
		default="./txtFiles/",
		help="Directory where text files will be saved"
		)
	FLAGS = parser.parse_args()
	trainingPairsGenerator = pairs(FLAGS.dir, FLAGS.examples, FLAGS.examples)
	trainingPairsGenerator.get_all_images_in_lists()
	pairsList = trainingPairsGenerator.create_pairs()
	trainingPairsGenerator.split_list_into_four_textfiles(pairsList, FLAGS.txt_dir)


