from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def courses(request):
    return render(request, 'courses.html')

def course_detail(request,data):
    return render(request, 'course_detail.html',{'data':data})
