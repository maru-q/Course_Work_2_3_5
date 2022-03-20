from flask import Blueprint, render_template, request
from utils import get_posts_all, get_posts_by_user, get_post_by_postid, get_comments_by_post_id, get_post_by_pk, search_for_posts

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/GET")
def main_page():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/GET/post/<int:postid>")
def post_page(postid):

    post = get_post_by_postid(postid)

    if not post:
        return "Пост не найден"

    comments = get_comments_by_post_id(postid)
    comments_count = len(comments)

    return render_template("post.html", post=post, comments=comments, comments_count=comments_count)


@main_blueprint.route("/search")
def search_page():
    s = request.args.get("s", "")
    posts = search_for_posts(s)
    post_count = len(posts)

    return render_template("search.html", posts=posts, post_count=post_count, s=s)


@main_blueprint.route("/users/<username>")
def post_by_user_page(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)
