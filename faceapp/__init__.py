import io
import json
import random
import string

import requests
from PIL import Image


class FaceApp:
    def __init__(self):
        self.FILTERS = ['smile', 'smile_2', 'hot', 'old', 'young', 'female', 'male']
        self.URL = 'https://node-01.faceapp.io'
        self.USER_AGENT = 'FaceApp/1.0.229 (Linux; Android 4.4)'
        self.DEVICE_ID = self.__gen()

    def create(self, ip, sfp, fn, c=True):
        """
        add a filter on the image
        :param ip: the path to the image you want to apply filters on
        :param sfp: the path to the FOLDER where you want to save image with filters applied
        :param fn: name of the filter you want to apply on the image
        :param c: true if you want to crop the photo
        :return path: path to the image with filter
        """
        code = self.get_code(ip)
        im_bytes = self.make_img(code, fn, c)
        image = Image.open(io.BytesIO(im_bytes))

        try:
            path = sfp + "/{}".format(fn) + '.png'
            image.save(path)
            return path
        except Exception as e:
            raise FaceAppException(str(e))

    def get_code(self, fp):
        """
        get photo code
        :param fp: photo's file path
        :return: photo code
        """
        if fp is not None:
            with open(fp, 'rb') as p:
                r = requests.post(self.URL + '/api/v2.3/photos', files={'file': p},
                                  headers={'User-Agent': self.USER_AGENT, 'X-FaceApp-DeviceID': self.DEVICE_ID})
                rb = json.loads(json.dumps(r.json()))

                if r.status_code not in [200, 201, 202]:
                    raise FaceAppException("Error {}: {}\n{}".format(rb['code'], rb['err'], rb['err']['desc']))
                else:
                    return rb['code']
        raise TypeError

    def make_img(self, code, filter_name, c):
        """
        Apply filter to the image
        :param c: true if you want to crop the photo
        :param code: the photo code you can get with get_code
        :param filter_name: the filter you want to apply
        :return: byte image
        """

        if filter_name in self.FILTERS:
            req = requests.get(
                self.URL + '/api/v2.3/photos/{0}/filters/{1}?cropped={2}'.format(code, filter_name, c),
                headers={'User-Agent': self.USER_AGENT, 'X-FaceApp-DeviceID': self.DEVICE_ID})

            if req.status_code == 200:
                req.raw.decode_content = True
                content = req.content
                return content

            else:
                raise FaceAppException(str(req.status_code))
        raise FaceAppException('Invalid filter')

    @staticmethod
    def __gen(size=8, chars=string.ascii_lowercase + string.digits):
        """
        this function generates a 8 chars string that will be used as DEVICE_ID
        """
        return ''.join(random.choice(chars) for _ in range(size))


class FaceAppException(Exception):
    def __init__(self, message):
        super(FaceAppException, self).__init__(message)
