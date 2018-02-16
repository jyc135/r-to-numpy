import numpy as np
import rpy2.robjects as ro
import sys
import os

usage_message = ("Usage: python " + os.path.basename(__file__) + "[file] [var_name]\n"
	"  [file]     the .Rdata file containing R workspace objects\n"
	"  [var_name] name of matrix variable in the R workspace(optional)")
	

#reads in .Rdata file into a numpy array 
def readRFileToNumpy(dataFilePath, varname = ''):
	data_dir = (os.path.abspath(os.path.dirname(dataFilePath)))
	dataFile = (os.path.basename(dataFilePath))

	ro.r('setwd("' + data_dir + '")')
	ro.r('load("'+ dataFile +'")')

	dataName = varname
	if(varname == ''):
		ls = str(ro.r('ls()'))
		startIndex = str.find(ls, '"') + 1
		endIndex = str.find(ls, '"', startIndex + 1)
		dataName = ls[startIndex:endIndex]

	rows = rToInt(ro.r('dim(' + dataName + ')[1]'))
	cols = rToInt(ro.r('dim(' + dataName + ')[2]'))

	data = np.zeros((rows, cols))
	
	for i in range(0, rows): 
		for j in range(0, cols):
			data[i, j] = getDataAt(dataName, i + 1, j + 1)

	return data

#gets the data point at a certain point in the matrix (in R)
def getDataAt(dataName, i, j):
	data = ro.r(dataName + '[' + str(i) + ', ' + str(j) + ']')
	return rToInt(data)
	
#converts R output to a String, removing the numbered prefix
def rToString(rOutput):
	outputString = str(rOutput)
	start = str.find(outputString, ']') + 2
	return outputString[start:]

#converts R output to an int
def rToInt(rOutput):
	return int(rToString(rOutput))

if __name__ == "__main__":
	numArgs = len(sys.argv)
	data = None
	if(numArgs == 2):
		data = readRFileToNumpy(sys.argv[1])
	elif(numArgs == 3):	
		data = readRFileToNumpy(sys.argv[1], sys.argv[2])
	else:
		print(usage_message)
		sys.exit(0)
	print(data)

