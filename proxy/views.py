from django.shortcuts import render
from django.views import View


page_args = {
    "title":"ProxyHome"
}

class ProxyView(View):
    def get(self, request):
        return render(request,'proxy/index.html', page_args)