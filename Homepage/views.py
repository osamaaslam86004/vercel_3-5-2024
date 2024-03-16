from django.views import View
from django.http import JsonResponse
import json
import requests
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from i.browsing_history import your_browsing_history


import cloudinary

if not settings.DEBUG:
    cloudinary.config(
        cloud_name="dh8vfw5u0",
        api_key="667912285456865",
        api_secret="QaF0OnEY-W1v2GufFKdOjo3KQm8",
        api_proxy="http://proxy.server:3128",
    )
else:
    cloudinary.config(
        cloud_name="dh8vfw5u0",
        api_key="667912285456865",
        api_secret="QaF0OnEY-W1v2GufFKdOjo3KQm8",
    )
import cloudinary.uploader
from cloudinary.uploader import upload


class HomePageView(TemplateView):
    template_name = "store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        import requests

        headers = {"Content-type": "applications/json"}
        url = "https://diverse-intense-whippet.ngrok-free.app/Homepage/"
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
        json_data = json.dump(data)

        response = requests.post(url=url, data=json_data, headers=headers)
        if response.status_code == 200:
            image_urls = response.content["images"]
            cart_url = response.content["cart_icon"]
            zipped = response.content["zipped"]

            context["images"] = image_urls
            context["cart_url"] = cart_url
            context["zipped"] = zipped
            return context
