# notes-api
api for personal notes app

to run the app you have two ways manual or by having dockcer installed

if you have docker installed just run the following command
```console
docker-compose up -d --build
```
antoher option is by having python installed
run the following commands
```console
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
after running the application you can go to the following url:</p>
http://127.0.0.1:8000/
</p>
you will see the swagger page like this:
</p>
![photo_2023-02-09_20-08-57](https://user-images.githubusercontent.com/53129045/217887535-8e4192d6-6115-44b1-a555-4983c22e9c75.jpg)
</p>
to use the api you need to register an account and get the key
the authorize with it in the swagger page like the following screen:</p>
![image](https://user-images.githubusercontent.com/53129045/217888184-00a223cd-02f2-494f-967c-46ecf392f6a7.png)
</p>
then you can use the /notes end points:
</p>
GET /notes/ to get all pf your notes
</p>
POST /notes/ to create a new note
</p>
GET /notes/{id}/ retrieve specific note by id
</p>
DELETE /notes/{id}/ delete note by it's id
</p>
note: you can only access your user notes and delete them
