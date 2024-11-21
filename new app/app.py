from flask import Flask,render_template


flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    dic={"name":"taanish","ph":7777777777}
    return render_template('index.html',context=dic)

@flask_app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@flask_app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1',port=5004,debug=True)
