import subprocess
import os
import re
import shutil
#subprocess.run(r"C:\Users\onoga\desktop\MyDocker\Git\origin\test\opencv_createsamples.exe -info C:\Users\onoga\desktop\MyDocker\Git\origin\test\pos\poslist.txt -vec C:\Users\onoga\desktop\MyDocker\Git\origin\test\vec\positive.vec -num 1000 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 ")
#subprocess.run(r"C:\Users\onoga\desktop\MyDocker\Git\origin\test\opencv_traincascade.exe -data C:\Users\onoga\desktop\MyDocker\Git\origin\test\cascade -vec C:\Users\onoga\desktop\MyDocker\Git\origin\test\vec\positive.vec -bg C:\Users\onoga\desktop\MyDocker\Git\origin\test\neg\neglist.txt -numPos 10 -numNeg 20")

#ファイルを一括リネーム
def rename(path,cas_name):
    
    count = 1
    file = os.listdir(path)
    
    for zname in file:
        under_name = os.path.splitext(zname)[1] #拡張子取得
        new_name = os.path.join(path,zname) #取得したファイル名を絶対パスに変更
 
        os.rename(new_name,os.path.join(path,f"{cas_name}{count}{under_name}"))#リネーム
        count +=1

#shutil.copyfile(r"C:\Users\onoga\Desktop\MyDocker\Git\sqlite\onogam\aaaaaaa.py",r"C:\Users\onoga\Desktop\aaaaaaa.py")
#print(os.listdir(r"C:\Users\onoga\Desktop\MyDocker\Git\origin\opencv_win_32bit"))
#print(os.path.split(r"C:\Users\onoga\Desktop\MyDocker\Git\origin\opencv_win_32bit"))

file = "onogami.tt"

print(".txt" in file)