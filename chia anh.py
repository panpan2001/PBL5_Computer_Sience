# chia anh ran dom ti le 7 2 1 train val test ban 22/6 - dung face_re - sua data-csv theo face_re di
# sua face_re cai luu dl theo haar roi dung cai face_re thay haar
# tum lai la lm hoan chinh 2 ban cang tot
import os
import random
import cv2

raw_path=r'E:\\1\\code\\PBL5_Computer_Sience\\othersgray\\' #sleep/cry/others(+gray)
save_path_train=r"E:\\image-gray-face-re\\train\\others\\"#sleep/cry/others+cut
save_path_test=r"E:\\image-gray-face-re\\test\\others\\"#sleep/cry/others+cut
save_path_val=r"E:\\image-gray-face-re\\val\\others\\"#sleep/cry/others+cut

img_folder = os.listdir(raw_path)
img_folder_2 = os.listdir(raw_path)

l_train=[]
l_test=[]
l_val=[]
num_train=round(len(img_folder)*0.7)
num_val=round(len(img_folder)*0.2)
num_test=len(img_folder)-num_train-num_val
#train
for i in range(num_train):
    a=random.choice(img_folder)
    img_folder.remove(a)
    l_train.append(a)
    print(l_train)
for j in range(len(l_train)):
    path = os.path.join(raw_path, l_train[j])
    image = cv2.imread(path)
    os.chdir(save_path_train) 
    filename = l_train[j]
    cv2.imwrite(filename,image) 
    print("save_path")  
    print(os.path.join(save_path_train,l_train[j]))  



for i in range(num_val):
    a=random.choice(img_folder)
    img_folder.remove(a)
    l_val.append(a)
for j in range(len(l_val)):
    path = os.path.join(raw_path, l_val[j])
    image = cv2.imread(path)
    os.chdir(save_path_val) 
    filename = l_val[j]
    cv2.imwrite(filename,image) 
    print("save_path")  
    print(os.path.join(save_path_val,l_val[j]))  


for i in range(num_test):
    a=random.choice(img_folder)
    img_folder.remove(a)
    l_test.append(a)
for j in range(len(l_test)):
    path = os.path.join(raw_path, l_test[j])
    image = cv2.imread(path)
    os.chdir(save_path_test) 
    filename = l_test[j]
    cv2.imwrite(filename,image) 
    print("save_path")  
    print(os.path.join(save_path_test,l_test[j]))  


print("len folder",len(img_folder_2))
print("len train",len(l_train))
print("len val",len(l_val))
print("len test",len(l_test))