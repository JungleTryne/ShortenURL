from django.shortcuts import render, redirect
from .models import URLPair

#custom lib to generate converted urls
from mshin_shortener import shorten 


def main_page(request):
    """Returns main page. Only GET support"""
    if request.method == "GET":
        return render(request, 'index.html')


def generate_url(request):
    """The view which gets POST request to convert url"""
    if request.method == "POST":
        recieved_url = request.POST['url']
        shortened = shorten.shorten_url(recieved_url)
        return render(request, "result.html", {"final_url":shortened})


def redirect_to_url(request):
    """Redirects to initial url which was converted"""
    path = request.path[1:]
    all_urls = URLPair.objects.all().filter(new_url=path)

    if len(all_urls) == 0:
        return render(request, "redirect.html", {"final_url":"no"})
    else:
        existing_pair = list(all_urls)[0]
        redirect_to = existing_pair.initial_url
        return render(request, "redirect.html", {"final_url":redirect_to})
