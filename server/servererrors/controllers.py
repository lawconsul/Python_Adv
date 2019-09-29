from decorators import logged, freeze

@freeze('Start : %(Start)s - End : %(End)s; Sleep: %(Sleep)s', time_sleep = 5)
@logged('request: %(request)s - response: %(result)s')
def errors_controller(request):
    raise Exception('Server error')
