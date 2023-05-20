import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pinecone
from sentence_transformers import SentenceTransformer
from string import digits
import re 
import string
import pandas as pd

pinecone.init(api_key='a61b9ef4-d220-4d9c-a8ae-2a82928604bf', environment='us-central1-gcp')
model = SentenceTransformer('all-mpnet-base-v2',device='cpu')

def preprocess_sentence(s):
    s=s.apply(lambda x: x.lower())  ##lower case
    s=s.apply(lambda x: re.sub("'", '', x)) ##remove quote
    s=s.apply(lambda x: re.sub("’", '', x))
    s=s.apply(lambda x: ''.join(ch for ch in x if ch not in set(string.punctuation)))  ## remove puncuation
    s=s.apply(lambda x: x.translate(str.maketrans('', '', digits)))
    s=s.apply(lambda x: x.strip())
    s=s.apply(lambda x: re.sub(" +", " ", x))
    return s

def process(query):
  da= {'name':[query] ,}
  # Create DataFrame
  him= pd.DataFrame(da)
  return preprocess_sentence(him["name"])
 
app = Flask(__name__)

data=(('cinch western denim jeans mens white label low dark wash mb', 'https://www.amazon.com/Cinch-White-Relaxed-Mid-Rise-Stonewash/dp/B07F5LHFKY/ref=sr_1_2200?crid=1DVUGE5NG5UUO&keywords=men+fashion&qid=1684499787&rnid=7141123011&s=apparel&sprefix=menfashion%2Caps%2C282&sr=1-2200'),
('men regular high rise black jeans', 'https://www.flipkart.com/crishtaliyo-regular-men-black-jeans/p/itmbe5b4e877bc50?pid=JEAGZS88EFQYXKJ9&lid=LSTJEAGZS88EFQYXKJ9B7OOIP&marketplace=FLIPKART&store=clo&srno=b_20_779&otracker=browse&fm=organic&iid=d54f2af1-65b8-48dd-9240-354ef9fd2067.JEAGZS88EFQYXKJ9.SEARCH&ppt=None&ppn=None&ssid=o98bgb7ojk0000001684497563652'))


@app.route('/')
def home():
    return render_template('index.html',data=data)

@app.route('/predict',methods = ['POST'])
def predict():
    result = str(request.form.get("cgpa"))
    print(result)
    index = pinecone.Index('clothing-rank-search')
    xq = model.encode([process(result)[0]]).tolist()
    result = index.query(xq, top_k=5, includeMetadata=True)
        
    datalist = []
    for match in result['matches']:
        product_name = match['metadata']['Product Name']
        product_link = match['metadata']['Product Link']
        datalist.append((product_name, product_link))
    return render_template('index.html',data=datalist)


if __name__ == '__main__':
    app.run(debug=False)