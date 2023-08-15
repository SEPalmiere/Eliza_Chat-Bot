# app.py

from flask import Flask, request, render_template
import eliza_aprimorada

app = Flask(__name__)

eliza = eliza_aprimorada.Eliza()

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get") 
def get_bot_response():
  userText = request.args.get('msg')
  return str(eliza.respond(userText))

if __name__ == "__main__":
  app.run()