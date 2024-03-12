#删除数据集、挑战集中生成的结果

import os
import shutil

def main():
    root='./dataset'
    for dirpath, dirnames, filenames in os.walk(root):
        for dir in dirnames:
            if dir=='01_RES' or  dir=='02_RES':
                shutil.rmtree(os.path.join(dirpath,dir))#递归删除

if __name__=='__main__':
    main()

