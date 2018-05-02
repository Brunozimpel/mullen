# Creates virtual enviroments
dev_env:
	virtualenv -p python3 .venv

# Install dependecies
dev_install:
	[ ! -z "${VIRTUAL_ENV}" ] # Check for virtualenv.
	pip3 install -r requirements.txt 

# Clean da rouse
clean:
	rm -rf .cache/ dist/ .mypy_cache/ *.egg-info/ *.log \
	   notebooks/.ipynb_checkpoints/ 
	find ./amc -name '__pycache__' -type d | xargs -I@ rm -rf @

# Remove virtual env
clean_venv:
	rm -rf .venv/

# Opens Jupyter Server
analyse:
	nohup jupyter-notebook > /dev/null &

# Kills Jupyter server
shutdown:
	ps -e | grep 'jupyter' | awk '{print $$1}' | xargs -I@ kill @
