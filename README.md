# model-loading-benchmark
A script for benchmarking the loading time of various ML models.

## Usage
### Loading time benchmarck
Install requirements from `requirements.txt` and run
```bash
python run.py
```
Produces a `report.txt` with results.

_Currently the reported model sizes are wrong, will try fixing it ASAP._

### Model unloading benchmark
Install requirements from `requirements.txt` and run
```bash
python unload.py
```
Compares memory usage when loading a model into CPU memory and then unloading it when using a _thread_ and a _subprocess_.
