from django.shortcuts import render

page_args = {
    "title":"ConsumerHome"
}

# Create your views here.
def index(request=None):
    return render(request,'proxy_consumer/index.html', page_args)