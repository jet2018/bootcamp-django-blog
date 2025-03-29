Set up:

 - Intall the dependencies
	
```sh
pip install -r requirements.txt
```

Run migrations

```sh
python manage.py migrate
```

Add your changes as you see fit

If your changes are oon the models, makemigrations and migrate accondingly

Makemigrations:

```sh
python manage.py makemigrations
```

Migrate

```sh
python manage.py migrate
```
 
Runserver

```sh
python manage.py runserver
```

Navigate to `http://localhost:8000/admin` for the admin site 

To create a super user, run the following:-

```sh
python manage.py createsupersuer
```

And follow the prompts
