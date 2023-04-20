



from course.models import Course


def get_course_details(request):
    c = Course.objects.all()
    context = {'courses':c}
    
    return context