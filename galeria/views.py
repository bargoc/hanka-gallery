from django.shortcuts import render


def starting_page(request):
    return render(request, "galeria/index.html")

def posts(request):
    pass

def post_detail(request):
    pass

