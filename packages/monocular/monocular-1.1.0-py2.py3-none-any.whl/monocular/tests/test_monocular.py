import monocular
import unittest
import unicodedata
import collections
from PIL import Image

client_id = '109f2bf54fee516f366c57254e77cb87'
client_secret = '8c4858a9400ea57b626aef87ddbe1ae3aa59bb84'

def _parse(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(_parse, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(_parse, data))
    else:
        return data

class TestMonocularSDK(unittest.TestCase):
    def test_config(self):
        self.assertIsNotNone(monocular.initialize)

    def test_init(self):
        monocular.initialize({
            'client_id': client_id,
            'client_secret': client_secret
        })


class TestEndpoints(unittest.TestCase):
    monocular.initialize({ 'client_id': client_id, 'client_secret': client_secret, 'base_url': 'http://monocular.dev/api' })

    def test_existance(self):
        self.assertIsNotNone(monocular)
        self.assertIsNotNone(monocular.blur)
        self.assertIsNotNone(monocular.crop)
        self.assertIsNotNone(monocular.dilate)
        self.assertIsNotNone(monocular.distance_transform)
        self.assertIsNotNone(monocular.downscale)
        self.assertIsNotNone(monocular.erode)
        self.assertIsNotNone(monocular.face_detection)
        self.assertIsNotNone(monocular.flip)
        self.assertIsNotNone(monocular.greyscale)
        self.assertIsNotNone(monocular.invert)
        self.assertIsNotNone(monocular.resize)
        self.assertIsNotNone(monocular.rotate)
        self.assertIsNotNone(monocular.threshold)
        self.assertIsNotNone(monocular.upscale)

#     # Params
#     def test_blur(self):
#         response = monocular.blur(image)
#         self.assertIsNotNone(response.show())
#
#     def test_crop(self):
#         repsonse = monocular.crop(image, top=10, left=10, bottom=110, right=110)
# 	self.assertIsNotNone(response.show())
# #params
#     def test_dilate(self):
#         response = monocular.dilate(image)
#         self.assertIsNotNone(monocular.downscale)
# #params
#     def test_distance_transform(self):
#         repsonse = monocular.distance_transform
#         self.assertIsNotNone(monocular.erode)
#
class TestImages(unittest.TestCase):
    monocular.initialize({ 'client_id': client_id, 'client_secret': client_secret })

    def test_crud_existance(self):
        self.assertIsNotNone(monocular.images)
        self.assertIsNotNone(monocular.images.create)
        self.assertIsNotNone(monocular.images.delete)
        self.assertIsNotNone(monocular.images.download)
        self.assertIsNotNone(monocular.images.find_all)
        self.assertIsNotNone(monocular.images.find_one)
        self.assertIsNotNone(monocular.images.update)

    def test_crud(self):
        response = _parse(monocular.images.create({ 'url': 'https://pbs.twimg.com/profile_images/637099631902486531/wZ-KImSi_400x400.png'}))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.images.find_one(response['id']))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.images.update(response['id'], {'label': 'test'}))
        self.assertIsNotNone(response['label'])
        response = _parse(monocular.images.delete(response['id']))

    def test_endpoint_existance(self):
        self.assertIsNotNone(monocular.images.blur)
        self.assertIsNotNone(monocular.images.crop)
        self.assertIsNotNone(monocular.images.dilate)
        self.assertIsNotNone(monocular.images.distance_transform)
        self.assertIsNotNone(monocular.images.downscale)
        self.assertIsNotNone(monocular.images.erode)
        self.assertIsNotNone(monocular.images.face_detection)
        self.assertIsNotNone(monocular.images.flip)
        self.assertIsNotNone(monocular.images.greyscale)
        self.assertIsNotNone(monocular.images.invert)
        self.assertIsNotNone(monocular.images.resize)
        self.assertIsNotNone(monocular.images.rotate)
        self.assertIsNotNone(monocular.images.threshold)
        self.assertIsNotNone(monocular.images.upscale)

