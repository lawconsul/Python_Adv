from protocol import make_200
from decorators import logged, freeze

@freeze('Start : %(Start)s - End : %(End)s; Sleep: %(Sleep)s', time_sleep = 5)
@logged('request: %(request)s - response: %(result)s')
def echo_controller(request):
    return make_200(request, request.get('data'))
