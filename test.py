from training_pairs_generator import pairs

class tester():
	def __init__(self):
		print "Tester initialized"
		
	def get_testing_data(self, path, noOfExamples):
		testPairsGenerator = pairs(path, noOfExamples, noOfExamples)
		testPairsGenerator.get_all_images_in_lists()
		pairsList = testPairsGenerator.create_pairs()
		return pairsList
	
	def testSiamese(self, testList):
		
	def testInceptionFeatures(self, testList):
	


#------------------------------------------------------------------
def main():
	siameseTester = tester()
	testList = siameseTester.get_testing_data("/media/jedrzej/SAMSUNG/DATA/ILSVRC2012/TRAIN/", 50)


if __name__ == "__main__":
    main()
