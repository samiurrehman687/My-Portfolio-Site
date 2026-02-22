from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

#.......................................
#       Project Model
#.......................................
class ProjectModel(models.Model):
    ProName = models.CharField(max_length=255, blank=False)
    Picture = models.ImageField(upload_to='projects/', blank=False)
    Description = CKEditor5Field('text', config_name='extends')
    Github_link = models.URLField(blank=True, null=True)
    Live_site_link = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.ProName


#.......................................
#       Contact Model
#.......................................
class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


#.......................................
#       Site Data Model
#.......................................
class SiteDataModel(models.Model):
    Name_Choices = [
        ('logo', 'Site Logo'),
        ('home_heading_skill', 'Home Heading Skill'),
        ('home_skill_detail', 'Home Short Skill Define'),
        ('home_pic', 'Home Picture'),
        ('footer_skill_short', 'Footer Skill'),
        ('linkedIn_link', 'LinkedIn Link'),
        ('github_link', 'Github Link main'),
        ('profile_pic', 'Profile Picture'),
        ('about_me', 'About Me'),
        ('email', 'Email'),
        ('contact_number', 'Contact Number'),
        ('resume', 'Resume')
    ]
    name = models.CharField(max_length=100, choices=Name_Choices, unique=True)
    pictures = models.ImageField(upload_to='site_pics/', null=True, blank=True)
    text = CKEditor5Field('text', config_name='extends', default='not define')
    email = models.EmailField(max_length=255, null=True, blank=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    links = models.URLField(max_length=200, blank=True, null=True)
    resume = models.FileField(upload_to='projects/files/', blank=True, null=True)

    def __str__(self):
        return self.name


#.......................................
#       Education Model
#.......................................
class EducationModel(models.Model):
    DEGREE_CHOICES = [
        ('BSc', "Bachelor of Science"),
        ('BSSE', "BS Software Engineering"),
        ('Intermediate', 'Intermediate'),
        ('BA', "Bachelor of Arts"),
        ('BCom', "Bachelor of Commerce"),
        ('BBA', "Bachelor of Business Administration"),
        ('MSc', "Master of Science"),
        ('MSSE', "MS Software Engineering"),
        ('MA', "Master of Arts"),
        ('MCom', "Master of Commerce"),
        ('MBA', "Master of Business Administration"),
        ('PhD', "Doctor of Philosophy"),
    ]
    degree_name = models.CharField(max_length=255, choices=DEGREE_CHOICES)
    institute = models.CharField(max_length=255, blank=True)
    program = models.CharField(max_length=255, blank=True)
    percentage = models.FloatField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    resume = models.FileField(upload_to='projects/files/', null=True, blank=True)
    experience = CKEditor5Field('text', config_name='extends', null=True, blank=True)

    def __str__(self):
        return self.degree_name


#.......................................
#       Languages Model
#.......................................
class LanguagesModel(models.Model):
    l_name = models.CharField(max_length=255, unique=True)
    note = models.TextField(max_length=500)

    def __str__(self):
        return self.l_name


#.......................................
#       Under Construction Model
#.......................................
class UnderConstruction(models.Model):
    is_under_const = models.BooleanField(default=False)
    uc_note = models.TextField(blank=True, null=True, help_text='Note for under construction..')
    uc_duration = models.DateTimeField(blank=True, null=True, help_text='End duration for under construction..')
    uc_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Under Construction : {self.is_under_const}'
