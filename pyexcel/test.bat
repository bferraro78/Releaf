pip freeze
nosetests --with-cov --cover-package pyexcel --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source pyexcel && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long

