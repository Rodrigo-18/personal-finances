from django.contrib.auth import authenticate, login, logout as sair
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Balanco, Usuario
from .forms import SignUpForm, ReceitaForm, DespesaForm
from django.utils import timezone
import logging
@login_required(login_url='/login')
def index(request):
    try:
      user = Usuario.objects.get(user = request.user)                                                               
      context = Balanco.objects.filter(user = user, date__month__gte = timezone.now().month)[0]
      return render(request, 'index.html',{'balanco': context})
    except: 
      user = Usuario.objects.get(user = request.user)
      balanco = Balanco.objects.create(user = user, date = timezone.now())
      return render(request, 'index.html',{'balanco': balanco})
@login_required
def logout(request):
    sair(request)
    return redirect('/login')
    
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        usuario = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if usuario:
            login(request, usuario)
            return redirect('/')
        else:
            return render(request, 'login.html', {'message':"Usuario ou Senha incorretos"})
    return render(request, 'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form_usuario = SignUpForm(request.POST)
        if form_usuario.is_valid():
            user = form_usuario.save()
            usuario = Usuario.objects.create(user = user)
            balanco = Balanco.objects.create(user = usuario, date = timezone.now())
            balanco.save()
            usuario.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form_usuario': form_usuario})
    else:
        form_usuario = SignUpForm()
        return render(request, 'signup.html', {'form_usuario': form_usuario})
@login_required(login_url='/login')
def receita(request):
    if request.method == "POST":
        form_receita = ReceitaForm(request.POST)
        if form_receita.is_valid():
            post = form_receita.save(commit=False)
            user = Usuario.objects.get(user = request.user)
            try:
                balanco = Balanco.objects.filter(date__month__gte = post.date.month, user = user)[0]
                if(balanco.date.month == post.date.month):
                   post.balanco = balanco
                   post.save()
                   return render(request, 'add_receita.html', {'message': 'Adicionado com sucesso','form_receita': form_receita})
                else:
                    balanc = Balanco.objects.create(user = user, date = post.date)
                    post.balanco = balanc
                    post.save()
                    return render(request, 'add_receita.html', {'message': 'Adicionado com sucesso','form_receita': form_receita})
            except:
                balanc = Balanco.objects.create(user = user, date = post.date)
                post.balanco = balanc
                post.save()
                return render(request, 'add_receita.html', {'message': 'Adicionado com sucesso','form_receita': form_receita})
        else:
            return render(request, 'add_receita.html', {'form_receita': form_receita})
    else:
        form_receita = ReceitaForm()
        return render(request, 'add_receita.html', {'form_receita': form_receita})

@login_required(login_url='/login')
def despesa(request):
    if request.method == "POST":
        form_despesa = DespesaForm(request.POST)
        if form_despesa.is_valid():
            post = form_despesa.save(commit=False)
            user = Usuario.objects.get(user = request.user)
            try:
                balanco = Balanco.objects.filter(date__month__gte = post.date.month, user = user)[0]
                if(balanco.date.month == post.date.month):
                   post.balanco = balanco
                   post.save()
                   return render(request, 'add_despesa.html', {'message': 'Adicionado com sucesso','form_despesa': form_despesa})
                else:
                    balanc = Balanco.objects.create(user = user, date = post.date)
                    post.balanco = balanc
                    post.save()
                    return render(request, 'add_despesa.html', {'message': 'Adicionado com sucesso','form_despesa': form_despesa})
            except:
                balanc = Balanco.objects.create(user = user, date = post.date)
                logger = logging.getLogger(__name__)
                logger.error('page_processor logging test')
                post.balanco = balanc
                post.save()
                return render(request, 'add_despesa.html', {'message': 'Adicionado com sucesso','form_despesa': form_despesa})
    else:
        form_despesa = DespesaForm()
        return render(request, 'add_despesa.html', {'form_despesa': form_despesa})

@login_required(login_url='/login')       
def outros(request):
    user = Usuario.objects.get(user = request.user)
    context = Balanco.objects.filter(user = user).order_by('date')
    return render(request, 'outros.html',{'balanco': context})