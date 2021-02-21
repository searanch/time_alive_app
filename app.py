from flask import Flask, render_template
import datetime
from datetime import date
from datetime import datetime

import function


app = Flask(__name__)

@app.route('/')
def days_alive():
#     '''function to find out how many days I have been alive'''
    return function.time_alive()


    

    







    
if __name__ == "__main__":
    app.run(debug=True)
  #We made two new changes