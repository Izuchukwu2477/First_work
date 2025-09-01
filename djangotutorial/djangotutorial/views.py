from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>go and buy data</h1> <h1 style='background-color:Tomato;'>Tomato</h1>")
