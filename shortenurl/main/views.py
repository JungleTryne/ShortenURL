from django.shortcuts import render
from mshin_shortener import shorten

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