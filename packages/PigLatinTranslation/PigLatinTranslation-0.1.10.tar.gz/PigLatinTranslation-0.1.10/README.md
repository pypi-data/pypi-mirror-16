# Pig Latin Translation Microservice [![Build Status](https://travis-ci.org/Jai-Chaudhary/pig-latin-translation-microservice.svg?branch=master)](https://travis-ci.org/Jai-Chaudhary/pig-latin-translation-microservice) [![Coverage Status](https://coveralls.io/repos/github/Jai-Chaudhary/pig-latin-translation-microservice/badge.svg?branch=master)](https://coveralls.io/github/Jai-Chaudhary/pig-latin-translation-microservice?branch=master) [![docs](https://readthedocs.org/projects/pig-latin-translation-microservice/badge/)](http://pig-latin-translation-microservice.readthedocs.io)


A flask-based microservice to translate english text to pig latin. [Wikipedia Link](https://en.wikipedia.org/wiki/Pig_Latin). 

> Pig Latin is a language game in which words in English are altered. The objective is to conceal the words from others not familiar with the rules.

Pig Latin is simply a form of jargon with rules. The Rules are described later

## Demo
You can try your own examples at a web form [here](https://piglatin.jaichaudhary.com). 

## Example Usage

The fastest way to get started is to request this service from the demo api

### Curl
```
curl --request POST \
  --url https://piglatin.jaichaudhary.com/api/translate \
  --form 'text=How do you say ... in Pig Latin?'
```

### Python
```
import requests
url = "https://piglatin.jaichaudhary.com/api/translate"
payload = {"text": "How do you say ... in Pig Latin?"}
response = requests.request("POST", url, data=payload)
print response.text
```

You should see a response like
```
{
  "text": "Owhay oday ouyay aysay ... inyay Igpay Atinlay?"
}
```


## Installation

If you would like to run the service locally, there are multiple ways

### Dockerfile
```
  docker pull ja1chaudhary/pig-latin-translation-service
  docker run --name pig-latin-service -p 8000:8000 -d ja1chaudhary/pig-latin-translation-service
```

### Python Package
To install the python package, simply
```
  pip install piglatintranslation
```

### Source
```
  git clone https://github.com/Jai-Chaudhary/pig-latin-translation-microservice
  cd pig-latin-translation-microservice
  python setup.py install
  python run.py
```

## Rules

If word begins with consonant sound, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added.

* pig     => igpay 
* banana  => ananabay
* trash   => ashtray
* happy   => appyhay
* duck    => uckday
* glove   => oveglay

If word begins with vowel sounds or a silent letter, one just adds "yay" to the end.

* eat     => eatyay
* omelet  => omeletyay
* are     => areyay


## Documentation
API documentation is available at http://pig-latin-translation-microservice.readthedocs.io

## How to Contribute

