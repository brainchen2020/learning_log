from django.shortcuts import render
from .models import Video
from pytube import request
from . import date_clock
from datetime import datetime , timedelta

# Create your views here.
def parse_link(url):
    req = request.get(url)
    content = [x for x in req.split('\n') if 'pl-video-title-link' in x]
    link_list = [x.split('href="', 1)[1].split('&', 1)[0] for x in content]
    return link_list
def video(request):
    videos_id = []
    url = "https://www.youtube.com/playlist?list=PLA5501E1A2A1D7CBF"
    link_list = parse_link(url)

    for video_id in link_list:
        video_id = video_id.split('v=')[1]
        print("video_id; ", str(video_id))
        videos_id.append(video_id)
    youtube_url = "https://www.youtube.com/embed/"
    date_index = date_clock.DateClocker("2018-04-17", "2018-05-17", fmt="%Y-%m-%d",index=16)
    index_daily = date_index[str(datetime.today().strftime("%Y-%m-%d"))]
    video = Video.objects.all()
    video.url = youtube_url + str(videos_id[int(index_daily)])
    return render(request, "movies/video.html", { 'video': video } )