from setuptools import setup, find_packages

setup(
    name='pyStrich',
    version='0.8',
    packages=['pystrich',
              'pystrich.ean13',
              'pystrich.qrcode',
              'pystrich.code39',
              'pystrich.code128',
              'pystrich.datamatrix',
              'pystrich.fonts'],
    package_data={
        'pystrich.fonts': ['*.pil', '*.pbm'],
        'pystrich.qrcode': ['qrcode_data/*.dat']
    },
    install_requires = ['Pillow'],
    url='http://method-b.uk/pystrich/',
    license='Apache 2.0',
    author='Michael Mulqueen',
    author_email='michael@mulqueen.me.uk',
    description='PyStrich is a Python module to generate 1D and 2D barcodes (Code 39, Code 128, DataMatrix, QRCode and '
                'EAN13). Forked from huBarcode.',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Office/Business"
    ]
)
