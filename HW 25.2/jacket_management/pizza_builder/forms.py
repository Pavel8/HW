from django import forms

class PizzaForm(forms.Form):
    ingredients = forms.MultipleChoiceField(
        choices=[
            ('cheese', 'Sýr'),
            ('tomato', 'Rajčata'),
            ('bacon', 'Slanina'),
            ('mushrooms', 'Hlíva'),
            ('pepper', 'Paprika'),
            ('olives', 'Olivy'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
