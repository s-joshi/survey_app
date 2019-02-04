from django.db import models

# Create your models here.


class Organization(models.Model):
    """
    Model to store the organization information
    """
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Employee model
    """
    name = models.CharField(max_length=30)
    emp_id = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.emp_id)+"---"+str(self.name)

    class Meta:
        verbose_name_plural = 'Employees'


class QuestionLibrary(models.Model):
    """
    Models to store the questions of surveys.
    """
    question_text = models.TextField()

    CHOICES = (('comment_box', 'comment_box'),
               ('single_row_text', 'single_row_text'),
               ('Numeric_input', 'Numeric_input'), ('email_qns', 'email_qns'))

    question_type = models.CharField(max_length=50, choices=CHOICES, default=1)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name_plural = 'Question Library'


class ChoiceAnswer(models.Model):
    """
    Contains choice answers for questions.
    """
    choice_answers_text = models.CharField(max_length=50)
    question = models.ForeignKey(QuestionLibrary, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_answers_text


class Survey(models.Model):
    """
    Survey for a particular organization
    """
    name = models.CharField(max_length=256)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class SurveyQuestion(models.Model):
    """
    mapping of survey and questions.
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionLibrary, on_delete=models.CASCADE)


class SurveyEmployee(models.Model):
    """
    mapping of Employee and survey.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class SurveyResponse(models.Model):
    """
    Model to keep track of ans given by users.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_id = models.ForeignKey(QuestionLibrary, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)

    class Meta:
        unique_together = (('survey', 'question_id'),)
