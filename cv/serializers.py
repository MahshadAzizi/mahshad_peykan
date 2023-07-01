from rest_framework import serializers
from cv.models import *
from user.models import Profile
from user.serializers import UserSerializer


class AddSkillSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=Profile.objects.all())
    cv = serializers.PrimaryKeyRelatedField(queryset=CV.objects.all(), many=False, read_only=False,
                                            allow_empty=True, allow_null=True, required=False)

    class Meta:
        model = Skill
        fields = ['id', 'user', 'title', 'level', 'cv']


class AddEducationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=Profile.objects.all())
    cv = serializers.PrimaryKeyRelatedField(queryset=CV.objects.all(), many=False, read_only=False,
                                            allow_empty=True, allow_null=True, required=False)

    class Meta:
        model = Education
        fields = ['id', 'user', 'title', 'university', 'start_date', 'end_date', 'cv']


class AddJobExperienceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=Profile.objects.all())
    cv = serializers.PrimaryKeyRelatedField(queryset=CV.objects.all(), many=False, read_only=False,
                                            allow_empty=True, allow_null=True, required=False)

    class Meta:
        model = JobExperience
        fields = ['id', 'user', 'title', 'company', 'start_date', 'end_date', 'description', 'cv']


class AddCertificateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=Profile.objects.all())
    cv = serializers.PrimaryKeyRelatedField(queryset=CV.objects.all(), many=False, read_only=False,
                                            allow_empty=True, allow_null=True, required=False)

    class Meta:
        model = Certificate
        fields = ['id', 'user', 'title', 'certified_body', 'duration', 'file', 'brief', 'cv']


class AddLanguageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=Profile.objects.all())
    cv = serializers.PrimaryKeyRelatedField(queryset=CV.objects.all(), many=False, read_only=False,
                                            allow_empty=True, allow_null=True, required=False)

    class Meta:
        model = Language
        fields = ['id', 'user', 'title', 'level', 'cv']


class AddCVSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=Profile.objects.all())

    class Meta:
        model = CV
        fields = ['id', 'user', 'title']


class CVSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = CV
        fields = ['id', 'user', 'title']


class SkillListSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Skill
        fields = ['id', 'user', 'title', 'level']


class JobExperienceListSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = JobExperience
        fields = ['id', 'user', 'title', 'company', 'start_date', 'end_date', 'description']


class CertificateListSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Certificate
        fields = ['id', 'user', 'title', 'certified_body', 'duration', 'file', 'brief']


class EducationListSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Education
        fields = ['id', 'user', 'title', 'university', 'start_date', 'end_date']


class LanguageListSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Language
        fields = ['id', 'user', 'title', 'level']


class CVListSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    certificate_cv = CertificateListSerializer(many=True)
    skill_cv = SkillListSerializer(many=True)
    education_cv = EducationListSerializer(many=True)
    job_experience_cv = JobExperienceListSerializer(many=True)
    language_cv = LanguageListSerializer(many=True)

    class Meta:
        model = CV
        fields = ['id', 'user', 'title', 'certificate_cv', 'skill_cv', 'education_cv', 'job_experience_cv',
                  'language_cv']
