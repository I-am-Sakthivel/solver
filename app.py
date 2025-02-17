# /// script
# requires-python = ">=3.11"
# dependencies = [
# "flask",
# "requests",
# ]
# ///

import flask
from flask import render_template
from resp import send_req
from exec import exec
app = flask.Flask(__name__) 

@app.route("/") 
def hello():    
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    question = flask.request.json["question"]
    func,args,message=send_req(question)
    if not message:
        global sol
        sol=exec(func,args)
    return {"message":"success"}

@app.route("/solution", methods=["GET"])
def soln():
    return {"solution":sol}


if __name__ == "__main__":  
    app.run()