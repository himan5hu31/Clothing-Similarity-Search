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

@app.route('/predict',methods = ['POST'])
def predict():
    # file =  request.form.get('text')
    args = request.json
    print(args['text'])
    inp=process(args['text'])[0]
    print()

    index = pinecone.Index('clothing-rank-search')
    xq = model.encode([str(inp)]).tolist()
    
    result = index.query(xq, top_k=5, includeMetadata=True)
    getdata = []
    for match in result['matches']:
        product_name = match['metadata']['Product Name']
        product_link = match['metadata']['Product Link']
        getdata.append({"productname": product_name, "product_link": product_link})

    print(getdata)
    return jsonify(getdata)

if __name__ == '__main__':
    app.run(debug=False)