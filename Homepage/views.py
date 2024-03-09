from django.views import View
from django.http import JsonResponse
import json
import requests
from django.shortcuts import render



class HomePageView(View):
    template_name = "store.html"

    def get(self, request, **kwargs):
        # Sending a POST request to the specified URL
        url = 'https://osamaaslampythonanywhere.com/api/auth/status'
        headers = {"Content-type" : "application/json"}

        data = json.dumps({"The message has received"})

        response = requests.post(url,  data = data, headers=headers, verify=False)
        if response.status_code == 200:
        # Rendering the response in the template
            return render(request, self.template_name, {'response_content': response.content})
        else:
            return render(request, self.template_name, {'response_content': response.status_code})






