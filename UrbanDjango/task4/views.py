from django.shortcuts import render

# Create your views here.
def main_index(request):
    return render(request, 'fourth_task/main_page.html')

def second_index(request):
    context = {'games': ['Atomic Heart', "Cyberpunk 2077"]}
    return render(request, 'fourth_task/second_page.html', context)

def third_index(request):
    return render(request, 'fourth_task/third_page.html')
