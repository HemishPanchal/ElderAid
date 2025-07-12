from django.shortcuts import render,redirect
from .forms import ServiceForm,services
# Create your views here.
def services_list(request):
    context= {'services_list': services.objects.all()}
    return render(request,"elder_services/services_list.html",context)

def services_add(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = ServiceForm()
        else:
            ser=services.objects.get(pk=id)
            form=ServiceForm(instance=ser)
        return render(request,"elder_services/services_add.html",{'form':form})
    else:
        if id==0:
            form=ServiceForm(request.POST)
        else:
            ser=services.objects.get(pk=id)
            form = ServiceForm(request.POST,instance=ser)        
        if form.is_valid():
            form.save()
        return redirect('/services/list')

def services_delete(request,id):
    ser=services.objects.get(pk=id)
    ser.delete()
    return redirect('/services/list')
    