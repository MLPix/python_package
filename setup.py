from setuptools import setup

setup(
    name= 'movie_recommender_package', 
    version= 0.1, 
    description= 'A simple random movie recomender package',
    author = 'MLP, with support from Arjun',
    url ='https://github.com/MLPix/python_package',
    packages=['recommender_movie'],
    package_data={'recommender_movie':['data/*.txt']},
    install_requires = ['numpy','pandas']

    )