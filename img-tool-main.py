# crawl anh va chuyen xam, luu vao thu muc - last version
import icrawler
import cv2
import os
from icrawler.builtin import GoogleImageCrawler
import numpy as np
# 25/5 version
#crawl anh
# google_crawler = GoogleImageCrawler(storage={'root_dir': 'babysad'})
# google_crawler.crawl(keyword='baby sad', max_num=100)

#chuyen anh xam va luu anh
raw_path=r'E:\\1\\code\\PBL5_Computer_Sience\\cry\\' 
window_name = 'Image'
save_path=r"E:\\1\\code\\PBL5_Computer_Sience\\crygray\\"

img_folder = os.listdir(raw_path)#trả về một danh sách chứa các tên va dinh dang của các file trong thư mục đã cho bởi path.
print(img_folder)
for j in range(len(img_folder)):
    path = os.path.join(raw_path, img_folder[j])#noi duong dan thanh ten duong dan toi file anh
    image = cv2.imread(path)# doc duong dan
    if image is None:
        print('Wrong path:', path)
    else:
        print("0")
    path=raw_path
    image = cv2.resize(image, dsize=(500,500))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    os.chdir(save_path) #thay đổi thư mục làm việc hiện tại thành đường dẫn được chỉ định. Nó chỉ lấy một đối số duy nhất làm đường dẫn thư mục mới.
    file=img_folder[j].split(".")
    if file[1]!="jpg":
       img_folder[j]=file[0]+".jpg"
    filename = img_folder[j]
    cv2.imwrite(filename,image) # lưu hình ảnh vào bất kỳ thiết bị lưu trữ nào
    print("save_path")  
    print(os.path.join(save_path,img_folder[j]))  # noi thanh duong dan toi noi can luu file anh

