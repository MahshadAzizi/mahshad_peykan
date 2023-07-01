from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from cv.serializers import *


class AddSkill(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddSkillSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddEducation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddEducationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddJonExperience(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddJobExperienceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddCertificate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddCertificateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddLanguage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddLanguageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddCV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddCVSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CVList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cvs = CV.objects.filter(user=user)
        serializer = CVSerializer(cvs, many=True)
        return Response(serializer.data)


class CVDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        cv = CV.objects.get(pk=pk)
        serializer = CVListSerializer(cv, many=False)
        return Response(serializer.data)


class SkillList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        cv = CV.objects.get(pk=pk)
        skills = Skill.objects.filter(cv=cv)
        serializer = SkillListSerializer(skills, many=True)
        return Response(serializer.data)


class JobExperienceList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        cv = CV.objects.get(pk=pk)
        job_experiences = JobExperience.objects.filter(cv=cv)
        serializer = JobExperienceListSerializer(job_experiences, many=True)
        return Response(serializer.data)


class EducationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        cv = CV.objects.get(pk=pk)
        educations = Education.objects.filter(cv=cv)
        serializer = EducationListSerializer(educations, many=True)
        return Response(serializer.data)


class CertificateList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        cv = CV.objects.get(pk=pk)
        certificates = Certificate.objects.filter(cv=cv)
        serializer = CertificateListSerializer(certificates, many=True)
        return Response(serializer.data)


class LanguageList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        cv = CV.objects.get(pk=pk)
        languages = Language.objects.filter(cv=cv)
        serializer = LanguageListSerializer(languages, many=True)
        return Response(serializer.data)
