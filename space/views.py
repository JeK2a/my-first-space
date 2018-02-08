from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Space


def message_list(request):
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'space/message_list.html', {'messages': messages})


def mark_read(request):
    id = request.GET.get('id')
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    Space.objects.update_or_create(id=id, defaults={'read': True})
    return render(request, 'space/message_list.html', {'messages': messages})


def mark_all_not_read(request):
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    for message in messages:
        Space.objects.update_or_create(id=message.id, defaults={'read': False})
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'space/message_list.html', {'messages': messages})
