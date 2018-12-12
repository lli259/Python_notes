from keras.datasets import mnist
import cv2,glob
import matplotlib.pyplot as plt
import numpy as np
(x_train, y_train), (x_test, y_test) = mnist.load_data()
first=x_train[0]
print(first[6])
plt.subplot(131)
plt.imshow(first,cmap=plt.get_cmap('gray'))
second=[]
for i in range(len(first[0])):
    tem=[]
    for j in range(len(first[1])):
        tem.append(first[i][j])
    tem=[255.0 if m>0 else 0.0 for m in tem]
    second.append(tem)
plt.subplot(132)
plt.imshow(second)

third=cv2.resize(np.array(second),(100,100),interpolation=cv2.INTER_CUBIC)
plt.subplot(133)
plt.imshow(third,cmap=plt.get_cmap('gray'))

plt.show()
'''
images=glob.glob("F*.png")
print(images)
for image in images:
    img=cv2.imread(image,0)
    print(img)
    plt.imshow(img)
    plt.show()
'''
