# flask-time-api

To do the docker build execute the following in the root directory:
```bash
$ docker build -t docker-time-api:latest .
```


To run the api rate test using docker container that we built, execute the following command:
```bash
$ docker run -d --name test-time-api --restart=always -p 80:80 docker-time-api:latest
```

To stop running the docker container and remove the container execute the below command
```bash
$ docker stop test-time-api && docker rm test-time-api
```

To stop run the docker container in a specific docker network execute the below command(this might be needed to make the containers talk to each other):
```bash
$ docker run -d --name test-time-api --restart=always -p 80:80 --network my_docker_network docker-time-api:latest
```