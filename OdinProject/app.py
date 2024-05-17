from flask import Flask, render_template, request
import validators

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    text_url = request.args.get('text')
    if validators.url(text_url):
        return render_template('search.html', name=text_url)
    else:
        return render_template('search.html', name="Введен некорректный URL")

if __name__ == '__main__':
    app.run(debug=True)