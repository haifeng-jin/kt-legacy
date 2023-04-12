# kt-legacy

This repository is to support the deprecated import name of Keras Tuner.
With this repo, you can import Keras Tuner as `kerastuner`.
In the main Keras Tuner repository the import name has been changed to `keras_tuner`.

how to upload to pypi:
`python3 -m pip install --user --upgrade setuptools wheel twine`
`python3 -m build`
`twine upload dist/*`
username is __token__. password use the created token.