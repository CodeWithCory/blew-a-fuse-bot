# Blew A Fuse

Twitter bot @BlewAFuse

## Setup

* Install dependencies with `pip install -r requirements.txt`
* Run `source venv/bin/activate` to activate the local python environment in your terminal

## Continuous development

* Use `uvicorn main:app --reload` to run the server

### Package Management

* Install new packages using `pip install packagename`
* Record changes to packages using `pip freeze >> requirements.txt` and commit this file
