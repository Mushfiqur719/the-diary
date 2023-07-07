from django.db import models

# Create your models here.

from django.db import models

class Case(models.Model):
    CASE_TYPES = (
        ('Option 1', 'Option 1'),
        ('Option 2', 'Option 2'),
        ('Option 3', 'Option 3'),
        ('Option 4', 'Option 4'),
        ('Option 5', 'Option 5'),
    )

    COURTS = (
        ('Court 1', 'Court 1'),
        ('Court 2', 'Court 2'),
        ('Court 3', 'Court 3'),
        ('Court 4', 'Court 4'),
        ('Court 5', 'Court 5'),
    )

    case_type = models.CharField(max_length=50, choices=CASE_TYPES)
    court = models.CharField(max_length=50, choices=COURTS)
    date = models.DateField()
    first_party = models.TextField()
    appointed_by = models.TextField()
    law_and_section = models.TextField()
    case_no = models.PositiveIntegerField()
    police_station = models.CharField(max_length=50)
    fixed_for = models.TextField()
    second_party = models.TextField()
    mobile_no = models.CharField(max_length=15)
    comments = models.TextField()

    def __str__(self):
        return f"Case {self.case_no}"
