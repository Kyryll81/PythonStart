from flask import Flask


app: Flask = Flask(__name__)


@app.get('/')
def hello_world():
    return '''
<!doctype html>
<html lang="uk">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, Flask!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

    <div class="container text-center mt-5">
        <h1 class="display-4 text-primary">Привіт, це Flask з Bootstrap!</h1>
        <p class="lead">Це наш перший веб-додаток, що повертає стилізований HTML.</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''


if __name__ == '__main__':
    app.run(debug=True)