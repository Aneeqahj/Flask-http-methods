from flask import *

app = Flask(__name__)


@app.route('/')
def entry_page():
    return render_template('shoppinglist.html')


@app.route('/showitems', methods=['POST'])
def showitems():
    if request.method == 'POST':
        result = request.form
    return render_template('showitems.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
