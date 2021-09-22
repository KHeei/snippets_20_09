from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet
from MainApp.froms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
                   'form': form
                   }
        return render(request, 'pages/add_snippet.html', context)

    print(request.POST)
    form = SnippetForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('List')
    raise Http404

def snippets_page(request):
    snippet = Snippet.objects.all()
    context = {
        "pagename": 'Просмотр сниппетов',
        "snippets": snippet
    }
    return render(request, 'pages/view_snippets.html', context)


def snippet_edit(request,id):
    if request.method == "GET":
        snippet = get_object_or_404(Snippet, pk=id)
        form = SnippetForm(instance=snippet)
        context = {'pagename': 'Редактирование сниппета',
                   'form': form,
                   'button_name': 'Редактировать'
                   }
        return render(request, 'pages/add_snippet.html', context)
    # POST
    snippet = get_object_or_404(Snippet, pk=id)
    form = SnippetForm(request.POST, instance=snippet)
    if form.is_valid():
        form.save()
        return redirect('List')

def snippet_delete(request, id):
    if request.method == "GET":
        snippet = get_object_or_404(Snippet, pk=id)
        snippet.delete()
        return redirect('List')
