from django.shortcuts import render

page_args = {
    "title":"ServerHome"
}

# Create your views here.
def index(request=None):
    return render(request,'proxy_server/index.html', page_args)