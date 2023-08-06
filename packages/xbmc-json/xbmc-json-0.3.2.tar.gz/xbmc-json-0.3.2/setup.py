from setuptools import setup
import version

PACKAGE = 'xbmc-json'

setup(name=PACKAGE,
      version=version.VERSION,
      license="WTFPL",
      description="Python module for controlling xbmc over HTTP Json API",
      author="Jean-Christophe Saad-Dupuy",
      author_email="saad.dupuy@gmail.com",
      url="https://github.com/jcsaaddupuy/python-xbmc",
      py_modules=["xbmcjson/xbmcjson"],
      packages=["xbmcjson"],
      install_requires=["requests"],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'pytest-cov', 'responses'],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "Topic :: Multimedia",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.1",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
      ])
