from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import User

def show_user_info(request):
    # 获取所有用户信息
    users = User.objects.all()
    # 将用户信息传递给模板
    return render(request, 'user_info.html', {'users': users})
def search_user(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')  # 获取用户输入的名字
        users = User.objects.filter(Fname__icontains=name)  # 根据名字搜索用户，忽略大小写
        num=users.count()
        return render(request, 'user_info.html', {'users': users, 'searched_name': name,'num':num})
    return render(request, 'user_info.html', {'users': None, 'searched_name': None})
