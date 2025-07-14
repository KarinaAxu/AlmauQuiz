from django.contrib import admin
from django.urls import path
from alma_statistics.views import statistic_view, quiz_page, save_quiz_result, submit_form, save_full_data, QuizAPIView
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quiz_page, name='quiz_page'),  
    path('quiz/', quiz_page, name='quiz_page'),
    path('quiz/save-full/', save_full_data, name='save_full_data'),
    path('quiz/save/', save_quiz_result, name='quiz_save'),
    path('api/quiz/', QuizAPIView.as_view(), name='quiz_api'),
    path('submit-form/', submit_form, name='submit_form'),
    path('form/', lambda request: render(request, 'statistics/form.html'), name='form'),
    path('statistics/', statistic_view, name='statistic'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)