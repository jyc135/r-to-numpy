import sys
sys.path.insert(0, '/Users/justin/Documents/E4E/r-to-numpy/src/')
import r_to_numpy as rnump

data_dir = "/Users/justin/Documents/E4E/coraldata/"
data_file = "HAW_2016_48.Rdata"

if __name__ == "__main__":
    data = rnump.readRFileToNumpy(data_dir + data_file, debug = True)
