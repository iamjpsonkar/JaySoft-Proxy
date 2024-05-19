from django.shortcuts import render
from django.views import View

page_args = {
    "title":"ConsumerHome"
}

class ProxyConsumerView(View):
    def get(self, request):
        return render(request,'proxy_consumer/index.html', page_args)
