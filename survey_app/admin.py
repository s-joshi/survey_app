from django.contrib import admin
from .models import (Survey, Organization, Employee,
                     QuestionLibrary, ChoiceAnswer,
                     SurveyEmployee, SurveyQuestion, SurveyResponse)
# Register your models here.

admin.site.register(Organization)
admin.site.register(Employee)
admin.site.register(QuestionLibrary)
admin.site.register(ChoiceAnswer)
admin.site.register(Survey)
admin.site.register(SurveyEmployee)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyResponse)
