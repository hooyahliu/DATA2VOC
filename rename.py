import os
import time
 
class BatchRename():
    '''
    对相应文件夹下的图片和xml文件按顺序批量命名
    图片与xml文件在同一个文件夹中
    '''
    def __init__(self):
        #图片路径
        self.path = ''you/images/and/xmls/path''
 
    def rename(self):
        filelist = os.listdir(self.path)

        #此处的排序可以使得图片和对应的xml文件被命名为同一个名字
        filelist.sort()
        total_num = len(filelist)
        i = 1071
        val_jpg=0
        val_xml=0
        n = 6
        for item in filelist:
            if item.endswith('.jpg'):
                n = 6 - len(str(i))
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(0)*n + str(i) + '.jpg')
                os.rename(src, dst)
                time.sleep(0.01)
                val_jpg=val_jpg+1
                print('converting %s to %s ...' % (src, dst))

            elif item.endswith('.xml'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(0)*n + str(i) + '.xml')
                os.rename(src, dst)
                time.sleep(0.01)
                val_xml=val_xml+1
                print('converting %s to %s ...' % (src, dst))
                i=i+1            
        print('total %d to rename & converted %d jpgs & %d xmls' % (total_num, val_jpg,val_xml))
 
if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
