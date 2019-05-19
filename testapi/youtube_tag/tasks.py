import requests
#
from testapi.testapi import celery_app as app
from .models import Tags


def update_url(tag_id):
    tag = Tags.objects.filter(id=tag_id).first()
    url = f'https://www.googleapis.com/youtube/v3/' \
        f'search?part=snippet&maxResults=1&q={tag.tag}&order=date&' \
        f'key=AIzaSyBc1HUbXtsV3UMjNd9zNYJjVCPSzxL4aJ0'
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    response = r.json()
    if response.get('items', None):
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        if tag.url != video_url:
            tag.url = video_url
            tag.save()



@app.task
def check_new_video(tag_id):
    try:
        update_url(tag_id)
    except Exception as ex:
        print(ex)


@app.task
def update_urls():
    all_tags = [x.id for x in Tags.objets.all()]
    for tag_id in all_tags:
        try:
            update_url(tag_id)
        except Exception as ex:
            print(ex)
