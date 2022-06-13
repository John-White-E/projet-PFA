from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import os
import sys

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET', 'POST'])
def home():
   

    return jsonify({"response":"Salam"})


@app.route("/color", methods=['GET', 'POST'])
def color():
    import main

    image = request.files['file']
    image.save(image.filename)
    
    answer = main.get_color(image.filename)
    

    if "main" in sys.modules:
        del sys.modules["main"]


    return jsonify({"response":answer})

if __name__ == "__main__":
    port=os.environ.get("PORT",3000)
    app.run(host="0.0.0.0", port=port, debug=False)

