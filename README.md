# Fashion-RecommendationSystem
<p>This is a fashion recommendation system which can be used by any e-commerce website. If this model is used in any e-commerce website they will get best recommendations of their product with 100% accuracy. Here I have used django for Web development purpose.</p>
<p>In the DataTrained Folder, There are all required files to train the machine and make .pkl files. I have used 1002 images to train the machine. There is also a excel file from where you can understand the schema of the database also. So 5 products will be given as recommendatios for a product. If we use more numbers of the images to train the model it will give us more accurate recommendations. ResNet algorithm is used to train the machine by using those images.</p>

<p><b>ResNet algorithm-</b>Residual Network (ResNet) is a deep learning model used for computer vision applications. It is a Convolutional Neural Network (CNN) architecture designed to support hundreds or thousands of convolutional layers. The layers are used to extract the features. Particularly we have used ResNet-50 algorithm here. So ResNet-50 is 50 layers deep. You can load a pretrained version of the neural network trained on more than a million images from the ImageNet database</p>

**➤ TECH USED :**
<p>HTML, CSS, BOOTSTRAP, JAVASCRIPT, JQUERY, DJANGO, PYTHON, MYSQL, NUMPY, PANDAS, TENSORFLOW, SKLEARN, PICKLE, JUPYTER NOTEBOOK, EXCEL</p>

### To run this website in your local computer follow the steps below and run the commands:

1. Clone this git repo->

   ```git
   git clone <gitRepoLink>
   ```
2. Go to the directory->

   ```git
   cd Fashion-RecommendationSystem
   ```
   
3. Put django secret key in the settings.py SECRET_KEY section.
   
4. Create virtual environment->
   
   ```python
   python -m venv <your_virtual_environment_name>
   ```
5. To activate virtual environment(windows)->

   ```python
   <your_virtual_environment_name>\Scripts\activate
   ```
   
6. Install dependencies(requirements.py file)->
   
   ```python
   pip install -r requirements.txt
   ```
7. Configure your database(I have used mysqlworkbench) or the default sqllite server can be used also->

   ```python
   DATABASES = {
        'default': {
            'ENGINE': '<yourDatabaseEngine>',
            'NAME': '<yourdatabasename>',
            'USER' : '<username>',
            'PASSWORD' : '<password>',
            'PORT':<yourportnumber>,
            'HOST' : '<yourhost>',
        }
    }
   ```
   <p>For better understanding go through settings.py where I have shared an example database configaration. I have created the database in mysql workbench. Writing the   
      credentials of the database in .env file and using that from that .env file will be a better practice</p>
   
8. Migrate database->

   ```python
   python manage.py makemigrations
   ```

   ```python
   python manage.py migrate
   ```
9. Data Upload->
   <p>As I have not shared the database file so The products and details have to be uploaded in the database. So for that create a database in mysql workbench and upload the 
    csvfile(dbtestSmall1000.csv in dataTrained folder) there. From that database the products will be recommended. The machine is trained by using that products. Extra 
    products can be added there as many as you can. This website will give recomendations from that extra product also</p>
   
10. Create superuser for accessing admin panel that the extraproducts or products can be added also from there->
    ```python
      python manage.py createsuperuser 
    ```

11. To run the application in local machine->
   
    ```python
    python manage.py runserver
    ```
#### Glimpses of the website:
   <p>Home page</p>
   <img src="https://i.ibb.co/0VTjPxs/screencapture-127-0-0-1-8000-2023-12-13-01-14-09.png" alt="screencapture-127-0-0-1-8000-2023-12-13-01-14-09" border="0">
   <p>Empty cart</p>
   <img src="https://i.ibb.co/Kr8W55T/screencapture-127-0-0-1-8000-cart-2023-12-13-02-06-48.png" alt="screencapture-127-0-0-1-8000-cart-2023-12-13-02-06-48" border="0">
   <p>Cart</p>
   <img src="https://i.ibb.co/k9JYsSY/screencapture-127-0-0-1-8000-cart-2023-12-13-02-09-58.png" alt="screencapture-127-0-0-1-8000-cart-2023-12-13-02-09-58" border="0">
   <p>According to cart in the previous picture, this website is giving recommendations. For each product we are giving 5 recommendations.</p>
   <img src="https://i.ibb.co/dGG9GKS/screencapture-127-0-0-1-8000-2023-12-13-02-10-58.png" alt="screencapture-127-0-0-1-8000-2023-12-13-02-10-58" border="0">
   <p>Recommending the products in the "you also can buy this items too" section depending the product which is clicked</p>
   <img src="https://i.ibb.co/9pL0hjf/screencapture-127-0-0-1-8000-product-detail-1542-2023-12-13-01-10-02.png" alt="screencapture-127-0-0-1-8000-product-detail-1542-2023-12-13-01-10-02" border="0">
   <img src="https://i.ibb.co/s1BWKT5/screencapture-127-0-0-1-8000-product-detail-1531-2023-12-13-01-02-18.png" alt="screencapture-127-0-0-1-8000-product-detail-1531-2023-12-13-01-02-18" border="0">
   <p>According the cart, Recommendations</p>
   <img src="https://i.ibb.co/4ZyGRbx/screencapture-127-0-0-1-8000-cart-2023-12-13-01-03-29.png" alt="screencapture-127-0-0-1-8000-cart-2023-12-13-01-03-29" border="0">
   <img src="https://i.ibb.co/TcpzFBL/screencapture-127-0-0-1-8000-2023-12-13-00-56-08.png" alt="screencapture-127-0-0-1-8000-2023-12-13-00-56-08" border="0">
   
