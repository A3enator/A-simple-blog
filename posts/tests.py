from django.urls import reverse
from django.test import TestCase
from .models import Post



# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Just a test text!")

    def test_text_contant(self):
        Post.objects.create(text="just a test text!")
        post = Post.objects.get(text="just a test text!")
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, "just a test text!")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_veiw_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