class TestDetector(unittest.TestCase):
    monocular.initialize({ 'client_id': client_id, 'client_secret': client_secret })

    def test_existance(self):
        self.assertIsNotNone(monocular.detectors)
        self.assertIsNotNone(monocular.detectors.create)
        self.assertIsNotNone(monocular.detectors.find_all)
        self.assertIsNotNone(monocular.detectors.find_one)
        self.assertIsNotNone(monocular.detectors.detect)
        self.assertIsNotNone(monocular.detectors.train)
        self.assertIsNotNone(monocular.detectors.update)
        self.assertIsNotNone(monocular.detectors.delete)

    def test_crud(self):
        response = _parse(monocular.detectors.create('Test'))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.detectors.find_one(response['id']))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.detectors.update(response['id'], {'label': 'Test2'}))
        self.assertIsNotNone(response['label'])
        self.assertEqual(response['label'], 'Test2')
        response = _parse(monocular.detectors.delete(response['id']))

class TestDataBuckets(unittest.TestCase):
    monocular.initialize({ 'client_id': client_id, 'client_secret': client_secret })

    def test_existance(self):
        self.assertIsNotNone(monocular.databuckets)
        self.assertIsNotNone(monocular.databuckets.create)
        self.assertIsNotNone(monocular.databuckets.find_all)
        self.assertIsNotNone(monocular.databuckets.find_one)
        self.assertIsNotNone(monocular.databuckets.update)
        self.assertIsNotNone(monocular.databuckets.delete)
        self.assertIsNotNone(monocular.databuckets.add_data)
        self.assertIsNotNone(monocular.databuckets.remove_data)

    def test_crud(self):
        response = _parse(monocular.databuckets.create('Test'))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.databuckets.find_one(response['id']))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.databuckets.update(response['id'], {'label': 'Test2'}))
        self.assertIsNotNone(response['label'])
        self.assertEqual(response['label'], 'Test2')
        response = _parse(monocular.databuckets.delete(response['id']))

class TestIdentifiers(unittest.TestCase):
    monocular.initialize({ 'client_id': client_id, 'client_secret': client_secret })

    def test_existance(self):
        self.assertIsNotNone(monocular.face_identifiers)
        self.assertIsNotNone(monocular.face_identifiers.create)
        self.assertIsNotNone(monocular.face_identifiers.find_all)
        self.assertIsNotNone(monocular.face_identifiers.find_one)
        self.assertIsNotNone(monocular.face_identifiers.identify)
        self.assertIsNotNone(monocular.face_identifiers.train)
        self.assertIsNotNone(monocular.face_identifiers.update)
        self.assertIsNotNone(monocular.face_identifiers.delete)
        self.assertIsNotNone(monocular.face_identifiers.add_face)
        self.assertIsNotNone(monocular.face_identifiers.remove_face)

    def test_crud(self):
        response = _parse(monocular.face_identifiers.create('Test'))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.face_identifiers.find_one(response['id']))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.face_identifiers.update(response['id'], {'label': 'SomeNewLabel' }))
        self.assertIsNotNone(response['label'])
        self.assertEqual(response['label'], 'SomeNewLabel')
        response = _parse(monocular.face_identifiers.delete(response['id']))

class TestBackgroundSubtraction(unittest.TestCase):
    monocular.initialize({ 'client_id': client_id, 'client_secret': client_secret })

    def test_existance(self):
        self.assertIsNotNone(monocular.background_subtractors)
        self.assertIsNotNone(monocular.background_subtractors.create)
        self.assertIsNotNone(monocular.background_subtractors.update)
        self.assertIsNotNone(monocular.background_subtractors.delete)
        self.assertIsNotNone(monocular.background_subtractors.find_one)
        self.assertIsNotNone(monocular.background_subtractors.find_all)
        self.assertIsNotNone(monocular.background_subtractors.add_image)
        self.assertIsNotNone(monocular.background_subtractors.add_image_url)
        self.assertIsNotNone(monocular.background_subtractors.add_image_id)

    def test_crud(self):
        response = _parse(monocular.background_subtractors.create('Test', 'MOG', {}))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.background_subtractors.find_one(response['id']))
        self.assertIsNotNone(response['id'])
        response = _parse(monocular.background_subtractors.update(response['id'], {'label': 'Test2'}))
        self.assertIsNotNone(response['label'])
        self.assertEqual(response['label'], 'Test2')
        image = monocular.background_subtractors.add_image_url(response['id'], 'https://pbs.twimg.com/profile_images/637099631902486531/wZ-KImSi_400x400.png', 0, 'PNG')
        print(image)
        image.show()
        response = _parse(monocular.background_subtractors.delete(response['id']))

if __name__ == '__main__':
    unittest.main()
