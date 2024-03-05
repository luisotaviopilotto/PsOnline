from django.shortcuts import render

# FORMULÁRIO DE LOGIN
def user_authentication(request):
    return render(request, 'login.html')
