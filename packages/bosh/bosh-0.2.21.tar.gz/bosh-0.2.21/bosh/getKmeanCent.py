#!/usr/bin/python
import sys
import numpy as np
import re

def get_kmean_centroid(tmp_file_name='./centroids.txt'):
	a = np.loadtxt(tmp_file_name, dtype=np.float)
	#print(re.sub('[\[\]]', '', np.array_str(a)))
	#print ' '.join(str(n) for n in a)
	res_str = "\n".join([",".join([str(wtf) for wtf in p]) for p in a])
	print res_str
	#print ' '.join(map(str, a))

if __name__ == "__main__":
	tmp_file = './centroids.txt'
	if len(sys.argv) > 1:
		tmp_file = sys.argv[1]
	get_kmean_centroid(tmp_file)
