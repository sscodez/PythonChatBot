from flask import Flask, render_template, request, jsonify
from chatgpt import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "https://ai-clinic-chatbot.vercel.app"}})

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    data = request.get_json()
    text = data.get("message")
    print('text',text)
    response=get_response(text)
    message ={"answer":response}
    print('message',message)
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug="True",host="0.0.0.0",port=8080)
    
    