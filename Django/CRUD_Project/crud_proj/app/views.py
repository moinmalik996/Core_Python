from django.shortcuts import render, HttpResponseRedirect
#importing Models
from .models import StudentData
#importing Forms
from .forms import StudentRegistration
# Create your views here.



# This function will ADD and SHOW records of students
def add_show(request):
    if request.method == 'POST':
        stu_fm = StudentRegistration(request.POST)
        if stu_fm.is_valid():
            # stu_fm.save()                  # This method do not require model in views.py
            #                                # instead it saves the data in database in shortcut form.
            nm = stu_fm.cleaned_data['name']
            em = stu_fm.cleaned_data['email']
            pw = stu_fm.cleaned_data['pass_w']

            reg = StudentData(name=nm, email=em, pass_w=pw)
            reg.save()

            stu_fm = StudentRegistration()
    else:
        stu_fm = StudentRegistration()
    
    stu_db = StudentData.objects.all()
        
    return render(request, 'app/addAndshow.html', {'stu_fm':stu_fm, 'stu_db':stu_db})



#This function will update the data
def update_data(request, id):
    if request.method == 'POST':
        stu_db = StudentData.objects.get(pk=id)
        stu_fm = StudentRegistration(request.POST, instance=stu_db)
        if stu_fm.is_valid():
            stu_fm.save()
    else:
        stu_db = StudentData.objects.get(pk=id)
        stu_fm = StudentRegistration(instance=stu_db)

    return render(request, 'app/updateStudent.html', {'form': stu_fm})



#This function will DELETE the records
def delete_data(request, id):
    if request.method == 'POST':
        pi = StudentData.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
