# ModernAI

## Introduction
This is a simple API for accessing machine learning (ML) tools for natural language processing (NLP) and computer vision (CV) tasks. 
New models and methods are being added for named entity recognition, sentiment analysis, 
noun-phrase extraction, image classification and more.

This repo provides the base code for a Flask-Restful API that exposes various NLP and CV models,
based on Spacy.io and PyTorch. 

Note: This is not a flask extension, simply an implementation of a system that can be used for experimenting with language processing and computer vision models. 

## Installing
Use Python 3.6+, create a directory, and cd into that directory.


```
pip install virtualenv
mkdir flask_nlp_api
cd flask_nlp_api

```

Create a virtual environment on your machine, and activate the new environment.


```
virtualenv genesis
source genesis/bin/activate
```

Now install libs...


```
pip install requests
pip install --upgrade google-auth
pip install --upgrade google-cloud-vision

```

Will come back to the google stuff. But needed for some of the intitial OCR features.

Get additional resources, Flask, PyTorch and Scipy.


```
pip install flask_restful
pip install torch torchvision
pip install scipy

```

We use Spacy a lot for training models and text processing. 


```
pip install -U  spacy

python -m spacy download en_core_web_md

```

Once downloaded, and installed you are ready to complete the rest of the install.


```
pip install numba
pip install networkx
pip install flask_cors
pip install flask_sqlalchemy
pip install flask_httpauth
pip install textblob
pip install bs4
pip install lxml
pip install gensim

```

Now you should be able to run the run.py script and the client.py script.

For Redis Queue, first install Redis.


```
curl -O http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make

```

For IPFS, first install IPFS, and then the Python client lib.


```
pip install ipfsapi

```
