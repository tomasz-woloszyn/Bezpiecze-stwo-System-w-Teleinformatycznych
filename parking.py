import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import random

################MATH VAL#################
mu = 3523
sigma = 21.9
#########################################

#################MY VAL##################
nr_trials = 12000
nr_helicopter = 0
nr_values = 1200000
wide = 100.0
high = 100.0
k = 1
x = 0
y = 0
#counter = 0
#
wide_len = []
high_len = []
succ = list()


#########################################

#		TO DO -> NASZ PLIK WARTOSCI		#

#data_2 = open("file.bin", "rb")
#data = np.fromfile(data_2, dtype=np.uint32)
       
#for i in data:
#    if counter % 2:
#        high_len.append(round(np.uint32(i)/256 * 100))
#    else:
#        wide_len.append(round(np.uint32(i)/256 * 100))
#   counter += 1

####################RAND#################

for i in range(0, nr_values):
    wide_len.append(random.random()  * wide)

for i in range(0, nr_values):
    high_len.append(random.random()  * high)



for nr_test in range(0, 10):
    nr_succ = 0
    wide_heli_parkd = []
    high_heli_parkd = []
    for i in range(nr_helicopter, nr_helicopter+nr_trials):
        crash = False
        x = wide_len[i]
        y = high_len[i]

        for j in range(0, len(wide_heli_parkd)):
            if abs(x - wide_heli_parkd[j]) <= 1.0 and abs(y - high_heli_parkd[j]) <= 1.0:
                crash = True
                #print(i, j, x, y, wide_heli_parkd[j], high_heli_parkd[j])
                break

        if not crash:
            wide_heli_parkd.append(x)
            high_heli_parkd.append(y)
            nr_succ += 1

    nr_helicopter += nr_trials
    succ.append((nr_succ - mu) / sigma)
    print(nr_test, nr_succ)
print(succ)
print("P VALUE:")
print(stats.kstest(succ, 'norm'))