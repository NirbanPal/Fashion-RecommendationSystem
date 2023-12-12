# Fashion-RecommendationSystem
<p>This is a fashion recommendation system which can be used by any e-commerce website. If this model is used in any e-commerce website they will get best recommendations of their product with 100% accuracy. Here I have used django for Web development purpose.</p>
<p>In the DataTrained Folder, There are all required files to train the machine and make .pkl files. I have used 1002 images for tranning the machine. There is also a excel file from where you can understand the schema of the database also.</p>

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
            'PORT':<yourport>,
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

 






   
