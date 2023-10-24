# Flask Application Docker Setup

This project is a simple setup for using Flask on docker.
## Prerequisites
- docker
- docker compose
- curl (optional: used to test POST request)

## Initial Setup

### Step 1: Clone Repository
`git clone https://github.com/MNasser99/flask-docker-setup.git`

`cd flask-docker-setup`

### Step 2: Build Docker Image
`docker build -t flask-app .`

Note: If you change the name "flask-app" here, make sure to also change it in the **docker-compose.yml** file.

### Step 3: Run Docker Compose
`docker compose up -d`

### Step 4: Try out the default GET and POST methods.
#### To try a GET request:
Visit **localhost:5000/** in browser
#### To try a POST request:
`curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"username":"MNasser", "password":"123456789"}'`


## Adding Libraries

As you write your program, you'll start needing to import more Python libraries, but these libraries will have to be installed in the docker image too. To do that, you can do the following:
### Step 1: Add libraries to requirements.txt file
Open requirements.txt, and add the names of the libraries you need each on a new line.
### Step 2: Rebuild docker image
`docker build -t flask-app .`
