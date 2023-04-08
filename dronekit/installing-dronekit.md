# Installing instructions for Dronekit

1. Install required packages from terminal.

`sudo apt-get install python3-dev python3-pip`

2. Install dronekit Python module.

`python3 -m pip install dronekit`

## Updating the Dronekit

1. To update the Dronekit for using the latest version, run the command.

`python3 -m pip install dronekit --upgrade`

## Using Dronekit with Python >= 3.10

1. If you are using Python 3.10 or above, you need to add the following lines before importing dronekit.

```python
import sys
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    from collections.abc import MutableMapping
    setattr(collections, "MutableMapping", MutableMapping)
```

2. Or just simply import the `dronekit_python310_compat` module inside the project.

```python
import dronekit_python310_compat
```   

[Source](https://dronekit-python.readthedocs.io/en/latest/develop/installation.html)