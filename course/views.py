from django.shortcuts import render

from course.models import Course

# Create your views here.




def Home(request):
    n = [i for i in range(16)]
    context = {'products' :n }
    # return render(request,"course/explore.html",context)
    return render(request,"components/cart1.html",context)


def course_detail(request,slug):
    course = Course.objects.get(name_slug=slug)
    return render(request,"course/product_detail.html",context ={'course':course})