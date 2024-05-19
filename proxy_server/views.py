from django.shortcuts import render
from django.views import View

page_args = {
    "title":"ServerHome",
    "title_url":"/proxy/server"
}

class ProxyServerView(View):
    def get(self, request):
        return render(request, 'proxy_server/index.html', page_args)