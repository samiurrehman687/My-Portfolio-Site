from main.models import SiteDataMOdel
from django.templatetags.static import static
def Site_Data(request):
    # logo 
    try:
        logo = SiteDataMOdel.objects.get(name='logo')
        logo_url = logo.pictures.url
    except SiteDataMOdel.DoesNotExist:
        logo_url = static('main/images/site_logo.png')
    # Footer skills
    try:
        footer_skill = SiteDataMOdel.objects.get(name='footer_skill_short')
        footer_url = footer_skill.text
    except SiteDataMOdel.DoesNotExist:
        footer_url = 'Django and Fast Api Developer'
    # LinkedIn link
    try:
        linkedin_obj = SiteDataMOdel.objects.get(name='linkedIn_link')
        linkedin = linkedin_obj.links
    except  SiteDataMOdel.DoesNotExist:
        linkedin = '#'
    # Github Link
    try: 
        github_obj = SiteDataMOdel.objects.get(name='github_link')
        github = github_obj.links
    except SiteDataMOdel.DoesNotExist:
        github = '#'
    return {
        'logo_url':logo_url,
        'footer_url': footer_url,
        'linkedin':linkedin,
        'github' : github,
    }