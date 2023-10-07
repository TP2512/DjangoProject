from django.test import TestCase
from website.models import Record


class PostTestCase(TestCase):
    def testPost(self):
        post = Record(first_name="Trkesh")
        self.assertEqual(post.first_name, "Trkesh")

