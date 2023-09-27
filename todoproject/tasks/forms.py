from django import forms

from .models import Task
# pip install django-crispy-forms
# pip install crispy-bootstrap4

# controla os recursos solicitados pelo form
class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        # modelo de formulario disponivel no proprio Django
        fields = ('title','description')
        # fields = ('title','description','done')