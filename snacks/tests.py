from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="adham", email="adham@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="shaowrma", description="hello world", purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "shaowrma")

    def test_thing_content(self):
        self.assertEqual(f"{self.snack.title}", "shaowrma")
        self.assertEqual(f"{self.snack.description}", "hello world")
        self.assertEqual(self.snack.purchaser,self.user)

    def test_thing_list_view(self):
        response = self.client.get(reverse("snack_view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "shaowrma")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_thing_detail_view(self):
        response = self.client.get(reverse("list", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("create"),
            {
                "title": "KitKat",
                "description": "zaky",
                "purchaser": self.user.pk,
            }, follow=True
        )

        self.assertRedirects(response, reverse("list", args="2"))
        



    def test_thing_update_view_redirect(self):
        response = self.client.post(
            reverse("update", args="1"),
            {"title": "Updated name","description":"amaizeing","purchaser":self.user.pk}
        )

        self.assertRedirects(response, reverse("list", args="1"))

    def test_thing_delete_view(self):
        response = self.client.get(reverse("delete", args="1"))
        self.assertEqual(response.status_code, 200)