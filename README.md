# HuggingFace Transformers Playground

## Documentation

<https://huggingface.co/docs/transformers/v4.15.0/index>

## Installation

<https://huggingface.co/docs/transformers/v4.15.0/installation>

## Errors

In case of this error
> RuntimeError: Failed to import transformers.models.distilbert.modeling_tf_distilbert because of the following error (look up to see its traceback): \
No module named 'tensorflow.keras.engine

replace lines 68 to 77 in site-packages/transformers/modeling_tf_utils.py with these

```python
# if parse(tf.__version__) >= parse("2.11.0"):
#     from tensorflow.keras import backend as K
#     from tensorflow.keras.engine import data_adapter
#     from tensorflow.keras.engine.keras_tensor import KerasTensor
#     from tensorflow.keras.saving.legacy import hdf5_format
# else:
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.engine import data_adapter
from tensorflow.python.keras.engine.keras_tensor import KerasTensor
from tensorflow.python.keras.saving import hdf5_format
```
