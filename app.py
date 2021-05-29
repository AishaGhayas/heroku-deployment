from flask import Flask, request  # request handles url requests from post or get methods
from tensorflow import keras
import tensorflow as tf
import numpy as np

m = tf.keras.models.load_model(r'C:\Users\DMEO\Desktop\python\VS\model on web\model.h5')

app = Flask(__name__)

@app.route("/") # home page form data will route on info page (action="/info") by post method
def index():
    return """
    <h1> User Info </h1> 
    <form action = "/info" method = "POST">  
    <input type="text" name="height" placeholder="Height">

    <input type="submit" value="Send">
    </form>
    """
    
@app.route("/info", methods=["GET","POST"])  # info page is accepting data from get and post
def info():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        print(m.summary())
        print(request.form["height"])
        input1 = np.int64([[request.form["height"]]])
        print("input",input1, type(input1))
        a = m.predict(input1)
        return "data is showing with post method {} prediction is {}".format(input1,a)


app.run(debug = True)