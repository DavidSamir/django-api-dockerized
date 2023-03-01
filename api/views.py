from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def scrappRes(request):
    res = {
        'message': "user has been saved!",
        "data": "theRes"
    }

    return Response(res, status=200)

