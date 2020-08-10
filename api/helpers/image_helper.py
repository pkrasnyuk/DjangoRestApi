import os

from PIL import Image


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


def make_thumbnail(file_path, thumbnails=[]):
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)

    thumbnail_file = ''
    try:
        img = Image.open(file_path)
        for w, h in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = os.path.join(path, f'{file_name}_{w}x{h}{ext}')
            img_copy.save(thumbnail_file)

        img.close()
    except IOError as e:
        print(e)

    return thumbnail_file
