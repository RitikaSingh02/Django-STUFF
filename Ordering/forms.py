from django import forms
from . models import Pizza


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(
#         label='topping1', max_length=100)
#     topping2 = forms.CharField(label='topping2', max_length=100)
#     topping3 = forms.CharField(label='topping3', max_length=100)
#     # toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), (
#     #     'cheese', 'Cheese'), ('olives', "Olives")], widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label="size", choices=[(
#         "small", "Small"), ("medium", "Medium"), ("large", "Large")])


# creating a model form

class PizzaForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'topping3', 'size']
        labels = {'topping1': "TOPPING 1"}
        # changes the label for field 'toppping1' to TOPPING 1
