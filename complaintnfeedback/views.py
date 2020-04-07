from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView  
from rest_framework import viewsets
from .serializers import *


# def hello(request):
#    return render(request, "complaintnfeedback/template/hello.html", {})  

class AcademicCourseComplaintView(ListCreateAPIView):       
    serializer_class = AcademicCourseComplaintSerializer       
    queryset = AcademicCourseComplaint.objects.all()  
    
class AcademicFacultyComplaintView(ListCreateAPIView):      
    serializer_class = AcademicFacultyComplaintSerializer        
    queryset = AcademicFacultyComplaint.objects.all()  

class AcademicTimetableComplaintView(ListCreateAPIView):       
    serializer_class = AcademicTimetableComplaintSerializer         
    queryset = AcademicTimetableComplaint.objects.all()         
    
class InfrastructureLabComplaintView(ListCreateAPIView):       
    serializer_class = InfrastructureLabComplaintSerializer        
    queryset = InfrastructureLabComplaint.objects.all()    

class InfrastructureProjectorComplaintView(ListCreateAPIView):       
    serializer_class = InfrastructureProjectorComplaintSerializer       
    queryset = InfrastructureProjectorComplaint.objects.all()  

class InfrastructureFurnitureComplaintView(ListCreateAPIView):      
    serializer_class = InfrastructureFurnitureComplaintSerializer        
    queryset = InfrastructureFurnitureComplaint.objects.all()  

class InfrastructureElectricityComplaintView(ListCreateAPIView):       
    serializer_class = InfrastructureElectricityComplaintSerializer         
    queryset = InfrastructureElectricityComplaint.objects.all()            

class SanitationComplaintView(ListCreateAPIView):      
    serializer_class = SanitationComplaintSerializer        
    queryset = SanitationComplaint.objects.all()  

class MiscellaneousComplaintView(ListCreateAPIView):       
    serializer_class = MiscellaneousComplaintSerializer         
    queryset = MiscellaneousComplaint.objects.all()     

class FeedbackView(ListCreateAPIView):       
    serializer_class = FeedbackSerializer         
    queryset = Feedback.objects.all()     
       
