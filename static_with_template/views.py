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

def p1(request):
    body = {
        'user': "John",
        'login': True,
        'password_length': 16
    }
    return render(request, 'static_with_template/page1.html', body)

def p2(request):
    list1 = {
        'list1': [1, 2, 100, 200]
    }
    dict1 = {
        'dict1': {"A": 1, "B": 2, "C": 3, "D": 4, "E": 3}
    }
    return render(request, 'static_with_template/page2.html', list1, dict1)


# Create your views here.

