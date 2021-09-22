from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippet = Snippet.objects.all()
    context = {
        "pagename": 'Просмотр сниппетов',
        "snippets": snippet
    }

    return render(request, 'pages/view_snippets.html', context)

def snippets_create(request):
    if request.method == "POST":
        print(request.POST)
        snippet = Snippet(name=request.POST["name"], lang=request.POST["lang"], code=request.POST["code"])
        snippet.save()
        return redirect('List')
    raise Http404
