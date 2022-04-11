import flickrapi

api_key = '636bd872cd404868531ed627c53f61f3'
api_secret = 'be7d5fa682f09280'

def searchFlickrImages(term, category='architecture'):
    global api_key, api_secret
    urls = []
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    returnedImages = flickr.photos_search(text=term, tags=category, per_page=5, pages=1, extras='url_0', sort='interestingness-desc')

    photos = returnedImages.get('photos').get('photo')
    for photo in photos:
        farm = type(photo.get('farm'))
        server = type(photo.get('server'))
        id = type(photo.get('id'))
        secret = type(photo.get('secret'))
        url = 'http://farm' + f'{farm}' + '.static.flickr.com/' + server + '/' + id + '_' + secret + '_m.jpg'
        print(url)
    
    return(returnedImages.get('photos').get('photo')[0].get('id'))

output = searchFlickrImages('Tree')
print(output)