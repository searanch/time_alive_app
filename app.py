from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")

def time_alive():

    '''function to find out how many days I have been alive'''
    import datetime
    from datetime import date
    from datetime import datetime
    d = datetime.now()
    only_date = d.date()
    born = date(1978,2,20)
    today = only_date
    delta = today - born
    
    # ninty = 32850
    # days_till_90 = ninty - delta
    return print(f"Congratulations, Liz! You have been alive for {delta.days} days!")
    #print(f"If you live until 90, you have {days_till_90.days} days to live.")

time_alive()
 
    
if __name__ == "__main__":
    app.run(debug=True)
  #We made two new changes