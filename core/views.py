from django.shortcuts import render


def heandl404(request):
    return render(request, '404.html')
