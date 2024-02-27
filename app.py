from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/addnote',methods=['POST'])
def add_note():
    n= request.form.get("note")
    notes.append(n)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)




    