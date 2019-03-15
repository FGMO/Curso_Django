from django.shortcuts import render
from datetime import datetime

# Create your views here.

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Alguien',
            'img': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %d %Y'),
        'photo': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'title': 'Via lactea',
        'user': {
            'name': 'Fulano',
            'img': 'https://picsum.photos/60/60/?image=903'
        },
        'timestamp': datetime.now().strftime('%b %d %Y'),
        'photo': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'img': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]


def list_posts(request):
    return render(request, 'feed.html', {'posts': posts})
