import requests

session = requests.Session()


def get_images(url: str):
    if not url.startswith('https://'):
        url = f'https://{url}'

    if '?__a=1' in url:
        request = session.get(url)
    else:
        request = session.get(f'{url}?__a=1')

    response = request.json()

    username = response.get('graphql').get('shortcode_media').get('owner').get('username')

    try:
        images_url = response.get('graphql').get('shortcode_media').get('edge_sidecar_to_children').get('edges')
        for item in images_url:
            post_id = item.get('node').get('id')
            is_video = item.get('node').get('is_video')
            if not is_video:
                media_url = item.get('node').get('video_url')
                media = requests.get(media_url).content
                file_name = f'{username}_{post_id}.jpg'
            else:
                media_url = item.get('node').get('display_url')
                media = requests.get(media_url).content
                file_name = f'{username}_{post_id}.mp4'

            path_location = f'media/{file_name}'
            open(path_location, 'wb').write(media)

            return True

    except AttributeError:
        post_id = response.get('graphql').get('shortcode_media').get('id')
        is_video = response.get('graphql').get('shortcode_media').get('is_video')

        if not is_video:
            image_url = response.get('graphql').get('shortcode_media').get('display_url')
            media = requests.get(image_url).content
            file_name = f'{username}_{post_id}.jpg'
        else:
            image_url = response.get('graphql').get('shortcode_media').get('video_url')
            media = requests.get(image_url).content
            file_name = f'{username}_{post_id}.mp4'

        path_location = f'media/{file_name}'
        open(path_location, 'wb').write(media)

        return True
