from django.views.generic import ListView
from .models import message
#def messageView(request):
#    return render (request, 'home.html')

class MessageView(ListView):
    model = message
    template_name = 'home.html'
