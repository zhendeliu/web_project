from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'r_name':'资源1', 'r_links':'www.auphd.com',}
    return render(request, "resources/list.html", context)