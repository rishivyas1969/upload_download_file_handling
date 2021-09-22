from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import count

from werkzeug.utils import secure_filename

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:rishi1969@localhost:5432/height_collector'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://cccmxzxtntzroq:e4c92fc032b8d4b6d00e4385dc0791c42f49d78c5e406732defe435f4e06e7a6@ec2-44-194-6-121.compute-1.amazonaws.com:5432/dfk93uhn66s9c4?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id=db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route('/')
def index():
    return render_template("index.html", btn=None)

@app.route('/success', methods=["POST"])
def success():
    global file
    if request.method=='POST':
        file = request.files['file']
        file.save(secure_filename('Uploaded'+file.filename))

        with open('Uploaded'+file.filename, 'a') as f:
            f.write("This was added later!")
        
        return render_template("index.html", btn='download.html')

@app.route('/download')
def download():

    response = send_file("Uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)
    return response

if __name__ == '__main__':
    app.debug=True
    app.run()