from django.shortcuts import render

page_args = {
    "title":"ProxyHome"
}

# Create your views here.
def index(request=None):
    return render(request,'proxy/index.html', page_args)