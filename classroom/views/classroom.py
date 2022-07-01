from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.db.models import Count


from ..models import Student
from classroom.models import Quiz

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            return redirect('students:quiz_list')
    
    top_student = Student.objects.order_by('-score')

    return render(request,'classroom/quiz_list.html',{
        'quizzes':Quiz.objects.annotate(questions_count=Count('questions')) \
            .filter(questions_count__gt=0), 'top_student' : top_student })


def save_github_user(backend, user, response, *args, **kwargs):
    if backend.name == 'github':
        if not user.is_student:
            user.is_student = True
            user.save()
            student = Student.objects.create(user=user)


class AboutView(TemplateView):
    template_name = 'classroom/about.html'