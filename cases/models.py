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

class Client(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    chamber_file_number = models.PositiveIntegerField(blank=True, null=True)
    Representativ = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    additional_mobile = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    short_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Client: {self.name}"

class Case(models.Model):
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
