from django.urls import include, path

from .views import classroom, students_en, teachers

urlpatterns = [
    path('', classroom.home, name='home_en'),
    path('about_en/', classroom.AboutView.as_view(), name='about_en'),
    # path('quizzes/', classroom.QuizListView.as_view(), name='quiz_list'),

    path('students_en/', include(([        
        path('', students_en.StudentList.as_view(), name='student_list_en'),
        path('<int:student>/', students_en.StudentDetail.as_view(), name='student_detail_en'),
        path('interests/', students_en.StudentInterestsView.as_view(), name='student_interests_en'),
        path('taken/', students_en.TakenQuizListView.as_view(), name='taken_quiz_list_en'),
        path('quiz/', students_en.QuizListView.as_view(), name='quiz_list_en'),
        path('quiz/<int:pk>/', students_en.take_quiz, name='take_quiz_en'),        
        path('quiz/<int:pk>/studentresults/', students_en.QuizResultsView.as_view(), name='student_quiz_results_en'),
    ], 'classroom'), namespace='students_en')),
    path('teachers_en/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/preview/', teachers.QuestionPreviewView.as_view(), name='question_preview'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='teachers')),
]
