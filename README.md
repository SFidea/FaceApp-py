# FaceApp UNOFFICIAL Python wrapper.

You can transform your face using AI with Faceapp.

FaceApp is an [Android](https://play.google.com/store/apps/details?id=io.faceapp) and [iOS](https://itunes.apple.com/app/id1180884341) application.

This module is an unofficial wrapper to their AI system.

When I wrote this module I looked at [t3hk0d3](https://github.com/t3hk0d3/ruby_faceapp)'s one (thx).

##### How to install:

```
git clone https://github.com/veetaw/FaceApp-py.git faceapp && cd faceapp
python3 setup.py install
```

##### How to use:
```python
from faceapp import FaceApp

face_app = FaceApp()
face_app.create('/path/to/the/image', '/path/to/output/folder', 'filter name', True) # True if you want to automatically crop the image, false if not
```

##### Allowed filters:
_smile, smile_2, hot, old, young, female, male_

##### Features:
- [x] All basic FaceApp features
- [ ] Automatically add emojiis in images // TODO

#### Credits
This is ONLY a wrapper, all credits for the IA and image creation goes to FaceApp devs.
