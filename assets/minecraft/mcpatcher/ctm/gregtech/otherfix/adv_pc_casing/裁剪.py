from PIL import Image as pic
n = 0
ctm_image = pic.open("./temp.png").convert("RGBA")
for i in range(2):
    for j in range(14):
        box = (16*j, 16*i, 16*(j+1), 16*(i+1))
        rect_on_ctm = ctm_image.crop(box)
        result = pic.new('RGBA', (16, 16),(0, 0, 0, 0))
        r, g, b, a = rect_on_ctm.split()
        result.paste(rect_on_ctm, (0, 0, 16, 16), mask=0)
        result.save("./"+str(n)+'.png')
        n += 1