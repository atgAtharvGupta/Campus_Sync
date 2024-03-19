# from functools import _Descriptor
from io import StringIO
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from Resources.models import Department, Student
from datetime import date
from Thesis import models
from .models import Thesis
import os


from .forms import AddForm
from django.core.paginator import Paginator
from django.urls import reverse
import csv
import datetime
from django.template.loader import get_template
from xhtml2pdf import pisa



# @permission_required('Resources.student_rights')
def manage(request):
    return render(request, 'Thesis/Manage.html', {'AddForm': AddForm()})

@permission_required('Resources.student_rights')
def Search_by_Name(request):
    if request.method == "POST":
        Search_thesis = request.POST.get('Thesis_Name')
        Search = Thesis.objects.filter(Thesis_Name__contains=Search_thesis)
        total=Search.count()
        
        if total:
            paginator = Paginator(Search, 10)  # Show 10 contacts per page
            page = request.GET.get('page')
            thesis= paginator.get_page(page)
            return render(request, 'Thesis/Search.html', {"thesis":thesis,'total':total})
        else:
            return render(request, 'Thesis/Manage.html', {'Message_Search': 'Thesis not found.', 'visiblity': 'visible', 'color': 'danger', 'AddForm': AddForm()})
    
    return render(request, 'Thesis/Manage.html',{'AddForm': AddForm()})

def Search_by_Area(request):
    if request.method == "POST":
        Search_the_thesis = request.POST.get('Thesis_Area')
        SearchArea= Thesis.objects.filter(Area__contains=Search_the_thesis)
        total=SearchArea.count()
        
        if total:
            paginator = Paginator(SearchArea, 10)  # Show 10 contacts per page
            page = request.GET.get('page')
            thesis= paginator.get_page(page)
            return render(request, 'Thesis/Search.html', {"thesis":thesis,'total':total})
        else:
            return render(request, 'Thesis/Manage.html', {'Message_Search': 'Thesis not found.', 'visiblity': 'visible', 'color': 'danger', 'AddForm': AddForm()})
    
    return render(request, 'Thesis/Manage.html',{'AddForm': AddForm()})
def Search_by_Tech_used(request):
    if request.method == "POST":
        Search_the_thesis_tech = request.POST.get('Technology_used')
        SearchTech = Thesis.objects.filter(Technology_used__contains=Search_the_thesis_tech)
        total=SearchTech.count()
        
        if total:
            paginator = Paginator(SearchTech, 10)  # Show 10 contacts per page
            page = request.GET.get('page')
            thesis= paginator.get_page(page)
            return render(request, 'Thesis/Search.html', {"thesis":thesis,'total':total})
        else:
            return render(request, 'Thesis/Manage.html', {'Message_Search': 'Thesis not found.', 'visiblity': 'visible', 'color': 'danger', 'AddForm': AddForm()})
    
    return render(request, 'Thesis/Manage.html',{'AddForm': AddForm()})



        
@permission_required('Resources.student_rights')
def RemoveThesis(request,tname):

    
        tdelete = models.Thesis.objects.get(Thesis_Name=tname)
        tdelete.delete()
        return render(request, 'Thesis/Manage.html', { 'Message': 'Thesis Removed!', 'visiblity': 'visible', 'color': 'success', 'AddForm': AddForm()})



def Remove(request):
    if request.method == "POST":
        Search_thesis = request.POST.get('thesis_remove', None)
        Search = Thesis.objects.filter(Thesis_Name__contains=Search_thesis)
        total=Search.count()
        
        if total:
            paginator = Paginator(Search, 10)  # Show 10 contacts per page
            page = request.GET.get('page')
            thesis= paginator.get_page(page)
            return render(request, 'Thesis/Remove.html', {"thesis":thesis,'total':total})
        else:
            return render(request, 'Thesis/Manage.html', {'Message': 'Thesis not found.', 'visiblity': 'visible', 'color': 'danger', 'AddForm': AddForm()})
    
    return render(request, 'Thesis/Manage.html',{'AddForm': AddForm()})
    


@permission_required('Resources.student_rights')
def AddThesis(request):
    # context={}
    

    
    if request.method == 'POST':
        Form=AddForm(request.POST, request.FILES)
        
        if Form.is_valid():
            Tname=Form.cleaned_data['Thesis_Name']
            Des=Form.cleaned_data['Description']
            area=Form.cleaned_data['Area']
            tech=Form.cleaned_data['Technology_used']
            Sname=Form.cleaned_data['Student_Name']
            Enroll=Form.cleaned_data['Enrollment']
            Date=datetime.date.today()
            files=Form.cleaned_data['Pdf']
            ext = os.path.splitext(files.name)[1]  # [0] returns path+filename
            valid_extensions = ['.pdf']
            if ext.lower() in valid_extensions:
                print("iiiiiiiiiiiiiiiiiii")
                Thesis(Thesis_Name=Tname,Description=Des,Area=area,Technology_used=tech,Student_Name=Sname,Enrollment=Enroll,DOS=Date,Pdf=files).save()
                return render(request, 'Thesis/Manage.html', {'MessageExtension': 'Thesis added ', 'visiblity': 'visible', 'color': 'success', 'AddForm': AddForm()})
            else:
                return render(request, 'Thesis/Manage.html', {'MessageExtension': 'Thesis cannot be added. File extension should be .pdf', 'visiblity': 'visible', 'color': 'danger', 'AddForm': AddForm()})
       
        else:
            Form=AddForm()
            return render(request, 'Thesis/Manage.html',{'AddForm': Form})
    else:
        return render(request, 'Thesis/Manage.html',{'AddForm': AddForm()})
            

    
# @permission_required('Resources.student_rights')
# def Message(request):
#     return render(request, 'Thesis/Message.html')



@permission_required('Resources.student_rights')
def ListThesis(request):
    thesisAll=Thesis.objects.all()
    total=thesisAll.count()
    paginator = Paginator(thesisAll, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    thesis = paginator.get_page(page)
    return render(request, 'Thesis/List.html',{'thesis':thesis,'total':total})

@permission_required('Resources.student_rights')
def Report(request):
    template_path = 'Thesis/report.html'
    thesisAll =  models.Thesis.objects.all()
    total=thesisAll.count()
    context = {'thesis': thesisAll,'total':total}    
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    


        
        

