# Blew A Fuse

Twitter bot @BlewAFuse

## Setup

### 1) Dependencies
* Install dependencies with `pip install -r requirements.txt`
* Run `source venv/bin/activate` to activate the local python environment in your terminal

### 2) Keys

* Create `.env` file by copying and renaming the `.env-template` and filling in the appropriate fields

## Continuous development

* Use `uvicorn main:app --reload` to run the server

### Package Management

* Install new packages using `pip install packagename`
* Record changes to packages using `pip freeze >> requirements.txt` and commit this file

### Key Management

* After adding or removing a key from the `.env`, run `python update_env_template.py` to generate a new `.env-template` from the updated `.env` file.