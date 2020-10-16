# applogging

This repo is on a simple paradigm to set up module logging in a `python` project. It features

- providing a helper module for global logging configuration
- presenting an example that demos mixed logs from single process and also parallel processes

In this simple paradigm, we define a logger in each `python` module with one line as follows
```python
mylogger = logging.getLogger(__name__)
```
Within the module, logging will be something like
```python
mylogger.info('data are fetched.')
```

The module loggers will propagate to the root logger for handling, which is able to be configured globally by the helper functions in ``applogger.py``.

This repo contains an example to demo how to log for both single and multiple processes. The example consists of 3 files
```
main.py
featureselection.py
dataprocess.py
```
where `main.py` is the place showing how to configure logs produced by two modules `featureselection.py` (single processing) and `dataprocess.py` (multiple processing). Within each of these two modules, only one line is used to define the module logger as mentioned above.
