# Docker Django

### run
```
make all
```


### into Docker container
```
docker exec -ti docker-django_web_1 bash

```

### create createsuperuser

```
# into docker
python manage.py createsuperuser
```

### makemigrations
```
python manage.py makemigrations tasks
python manage.py sqlmigrate tasks {migrate number}

```
