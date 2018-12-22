##########
#从Annotations和JPEGImages中随机提取移动数量的jpg和xml文件
##########
import os
import time
import random
import numpy as np
import shutil

path1='./test/'
path2='./test/'

flist1=os.listdir(path1)
flist2=os.listdir(path2)

flist1.sort()
flist2.sort()

total_num=len(flist1)

rand_data= np.random.randint(total_num/2,size=2500)

file_out1=''
file_out2=''


print(len(rand_data))

if not os.path.exists('out'):
    os.makedirs('out')


for i in range(len(rand_data)):
    n=6-len(str(rand_data[i]))
    file_out1=path1+str(0)*n+str(rand_data[i])+'.xml'
    file_out2=path2+str(0)*n+str(rand_data[i])+'.jpg'
    shutil.copy(str(file_out1),"out")
    shutil.copy(str(file_out2),"out")
    print(i)


