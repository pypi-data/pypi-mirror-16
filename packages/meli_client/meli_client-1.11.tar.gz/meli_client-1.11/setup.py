from setuptools import setup, find_packages
setup(
        name='meli_client',
        packages=find_packages(exclude=['test*','examples']),
        version='1.11',
        description='A MercadoLibre wrapper built for python development',
        author='MercadoLibre',
        author_email='daniel.amador@mercadolibre.com.mx',
        url='https://github.com/DanAmador/python-sdk',
        download_url='https://github.com/DanAmador/python-sdk/tarball/0.1',
        keywords=['mercado', 'libre', 'restful', 'client', 'wrapper'],
        classifiers=[],
)
