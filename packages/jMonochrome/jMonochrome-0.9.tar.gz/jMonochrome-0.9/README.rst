#Monochrome
Make your photos black and white with **Monochrome** !

_full-featured, easy-to-use, fast and lightweight python library based on Python Image Library(PIL)._

_available for both python 2.x and 3.x !_
supports various image formats like : JPEG, PNG, ...

Covered Algorithms |
------------------ |
average |
luma |
desaturation |
decomposing |
single channel |
gray shades |

#Installation 

via git :

	git clone git://abc.xyz/monochrome
	cd monochrome
	python setup.py install

via pip :

	pip install monochrome

via easy_install :

	easy_install monochrome


##make your first photo monochrome

It's just a few lines of codes :
```python
from monochrome import Monochrome
image = Monochrome(ImagePath)
image.average(outputImagePath)
```

that's all !
