from django.db import models
from django.utils.formats import localize
from django.db import models

class QuizQuestion(models.Model):
    question_text = models.CharField("Вопрос", max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Вопрос квиза"
        verbose_name_plural = "Вопросы квиза"

    def __str__(self):
        return self.question_text


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name="answers", on_delete=models.CASCADE)
    icon = models.CharField("Иконка (emoji)", max_length=10)
    text = models.CharField("Ответ", max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Ответ квиза"
        verbose_name_plural = "Ответы квиза"

    def __str__(self):
        return self.text

class QuizResult(models.Model):
    answers = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)

class Applicant(models.Model):
    SCHOOL_CHOICES = [
        ("Школа Цифровых Технологий", "Школа Цифровых Технологий"),
        ("Школа Предпринимательства и инноваций", "Школа Предпринимательства и инноваций"),
        ("Школа Менеджмента", "Школа Менеджмента"),
        ("Школа Экономики и Финансов", "Школа Экономики и Финансов"),
        ("Школа Политики и Права", "Школа Политики и Права"),
        ("Школа Медиа и Кино", "Школа Медиа и Кино"),
    ]

    SOURCE_CHOICES = [
        ("Instagram", "Instagram"),
        ("Website", "Website"),
        ("Facebook", "Facebook"),
        ("Threads", "Threads"),
    ]

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, help_text="Пример: +77771234567")
    application_number = models.CharField(max_length=20, editable=False, unique=True)
    registration_date = models.DateField()
    registration_time = models.TimeField()
    school = models.CharField(max_length=150, choices=SCHOOL_CHOICES)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES)
    city = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.application_number:
            last_id = Applicant.objects.count() + 1
            self.application_number = f"{last_id:03}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"