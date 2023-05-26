import os
import csv
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/Maksik/PycharmProjects/python_advanced/module_21_orm_2/homework/files'
ALLOWED_EXTENSIONS = {'txt', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello():
    return '<p>hello world</p>'


@app.route('/students/insert_csv', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '<h4>file saved successful</h4>'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/import', methods=['GET'])
def import_data_from_csv():
    file_path = 'files/students.csv'
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'], row['surname'], row['phone'], row['email'], row['average_score'], row['scholarship'])
    return '<h4>import successful</h4>'


@app.route('/write-csv', methods=['GET'])
def csv_test_file_add():
    with open('students.csv', 'w', newline='') as csvfile:
        field_names = ['name', 'surname', 'phone', 'email', 'average_score', 'scholarship']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow({'name': 'name1', 'surname': 'surname1', 'phone': '788', 'email': 'q@r.ru',
                         'average_score': '7.0', 'scholarship': '1'})
        writer.writerow({'name': 'name1', 'surname': 'surname1', 'phone': '788', 'email': 'q@r.ru',
                         'average_score': '7.0', 'scholarship': '1'})
        writer.writerow({'name': 'name1', 'surname': 'surname1', 'phone': '788', 'email': 'q@r.ru',
                         'average_score': '7.0', 'scholarship': '1'})
    return '<h4>write scv successful</h4>'


if __name__ == "__main__":
    app.run()
