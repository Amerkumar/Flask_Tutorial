from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/tuna")
def tuna():
    return "THis is it"

@app.route("/home/<name>")
def home(name):
    return render_template("profile.html", name = name)

@app.route("/profile/<username>")
def profile(username):
    return "Hello %s" %username

@app.route("/post_id/<int:post_id>")
def post(post_id):
    return "Post id is %s" %post_id

@app.route("/bacon",methods = ['GET','POST'])
def bacon():
    return "Post worker %s" %request.method

#Mapping Multiple urls

@app.route("/user")
@app.route("/user/<name>")
def user(name=None):
    return render_template("user.html", name = name)
#Passing a list
@app.route("/shopping")
def shopping():
    items = ['Roll','Eggs','Milk']
    return render_template("shopping.html" , items = items)

if __name__ == "__main__":
    app.run(debug=True)