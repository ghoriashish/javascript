from django.shortcuts import render

# Create your views here.
def JSPage(request):
    return render(request,"app/js.html")
