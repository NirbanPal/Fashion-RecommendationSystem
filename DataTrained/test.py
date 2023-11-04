import pickle
import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from numpy.linalg import norm
from tensorflow.keras.layers import GlobalMaxPooling2D
from sklearn.neighbors import NearestNeighbors
import re

feature_list= np.array(pickle.load(open('embeddings.pkl','rb')))
filenames=pickle.load(open('filenames.pkl','rb'))

model=ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
model.trainable=False

model=tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])


img=image.load_img("tesingimg/1165.jpg", target_size=(224,224))
img_array = image.img_to_array(img)
expanded_img_array = np.expand_dims(img_array, axis=0)
preprocessed_img = preprocess_input(expanded_img_array)
result=model.predict(preprocessed_img).flatten()
normalized_result=result/norm(result)

neighbors =NearestNeighbors(n_neighbors=8,algorithm='brute',metric='euclidean')
neighbors.fit(feature_list)

distances,indices=neighbors.kneighbors([normalized_result])
# print(indices)

n_array=[]
for file in indices[0]:
    print(filenames[file])
    # temp_img=cv2.imread(filenames[file])
    # cv2.imshow('output',cv2.resize(temp_img,(512,512)))
    # cv2.waitKey(0)
    n_array.append(filenames[file])

id_list=[]
for pos in n_array:
    pattern = r'\\(\d+)\.jpg'
    match = re.search(pattern, pos)
    number = match.group(1)
    id_list.append(int(number))
print(id_list)



