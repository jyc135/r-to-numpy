import numpy as np
import rpy2.robjects as ro
import sys
import os

usage_message = "Usage: python " + os.path.basename(__file__) + " [file]"

dataName = 'all_classes'

#reads in .Rdata file into a numpy array 
def readRFileToNumpy(dataFilePath):
	data_dir = (os.path.abspath(os.path.dirname(dataFilePath)))
	dataFile = (os.path.basename(dataFilePath))

	r('setwd("' + data_dir + '")')
	r('load("'+ dataFile +'")')

	ls = str(r('ls()'))
	startIndex = str.find(ls, '"') + 1
	endIndex = str.find(ls, '"', startIndex + 1)
	dataName = ls[startIndex:endIndex]

	rows = rToInt(r('dim(' + dataName + ')[1]'))
	cols = rToInt(r('dim(' + dataName + ')[2]'))

	rows = 5;
	cols = 5;

	data = np.zeros((rows, cols))
	
	for i in range(0, rows): 
		for j in range(0, cols):
			data[i, j] = getDataAt(i + 1, j + 1)

	return data

#gets the data point at a certain point in the matrix (in R)
def getDataAt(i, j):
	data = r(dataName + '[' + str(i) + ', ' + str(j) + ']')
	return rToInt(data)
	
#runs an R command
def r(command):
	return ro.r(command)

#converts R output to a String, removing the numbered prefix
def rToString(rOutput):
	outputString = str(rOutput)
	start = str.find(outputString, ']') + 2
	return outputString[start:]

#converts R output to an int
def rToInt(rOutput):
	return int(rToString(rOutput))

if __name__ == "__main__":
	if(len(sys.argv) != 2):
		print(usage_message)
		sys.exit(0)
	inputFile = sys.argv[1]
	print(readRFileToNumpy(inputFile))
