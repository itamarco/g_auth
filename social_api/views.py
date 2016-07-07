from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from social_api import user_manager, oauth_client



@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def auth(request):

    try:
        access_token = request.data['access_token']
        backend = request.data['backend']
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if not access_token or not backend:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if backend != 'google':
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    google_user_info = oauth_client.google_auth(access_token)
    if "error" in google_user_info:
        return JsonResponse(google_user_info, status=status.HTTP_400_BAD_REQUEST)

    user, created = user_manager.get_or_create(google_user_info)

    response = {}
    response['token'] = user.token
    response['user_id'] = user.id
    response['is_new'] = created

    return JsonResponse(response, status=status.HTTP_200_OK)

