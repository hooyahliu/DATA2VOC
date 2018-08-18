'''
参照 https://github.com/pjreddie/darknet/blob/master/scripts/voc_label.py 更改
用于生成YOLO训练所用的train.txt,val.txt和test.txt
'''
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=['train','val','test']

classes = ["Vehicle"]


def convert(size, box):
    '''
    YOLO的bounding box计算
    '''
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

'''
需要的VOC数据集结构（可以先把文件夹创建好）：

--VOC
    |--Annotations
    |--ImageSets
        |--Main
    |--JPEGImages
    |--labels

Annotations:存放每张图片对应的xml文件，命名与对应的图片相同
JPEGImages:存放重命名后的原始图片
ImageSets:
    Main:存放目标检测数据，主要有train.txt, val.txt, trainval.txt, test.txt四个文件
labels:存放YOLO训练测试所需的每张图片的检测信息，为xml转换的txt文件，与对应图片重名
'''



def convert_annotation(image_id):
    '''
    PRCV给出的xml文件标签较为“奇特”
    convert_annatation()将PRCV的xml直接输出为YOLO用到的含有图片检测信息的txt
    而不是将PRCV的xml修改为VOC的xml（好啰嗦）
    '''
    in_file = open('./Annotations/%s.xml'%(image_id))
    out_file = open('./labels/%s.txt'%(image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('img_width').text)
    h = int(size.find('img_height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls_id = 0
        xmlbox = obj.find('bounding_box')

        #这里是“奇特”的标签转换+计算
        b = (float(xmlbox.find('x_left_top').text), (float(xmlbox.find('x_left_top').text)+float(xmlbox.find('width').text)), float(xmlbox.find('y_left_top').text), (float(xmlbox.find('y_left_top').text)+float(xmlbox.find('height').text)))
        bb = convert((w,h), b)

        #将xml转换成txt并保存，每张图片都有一个对应的txt
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd=getcwd()
for image_set in sets:
    image_ids = open('./ImageSets/Main/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        #在当前目录输出train.txt，val.txt，test.txt
        list_file.write('%s/JPEGImages/%s.jpg\n'%(wd,image_id))
        convert_annotation(image_id)
    list_file.close()

