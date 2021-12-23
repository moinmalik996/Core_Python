from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'innerapp/home.html')


def show_data(request, stu_id):
    # print(stu_id)
    if stu_id == 1:
        student = {'stu_id':stu_id, 'name':'Moin'}
    if stu_id == 2:
        student = {'stu_id':stu_id, 'name':'Hamza'}
    if stu_id == 3:
        student = {'stu_id':stu_id, 'name':'Junaid'}

    return render(request, 'innerapp/show.html', student)