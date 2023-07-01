from cv.views import *
from django.urls import path

urlpatterns = [
    path('add_skill/', AddSkill.as_view(), name='add_skill'),
    path('add_education/', AddEducation.as_view(), name='add_education'),
    path('add_job_experience/', AddJonExperience.as_view(), name='add_job_experience'),
    path('add_certificate/', AddCertificate.as_view(), name='add_certificate'),
    path('add_language/', AddLanguage.as_view(), name='add_language'),
    path('add_cv/', AddCV.as_view(), name='add_cv'),

    path('cv_list/', CVList.as_view(), name='cv_list'),
    path('cv_detail/<int:pk>/', CVDetail.as_view(), name='cv_detail'),

    path('skill_list/<int:pk>/', SkillList.as_view(), name='skill_list'),
    path('education_list/<int:pk>/', EducationList.as_view(), name='education_list'),
    path('job_experience_list/<int:pk>/', JobExperienceList.as_view(), name='job_experience_list'),
    path('certificate_list/<int:pk>/', CertificateList.as_view(), name='certificate_list'),
    path('language_list/<int:pk>/', LanguageList.as_view(), name='language_list'),
]
