# JOGA BACKEND

- Install prerequsites

```shell
pip install cryptography --global-option=build_ext --global-option="-L/usr/local/opt/openssl/lib" --global-option="-I/usr/local/opt/openssl/include"
pip install docker-compose
```

- Create env file at the root of the directory and paste lines below with correct valudes

```shell
DJANGO*SECRET_KEY=secretkey
DEBUG=False
DJANGO_ALLOWED_HOSTS=your_server_IP_address
DATABASE_ENGINE=postgresql_psycopg2
DATABASE_NAME=jogadb
DATABASE_USERNAME=jogadba
DATABASE_PASSWORD=8QxpF-ZdJ%RT9T=NQ-7cFUgr
DATABASE_HOST=db
DATABASE_PORT=5432
DJANGO_LOGLEVEL=info
```

- Build containers

```shell
make up

```

- Connect to Joga web container shell

```shell
docker exec -it `docker ps -aqf "name=joga_web"` /bin/sh

```

- Create a superuser in order to access Django admin IHM

```shell
python manage.py createsuperuser
```

- Finally, generate the static files for the app

```shell
python manage.py collectstatic --noinput

```

- See logs

```shell
docker logs `docker ps -aqf "name=joga_web"` --follow
docker logs `docker ps -aqf "name=joga_db"` --follow
docker logs `docker ps -aqf "name=joga_nginx"` --follow

```
