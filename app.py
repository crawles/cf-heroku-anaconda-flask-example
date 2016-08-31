import os

from flask import Flask
import numpy as np
import pandas as pd
import scipy
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = np.array([[1,2,3,4,5,6,7,8,9],[0,0,0,0,0,1,1,1,1]])
    df = pd.DataFrame(data.T,columns = ['x','y'])
    cl = LogisticRegression()
    cl.fit(df.x[:,None],df.y)
    res = cl.predict_proba(df.x[:,None])
    return 'Hello, World! {}'.format(str(res))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
   # if os.environ.get('VCAP_SERVICES') is None: # running locally
   #     PORT = 8080
   #     DEBUG = True
   # else:                                       # running on CF
   #     PORT = int(os.getenv("PORT"))
   #     DEBUG = False

   # app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
