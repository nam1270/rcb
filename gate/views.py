from django.shortcuts import render
from .forms import ResidentCheckForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Resident, Cottage
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ResidentCheckForm(request.POST)
        if form.is_valid():
            cottage_num_entered = form.cleaned_data['cottage_number']
            cottage_key_entered = form.cleaned_data['cottage_key']
            try:
                cottage = Cottage.objects.filter(cottage_number=cottage_num_entered)
                key = Cottage.objects.filter(unique_key=cottage_key_entered)
            except ObjectDoesNotExist:
                cottage = None;
                key = None;
            if cottage and key:
                return HttpResponse('<p>Yes</p>')
            else:
                return HttpResponse('<p>Nah</p>')
    else:
        form = ResidentCheckForm()
    return render(request, 'gate/index.html',{'form':form})