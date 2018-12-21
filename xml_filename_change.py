import xml.etree.ElementTree as ET
import time 
import os

path = '.'
filelist = os.listdir(path)
filelist.sort()
i=1
for item in filelist:
    if item.endswith('.xml'):
        tree=ET.parse(item)
        root=tree.getroot()


        root.find('folder').text='Four_Class'
        root.find('filename').text=str(item)

        for ele1 in root.findall('object'):
            ele1.find('name').text='Civilian'

        tree.write(item)
        print('total= %d',i)
        print('%s is changed'%item)
        i=i+1

