from django.shortcuts import render
from django.utils import timezone
from .models import Space


def post_list(request):
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'space/message_list.html', {'messages': messages})
