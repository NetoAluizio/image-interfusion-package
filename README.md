# package_name

Description. 
The package imageInterfusion is used to:
	* Interfusion:
		- Find difference;
		- Transfer histogram;
		- Resize image.
	* Useful:
		- Read image;
		- Save image;
		- Plot image;
		- Plot Result;
		- Plot histogram.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install imageInterfusion

```bash
pip install imageInterfusion
```

## Usage

```python
from imageInterfusion.interfusion import imageFit
imageFit.resizeImage()
from imageInterfusion.interfusion import imageMerge
imageMerge.findDifference()
imageMerge.transferHistogram()
from imageInterfusion.useful import io
io.readImage()
io.saveImage()
from imageInterfusion.useful import plot
plot.plotImage()
plot.plotResult()
plot.plotHistogram()
```

## Author
Aluizio Neto

## License
[MIT](https://choosealicense.com/licenses/mit/)