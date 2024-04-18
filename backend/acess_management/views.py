from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import users
from .forms import YourForm
from django.core.paginator import Paginator
from django.http import QueryDict
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse

def members(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())


def updateUserData(request):
    success_msg = None
    body_unicode = request.body.decode('utf-8')
    body_data = QueryDict(body_unicode)
    if(body_data.get('_method') == 'PUT'):
        user_data = users.objects.get(id=body_data.get('id'))
        user_data.first_name = body_data.get('first_name')
        user_data.last_name = body_data.get('last_name')
        user_data.phone = body_data.get('phone')
        user_data.gender = body_data.get('gender')
        user_data.address = body_data.get('address')
        user_data.city = body_data.get('city')
        user_data.salary = body_data.get('salary')
        user_data.save()
    return datawithpaginator(request,True)

def deleteUser(request, id):
    try:
        user = get_object_or_404(users, pk=id)
        user.delete()
        # Return a success message
        return datawithpaginator(request,False)
    except Exception as e:
        # Return an error message if deletion fails
        return JsonResponse({'success': False, 'error': str(e)})

def userData(request):
    success_msg = None
    if (request.method == 'POST'):
        form = YourForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            your_model_instance = users(
                id=form_data['id'],
                first_name=form_data['first_name'],
                last_name=form_data['last_name'],
                phone=form_data['phone'],
                gender=form_data['gender'],
                address=form_data['address'],
                city=form_data['city'],
                salary=form_data['salary']  
            )
            success_msg = True
            your_model_instance.save()
            data = users.objects.all().values()
            paginator = Paginator(data, 5)  # 10 items per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            template = loader.get_template('users.html')
            context = {'usersData': page_obj,'success_msg': success_msg}
            return HttpResponse(template.render(context, request))
           
        else:
            return HttpResponse("Method not allowed!")
    else:
        return datawithpaginator(request,False)
       
def fetchUserData(request,id):
    data = users.objects.get(id=id)
    context = {'usersData': [data],'fetchUsersData': [data]}
    rendered_template = render(request, 'users.html', context)
    return HttpResponse(rendered_template)



def datawithpaginator(request,context_with_msg):
    data = users.objects.all().values()
    paginator = Paginator(data, 5)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = loader.get_template('users.html')
    if(context_with_msg):
        context = {'usersData': page_obj,'success_msg': True}
    else:
        context = {'usersData': page_obj}
        
    return HttpResponse(template.render(context, request))