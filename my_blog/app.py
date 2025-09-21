from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

posts = [{'id': 1, 'title': 'Перший крок у Flask', 'author': 'Іван', 'content': 'Сьогдні ми вивчили як...'},
         {'id': 2, 'title': 'Про що говорять декоратори', 'author': 'Марія', 'content': 'Декоратори - це потужний інструмент...'},
         {'id': 3, 'title': 'Основи роботи з шаблонами Jinja2', 'author': 'Петро', 'content': 'Декоратори - це потужний інструмент...'},
]


@app.get('/blog')
def show_blog_list():
    return render_template('blog_list.html', posts=posts)


@app.get('/blog/<int:post_id>')
def show_post_details(post_id):
    post: list = list(filter(lambda i: i["id"] == post_id, posts))
    return render_template('post_detail.html', post=post[-1])


@app.get('/api/posts')
def get_post_api():
    return jsonify(posts)


if __name__ == '__main__':
    app.run(debug=True)