# DOCKERIZED WORD2VEC RECOMMENDATION SYSTEM MODEL

About Running:

```sh
sudo docker build -t test .
```
```sh
sudo docker run --net=host test
```

POSTMAN;

POST REQUEST URL : http://0.0.0.0:80/predict 

Example Request JSON Body; {"product_id" : "a368901216"}
