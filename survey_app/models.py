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
        return self.emp_id, "---", self.name


class QuestionLibrary(models.Model):
    """
    Models to store the questions of surveys.
    """
    question_text = models.TextField()

    CHOICES = ((1, 'comment_box'), (2, 'single_row_text'),
               (3, 'Numeric_input'), (4, 'email_qns'))

    question_type = models.CharField(max_length=50, choices=CHOICES, default=1)

    def __str__(self):
        return self.question_text


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
