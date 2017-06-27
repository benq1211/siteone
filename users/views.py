from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegisterForm

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', '')) #从 get 或者 post 请求中获取 next 参数值
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form,'next':next})


def index(request):
    return render(request,'index.html')