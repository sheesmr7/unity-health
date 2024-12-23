from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'index.html')

def doctors(request):
    return render(request,'doctors.html') 

def contacts(request):
    return render(request,'contact.html')

def blogs(request):
    return render(request,'blog.html')

def blog_details(request):
    return render(request,'blog-details.html')

def about_us(request):
    return render(request,'about.html')

def registers(request):
    return render(request,'registration.html')


