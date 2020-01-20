from django.shortcuts import render, redirect
from .models import Student, Marks
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, "home.html")

def details(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        PRN = request.POST['prn']
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        subject3 = request.POST['subject3']
        subject4 = request.POST['subject4']
        semester = request.POST['semester']
        if Student.objects.filter(PRN=PRN).exists():
            messages.info(request, "PRN already assigned")
            return redirect('details')
        else:
            user = Student.objects.create(PRN=PRN, first_name=first_name, last_name=last_name)
            user.save()
            marks = Marks.objects.create(PRN=user, semester=semester,subject1=subject1, subject2=subject2, subject3=subject3, subject4=subject4)
            marks.save()
            return redirect('details')
    return render(request, 'sdet.html')


def enter(request):
    if request.method == "POST":
        PRN = request.POST.get('prn')
        semester = request.POST.get('semester')
        prn = int(PRN)
        user = Student.objects.filter(PRN=prn)
        if not user:
            messages.info(request, 'PRN does not exist')
            return redirect('/')
        else:
            marks = Marks.objects.filter(PRN=prn, semester=semester).values()
            # subject1 = request.POST.get('subject1')
            # subject2 = request.POST.get('subject2')
            # subject3 = request.POST.get('subject3')
            # subject4 = request.POST.get('subject4')
    return render(request, 'result.html', {'user': user, 'marks':marks})