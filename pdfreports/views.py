from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import PdfreportForm
from .models import Pdfreport


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def pdfreport_list(request):
    pdfreports = Pdfreport.objects.all()
    return render(request, 'pdfreport_list.html', {
        'pdfreports': pdfreports
    })


def upload_pdfreport(request):
    if request.method == 'POST':
        form = PdfreportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdfreport_list')
    else:
        form = PdfreportForm()
    return render(request, 'upload_pdfreport.html', {
        'form': form
    })


def delete_pdfreport(request, pk):
    if request.method == 'POST':
        pdfreport = Pdfreport.objects.get(pk=pk)
        pdfreport.delete()
    return redirect('pdfreport_list')


class PdfreportListView(ListView):
    model = Pdfreport
    template_name = 'class_pdfreport_list.html'
    context_object_name = 'pdfreports'


class UploadPdfreportView(CreateView):
    model = Pdfreport
    form_class = PdfreportForm
    success_url = reverse_lazy('class_pdfreport_list')
    template_name = 'upload_pdfreport.html'
# Create your views here.
