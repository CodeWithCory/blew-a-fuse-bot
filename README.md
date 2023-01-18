# Blew A Fuse

Twitter bot @BlewAFuse

## Setup

Dependencies

* Install dependencies with `pip install -r requirements.txt`
* Run `source venv/bin/activate` to activate the local python environment in your terminal

Keys

* Create `.env` file by copying and renaming the `.env-template` and filling in the appropriate fields

## Continuous development

* Run `source venv/bin/activate` to activate the local python environment in your terminal
* Use `uvicorn app.main:app --reload` to run the server
* All-in-one startup: `source venv/bin/activate && uvicorn app.main:app --reload`

### Package Management

* Install new packages using `pip install packagename`
* Record changes to packages using `pip freeze >> requirements.txt` and commit this file

### Key Management

* After adding or removing a key from the `.env`, run `python update_env_template.py` to generate a new `.env-template` from the updated `.env` file.

## @BlewAFuse Info

* Twitter ID: 1541247183919382528
