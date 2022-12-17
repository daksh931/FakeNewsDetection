# importing the libraries
from flask import Flask,render_template,request
from ScrapeTweets import scrapedata
from predictions import pre
import pickle
import pandas as pd


#Global variables
df = scrapedata()
app=Flask(__name__)


#user defined routes
@app.route("/", methods=("POST" , "GET"))
def home():
    context = df
    return render_template('index.html',tables=context)
    # return render_template('index.html', tables=[df.to_html(classes='table table-stripped')] , titles=df.columns.values)

@app.route("/prediction",methods=['GET','POST'])
def predict():
    output = pre(list(df['text']))
    df['ouput'] = output
    context = df
    return render_template('prediction.html',tables=context)


if __name__ =='__main__':
    app.run(debug=True)       


