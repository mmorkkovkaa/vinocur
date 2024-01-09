from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import wineshop
from django.shortcuts import HttpResponseRedirect
from wineshop import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket, Товары , ОформленныйЗаказ, ТоварВЗаказе, Отзыв, Поставщики
from django.contrib.auth.decorators import login_required



def index(request):
    index = models.Index.objects.all()
    поставщики = models.Поставщики.objects.all()
    return render(request, 'index.html', {'index': index, 'поставщики': поставщики})

def товары(request):
    товары = models.Товары.objects.all()
    отзывы = Отзыв.objects.all()
    return render(request, 'tovary.html', {'товары': товары, 'отзывы': отзывы})


def сотрудники(request):
    сотрудники = models.Сотрудники.objects.all()
    image = models.ImageDev.objects.all()
    клиенты = models.Клиенты.objects.all()

    context = {'сотрудники': сотрудники, 'image': image, 'клиенты': клиенты}

    return render(request, 'aboutus.html',context )




def добавить_в_корзину(request, товар_id):
    товар = Товары.objects.get(id=товар_id)
    активная_корзина, создана = Basket.objects.get_or_create(user=request.user, товар=товар)
    активная_корзина.quantity += 1
    активная_корзина.save()
    return redirect('товары')

def корзина(request):
    корзина = Basket.objects.filter(user=request.user)
    общая_стоимость = sum(item.товар.price  * item.quantity for item in корзина)
    return render(request, 'корзина.html', {'корзина': корзина, 'общая_стоимость': общая_стоимость})

@login_required
def оплатить_заказ(request):
    корзина = Basket.objects.filter(user=request.user)

    новый_заказ = ОформленныйЗаказ.objects.create(user=request.user, оплачен=True)

    for item in корзина:
        ТоварВЗаказе.objects.create(заказ=новый_заказ, товар=item.товар, количество=item.quantity)

    корзина.delete()

    return redirect('/')

def все_заказы(request):
    все_заказы = ОформленныйЗаказ.objects.all()
    return render(request, 'все_заказы.html', {'все_заказы': все_заказы})

