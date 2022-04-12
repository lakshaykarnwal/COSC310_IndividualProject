import flickrapi
import urllib.request

api_key = '636bd872cd404868531ed627c53f61f3'
api_secret = 'be7d5fa682f09280'

def searchFlickrImages(term, category='pets'):
    global api_key, api_secret
    urls = []
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    returnedImages = flickr.photos_search(text=term, tags=category, per_page=5, pages=1, extras='url_0', sort='interestingness-desc')

    photos = returnedImages.get('photos').get('photo')
    for photo in photos:
        farm = photo.get('farm')
        server = photo.get('server')
        id = photo.get('id')
        secret = photo.get('secret')
        url = 'http://farm' + f'{farm}' + '.static.flickr.com/' + server + '/' + id + '_' + secret + '_m.jpg'
        urls.append(url)
        #print(type(farm))
    
    return(urls)

def url_to_jpg(i, url, file_path, saved_name):
    filename = 'image-{}{}.jpg'.format(saved_name,i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))
    return None

urls_cute = searchFlickrImages('cute')
file_path = 'images/cute_pets/'
saved_name = 'cutePet'
counter = 0

for url in urls_cute:
    url_to_jpg(counter, url, file_path, saved_name)
    print("saved")
    counter = counter + 1

print("completed")