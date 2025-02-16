# /// script
# requires-python = ">=3.11"
# dependencies = ["flask"
# ]
# ///

import flask

app = flask.Flask(__name__) 

@app.route("/") 
def hello():    
    return "Hello World!"

if __name__ == "__main__":  
    app.run()