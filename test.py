from PIL import Image, ImageDraw, ImageFont
import time

tm_mday=time.gmtime().tm_mday
tm_mon=time.gmtime().tm_mon
tm_year=time.gmtime().tm_year
tm_hour=time.gmtime().tm_hour + 3
tm_min=time.gmtime().tm_min
stamp=(f'{tm_mday}.{tm_mon}.{tm_year} {tm_hour}-{tm_min}')
image = Image.open("some_cat.jpeg")
font = ImageFont.truetype("arial.ttf", 150)
drawer = ImageDraw.Draw(image)
drawer.text((500, 700), stamp, font=font, fill='red')
image.save('new_img.jpg')



#***

#Вывод текущего времени
#import time
#print(time.asctime())

#***

#Загрузка картинки с котом
#from PIL import Image
#myImage = Image.open('some_cat.jpeg');
#myImage.show();

#Лишнее
#import image
#myImage = Image.open("C:\newPython\bfe93e32e5644edd66935e0fdb2182c9.jpeg");
#myImage.show();
#myImage.load();

#font = ImageFont.load_default()
#image.show()