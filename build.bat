del /Q /S build dist htmlcov *.egg-info

python setup.py sdist build
python setup.py sdist bdist_wheel