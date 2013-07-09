__author__ = 'harshit'
from django.conf import settings
from PIL import Image

def crop_image( kwargs):
    left = int(kwargs['x'])
    top = int(kwargs['y'])
    width = int(kwargs['w'])
    height = int(kwargs['h'])
    source = settings.MEDIA_ROOT +'/' + kwargs['image_name']#todo  change it
    name = kwargs['image_name'].split('/')[-1]
    target = source.replace(name,'')
    box = (left, top, left+width, top+height)
    img = Image.open(source)
    img.thumbnail((kwargs['resize_x'],kwargs['resize_y']), Image.ANTIALIAS)
    area = img.crop(box)
    img_type = name.split('.')[-1]
    area.save(target + 'c_' + name, format='JPEG')
    ll = kwargs['image_name'].replace(name, 'c_' + name)
    return ll
