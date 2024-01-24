from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from . import models
import json

# Create your views here.
def main(request):
    contacts = models.Contact.objects.all()
    context = {'contacts' : contacts}
    return render(request, 'main.html', context)

def form(request):
    if request.method == 'POST':
        contact = json.loads(request.body)
        name = contact.get('name')
        phone = contact.get('phone')
        created = models.Contact.objects.create(name=name, phone=phone)
        return JsonResponse({'reply' : 'success', 'id':created.id, 'name':created.name, 'phone':created.phone})
    return JsonResponse({'reply' : 'reject', })

    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     models.Contact.objects.create(name=name, phone=phone)
    # return redirect('main')


def view(request, id):
    contact = models.Contact.objects.get(id=id)
    context = {'contact' : contact}
    return render(request, 'view.html', context)

def del_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    contact.delete()
    return redirect('main')

def search(request):
    q = request.GET.get('q')
    if q is not None:
        contacts = models.Contact.objects.filter(name__contains=q)
    else:
        contacts = models.Contact.objects.all()
    context = {'contacts' : contacts}
    return render(request, 'search.html', context)
