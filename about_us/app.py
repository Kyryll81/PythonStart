from flask import Flask, request

app = Flask(__name__)


@app.get('/about')
def about_page():
    return '''
<!doctype html>
<html lang="uk">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Про нас</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container text-center mt-5">
        <h1 class="display-4">Це сторінка "Про нас"</h1>
        <p class="lead">Це простий приклад GET-запиту.</p>
    </div>
</body>
</html>
'''

@app.get('/login')
def show_login_form():
    return '''
<!doctype html>
<html lang="uk">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вхід</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Сторінка входу</h1>
        
        <form method="POST" action="/login">
            <div class="mb-3">
                <label for="email" class="form-label">Електронна пошта</label>
                <input type="email" class="form-control" id="email" name="email">
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Пароль</label>
                <input type="password" class="form-control" id="password" name="password">
            </div>
            <button type="submit" class="btn btn-primary">Увійти</button>
        </form>
    </div>
</body>
</html>
'''


@app.post('/login')
def login_user():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email == "kozachukkirill81@gmail.com" and password == "1234567890": 
        return f'''
        <h1>Дані отримано!</h1>
        <p>Ваш email: {email}</p>
        <p>Ваш пароль: {password}</p>
        '''
    return '''
        <h1>Помилкове ім'я або пароль!</h1>
        '''

if __name__ == '__main__':
    app.run(debug=True)