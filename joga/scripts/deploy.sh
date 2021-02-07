#!/bin/bash
pip install docker-compose

git clone https://github.com/The-GeekCorner/joga-back.git
cd joga-back
docker build .

docker-compose run web python /code/manage.py migrate --noinput

docker-compose run web python /code/manage.py test

docker-compose run web python /code/manage.py collectstatic --noinput

docker-compose run web python /code/manage.py superuser --username administrator --password a_complex_password --noinput --email 'admin@email.com'

#Build again project and up with docker-compose in detached mode. You can remove ```-d``` option
docker-compose up -d --build
