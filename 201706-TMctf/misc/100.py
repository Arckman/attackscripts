from PIL import Image

im=Image.open('misc100.png')
one=im.crop((0,0,440,53))
two=im.crop((0,53,440,106))
one.save('one.png')
two.save('two.png')
third=Image.alpha_composite(one,two)
third.save('third.png')
