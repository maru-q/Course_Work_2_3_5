from flask import Flask, jsonify
from main.views import main_blueprint
from main.utils import get_posts_all

app = Flask(__name__)

app.register_blueprint(main_blueprint)


@app.route("/api/posts")
def get_json_posts():
    posts = get_posts_all()
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>")
def get_json_post(post_id):
    posts = get_posts_all()
    for post in posts:
        if post_id == post["pk"]:
            return jsonify(post)


if __name__ == "__main__":
    app.run()
