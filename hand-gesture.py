from roboflow import Roboflow
rf = Roboflow(api_key="sKsQzha8jrnm9Onvmp6p")
project = rf.workspace().project("rock-paper-scissors-sxsw")
model = project.version(11).model

# infer on a local image
#print(model.predict("sn-rockpaper.jpg", confidence=40, overlap=30).json())
predictions = model.predict("sn-rockpaper.jpg", confidence=40, overlap=30).json()

for i in predictions['predictions']:
    print(i['class'])