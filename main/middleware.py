import logging
from django.shortcuts import render
from django.conf import settings
from main.models import underconstruction

# Separate logger for maintenance middleware
logger = logging.getLogger('maintenance')


class UnderConstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        try:
            logger.info(f"Maintenance check started | Path: {request.path}")

            # Staff user bypass
            if getattr(request.user, 'is_staff', False):
                logger.info("Staff user bypassed maintenance mode")
                return self.get_response(request)

            # Get maintenance key safely
            uc_key = getattr(settings, 'UNDER_MAINTENANCE_KEY', None)

            #  URL key bypass
            if uc_key and request.GET.get('u') == uc_key:
                request.session['Bypass_maintenance'] = True
                request.session.set_expiry(0)
                logger.info("Maintenance bypass activated via key")

            #  Session bypass
            if request.session.get('Bypass_maintenance', False):
                logger.info("Maintenance bypass active from session")
                return self.get_response(request)

            #  Check maintenance status from DB
            uc = underconstruction.objects.first()

            if uc and uc.is_under_const:
                logger.warning("Site is under maintenance — showing maintenance page")
                return render(
                    request,
                    'main/underconstruction.html',
                    {'uc1': uc.uc_note}
                )

            # Normal flow
            return self.get_response(request)

        except Exception as e:
            logger.error(
                f"Maintenance Middleware Error: {str(e)}",
                exc_info=True
            )
            return self.get_response(request)