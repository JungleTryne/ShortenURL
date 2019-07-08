'''Views for the website.'''
import logging
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden
from django.shortcuts import render

#custom lib to generate converted urls
from mshin_shortener import shorten
from .models import URLPair


def main_page(request):
    """Returns main page. Only GET support"""
    if request.method == "GET":
        return render(request, 'index.html')
    return HttpResponseForbidden()


def generate_url(request):
    """The view which gets POST request to convert url"""
    if request.method == "POST":
        val = URLValidator()
        recieved_url = request.POST['url']
        try:
            val(recieved_url)
        except ValidationError:
            logging.error("Wrong template for url: {0}".format(recieved_url))
            return render(request, "error.html")
        shortened = shorten.shorten_url(recieved_url)
        return render(request, "result.html", {"final_url":shortened})
    return HttpResponseForbidden()


def redirect_to_url(request):
    """Redirects to initial url which was converted"""
    path = request.path[1:]
    all_urls = URLPair.objects.all().filter(new_url=path)

    if not all_urls:
        return render(request, "redirect.html", {"final_url":"no"})
    existing_pair = list(all_urls)[0]
    redirect_to = existing_pair.initial_url
    return render(request, "redirect.html", {"final_url":redirect_to})
