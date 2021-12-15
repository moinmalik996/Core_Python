#   API_KEY  :   AIzaSyCCfrhSRSJkO5lTqKnuFKpuq-OBcQECK30

from googleapiclient.discovery import build
from datetime import timedelta
import re

API_KEY = "AIzaSyCCfrhSRSJkO5lTqKnuFKpuq-OBcQECK30"
nextPageToken = None
total_seconds = 0

hours_pattren   = re.compile(r'(\d+)H')
minutes_pattren = re.compile(r'(\d+)M')
seconds_pattren = re.compile(r'(\d+)S')

while True:
    youtube = build("youtube", "v3", developerKey=API_KEY)

    pl_request = youtube.playlistItems().list(
        part        ='contentDetails',
        playlistId  ='PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL',
        maxResults  = 50,
        pageToken   = nextPageToken
    )


    pl_response = pl_request.execute()
    # print(pl_response)

    Vid_Ids = []

    for item in pl_response['items']:
        Vid_Ids.append(item['contentDetails']['videoId'])
        
    vid_requests = youtube.videos().list(
        part='contentDetails',
        id=','.join(Vid_Ids)
        
    )

    vid_response = vid_requests.execute()

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']
        
        hours    = hours_pattren.search(duration)
        minutes  = minutes_pattren.search(duration)
        seconds  = seconds_pattren.search(duration)
        
        hours    = int(hours.group(1)) if hours else 0
        minutes  = int(minutes.group(1)) if minutes else 0
        seconds  = int(seconds.group(1)) if seconds else 0
        
        video_seconds = timedelta(
            hours= hours,
            minutes= minutes,
            seconds= seconds
        ).total_seconds()
        
        total_seconds += video_seconds
    
    nextPageToken = pl_response.get('nextPageToken')
    
    if not nextPageToken:
        break
    
total_seconds = int(total_seconds)

minutes, seconds = divmod(total_seconds, 60)
hours , minutes  = divmod(minutes, 60)
    

print(f'\nThe duration of this playlist is {hours}:{minutes}:{seconds}.')


