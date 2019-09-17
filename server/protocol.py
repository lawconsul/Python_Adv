from datetime import datetime


def validate_request(request):
    return 'action' in request and 'time' in request and request.get('action') and request.get('time')


def make_response(request, code, data=None, date=datetime.now()):
    return {
        'action': request.get('action'),
        'time': date.timestamp(),
        'code': code,
        'data': data
    }


def make_200(request, data=None, date=datetime.now()):
    return make_response(request, 200, data, date)

def make_400(request, data=None, date=datetime.now()):
    return make_response(request, 400, data, date)

def make_402(request, data=None, date=datetime.now()):
    return make_response(request, 402, 'This could be "​wrong password​" or "​no account ​with​ that name​"', date)

def make_409(request, data=None, date=datetime.now()):
    return make_response(request, 409, "Someone is already connected with the given user name", date)

def make_404(request, date=datetime.now()):
    return make_response(request, 404, f'Action "{request.get("action")}" not found', date)


def make_500(request, date=datetime.now()):
    return make_response(request, 500, 'Internal server error', date)