from flask import Flask,render_template

app = Flask(__name__)

posts = [
    {
        'author':"jadeja virpal",
        'title':"Blog post",
        "date_posted":" April 20,2020",
        "commnet":"hey their my name is jadeja virapl i am trying to learn the Flask"
    },
    
        {
        'author':"jadeja Hardik",
        'title':"Blog post",
        "date_posted":" April 20,2020",
        "commnet":"hey their my name is jadeja virapl i am trying to learn the Flask"
    }
]
    



@app.route("/")
def hello():
    return "<h1>Hello Flask</h1>"

@app.route("/about")
def about():
    return render_template("about.html",title='About')

@app.route('/home')
def home():
    return render_template("home.html",posts=posts)

if __name__=='__main__':
    app.run(debug=True)