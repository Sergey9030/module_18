from django.shortcuts import render

# Create your views here.
def main_index(request):
    return render(request, 'third_task/main_page.html')

def second_index(request):
#    p1 = {'1': 'П1', '2': 'П2', '3': 'П3', '4': 'П4'}
    btn_list = [['/', 'На главную'],
                ['/funct/', 'Функциональное представление'],
                ['/class/', 'Классовое представление'],
                ['https://t.me/telegram', 'Телега']
                ]
    context = {'bl': btn_list}
    return render(request, 'third_task/second_page.html', context)

def third_index(request):
    return render(request, 'third_task/third_page.html')
