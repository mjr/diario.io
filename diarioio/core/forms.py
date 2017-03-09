from django import forms


class EntradaForm(forms.Form):
    objetivos = forms.CharField(widget=forms.Textarea)
    materiais_metodos = forms.CharField(widget=forms.Textarea)
    link_tarefa = forms.URLField(widget=forms.URLInput)
