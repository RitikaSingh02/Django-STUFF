from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, 'home.html')


def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, request.FILES)
        print(filled_form)  # full form html
        if filled_form.is_valid():
            note = "YOUR %s %s %s %s PIZZA IS ON ITS WAY!!" % (filled_form.cleaned_data['size'],
                                                               filled_form.cleaned_data['topping1'],
                                                               filled_form.cleaned_data['topping2'],
                                                               filled_form.cleaned_data['topping3'])
            new_form = PizzaForm()
            return render(request, 'order.html', {'pizzaform': new_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'order.html', {'pizzaform': form})
# Create your views here.
