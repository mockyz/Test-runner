import os,sys
import time

def  changeVersion():

    find_str = "VERSION"
    replace_str = "VERSION = " + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    with open("sourcing.py", "r", encoding="utf-8") as f, open("test.py", "w", encoding="utf-8") as f_new:  # 打开源文件并创建一个新文件
        for line in f:
            if find_str == line[0:6] :
                line = replace_str
            f_new.write(line)



if __name__ == '__main__':
    changeVersion()
