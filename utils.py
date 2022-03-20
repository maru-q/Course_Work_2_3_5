
import json
from json import JSONDecodeError

POSTS_PATH = "data/data.json"
MARKS_PATH = "data/bookmarks.json"
COMMENTS_PATH = "data/comments.json"


def get_posts_all():
    """
    Возвращает все посты
    :return: posts
    """
    try:
        with open(POSTS_PATH, "r", encoding="utf-8") as file:
            posts_list = json.load(file)
        return posts_list
    except FileNotFoundError:
        raise FileNotFoundError
    except JSONDecodeError:
        raise JSONDecodeError


def get_posts_by_user(user_name):
    """
    Возвращает посты определенного пользователя
    :param user_name:
    :return: user_posts
    """
    user_posts = []
    posts = get_posts_all()

    for post in posts:
        if user_name.lower() == post.get("user_name").lower():
            user_posts.append(post.get("user_name"))
        else:
            return "Пользователь не найден"
        return user_posts


def get_comments_by_post_id(post_id):
    """
    Возвращает комментарии определенного поста
    :param post_id:
    :return: post_comments
    """
    post_comments = []
    with open(COMMENTS_PATH, "r", encoding="utf-8") as file:
        comments_list = json.load(file)
    for comment in comments_list:
        if post_id == comment.get("post_id"):
            post_comments.append(comment)
    return post_comments


def search_for_posts(query):
    """
    Возвращает список постов по ключевому слову
    post_comments
    :param query:
    :return: query_posts
    """
    query_posts = []
    posts = get_posts_all()
    for post in posts:
        if query.lower() in post["content"].lower():
            query_posts.append(post)
    return query_posts


def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору
    :param pk:
    :return: post
    """
    posts = get_posts_all()
    for post in posts:
        if pk == post["pk"]:
            return post
        else:
            return "Публикаций не найдено"


def get_post_by_postid(post_id):
    """
    Возвращает пост по его id
    :return: 
    """
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == post_id:
            return post


# post = get_post_by_postid(1)
# print(post)

# post_all = get_posts_all()
# print(post_all)
# post_id = 4
# post = get_post_by_postid(post_id)
# print(post)