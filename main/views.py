from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406436045',
        'name': 'Saikhah Ummu Anja Amalia',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)