from flask import Flask,render_template,request,jsonify
from chatbot_main import run_conversation

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_userQuery",methods=['GET','POST'])
def get_user_data():
    data=request.get_json()
    user_query=data.get('data')
    AiOutput=run_conversation(f"{user_query}")
    print(user_query,":",AiOutput)

    return jsonify({"response":True,"message":AiOutput})




if __name__=="__main__":
    app.run(debug=True)