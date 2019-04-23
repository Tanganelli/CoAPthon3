from distutils.core import setup

setup(
    name='CoAPthon3',
    version='1.0.1',
    packages=[
        'coapthon',
        'coapthon.caching',
        'coapthon.client',
        'coapthon.forward_proxy',
        'coapthon.layers',
        'coapthon.messages',
        'coapthon.resources',
        'coapthon.reverse_proxy',
        'coapthon.server',
    ],
    url='https://github.com/Tanganelli/CoAPthon3',
    license='MIT License',
    author='Giacomo Tanganelli',
    author_email='giacomo.tanganelli@for.unipi.it',
    download_url='https://github.com/Tanganelli/CoAPthon3/archive/1.0.1.tar.gz',
    description='CoAPthon is a python library to the CoAP protocol. ',
    scripts=[
        'coapclient.py',
        'coapforwardproxy.py',
        'coapreverseproxy.py',
        'coapserver.py',
        'exampleresources.py',
    ],
    requires=['sphinx', 'cachetools']
)
