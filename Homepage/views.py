from django.views import View
from django.http import JsonResponse
import json
import requests
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from i.browsing_history import your_browsing_history


import json
import requests
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        headers = {"Content-Type": "application/json"}
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

        try:
            response = requests.post(
                url, data=json_data, headers=headers, verify=True
            )  # Enable certificate verification
            response.raise_for_status()  # Raise an exception for non-200 status codes

            if response.status_code == 200:
                data = response.json()
                print(f"data_________________{data}")
                print(f"headers: {response.headers}")

                image_urls = data.get("data", {}).get("images", [])
                cart_url = data.get("data", {}).get("cart_icon")
                zipped = data.get("zipped")

                context["images"] = image_urls
                context["cart_url"] = cart_url
                context["zipped"] = zipped
            else:
                print(f"Unexpected content type: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")

        return context
