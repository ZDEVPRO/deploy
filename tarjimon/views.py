from django.shortcuts import render
from .models import Lugat



def index(request):
    soz = request.GET.get('q', '').title()

    if soz and soz != '':
        natija = Lugat.objects.filter(inglizcha=soz).all()  #prog -> Prog
    else:
        natija = None
    return render(request, 'index.html', {'q': soz, 'natija': natija})
