import unittest


def count_posts(posts):
    return len(posts)


def filter_posts_by_title(posts, query):
    query = query.strip().lower()

    if not query:
        return posts

    return [
        post for post in posts
        if query in post["title"].lower()
    ]


def filter_posts_by_user(posts, user_id):
    if user_id == "All Users":
        return posts

    return [
        post for post in posts
        if post["userId"] == user_id
    ]


class TestDashboardFunctions(unittest.TestCase):

    def setUp(self):
        self.posts = [
            {"id": 1, "userId": 1, "title": "Python Basics", "body": "Learn Python"},
            {"id": 2, "userId": 2, "title": "Django Tutorial", "body": "Learn Django"},
            {"id": 3, "userId": 1, "title": "Advanced Python", "body": "Practice Python"}
        ]

    def test_count_posts(self):
        self.assertEqual(count_posts(self.posts), 3)

    def test_search_by_title(self):
        self.assertEqual(len(filter_posts_by_title(self.posts, "python")), 2)

    def test_search_case_insensitive(self):
        self.assertEqual(len(filter_posts_by_title(self.posts, "PYTHON")), 2)

    def test_search_no_match(self):
        self.assertEqual(len(filter_posts_by_title(self.posts, "xyz")), 0)

    def test_filter_by_user(self):
        self.assertEqual(len(filter_posts_by_user(self.posts, 1)), 2)

    def test_all_users(self):
        self.assertEqual(len(filter_posts_by_user(self.posts, "All Users")), 3)


if __name__ == "__main__":
    unittest.main()