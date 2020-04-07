from django.db import models

# Create your models here.

class AcademicCourseComplaint(models.Model):
    # id= models.IntegerField(primary_key=True) 
    year= models.CharField(max_length=4) 
    # enrolno = models.CharField(max_length=15)
    course_code= models.CharField(max_length=7) 
    description = models.TextField()
    status = models.TextField(default='Registered')
    
    def _str_(self):
      return self.id
      
class AcademicFacultyComplaint(models.Model):
    faculty_name= models.CharField(max_length=50) 
    description = models.TextField()
    status = models.TextField(default='Registered')

    def _str_(self):
      return self.id
class AcademicTimetableComplaint(models.Model):
    year= models.CharField(max_length=5) 
    description = models.TextField()
    status = models.TextField(default='Registered')

    def _str_(self):
      return self.id

class InfrastructureLabComplaint(models.Model):
    lab_no= models.CharField(max_length=10) 
    sys_no= models.CharField(max_length=3) 
    description = models.TextField()
    status = models.TextField(default='Registered')

class InfrastructureProjectorComplaint(models.Model):
    room_no= models.CharField(max_length=10) 
    description = models.TextField()
    status = models.TextField(default='Registered')

class InfrastructureFurnitureComplaint(models.Model):

    building_name= models.CharField(max_length=3) 
    room_no= models.CharField(max_length=3) 
    description = models.TextField()
    status = models.TextField(default='Registered')

class InfrastructureElectricityComplaint(models.Model):

    building_name= models.CharField(max_length=3) 
    room_no= models.CharField(max_length=3) 
    description = models.TextField()
    status = models.TextField(default='Registered')

class SanitationComplaint(models.Model):

    building_name= models.CharField(max_length=3) 
    location= models.CharField(max_length=15) 
    description = models.TextField()
    status = models.TextField(default='Registered')

class MiscellaneousComplaint(models.Model):

    description = models.TextField()
    status = models.TextField(default='Registered')

class Feedback(models.Model):

    feedback = models.CharField(max_length=15)
    feedback_Description = models.TextField()
    status = models.TextField(default='Registered')
    