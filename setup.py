from setuptools import setup

setup( name='distancefrompicture',
    version='0.1.3a1',
    description='A small python module for determining the location of objects within static images based on characterstics of the object and the camera',
    url='https://www.github.com/Robtom5/distance_from_picture/blob/master/README.md',
    author='Robert Thomas',
    author_email='robtom_5@mac.com',
    license='MIT',
    packages=['distancefrompicture'],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4',
    ],
    python_requires='>=3',
    install_requires=['numpy'],
    zip_safe=False
    )