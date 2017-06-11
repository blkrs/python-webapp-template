docker build . -t webapp
docker stop webapp
docker rm webapp
docker run --name webapp -p 5004:5000 webapp:latest 
