from pytube import YouTube
from pytube import Playlist


def download_video(url, destination_folder, filename):
    yt = YouTube(url)
    mp4_files = yt.streams.filter(file_extension="mp4")
    mp4_files = mp4_files.get_by_resolution('720p')
    mp4_files.download(destination_folder, filename)


def download_playlist(url, destination_folder):
    playlist = Playlist(url)
    videos = [
        {'url': f'https://www.youtube.com/watch?v={video.video_id}', 'title': video.title}
        for video in playlist.videos
    ]
    videos = videos[::-1]
    for index, video in enumerate(videos):
        download_video(
            url=video['url'],
            destination_folder=destination_folder,
            filename=f'{index + 1} - {video["title"]}.mp4'
        )
