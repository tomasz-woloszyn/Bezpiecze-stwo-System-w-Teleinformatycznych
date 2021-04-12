import numpy as np
import matplotlib.pyplot as plt
import math
import imageio
import PIL
import scipy as sp
from scipy.stats import entropy as esp

def entropy(labels):
    prob_dict =np.zeros(256)
    for x in range(len(labels)):
        prob_dict[labels[x]]=prob_dict[labels[x]]+1
    entr=esp(prob_dict, base=2)
    return entr


##100 000 numbers generator
Data=[]
Raw=[]
for counter in range(3):
    PhotoName=("photo",str(counter),".bmp.")
    PhotoName="".join(PhotoName)
    Photo=PIL.Image.open(PhotoName)
    Photo=Photo.resize((512,512))
    #Photo.show()
    PhotoConverted=Photo.convert(mode="1",dither=PIL.Image.FLOYDSTEINBERG)
    #PhotoConverted.show()
    a = np.asarray(PhotoConverted)


  
    c=0
    d=0
    for x in range(512):
        for y in range(512):
            c+=1
            d+=int(a[[x],[y]])
            if c != 8:
                d=d<<1
            if c == 8:
                c=0
                #print(d)
                Raw.append(d)
                d=0




    p=2
    q=2
    A=np.array([[1,p],[q,((p*q)+1)]])
    PhotoInPost=np.array(a)
    PhotoAfterPost=np.array(PhotoInPost)

    for i in range(7):
        for x in range(512):
            for y in range(512):
                temp=np.array([[x],[y]])
                b=A.dot(temp)
                b[[0],[0]]=(b[[0],[0]] % 512)
                b[[1],[0]]=(b[[1],[0]] % 512)
                PhotoAfterPost[[b[[0],[0]]],[b[[1],[0]]]]=PhotoInPost[[x],[y]]
        PhotoInPost=PhotoAfterPost       

    #DisplayImg=PIL.Image.fromarray(PhotoAfterPost,mode="1")
    #DisplayImg.show()



    
    c=0
    d=0
    for x in range(512):
        for y in range(512):
            c+=1
            d+=int(PhotoAfterPost[[x],[y]])
            if c != 8:
                d=d<<1
            if c == 8:
                c=0
                #print(str(d)+'\n')
                Data.append(d)
                d=0

DataToSave=np.array(Data)
output_file = open('file.bin', 'wb')
DataToSave.tofile(output_file)
output_file.close()

#print("Ilość cyfr:",len(Data))
print("Surowe Dane ze źródła przed postprocesingiem:")
#figImage , his = plt.subplots()
#bins=255

ProbRaw, bins, patches = plt.hist(Raw,bins=255,range=[0,255],density=True)
print(esp(ProbRaw,base=2))


print("Dane po całym procesie")


#figImage , his = plt.subplots()





ProbDat, bins, patches = plt.hist(Data,bins=255,range=[0,255],density=True)
print(esp(ProbDat,base=2))

