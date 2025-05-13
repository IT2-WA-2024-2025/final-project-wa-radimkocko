from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
def index(): 
    return render_template('index.html')

@app.route('/sporty')
def sporty():
    return render_template('sporty.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == "__main__": 
    app.run()
