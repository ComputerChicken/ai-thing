innerLayerHeight = 10

layers = int(input("Inner layers: "))

layerList = [1]
layerList.extend([innerLayerHeight for i in range(layers)])
layerList.append(1)

networkNeurons = []

for x, v in enumerate(layerList):
    for y in range(v):
        