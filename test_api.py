from app import app
import random


def test_json_posts_type():
    response = app.test_client().get("/api/posts")
    assert type(response.json) == list


def test_json_posts_keys():
    response = app.test_client().get("/api/posts")
    posts = response.json
    for post in posts:
        assert post.get("poster_name")
        assert post.get("poster_avatar")
        assert post.get("pic")
        assert post.get("content")
        assert post.get("views_count")
        assert post.get("likes_count")
        assert post.get("pk")


def test_json_post_type():
    post_id = random.randint(1, 8)
    response = app.test_client().get(f"/api/posts/{post_id}")
    assert type(response.json) == dict


def test_json_post_keys():
    post_id = random.randint(1, 8)
    response = app.test_client().get(f"/api/posts/{post_id}")
    post = response.json
    assert post.get("poster_name")
    assert post.get("poster_avatar")
    assert post.get("pic")
    assert post.get("content")
    assert post.get("views_count")
    assert post.get("likes_count")
    assert post.get("pk")


