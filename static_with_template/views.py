from django.shortcuts import render

def home(request):
    content = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'static_with_template/home.html', content)

def contact(request):
    return render(request, 'static_with_template/contact.html')
# Create your views here.
