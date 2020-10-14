# applogging

This repo is on a simple paradigm to set up logging in a `python` project. It features

- providing a global logging configuration module with high-level helper functions
- presenting an example that produces mixed logs from main process and also parallel processes

In this simple paradigm, we define a logger in each `python` module with one line as follows
```python
mylogger = logging.getLogger(__name__)
```
Within the module, the logging will be something like
```python
mylogger.info('data are fetched.')
```

The central logger configuration is at the main running script.
