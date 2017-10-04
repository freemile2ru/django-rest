import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# funtion based view
def home(request):
    num = random.randint(1, 1000000000)
    some_list = ["gari", "sugar", "milk", "ground nut"]
    # return HttpResponse("<h1>hello</h1>")
    return render(request, "base.html", {"language": "Django", "num": num, "some_list": some_list})