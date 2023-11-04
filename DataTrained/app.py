import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
import numpy as np
from numpy.linalg import norm
import os
from tqdm import tqdm
import pickle


# standard size of an image in transfer learning is 224,224,3
#include_top=False means here we are removing top layer to put our own top layer
model=ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
#trainable false means we are using pre trianed model(ResNet) we are not going to train that model.
model.trainable=False

#here we have added our top layer (GlobalMaxPooling2D)
#cnn-->working of maxpooling layer
model=tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])
# print(model.summary())
def extract_features(img_path,model):
    img=image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims (img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result=model.predict(preprocessed_img).flatten()
    normalized_result=result/norm(result)
    return normalized_result


filenames=[]
for file in os.listdir('images'):
    filenames.append(os.path.join('images',file))
# print(os.listdir('images'))
# print(len(filenames))
# print(filenames[0:5])

feature_list=[]
for file in tqdm(filenames):
    feature_list.append(extract_features(file,model))

# print(np.array(feature_list).shape)

pickle.dump(feature_list,open('embeddings.pkl','wb'))
pickle.dump(filenames,open('filenames.pkl','wb'))







