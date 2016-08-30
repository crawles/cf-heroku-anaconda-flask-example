import os

from flask import Flask
import matplotlib
import numpy as np
import pandas as pd
import scipy
import sklearn

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

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
