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
   cd <directory>
   ```
   
3. Put your django secret key in the settings.py SECRET_KEY section.
   
4. Create virtual environment->
   
   ```python
   python -m venv <your_virtual_environment_name>
   ```
5. To activate your virtual environment(windows)->

   ```python
   <your_virtual_environment_name>\Scripts\activate
   ```
   
6. Install dependencies(requirements.py file)->
   
   ```python
   pip install -r requirements.txt
   ```

7. Migrate your database->

   ```python
   python manage.py makemigrations
   ```

   ```python
   python manage.py migrate
   ```

8. To run the application in your local machine->
   
   ```python
   python manage.py runserver
   ```

 






   
