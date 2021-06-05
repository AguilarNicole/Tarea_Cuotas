from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

datos = [
    {
        'monto': '10000',
        'tasa': '6',
        'plazo': '3',
        'cuotas': '555',
        'totalPagar': '11800'
    }
]


def plantilla(request):

    if request.method == 'POST':
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        r = tasa / 100 / 12
        n = plazo * 12

        c = (monto*r)/(1-(1+r)**-n)

        tp = monto + monto * r * n

        ctx = {
            'datos': datos
        }

        datos.append({
            'monto': monto,
            'tasa': tasa,
            'plazo': plazo,
            'cuotas': c,
            'totalPagar': tp,
        })

        return render(request, 'app/plantilla.html', ctx)

    else:
        #metodo GET
        #contexto va pa la plantilla
        ctx = {
            'datos': datos
        }

        return render(request, 'app/plantilla.html', ctx)
