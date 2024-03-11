from django.shortcuts import render,HttpResponse
 
def html_page(request):
    return render(request, 'RoPaSc.html')
