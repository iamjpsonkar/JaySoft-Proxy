from django.shortcuts import render
from django.views import View

page_args = {
    "title":"ConsumerHome",
    "title_url":"/proxy/consumer"
}

class ProxyConsumerView(View):
    def get(self, request):
        return render(request,'proxy_consumer/index.html', page_args)
