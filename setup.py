from setuptools import setup
import datetime

setup(
    name='CoAPthon3',
    version='1.0.1+fb.' + datetime.datetime.now().strftime("%Y%m%d%H%M"),
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
    license='MIT License',
    author='Giacomo Tanganelli',
    author_email='giacomo.tanganelli@for.unipi.it',
    maintainer="Bjoern Freise",
    maintainer_email="mcfreis@gmx.net",
    url="https://github.com/mcfreis/CoAPthon3",
    description='CoAPthon is a python library to the CoAP protocol.',
    scripts=[
        'coapclient.py',
        'coapforwardproxy.py',
        'coapreverseproxy.py',
        'coapserver.py',
        'exampleresources.py',
    ],
    requires=['sphinx', 'cachetools']
)
