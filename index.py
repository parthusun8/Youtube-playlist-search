import googleapiclient.discovery


def list(playlist_id, search_term):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="API_KEY_HERE")

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=1200
    )
    response = request.execute()

    playlist_items = []

    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    videoId = []

    for i in range(0, len(playlist_items)):
        title = playlist_items[i]['snippet']['title']

        if search_term.lower() in title.lower():
            videoId.append(title)

    return videoId


def main():
    play = str(input("Enter Link -> "))
    a = play.find('=') + 1
    playListId = play[a:]

    search_term = str(input("Enter term you want to search : "))
    playlistItems = list(playListId, search_term)

    print(f"total: {len(playlistItems)}")
    for i in range(0, len(playlistItems)):
        print(playlistItems[i], '\n')


if __name__ == '__main__':
    main()
