import json

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View


from .models import Tags, User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class GetTags(APIView):

    def get(self, request, tag_id, **kwargs):
        token = request.headers.get('Authorization', None)
        user = User.objects.filter(token=token).first()
        if user:
            a = Tags.objects.filter(id=tag_id).first()
            if a:
                return Response({'title': a.tag, 'id': a.id, 'url': a.url})
            else:
                return Response('Tag dose not exist')

        else:
            return Response('Invalid Token\n')


class SetTags(APIView):
    """Class for log views."""

    def post(self, request, **kwargs) -> Response:
        token = request.headers.get('Authorization', None)
        body = json.loads(request.body)
        user = User.objects.filter(token=token).first()
        if user:
            if isinstance(body, dict):
                Tags.objects.create(tag=body.get('key_word', None),
                                    id=body.get('id', None), user=user)

            elif isinstance(body, list):
                for tag in body:
                    Tags.objects.create(tag=tag.get('key_word', None),
                                        id=tag.get('id', None), user=user)

            return Response(body)
        else:
            return Response('Invalid Token\n')

    def get(self, request, **kwargs) -> Response:
        token = request.headers.get('Authorization', None)
        user = User.objects.filter(token=token).first()
        if user:
            returnable = Tags.objects.filter(user__token=token)
            answ = [{'key_word': x.tag, 'id': x.id} for x in returnable]

            return Response(answ)
        else:
            return Response('Invalid Token\n')

    def delete(self, request, tag_id, **kwargs) -> Response:
        token = request.headers.get('Authorization', None)
        user = User.objects.filter(token=token).first()
        if user:
            Tags.objects.filter(id=tag_id).delete()

            return Response(f'\n')
        else:
            return Response('Invalid Token\n')
