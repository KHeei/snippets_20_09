from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet
from MainApp.froms import SnippetForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


@login_required
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
        snippet = form.save(commit=False)
        snippet.author = request.user
        snippet.save()
        return redirect('List')
    raise Http404


def snippets_page(request):
    snippet = Snippet.objects.all()
    context = {
        "pagename": 'Просмотр сниппетов',
        "snippets": snippet
    }
    return render(request, 'pages/view_snippets.html', context)


@login_required
def snippets_my(request):
    snippet = Snippet.objects.filter(author=request.user)
    context = {
        "pagename": 'Просмотр моих сниппетов',
        "snippets": snippet
    }
    return render(request, 'pages/view_snippets.html', context)

@login_required
def snippet_edit(request, id):
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


@login_required
def snippet_delete(request, id):
    if request.method == "GET":
        snippet = get_object_or_404(Snippet, pk=id)
        snippet.delete()
        return redirect('List')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            context = {}
            context["error"] = "Введен неправильный логин или пароль"
            return render(request, 'pages/index.html', context)
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('Home')