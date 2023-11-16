from flask import Flask 
app = Flask(__name__)

@app.route ("/")
def Hello ():
	return "<h1>Pierwsza aplikacja w Pythonie (Flask) aaaaaa"

if __name__ ==  "__main__":
	 app.run(host='0.0.0.0')

