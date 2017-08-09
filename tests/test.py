from faceapp import FaceApp, FaceAppException

f = FaceApp()

for fi in ['smile', 'smile_2', 'hot', 'old', 'young', 'female', 'male']:
    try:
        r = f.create(ip='durov.png', sfp='output', fn=fi)
    except FaceAppException:
        print("error in faceapp")
    except Exception as e:
        print(e)
