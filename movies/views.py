from django.shortcuts import render


def home_view(request):
    template = 'movies/home.html'
    context = {
        'title': 'Graphene API'
    }
    return render(request, template, context)
