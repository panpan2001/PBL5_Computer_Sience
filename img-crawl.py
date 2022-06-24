# cat khuon mat tu anh- 1 anh:22/6-  ban Face_re- 3label
from asyncio.windows_events import NULL
from asyncore import write
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

#ad header
csv_columns = ['id','data','label']
csv_file = "E:\\1\\code\\PBL5_Computer_Sience\\data-csv-face-re.csv"
with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
t1=("id","data","label")

#duong dan thu muc luu anh    
# window_name = 'Image'
# save_path=r"E:\\1\\code\\PBL5_Computer_Sience\\photo-face-re\\"#sleep/cry/others+cut

# nhan sleep
raw_path_sleep=r'E:\\1\\code\\PBL5_Computer_Sience\\sleepgray\\' #sleep/cry/others(+gray)
save_path=r"E:\\1\\code\\PBL5_Computer_Sience\\sleep-cut-face-re\\"#sleep/cry/others+cut

img_folder_sleep = os.listdir(raw_path_sleep)
ok_s=0
for j in range(len(img_folder_sleep)):
    path = os.path.join(raw_path_sleep, img_folder_sleep[j])
    image = cv2.imread(path)
    if image is None:
        print('Wrong path:', path)
        break
    else:
        try:
            face_locations = face_recognition.face_locations(image)
            #nhan dien khuon mat
            for face_location in face_locations:
                top, right, bottom, left = face_location
                image = image[top:bottom, left:right]
                image=cv2.resize(image,dsize=(500,500))
                #luu anh vao thu muc
                os.chdir(save_path) 
                filename = img_folder_sleep[j]# neu luu 1 folder photo-face-re thi them o-s-c de phan biet- neu rieng thi thoi
                mplImg.imsave(filename,image)
                print("save_path")  
                print(os.path.join(save_path,img_folder_sleep[j]))  
                if os.path.join(save_path,img_folder_sleep[j])!=NULL:
                    ok_s=ok_s+1
                    print("file luu duoc so:",ok_s)
                #ghi dl vao csv
                image_size=np.size(image)
                image=np.reshape(image,(image_size))
                image=str(list(image))
                image=image[1:-1]
                image=image.replace(",", " ")
                t2=(ok_s,image,'others')
                data=dict(zip(t1,t2))                
                try:
                    with open(csv_file, 'a') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                            writer.writerow(data)
                except IOError:
                    print("I/O error")
        except:
            break
                    
# nhan cry
raw_path_cry=r'E:\\1\\code\\PBL5_Computer_Sience\\crygray\\' #sleep/cry/others(+gray)
save_path=r"E:\\1\\code\\PBL5_Computer_Sience\\cry-cut-face-re\\"#sleep/cry/others+cut
img_folder_cry = os.listdir(raw_path_cry)
ok_c=ok_s
for j in range(len(img_folder_cry)):
    path = os.path.join(raw_path_cry, img_folder_cry[j])
    image = cv2.imread(path)
    if image is None:
        print('Wrong path:', path)
        break
    else:
        try:
            face_locations = face_recognition.face_locations(image)
            #nhan dien khuon mat
            for face_location in face_locations:
                top, right, bottom, left = face_location
                image = image[top:bottom, left:right]
                image=cv2.resize(image,dsize=(500,500))
                #luu anh vao thu muc
                os.chdir(save_path) 
                filename = img_folder_cry[j]
                mplImg.imsave(filename,image)
                print("save_path")  
                print(os.path.join(save_path,img_folder_cry[j]))  
                if os.path.join(save_path,img_folder_cry[j])!=NULL:
                    ok_c=ok_c+1
                    print("file luu duoc so:",ok_c)
                #ghi dl vao csv
                image_size=np.size(image)
                image=np.reshape(image,(image_size))
                image=str(list(image))
                image=image[1:-1]
                image=image.replace(",", " ")
                t2=(ok_c,image,'others')
                data=dict(zip(t1,t2))
                try:
                    with open(csv_file, 'a') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                            writer.writerow(data)
                except IOError:
                    print("I/O error")                
        except:
            break           
        
# nhan others
raw_path_others=r'E:\\1\\code\\PBL5_Computer_Sience\\othersgray\\' #sleep/cry/others(+gray)
save_path=r"E:\\1\\code\\PBL5_Computer_Sience\\others-cut-face-re\\"#sleep/cry/others+cut
img_folder_others = os.listdir(raw_path_others)
ok_o=ok_c
for j in range(len(img_folder_others)):
    path = os.path.join(raw_path_others, img_folder_others[j])
    image = cv2.imread(path)
    if image is None:
        print('Wrong path:', path)
        break
    else:
        try:
            face_locations = face_recognition.face_locations(image)
            #nhan dien khuon mat
            for face_location in face_locations:
                top, right, bottom, left = face_location
                image = image[top:bottom, left:right]
                image=cv2.resize(image,dsize=(500,500))
                #luu anh vao thu muc
                os.chdir(save_path) 
                filename = img_folder_others[j]
                mplImg.imsave(filename,image)
                print("save_path")  
                print(os.path.join(save_path,img_folder_others[j]))  
                if os.path.join(save_path,img_folder_others[j])!=NULL:
                    ok_o=ok_o+1
                    print("file luu duoc so:",ok_o)
                #ghi dl vao csv
                image_size=np.size(image)
                image=np.reshape(image,(image_size))
                image=str(list(image))
                image=image[1:-1]
                image=image.replace(",", " ")
                t2=(ok_o,image,'others')
                data=dict(zip(t1,t2))
                try:
                    with open(csv_file, 'a') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                            writer.writerow(data)
                except IOError:
                    print("I/O error")                
        except:
            break  
                 
# xuat ket qua 
print("tong file sleep: ",len(img_folder_sleep))
print("so file sleep cat dc: ",ok_s)               
print("tong file cry: ",len(img_folder_cry))
print("so file cry cat dc: ",ok_c-ok_s)             
print("tong file others: ",len(img_folder_others))
print("so file others cat dc: ",ok_o-ok_c)   
print("tong file sleep + cry + others: ",len(img_folder_sleep)+len(img_folder_cry)+len(img_folder_others))
print("Tong file cat duoc:",ok_o)        