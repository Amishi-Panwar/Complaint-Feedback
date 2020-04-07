from rest_framework import serializers
from .models import *

class AcademicCourseComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= AcademicCourseComplaint
        fields =['id','year', 'course_code','description','status']
class AcademicFacultyComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= AcademicFacultyComplaint
        fields =['id', 'faculty_name','description','status' ]
class AcademicTimetableComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= AcademicTimetableComplaint
        fields =['id', 'year','description','status' ]

class InfrastructureLabComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= InfrastructureLabComplaint
        fields =['lab_no', 'sys_no','description','status' ]

class InfrastructureLabComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= InfrastructureLabComplaint
        fields =['lab_no', 'sys_no','description','status' ]

class InfrastructureProjectorComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= InfrastructureProjectorComplaint
        fields =['room_no','description','status' ]

class InfrastructureFurnitureComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= InfrastructureFurnitureComplaint
        fields =['building_name','room_no','description','status' ]

class InfrastructureElectricityComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= InfrastructureElectricityComplaint
        fields =['building_name','room_no','description','status' ]

class SanitationComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= SanitationComplaint
        fields =['building_name','location','description','status' ]

class MiscellaneousComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= MiscellaneousComplaint
        fields =['description','status' ]

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model= Feedback
        fields =['feedback','feedback_Description','status' ]
