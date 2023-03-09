from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm


def status(request):
    return render(request, 'status.html')


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect('form:status')

            
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'form': form})

    


def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('form:order')

def order(request):
    order = Order.objects.all()
    return render(request, 'order_list.html', {'order': order})
