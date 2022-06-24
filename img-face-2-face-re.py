# cat khuon mat tu anh- 1 anh:21/6-  ban Face_re 1 label
from asyncio.windows_events import NULL
from codecs import utf_8_encode
from copy import copy
from curses.ascii import *
from sys import maxsize
import numpy as np
import cv2
from matplotlib import pyplot as plt
import csv
import pandas as pd
import cv2
import os
from icrawler.builtin import GoogleImageCrawler
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mplImg
import dlib
import face_recognition


csv_columns = ['id','data','label']
csv_file = "E:\\1\\code\\PBL5_Computer_Sience\\z.csv"
with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()

t1=("id","data","label")

# cry-530-293
ok_c=0
raw_path=r'E:\\1\\code\\PBL5_Computer_Sience\\sleepgray\\' #sleep/cry/others(+gray)
window_name = 'Image'
save_path=r"E:\\1\\code\\PBL5_Computer_Sience\\sleepcut\\"#sleep/cry/others+cut
img_folder = os.listdir(raw_path)
for j in range(len(img_folder)):
    path = os.path.join(raw_path, img_folder[j])
    image = cv2.imread(path)
    if image is None:
        print('Wrong path:', path)
    else:
        print("0")
        face_locations = face_recognition.face_locations(image)
    try:
        for face_location in face_locations:
            top, right, bottom, left = face_location
            image = image[top:bottom, left:right]
            #image=cv2.resize(image,dsize=(500,500))
            os.chdir(save_path) 
            filename = img_folder[j]
            mplImg.imsave(filename,image)
            print("save_path")  
            print(os.path.join(save_path,img_folder[j]))  
            if os.path.join(save_path,img_folder[j])!=NULL:
                ok_c=ok_c+1
                print(ok_c)
            image_size=np.size(image)
            image=np.reshape(image,(image_size))
            image=str(list(image))
            image=image[1:-1]
            image=image.replace(",", " ")
            t2=(ok_c,image,'others')
            data=dict(zip(t1,t2))
            e=0
            try:
                with open(csv_file, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile,fieldnames=csv_columns)
                    writer.writerow(data)
            except IOError:
                print("I/O error")
    except:
        pass
print("tong file cry: ",len(img_folder))
print("so file cry cat dc: ",ok_c)             
# print("tong file others: ",len(img_folder))
# print("so file others cat dc: ",ok_o-ok_c)    
# print("tong file: ",len(img_folder))
# print("so file cat dc: ",ok_s-ok_c-ok_o)
# print("Tong file cat duoc:",ok_s)


    # with open ("E:\\1\\code\\PBL5_Computer_Sience\\filedata.csv","a",encoding=US) as file:
    #     writer = csv.writer(file)
    #     writer.writerows([str(ok_o), str(image),str("others")])
    #     file.close()