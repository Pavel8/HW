from django.shortcuts import render
from .forms import PizzaForm

def pizza_view(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            # Uložíme vybrané ingredience do cookies
            selected_ingredients = form.cleaned_data['ingredients']
            response = render(request, 'pizza.html', {'form': form, 'selected_ingredients': selected_ingredients})

            # Nastavíme cookies, které budou platné 7 dní
            response.set_cookie('selected_ingredients', ','.join(selected_ingredients), max_age=7*24*60*60)
            return response
    else:
        form = PizzaForm()

        # Načteme ingredience z cookies, pokud existují
        selected_ingredients = request.COOKIES.get('selected_ingredients', '').split(',')

        return render(request, 'pizza.html', {'form': form, 'selected_ingredients': selected_ingredients})
