from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Palmer
import cv2 

def main(request):
    return render(request, 'fp_app/main.html')
    
def new(request):
    if request.method == "POST":
        form = forms.PalmerForm(request.POST, request.FILES)
        if form.is_valid():
        
            palmer = form.save()    
            palmer.process()
            
        return redirect('fp_app.views.details', pk=palmer.id)

    else:
        form = forms.PalmerForm()
    
    return render(request, 'fp_app/new.html', {'form':form})
    
def details(request, pk):
    
    palmer = get_object_or_404(Palmer, id=pk)
    return render(request, 'fp_app/details.html', {'result_url':palmer.result_absolute_url()})
    
    