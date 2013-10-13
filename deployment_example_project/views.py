import logging

from django.shortcuts import render_to_response
from django.template import RequestContext

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

def home(request):

    """
    Say hello!

    :param request:
    :return response:
    """
    return render_to_response('hello_world.html',
                              context_instance=RequestContext(request))
