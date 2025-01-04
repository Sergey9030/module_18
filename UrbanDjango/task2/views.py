from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def funct_index(request):
    return render(request, 'second_task/funct_template.html')

class class_index(TemplateView):
    template_name = 'second_task/class_template.html'
