from django.conf import settings as original_settings


def settings(request):
    return {'settings': original_settings.__dict__}


def ip_address(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

