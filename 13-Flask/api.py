from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=["GET"])
def welcome():
    return "<html><h1>Welcome to the web</h1><html>"

@app.route("/hello/<name>")
def hello(name):
    return f'Welcome to the web page: {name}'

@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)