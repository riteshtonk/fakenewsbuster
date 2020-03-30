# fakenewsbuster
Fake News Buster

## Details
This is a POC done for Facebook Hackathon

## Requirements
Python
View requirements.txt


## Sample Run
Start the main.py file
```
python .\scripts\main.py
```

Send a REST message
```
curl -i -H "Content-Type: application/json" -X POST -d '{"message":"Not a single bomb blast took place in the country in last 6 yrs: Minister Javadekar"}' http://localhost:5000/message
```

See the response
```
{"result": "False" "source":"https://twitter.com/FactCheckIndia/status/1238117638229950465"}
```
