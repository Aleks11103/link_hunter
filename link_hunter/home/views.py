from django.shortcuts import render, HttpResponseRedirect
from home.forms import QuickContactForm, QuickForm


# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'home.html', context)


def about_page(request):
    context = {}
    return render(request, 'about.html', context)


def contact_page(request):
    context = {
        "form": QuickContactForm(),
    }
    if request.method == 'POST':
        form = QuicContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
        else:
            context.update(form=form)
    return render(request, 'contact.html', context)