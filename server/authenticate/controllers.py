from protocol import make_200


def authenticate_controller(request):
    return make_200(request, request.get('data'))
    return make_402(request, request.get('data'))
    return make_409(request, request.get('data'))
