from requests import put, get, post, delete


data = {
    'username': 'Peter2Face',
    'email': 'Peter2Face@live.com',
    'password_hash': 'I2Peter2Face'
}

data2 = {
    'username': 'Peter2Face',
    'password_hash': 'I2Peter2Face'
}


x = post('http://localhost:5000/modern_api/users/add', data=data).json()
print(x)

z = get('http://localhost:5000/modern_api/users/list').json()
print(z)

a = post('http://localhost:5000/modern_api/login', data=data2).json()
print(a)


corpus_data = {
    'username': 'Peter2Face',
    'api_key': a['valid_user'],
    'title': 'streamate',
    'type': 'website corpus',
    'seed_url': 'http://streammate.com',
    'description': '',
    'corpus_file': 'streammate_corpus.dict',
    'model_file': 'streammate_corpus.mm'

}

b = post('http://localhost:5000/modern_api/corpus/add', data=corpus_data).json()
print(b)


topic_data = {
    'username': 'Peter2Face',
    'api_key': a['valid_user'],
    'title': 'streamate',
    'type': 'topics',
    'url': 'http://streammate.com',
    'description': '',
}


#c = post('http://localhost:5000/modern_api/topics/url/add', data=topic_data).json()
#print(c)

d = post('http://localhost:5000/modern_api/topics/seed/add', data=topic_data).json()
print(d)

text_data = {
    'username': 'Peter2Face',
    'api_key': a['valid_user'],
    'title': 'streamate',
    'text': "We go through a process of encoding patterns and making note of anomalies to our patterns. "
            "When an anomaly is persist it becomes linked in memory, associated with the context of occurrence, "
            "which relate to other occurrences in thought and action."
}

e = post('http://localhost:5000/modern_api/topics/extract_from_text', data=text_data).json()
print(e)

f = get('http://localhost:5000/modern_api/sentiment/text/raw', data=text_data).json()
print(f)

"""
files = {'file': open('/Users/justinsmith/PycharmProjects/genesis_net/uploads/Screen_Shot_2018-10-29_at_9.21.02_PM.png',
                      'rb')}

y = get('http://localhost:5000/')
print(y)

x = put('http://localhost:5000/login', data={'email': email, 'password': password}).json()
print(x)

token = {'token': x}
z = post('http://localhost:5000/upload', files=files, data=token).json()
print(z)

files2 = {'file': open('/Users/justinsmith/Desktop/Data/festival_data_clean.csv', 'rb')}

a = post('http://localhost:5000/upload', files=files2, data=token).json()
print(a)


b = post('http://localhost:5000/crawl', data={'url': 'http://streammate.com', 'token': 'mytoken'}).json()
bj = json.loads(b)
print(bj)


c = get('http://localhost:5000/crawl', data={'crawl_id': bj['success']}).json()
bc = json.loads(c)
print(bc)

# c = post('http://localhost:5000/scrape', data={'targets': bj['targets'], 'token': x}).json()
# print(c)
"""




