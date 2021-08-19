from django.shortcuts import redirect, render
from .forms import ContactUsForm
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        f = ContactUsForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Your message has been sent. Thank you!')
            return redirect('/#contact')
    else:
        f = ContactUsForm()
    return render(request, 'resume/pages/index.html', {'form': f})