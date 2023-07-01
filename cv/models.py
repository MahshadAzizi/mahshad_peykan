import uuid
from django.db import models
from django.conf import settings


SKILL_LEVEL = [
    ('basic', 'basic'),
    ('intermediate', 'intermediate'),
    ('expert', 'expert'),
]

LANG_LEVEL = [
    ('native', 'native'),
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('C1', 'C1'),
    ('C2', 'C2'),
]


def certificate_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/certificate/<user>/<title>/<filename>
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'certificate/{0}/{1}/{2}'.format(instance.user.username, instance.title, filename)


class CV(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='cv_user',
                             on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='skill_user',
                             on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=12,
                             choices=SKILL_LEVEL,
                             default='basic')
    cv = models.ForeignKey(CV,
                           related_name='skill_cv',
                           on_delete=models.DO_NOTHING,
                           null=True,
                           blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='education_user',
                             on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=81)
    start_date = models.DateField(null=True,
                                  blank=True)
    end_date = models.DateField(null=True,
                                blank=True)
    cv = models.ForeignKey(CV,
                           related_name='education_cv',
                           on_delete=models.DO_NOTHING,
                           null=True,
                           blank=True)

    def __str__(self):
        return self.title


class JobExperience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='job_experience_user',
                             on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(null=True,
                                   blank=True)
    start_date = models.DateField(null=True,
                                  blank=True)
    end_date = models.DateField(null=True,
                                blank=True)
    cv = models.ForeignKey(CV,
                           related_name='job_experience_cv',
                           on_delete=models.DO_NOTHING,
                           null=True,
                           blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='certificate_user',
                             on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    certified_body = models.CharField(max_length=100)
    brief = models.TextField(null=True,
                             blank=True)
    duration = models.CharField(max_length=20,
                                null=True,
                                blank=True)
    file = models.FileField(upload_to=certificate_directory_path,
                            null=True,
                            blank=True)
    cv = models.ForeignKey(CV,
                           related_name='certificate_cv',
                           on_delete=models.DO_NOTHING,
                           null=True,
                           blank=True)

    def __str__(self):
        return self.title


class Language(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='language_user',
                             on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=6,
                             choices=LANG_LEVEL,
                             default='A1')
    cv = models.ForeignKey(CV,
                           related_name='language_cv',
                           on_delete=models.DO_NOTHING,
                           null=True,
                           blank=True)

    def __str__(self):
        return self.title
