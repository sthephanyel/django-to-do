from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages 
import datetime
# Create your views here.

from .forms import TaskForm

from .models import Task

# verifica se o usuario esta authenticado, nativo do proprio django
@login_required
def taskList(request):
    # name="search" - é o name do input de busca
    search = request.GET.get('search')
    # filtro dos status
    filter = request.GET.get('filter')
    # caso tenha o valor de busca entra nesse if

    # dados para serem mostrados no dashboard
    tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    if search:
        # filtra pelo search enviado para tag da url
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)
    else:
        # pegando todos as tasks do banco em ordem de criacao
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        # divide os valores recebidos de 3 por pagina
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        # valores que realmente serao exibidos para o usuario limitado pela paginacao de 3 por pagina
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {
        'tasks': tasks, 
        'tasksrecently': tasksDoneRecently,
        'tasksdone':tasksDone,
        'tasksdoing':tasksDoing
    })

# retorna informacoes de uma task especifica
@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
    # caso acione o metodo POST "Criar Tarefa", sera enviado e armazenado no BD
    if request.method == 'POST':
        # pega o modelo do formulario do Django
        form = TaskForm(request.POST)
        # valida se os dados estao corretos
        if form.is_valid():
            # pausa temporariamente a acao de salvar
            task = form.save(commit=False)
            # modifica o campo done para doing
            task.done = 'doing'
            # registra usando o id do usuario
            task.user = request.user
            # apos essa alteracao salva no banco
            task.save()
            # messagem que é mostrada ao usuario
            messages.success(request, 'Tarefa adicionada com sucesso.')
            # redireciona o usuario para tela principal da listagem
            
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    # carrega a task especifica
    task = get_object_or_404(Task, pk=id)
    # carrega o formulario com as informacoes antigas
    # pega o modelo do formulario do Django
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            messages.success(request, 'Tarefa alterada com sucesso.')
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

# delete a task do banco
@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)
    status = ''
    if(task.done == 'doing'):
        task.done = 'done'
        status = 'Concluido'
    else:
        task.done = 'doing'
        status = 'Em Andamento...'
    
    task.save()
    messages.info(request, "Status da tareda alterado para: %s" %status)
    return redirect('/')

def helloWorld(request):
    return HttpResponse('Hello World')

# pega um parametro passado na url
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})