import zoneinfo

from django.shortcuts import render

# Create your views here.
from .models import Order

tz_name = zoneinfo.available_timezones()
def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {
        'object_list': object_list,
        # 'tz_name': tz_name,
    })

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    # order01 = Order(order_name='Алексей',order_phone='222')
    # order01.save()
    Order.objects.create(order_name=name, order_phone=phone)
    return render(request,'./thanks_page.html', {'name': name, 'phone': phone})
