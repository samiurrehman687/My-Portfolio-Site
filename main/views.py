import logging
import random
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from main import models as m1
from main import form as f1

logger = logging.getLogger('app')


# Home View
class home(ListView):
    model = m1.ProjectModel
    template_name = 'main/home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        try:
            qs = list(super().get_queryset())
            random.shuffle(qs)
            logger.info("Home page projects loaded successfully")
            return qs[:3]
        except Exception as e:
            logger.error("Error loading home projects", exc_info=True)
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Getting home heading form database 
        try:
            heading_obj = m1.SiteDataMOdel.objects.get(name='home_heading_skill')
            context['home_heading'] = heading_obj.text
        except Exception:
            logger.warning("Home heading not found, using default")
            context['home_heading'] = 'Backend Developer'

        # Getting home skill form database 
        try:
            home_para = m1.SiteDataMOdel.objects.get(name='home_skill_detail')
            context['home_short_skill'] = home_para.text
        except Exception:
            logger.warning("Home skill detail not found, using default")
            context['home_short_skill'] = 'Not defined'

        # Getting home_pic form database 
        try:
            home_pic_obj = m1.SiteDataMOdel.objects.get(name='home_pic')
            context['home_picture'] = home_pic_obj.pictures.url
        except Exception:
            logger.warning("Home picture not found, using default")
            context['home_picture'] = '/static/main/images/home_pic.png'
        
        # Getting home resume form database 
        try:
            resume_obj = m1.SiteDataMOdel.objects.get(name='resume')
            context['resume'] = resume_obj.resume
        except Exception:
            logger.warning(" Home Resume not found")
            context['resume'] = '#'

        return context


# Project View
class PorjectView(ListView):
    model = m1.ProjectModel
    template_name = 'main/project.html'
    context_object_name = 'projects'

    def get_queryset(self):
        try:
            return super().get_queryset()
        except Exception:
            logger.error("Error loading project list", exc_info=True)
            return []


# About View
class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Getting aobut profile form database 
        try:
            my_pic_obj = m1.SiteDataMOdel.objects.get(name='profile_pic')
            context['about_pic'] = my_pic_obj.pictures
        except m1.SiteDataMOdel.DoesNotExist:
            logger.warning("Profile picture not found")
            context['about_pic'] = '/static/main/images/my_pic.jpg'
        # Site Text about me
        try:
            about_obj = m1.SiteDataMOdel.objects.get(name='about_me')
            context['about'] = about_obj.text
        except m1.SiteDataMOdel.DoesNotExist:
            logger.warning("About text not found")
            context['about'] = (
                'I am a passionate Backend Developer specializing in Python and Django.'
            )
        # Projects getting
        try:
            context['projects'] = m1.ProjectModel.objects.all()
        except Exception:
            logger.error("Error loading about projects", exc_info=True)
            context['projects'] = []
        # Education Data getting form database
        try:
            context['educations'] = m1.EducationModel.objects.exclude(degree_name='experience')
        except Exception:
            logger.error("Error loading education data", exc_info=True)
            context['educations'] = []
        # getting expereince data form database.....
        try:
            experience_obj = m1.EducationModel.objects.get(degree_name='experence')
            context['my_experience'] = experience_obj.experience
        except m1.EducationModel.DoesNotExist:
            logger.warning("Experience record not found")
            context['my_experience'] = 'Not Found'
        
        # Getting languages Data from database
        try:
            language_obj = m1.LanguagesModel.objects.all()
            context['languages'] = language_obj
        except m1.LanguagesModel.DoesNotExist:
            logger.warning('Language Record not found')
            context['languages'] = 'Record Not Found'
        return context


# Contact View
class ContactView(FormView):
    template_name = 'main/contact.html'
    form_class = f1.ContactForm
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Getting Email form database
        try:
            email_obj = m1.SiteDataMOdel.objects.get(name='email')
            context["my_email"] = email_obj.email
        except m1.SiteDataMOdel.DoesNotExist:
            logger.warning("Contact email not found, using default")
            context['my_email'] = 'sami@example.com'
        # Getting contact number 
        try:
            contact_whatsapp_obj = m1.SiteDataMOdel.objects.get(name='contact_number')
            context['Contact'] = contact_whatsapp_obj.contact_no
        except m1.SiteDataMOdel.DoesNotExist:
            logger.warning("Contact WhatsApp not found, using default")
            context['Contact'] = '03001234567'
        return context
    # checking form vaildality
    def form_valid(self, form):
        try:
            form.save()
            logger.info("New contact form submitted successfully")
            messages.success(self.request, 'Your Message Send Successfully!')
        except Exception:
            logger.error("Error saving contact form", exc_info=True)
            messages.error(self.request, 'Something went wrong.')
        return super().form_valid(form)
    

