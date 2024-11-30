from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/membership')
def membership():
    return render_template('membership.html')

@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')

if __name__ == '__main__':
    app.run(debug=True)
