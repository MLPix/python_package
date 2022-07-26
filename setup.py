from setuptools import setup

setup(
    name= 'randomrecommender', 
    version= 0.1, 
    description= 'A simple random movie recomender package',
    author = 'MLP, with support from Arjun',
    url =, #place github link here
    packages=['recommender_movie'],
    package_data={'recommender_movie':['data/*.txt']},
    install_requires = ['numpy','pandas']

    )