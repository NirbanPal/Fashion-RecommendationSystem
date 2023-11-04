from django.shortcuts import render,redirect
from django.db.models import Q
from .models import *

# machine learning stuffs
import pickle
import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from numpy.linalg import norm
from tensorflow.keras.layers import GlobalMaxPooling2D
from sklearn.neighbors import NearestNeighbors
import re

#machine learning model creation
feature_list= np.array(pickle.load(open('embeddings.pkl','rb')))
filenames=pickle.load(open('filenames.pkl','rb'))

model=ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
model.trainable=False

model=tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])



# Create your views here.
def index_page(request):
    top_wear = Product.objects.filter(subCategory = 'Topwear')[:40]
    bottom_wear = Product.objects.filter(subCategory = 'Bottomwear')[:40]
    shoes = Product.objects.filter(subCategory = 'Shoes')[:40]
    summer_wear=Product.objects.filter(season='Summer')[:40]
    cartProd=Cart.objects.all()
    recom_list_cart=[]
    if cartProd:
        all_ids=[]
        for i in cartProd:
            all_med="media/"+str(i.product_id.product_image)
            # product_poslist.append(all_med)
            img=image.load_img(all_med, target_size=(224,224))
            img_array = image.img_to_array(img)
            expanded_img_array = np.expand_dims(img_array, axis=0)
            preprocessed_img = preprocess_input(expanded_img_array)
            result=model.predict(preprocessed_img).flatten()
            normalized_result=result/norm(result)
            neighbors =NearestNeighbors(n_neighbors=7,algorithm='brute',metric='euclidean')
            neighbors.fit(feature_list)
            distances,indices=neighbors.kneighbors([normalized_result])

            n_array=[]
            for file in indices[0]:
                # print(filenames[file])
                n_array.append(filenames[file])
            for pos in n_array:
                pattern = r'\\(\d+)\.jpg'
                match = re.search(pattern, pos)
                number = match.group(1)
                all_ids.append(int(number))
        for fid in all_ids:
            pro=Product.objects.get(id=fid)
            recom_list_cart.append(pro)

        context={
            'top_wear':top_wear,
            'bottom_wear':bottom_wear,
            'shoes':shoes,
            'summer_wear':summer_wear,
            'in_cart':recom_list_cart,
        }
        return render(request,"home.html",context)
    else:
        context={
            'top_wear':top_wear,
            'bottom_wear':bottom_wear,
            'shoes':shoes,
            'summer_wear':summer_wear,
            'in_cart':recom_list_cart,
        }
        return render(request,"home.html",context)


def productdetails(request,id):
    prod_desc=Product.objects.get(id=id)
    prod_pos_str=str(prod_desc.product_image)
    # print(prod_pos_str)
    all_med="media/"+prod_pos_str
    # print(all_med)



    #machine learning 
    img=image.load_img(all_med, target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result=model.predict(preprocessed_img).flatten()
    normalized_result=result/norm(result)

    neighbors =NearestNeighbors(n_neighbors=7,algorithm='brute',metric='euclidean')
    neighbors.fit(feature_list)

    distances,indices=neighbors.kneighbors([normalized_result])
    # print(indices)

    n_array=[]
    for file in indices[0]:
        # print(filenames[file])
        n_array.append(filenames[file])

    id_list=[]
    for pos in n_array:
        pattern = r'\\(\d+)\.jpg'
        match = re.search(pattern, pos)
        number = match.group(1)
        id_list.append(int(number))
    
    recom_list=[]
    for fid in id_list:
        pro=Product.objects.get(id=fid)
        recom_list.append(pro)

    context={
        'prod_desc':prod_desc,
        'recom_list':recom_list,
    }
    return render(request,"productdetails.html",context)

def add_to_cart(request,id):
    prod_id=Product.objects.get(id=id)
    Cart(product_id=prod_id).save()
    return redirect('/cart')

def showcart(request):
    cartProd=Cart.objects.all()

    if cartProd:
        context={
            'cartProd':cartProd,
        }
        return render(request,"cart.html",context)
    else:
        context = {
            'empty_cart': 'Your Cart Is Empty.Please Add Products'
        }
        return render(request,'cart.html',context)






    

