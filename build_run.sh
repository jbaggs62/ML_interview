#build docker image no-caching for security reasons 
docker build --no-cache -t jb_ml_interview .

#remove old container 

docker rm jb

#run the container on port 1313
docker run -t -p 1313:1313 --name=jb jb_ml_interview 

