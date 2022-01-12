from django.shortcuts import render

# Create your views here.



def setCookie(request):
    response = render(request, 'student/setCookie.html')
    response.set_cookie('name', 'Moin', max_age=10)
    return response


def getCookie(request):
    nm = request.COOKIES.get('name', 'Guest')
    return render(request, 'student/getCookie.html', {'name':nm})


def delCookie(request):
    response = render(request, 'student/delCookie.html')
    response.delete_cookie('name')
    return response