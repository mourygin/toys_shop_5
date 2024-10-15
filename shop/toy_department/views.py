from django.shortcuts import render
from django.http import HttpResponse
from .forms import DjangoRegForm

# Create your views here.
def main_page(request):
    pn = 'Добро пожаловать в наш игрушечный магазин игрушек!'
    context = {'pn': pn}
    return render(request, 'main_page.html', context)
def shop_page(request):
    pn = 'Выбери игрушку по своему вкусу!'
    context = {'pn': pn}
    return render(request, 'toy_selection.html', context)
def basket_page(request):
    pn = 'BASKET'
    context = {'pn':pn}
    return render(request,'basket.html', context)
def purchases_page(request):
    pn ='К сожалению Ваша корзина пуста...'
    contest = {'pn': pn}
    return render(request,'purchases.html',contest)

def login_page(request):
    pn ='Мы рады Вас видеть!'
    contest = {'pn': pn}
    return render(request, 'login_page.html',contest)
def show_ignatiy(request):
    return render(request, 'show_ignatiy.html')
def show_teddy_bear(request):
    return render(request, 'show_teddy_bear.html')
def show_cat(request):
    return render(request, 'show_cat.html')
def show_pafnutiy(request):
    return render(request, 'show_pafnutiy.html')
def basket_page(request):
    return render(request, 'basket.html')

def html_reg(request):
    pn = 'Use this HTML-form for registration.'
    contest = {'pn': pn}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        print(username)
        print(email)
        print(age)
        print(password)
        print(re_password)
        print('-----------------------------------')

        if username in ['Бендер', 'Балаганов', 'Паниковский', 'Козлевич']:
            response = 'This username is used yet!'
        elif int(age) < 18:
            response = 'You are too yang for the site!'
        elif password != re_password:
            response = 'Your password typings are not identucal!'
        else:
            response = 'You have succefuly registrated via HTML-form!'
        print(response)
        return HttpResponse(response)
    else:
        pass
    return render(request, 'html_reg.html',contest)

def django_reg(request):
    pn = 'Use this Django-form for registration.'

    if request.method == 'POST':
        form = DjangoRegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']

            if username in ['Бендер', 'Балаганов', 'Паниковский', 'Козлевич']:
                response = 'This username is used yet!'
            elif int(age) < 18:
                response = 'You are too yang for the site!'
            elif password != re_password:
                response = 'Your password typings are not identucal!'
            else:
                response = 'You have succefuly registrated via Django-form!'
            print(response)
            return HttpResponse(response)

    else:
        form = DjangoRegForm()
    contest = {'pn': pn, 'form':form}
    return render(request, 'django_reg.html', contest)
