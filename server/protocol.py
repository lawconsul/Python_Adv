from datetime import datetime

max_len_action = 15
# max_len_code = 3
max_len_data = 500

codes = [100, 101, 200, 201, 202, 400, 401, 402, 403, 404, 409, 410, 500]


def validate_request(request):
    return 'action' in request and 'time' in request and request.get('action') and request.get('time')


def crop_len_code(code):
    if code not in codes:
        crop_code = 500
    return crop_code


def crop_len_action(action):
    crop_action = (action[:max_len_action-2] + '..') if len(action) > max_len_action else action
    return crop_action


def crop_len_data(data):
    crop_data = (data[:max_len_data-2] + '..') if len(data) > max_len_data else data
    return crop_data


def make_response(request, code, data=None, date=datetime.now()):
    return {
        'action': request.get('action'),
        'time': date.timestamp() if isinstance(date, datetime) else date,
        'code': code,
        'data': data
    }


def make_200(request, data=None, date=datetime.now()):
    return make_response(request, 200, data, date)


def make_400(request, data=None, date=datetime.now()):
    return make_response(request, 400, data, date)


def make_404(request, date=datetime.now()):
    return make_response(request, 404, f'Action "{request.get("action")}" not found', date)


def make_500(request, date=datetime.now()):
    return make_response(request, 500, 'Internal server error', date)
