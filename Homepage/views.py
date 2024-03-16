from django.views import View
from django.http import JsonResponse
import json
import requests
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from i.browsing_history import your_browsing_history


class HomePageView(TemplateView):
    template_name = "store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        headers = {"Content-type": "applications/json"}
        url = "https://ecommracapi.pythonanywhere.com/Homepage/"
        images = [
            "box_7",
            "box_6",
            "box_5",
            "box_3",
            "box_8",
            "box_2",
            "box_1",
            "U_N",
            "ama_zon_logo",
        ]
        cart_icon = "cart_50_50"
        data = {"images": images, "cart_icon": cart_icon}
        json_data = json.dumps(data)

        response = requests.post(url=url, data=json_data, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.content)

            image_urls = data["images"]
            cart_url = data["cart_icon"]
            zipped = data["zipped"]

            context["images"] = image_urls
            context["cart_url"] = cart_url
            context["zipped"] = zipped
            return context
