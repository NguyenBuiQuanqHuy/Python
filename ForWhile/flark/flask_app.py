from flask import Flask, render_template

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    posts = [
        {'title': 'Bài viết 1', 'content': 'Đây là nội dung bài viết 1.'},
        {'title': 'Bài viết 2', 'content': 'Đây là nội dung bài viết 2.'},
    ]
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    flask_app.run(debug=True)
