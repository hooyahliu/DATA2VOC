import os
import time
import shutil
class BatchRename():
    '''
    对相应文件夹下的图片和xml文件按顺序批量命名
    图片与xml文件在同一个文件夹中
    '''
    def __init__(self):
        #图片路径
        self.path1 = './new'
        self.path2='./out'
 
    def rename(self):
        filelist = os.listdir(self.path1)
        filelist2=[]
        fileerr=[]
        #此处的排序可以使得图片和对应的xml文件被命名为同一个名字
        filelist.sort()
        total_num = len(filelist)
        i = 0
        val_jpg=0
        val_xml=0
        n = 6



        for item in filelist:
            if item.endswith('jpg'):
                filelist2.append(item)

        for item in filelist2:
            jpgname=str(item)[-10:-4]
            xmlname=jpgname

            n = 6 - len(str(i))
            src1 = os.path.join(os.path.abspath(self.path1), item)
            dst1 = os.path.join(os.path.abspath(self.path2), str(0)*n + str(i) + '.jpg')
            print('converting %s to %s ...' % (src1, dst1))
            #os.rename(src1, dst1)
            shutil.copyfile(src1,dst1)
            time.sleep(0.01)

            src2 = os.path.join(os.path.abspath(self.path1), xmlname + '.xml')
            dst2 = os.path.join(os.path.abspath(self.path2), str(0)*n + str(i) + '.xml')
            print('converting %s to %s ...' % (src2, dst2))
            #os.rename(src2, dst2)
            shutil.copyfile(src2,dst2)
            time.sleep(0.01)
            i=i+1

                

            
        print('total %d to rename' %(i))
 
if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()