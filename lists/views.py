from django.shortcuts import render
from .models import Item  # Importe o modelo Item do seu aplicativo

def home_page(request):
    if request.method == 'POST':
        item_text = request.POST.get('item_text', '')
        item_priority = request.POST.get('priority', '')  # Supondo que você tenha um campo 'priority' no formulário
        Item.objects.create(text=item_text, priority=item_priority)

    items = Item.objects.all()  # Recupere todos os itens da base de dados
    return render(request, 'home.html', {'items': items})
