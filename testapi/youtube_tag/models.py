from django.db import models
from django.db.models import signals

import requests
from .tasks import check_new_video


# def update_url(tag_id):
#     tag = Tags.objects.filter(id=tag_id).first()
#     url = f'https://www.googleapis.com/youtube/v3/' \
#         f'search?part=snippet&maxResults=1&q={tag.tag}&order=date&' \
#         f'key=AIzaSyBc1HUbXtsV3UMjNd9zNYJjVCPSzxL4aJ0'
#     headers = {'content-type': 'application/json'}
#     r = requests.get(url, headers=headers)
#     response = r.json()
#     if response.get('items', None):
#         video_id = response['items'][0]['id']['videoId']
#         video_url = f'https://www.youtube.com/watch?v={video_id}'
#         if tag.url != video_url:
#             tag.url = video_url
#             tag.save()


def new_video(sender, instance, signal, *args, **kwargs):
    check_new_video.delay(instance.id)


class User(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30)
    token = models.UUIDField()


class Tags(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=128)
    url = models.URLField(null=True, blank=True)


signals.post_save.connect(new_video, sender=Tags)
