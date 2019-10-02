import unittest
from app.models import Blog

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(blog = 'inspire peaple with your opinion!', user_id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_save_comment(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)