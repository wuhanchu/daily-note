
import os
import os.path
import shutil

# 当前文件路径
print(__file__)
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
#
#
#def traversefile():
#    root = "/Users/wuhanchu/Project/dataknown/Z-Robot/01_src/spider/"
#    targetDir = "spider_temp"
#    shutil.rmtree(root+targetDir )
#    shutil.copytree( root+"spider", root+targetDir )
#    
#    for root, dirs, files in os.walk(root+targetDir):
#            path = root.split(os.sep)
#            for file in files:
#                if  file.endswith(".py") and "__" not in file:
#                    print(len(path) * '---',root, file)
#                    os.system("pyminifier  --obfuscate-import-methods  -o "+root+"/"+file+ " "+root+"/"+file)
#w
#
#traversefile()