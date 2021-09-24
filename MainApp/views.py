from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet, LANG_CHOICE
from MainApp.froms import SnippetForm, CommentForm
from MainApp.froms import UserForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


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
        messages.success(request, 'Сниппет добавлен успешно')
        return redirect('List')
    raise Http404


def snippets_page(request):
    lang = request.GET.get("lang", 'all')
    if request.user.is_authenticated:
        snippet = Snippet.objects.filter(Q(is_private=False) | Q(author=request.user))
    else:
        snippet = Snippet.objects.filter(is_private=False)

    if lang != 'all':
        snippet = snippet.filter(lang=lang)
    context = {
        "pagename": 'Просмотр сниппетов',
        "snippets": snippet,
        "langs": LANG_CHOICE,
        "selected": lang
    }
    return render(request, 'pages/view_snippets.html', context)


@login_required
def snippets_my(request):
    lang = request.GET.get("lang", 'all')
    if lang == 'all' or lang == '--------':
        snippet = Snippet.objects.filter(author=request.user)
    else:
        snippet = Snippet.objects.filter(author=request.user).filter(lang=lang)
    context = {
        "pagename": 'Просмотр моих сниппетов',
        "snippets": snippet,
        "langs": LANG_CHOICE,
        "selected": lang
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
    if snippet.author != request.user:
        raise HttpResponseForbidden
    form = SnippetForm(request.POST, instance=snippet)
    if form.is_valid():
        form.save()
        messages.success(request, 'Сниппет изменен')
        return redirect('List')


@login_required
def snippet_delete(request, id):
    if request.method == "GET":
        snippet = get_object_or_404(Snippet, pk=id)
        if snippet.author != request.user:
            raise HttpResponseForbidden
        snippet.delete()
        return redirect('List')


def snippet_page(request, id):
    snippet = get_object_or_404(Snippet, pk=id)
    if snippet.is_private and snippet.author != request.user:
        raise Http404
    comment = snippet.comments.all()
    form = CommentForm()
    context = {
        "snippet": snippet,
        "form": form,
        "comments": comment
    }
    return render(request, 'pages/snippet_page.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Вход выполнен успешно')
        else:
            context = {}
            context["error"] = "Введен неправильный логин или пароль"
            messages.error(request, 'Введен неправильный логин или пароль')
            return render(request, 'pages/index.html', context)
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('Home')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированны')
            return redirect('Home')
        else:
            context = {
                "pagename": "Регистрация пользователя",
                "form": form
            }
            return render(request, 'pages/register.html', context)
    else:
        form = UserForm()
        context = {
            "pagename": "Регистрация пользователя",
            "form": form
        }
        return render(request, 'pages/register.html', context)


@login_required
def comment_add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        snippet_id = request.POST["id"]
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            snippet = Snippet.objects.get(id=snippet_id)
            comment.snippet = snippet
            comment.save()
            messages.success(request, 'Комментарий добавлен')
            return redirect(f'/snippets/page/{snippet_id}')

    raise Http404
