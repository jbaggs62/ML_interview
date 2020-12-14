#test code to make sure docker container is online and listening

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
  "x57":88
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