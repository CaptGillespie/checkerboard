from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("checkerboard.html")

@app.route('/4')
def four():
    return render_template("checkerboard2.html")

# @app.route('/<num>/<num>')
# def crazyboard(num1, num2):
#     return render_template("checkerboard3.html")

if __name__=="__main__": 
    app.run(debug=True) 