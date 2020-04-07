from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^complaint/AcademicCourseComplaint/$', views.AcademicCourseComplaintView.as_view(),name='AcademicCourseComplaint'),
    url(r'^complaint/AcademicFacultyComplaint/$', views.AcademicFacultyComplaintView.as_view()),
    url(r'^complaint/AcademicTimetableComplaint/$', views.AcademicTimetableComplaintView.as_view()),
    url(r'^complaint/InfrastructureLabComplaint/$', views.InfrastructureLabComplaintView.as_view()),
    url(r'^complaint/InfrastructureProjectorComplaint/$', views.InfrastructureProjectorComplaintView.as_view()),
    url(r'^complaint/InfrastructureFurnitureComplaint/$', views.InfrastructureFurnitureComplaintView.as_view()),
    url(r'^complaint/InfrastructureElectricityComplaint/$', views.InfrastructureElectricityComplaintView.as_view()),
    url(r'^complaint/SanitationComplaint/$', views.SanitationComplaintView.as_view()),
    url(r'^complaint/MiscellaneousComplaint/$', views.MiscellaneousComplaintView.as_view()),
    url(r'^Feedback/$', views.FeedbackView.as_view()),
   ]