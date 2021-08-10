import warnings
from keras_tuner import *

warnings.warn(
    "`import kerastuner` is deprecated, please use `import keras_tuner`.",
    DeprecationWarning,
    stacklevel=2,
)

__version__ = "1.0.3"
