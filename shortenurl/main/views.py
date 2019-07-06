from django.shortcuts import render

# Create your views here.
def main_page(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        print(request.POST)
        return render(request, "index.html")