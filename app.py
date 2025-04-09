# app.py
from flask import Flask, render_template, request, jsonify , session
from ai_engine import ai_response
from ragdata import rag_query
import markdown2 



app = Flask(__name__)
app.secret_key = "Radheradhe"


###I created this chatbot such that it can handle multiple users but simpilcity for now we willl be using a single user and it uses chromadb for rag

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    rag_data = rag_query(user_message , "RadheKrishna")
    
    user_message ="This is the user message :" + user_message + f'''
    ================================================================================================================================================================================================
    
    Here is your obtained rag data based on user message:
    ================================================================================================================================================================================================
    
    {rag_data}
================================================================================================================================================================================================'''


    his = []

    his.append({"role": "user" , "parts":[user_message]})

    reply = ai_response(user_message , his)
    reply_markdown = markdown2.markdown(reply)

    his.append({"role": "model" , "parts":[reply]})
    return jsonify({"reply": reply_markdown})

if __name__ == '__main__':
    app.run(debug=True)
