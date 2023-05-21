# importing pandas module
import pandas as pd

# Reading an excel file

filename="./product_data.xlsx"
excelFile = pd.read_excel (filename)
# Converting excel file into CSV file
excelFile.to_csv ("ResultCsvFile.csv", index = None, header=True)
# Reading and Converting the output csv file into a dataframe object
df = pd.DataFrame(pd.read_csv("ResultCsvFile.csv"))

# initialize data of lists.
data = {'name': df["product_names"],
        'link': df["product_link"]}
  
# Create DataFrame
df2 = pd.DataFrame(data)

#preprocessing

import string
from string import digits
import re 


def preprocess_sentence(s):
    s=s.apply(lambda x: x.lower())  ##lower case
    s=s.apply(lambda x: re.sub("'", '', x)) ##remove quote
    s=s.apply(lambda x: re.sub("’", '', x))
    s=s.apply(lambda x: ''.join(ch for ch in x if ch not in set(string.punctuation)))  ## remove puncuation
    s=s.apply(lambda x: x.translate(str.maketrans('', '', digits)))
    s=s.apply(lambda x: x.strip())
    s=s.apply(lambda x: re.sub(" +", " ", x))
    return s


def print_data(data):
    for x in range(10):
        print(x+1, data.iloc[x] )


##

import pinecone
pinecone.init(api_key='your_api', environment='us-central1-gcp')
model = SentenceTransformer('all-mpnet-base-v2',device='cuda')

## create pinecode index
pinecone.create_index(name='clothing-rank-search', dimension=768)
index = pinecone.Index('clothing-rank-search')


## iterate and save to pine code
def pinecode_database(data,index,model):
  question_list = []
  for i,row in data.iterrows():
    question_list.append(
        (
           str(i+1),
           model.encode(row['name']).tolist(),
          {   
              'Product Name': str(row['name']),
              'Product Link':row['link']
          }
        )
    )
    if len(question_list)==100 or len(question_list)==len(data):
      index.upsert(vectors=question_list)
      question_list = []


pinecode_database(df2,index,model)











