from django.shortcuts import render


def post_list(request):
    return render(request, 'space/message_list.html', {})
