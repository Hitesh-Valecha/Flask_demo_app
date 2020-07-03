import os
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    print("ijhjboubiu")
    return render_template('hi.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    print("ok")
    with open('uploads/'+file.filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            print(row)
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)

    return render_template('hi.html')

if __name__ == '__main__':
    app.run()
