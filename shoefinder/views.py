from django.shortcuts import render


def finder(request):
    if request.method != 'POST':
        return render(request, 'finder.html')
    else:
        return render(request, 'finder.html')