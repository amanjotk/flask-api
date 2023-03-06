import requests
import json
import pickle
from scipy import sparse
import numpy as np
url = 'http://127.0.0.1:5000/predict'

data = sparse.load_npz("test_data.npz").toarray()[0].tolist()
r = requests.post(url, json=json.dumps(data))
print(r.json())