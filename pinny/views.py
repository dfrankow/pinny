from django.http import HttpResponse
from pinny.get_pin_from_search import get_first_pin_from_search_result
import logging

def slack(request, query=None):
    if not query:
        if request.method == 'GET':
            query = request.GET.get('text', '')
        elif request.method == 'POST':
            # Maybe it's in the POST as 'text', like from Slack
            # https://api.slack.com/slash-commands
            query = request.POST.get('text', '')

    logging.info("query %s" % query)
    print "query '%s'" % query
    pin, img_src = get_first_pin_from_search_result(query)
    return HttpResponse("%s\n%s" % (pin, img_src))
