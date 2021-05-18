from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def web_page(page_name):
    return render_template(page_name)


def write_to_db(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        file = database.write(f'\n{message},{subject},{email}')


def write_to_databasecsv(data):
    with open('database.csv', newline='', mode='a') as databasecsv:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        databasecsv_writer = csv.writer(
            databasecsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        databasecsv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def send_msg():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_db(data)
        write_to_databasecsv(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return "wrong data !!!!!!!"


""" @app.route('/index.html')
def index_web():
    return render_template('index.html')


@app.route('/about.html')
def about_web():
    return render_template('about.html')


@app.route('/works.html')
def work_web():
    return render_template('works.html')
 """
