**Project: Dockerize python flask application**

**Prerequisite**

**1)** You have docker installed on your machine
**2)** Basic knowledge about docker

**Clone this repository:**

```bash
git clone https://github.com/Prasadrasal2002/Python-App-docker1.git
cd Python-App-docker1
```

**Install docker**

```bash
curl -fsSL https://get.docker.com | sudo sh

docker --version
```

**Build the docker image**

```bash
docker build -t my-flask-app 
```

![image](https://github.com/user-attachments/assets/417e3025-5182-4521-861a-483dd631eef4)

show Docker Images:
```bash
docker images
```

![image](https://github.com/user-attachments/assets/77517a20-1323-42ff-a525-61aa4625d79d)



**Run the Docker container based on the image**

```bash
docker run -p 5000:5000 my-flask-app
```

![image](https://github.com/user-attachments/assets/7c6e7bc0-8a00-4860-bcdd-3f94339dbdeb)


**Verify the result**

```bash
curl localhost:5000
       or
curl <pub-ip-instance>:5000
```
Or open http://<pub-ip-instance>:5000/ in your browser

![image](https://github.com/user-attachments/assets/4380cec7-ff63-4e66-adc1-b71c74afaf46)





