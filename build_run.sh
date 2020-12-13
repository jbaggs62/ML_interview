#build docker image no-caching for security reasons 
docker build --no-cache -t jb_ML_interview .

#run the container on port 1313
docker run -p 1313:1313 --name=jb jb_ML_interview --host=0.0.0.0

#make sure its runnning

docker ps


#test app


curl --location --request POST 'http://0.0.0.0:1313/json' \
--header 'Content-Type: application/json' \
--data-raw '[{
  "x5": "monday",
  "x81": "May",
  "x31": "asia",
  "x91": 0.4,
  "x53": 0.88,
  "x44": 0.99,
  "x12": 0.012,
  "x62": 2,
  "x58": 33,
  "x56": 11,
  "x57":81
},
{
  "x5": "tuesday",
  "x81": "August",
  "x31": "japan",
  "x91": 0.3,
  "x53": 0.38,
  "x44": 0.29,
  "x12": 0.112,
  "x62": 3,
  "x58": 43,
  "x56": 1.122,
  "x57":11
}
]

'


