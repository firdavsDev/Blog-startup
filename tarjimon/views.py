from django.shortcuts import render
import string
# Create your views here.
from .models import Lugat


def tarjima(request):
    if request.method == 'GET':
        soz = request.GET.get('q', '')
        if soz and soz != '':
            natija = Lugat.objects.filter(inglizcha__contains=soz).all()[:5]
        else:
            natija = None

    return render(request, 'tarjimon.html', {'q':soz, 'natija': natija})
