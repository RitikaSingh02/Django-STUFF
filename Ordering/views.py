from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaform
from django.forms import formset_factory
from .models import Pizza


def home(request):
    return render(request, 'home.html')


def order(request):
    multiple_form = MultiplePizzaform()
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, request.FILES)
        print(filled_form)  # full form html
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_id = created_pizza.id
            note = "YOUR %s %s %s %s PIZZA IS ON ITS WAY!!" % (filled_form.cleaned_data['size'],
                                                               filled_form.cleaned_data['topping1'],
                                                               filled_form.cleaned_data['topping2'],
                                                               filled_form.cleaned_data['topping3'])
            new_form = PizzaForm()
            return render(request, 'order.html', {'pizzaform': new_form, 'note': note, 'created_pizza_id': created_pizza_id, 'multiple_form': multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'order.html', {'pizzaform': form, 'multiple_form': multiple_form})
# Create your views here.


def pizzas(request):
    number_pizza = 2
    filled_multiple_form = MultiplePizzaform(request.GET)
    if filled_multiple_form.is_valid():
        number_pizza = filled_multiple_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_pizza)
    print(PizzaFormSet)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        print(filled_formset)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'pizzas have been ordered'
        else:
            note = 'Order was not created , please try again'
        return render(request, 'pizzas.html', {'note': note, 'formset': formset})
    elif request.method == 'GET':
        return render(request, 'pizzas.html', {'formset': formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = "Order has been edited"
            return render(request, 'edit_order.html', {'pizzaform': form, 'pizza': pizza, 'note': note})

    return render(request, 'edit_order.html', {'pizzaform': form, 'pizza': pizza})
