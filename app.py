#from flask import Flask, render_template
from flask import Flask, render_template, redirect
import datetime
from datetime import date
from datetime import datetime

import function


app = Flask(__name__)

@app.route('/')
def home():
#     '''function to find out how many days I have been alive'''
    
    #return function.time_alive()
    alive = function.time_alive()
    templeteData = render_template('index.html')
    return render_template('index.html', alive = alive)
    #return function.time_alive()

if __name__ == "__main__":
    app.run(debug=True)
  #We made two new changes