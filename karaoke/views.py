from django.shortcuts import render

def index(request):
    context = {
        'nomes':[
        'João',
        'Murilo',
        'Carla',
        ],
        'vazio': False,
        'teste': 'teste'}
    return render(request, 'index.html',context)
