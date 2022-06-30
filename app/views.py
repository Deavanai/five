from django.shortcuts import render

# Create your views here.
def mugi(request):
    d={'name':'Mugesh','age':21}
    return render(request,'mugi.html',context=d)