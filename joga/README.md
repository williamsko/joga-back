# JOGA BACKEND

```docker build -t joga-back:v0 .
docker run --env-file env joga-back:v0 sh -c "python manage.py makemigrations && python manage.py migrate"

```

- Create a superuser in order to access Django admin IHM

```docker run -i -t --env-file env joga-back:v0 sh
python manage.py createsuperuser
```

- Finally, generate the static files for the app

```docker run --env-file env joga-back:v0 sh -c "python manage.py collectstatic --noinput"

```

- We can now run the app:

```docker run --env-file env -p 80:8000 django-polls:v0

```
