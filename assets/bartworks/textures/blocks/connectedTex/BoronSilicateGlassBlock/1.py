import os
from PIL import Image as pic
ept = pic.open("C:/Users/34314/AppData/Roaming/PrismLauncher/instances/GTNH 2.2.7/.minecraft/resourcepacks/Zederrian-Technology-GT5U/assets/bartworks/textures/blocks/connectedTex/BoronSilicateGlassBlock/BoronSilicateGlassBlock_15.png")
box = (0, 0, 16, 16)
for i in range(16):
    png = pic.new('RGBA', (16, 16), (0, 0, 0, 0))
    ref = ept.crop(box)
    r, g, b, a = ref.split()
    png.paste(ref, box, mask=a)
    png.save("C:/Users/34314/AppData/Roaming/PrismLauncher/instances/GTNH 2.2.7/.minecraft/resourcepacks/Zederrian-Technology-GT5U/assets/bartworks/textures/blocks/connectedTex/BoronSilicateGlassBlock/BoronSilicateGlassBlock_"+str(i)+".png")