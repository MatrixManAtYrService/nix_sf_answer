from setuptools import setup
setup(name='mypkg',
      version='0.1.0.dev1',
      description='some awesome thing',
      packages=['mypkg'],
      python_requires= '>=3',
      install_requires=[],
      entry_points={'console_scripts' : [
              'helloworld = mypkg.hello:world',
          ]})
