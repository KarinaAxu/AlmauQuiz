
from django.contrib import admin
from .models import Applicant
from django.contrib import admin
from .models import QuizQuestion, QuizAnswer

class QuizAnswerInline(admin.TabularInline):
    model = QuizAnswer
    extra = 2

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'order']
    inlines = [QuizAnswerInline]


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number', 'school', 'source', 'registration_date', 'registration_time')
    list_filter = ('school', 'source', 'registration_date')
    search_fields = ('last_name', 'first_name', 'middle_name', 'phone_number')
