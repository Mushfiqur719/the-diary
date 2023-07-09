from django.db import models

class CaseType(models.Model):
    case_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.case_type}"

class Court(models.Model):
    court = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.court}"

class PoliceStation(models.Model):
    station = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.station}"

class Case(models.Model):
    COURTS = (
        ('Court 1', 'Court 1'),
        ('Court 2', 'Court 2'),
        ('Court 3', 'Court 3'),
        ('Court 4', 'Court 4'),
        ('Court 5', 'Court 5'),
    )

    case_type = models.ForeignKey(CaseType, on_delete=models.SET_NULL, blank=True, null=True)
    court = models.ForeignKey(Court, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField()
    first_party = models.TextField()
    appointed_by = models.TextField()
    law_and_section = models.TextField()
    case_no = models.PositiveIntegerField()
    police_station = models.ForeignKey(PoliceStation, on_delete=models.SET_NULL, blank=True, null=True)
    fixed_for = models.TextField(blank=True, null=True)
    second_party = models.TextField(blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Case {self.case_no}"
