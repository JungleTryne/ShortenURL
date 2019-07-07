from django.shortcuts import render, redirect
from mshin_shortener import shorten
from .models import URLPair

# Create your views here.
def main_page(request):
    if request.method == "GET":
        return render(request, 'index.html')

def generate_url(request):
    if request.method == "POST":
        print(request.POST)
        recieved_url = request.POST['url']
        shortened = shorten.shorten_url(recieved_url)
        return render(request, "result.html", {"final_url":shortened})

def redirect_to_url(request):
    path = request.path[1:]
    all_urls = URLPair.objects.all().filter(new_url=path)

    if len(all_urls) == 0:
        return render(request, "redirect.html", {"final_url":"no"})
    else:
        print('success')
        existing_code = list(all_urls)[0]
        redirect_to = existing_code.initial_url
        print(redirect_to)
        return render(request, "redirect.html", {"final_url":redirect_to})

    