#!/bin/sh

# 提示信息
echo "start:"

# 定义变量
pst=.jpg

# 复制文件到目标文件夹
cp ./train_data/*/image/*$pst /home/lthpc/liuhy/PRCV/YOLO_data/image

pst2=.xml

cp ./train_data/*/xml/*$pst2 /home/lthpc/liuhy/PRCV/YOLO_data/image

