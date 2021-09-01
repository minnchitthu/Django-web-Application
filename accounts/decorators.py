from django.http.response import HttpResponse
from django.shortcuts import redirect
def authenticated_user(view_fun):
    def wrapper(request):
        if not request.user.is_authenticated:
            return view_fun(request)
        else:
            return redirect('/')
    return wrapper

def admin_only(view_fun):
    def wrapper(request):
        if request.user.groups.first().name=='admin':
            return view_fun(request)
        if request.user.groups.first().name=='customer':
            return redirect('/customer_profile')
    return wrapper

def allowed_roles(roles=[]):
    def decorators(views_fun):
        def wrapper(request,*args, **kwargs):
            if request.user.groups.first().name in roles:
                return views_fun(request,*args,**kwargs)
            else:
                return HttpResponse('You are not authorized this page.',request)
        return wrapper
    return decorators