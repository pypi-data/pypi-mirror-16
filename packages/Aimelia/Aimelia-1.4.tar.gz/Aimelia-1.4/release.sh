# I ended up running:
# python setup.py register
# ... and then run this ./release.sh script

rm -rf build dist aimelia.egg-info
python setup.py sdist upload
