Image Percent Diff
==================

[![Build Status](https://travis-ci.org/noaa-nws-cpc/img-percent-diff.svg?branch=master)](https://travis-ci.org/noaa-nws-cpc/img-percent-diff) [![Coverage Status](https://coveralls.io/repos/github/noaa-nws-cpc/img-percent-diff/badge.svg?branch=master)](https://coveralls.io/github/noaa-nws-cpc/img-percent-diff?branch=master)

Calculates the percent area that two images differ. This is useful for unit tests when you have to compare an image created by a unit test with a baseline image in the repo.

- Free software: Creative Commons license

Installation
------------

Create your virtual environment

    $ virtualenv <env-name>

Then activate your virtual environment and install `img-percent-diff`

    $ source <env-name>/bin/activate
    $ pip install img-percent-diff

Credits
-------

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
