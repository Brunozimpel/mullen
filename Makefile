# Install dependecies
dev_install:
	[ ! -z "${VIRTUAL_ENV}" ] # Check for virtualenv.
	pip3 install -r requirements.txt 

# Clean da rouse
clean:
	rm -rf cache/ dist/ .mypy_cache/ *.egg-info/ *.log \
		.ipynb_checkpoints/ 
	find ./ -name '__pycache__' -type d | xargs -I@ rm -rf @

# Opens Jupyter Server
analyse:
	nohup jupyter-notebook > /dev/null &

# Kills Jupyter server
shutdown:
	ps -e | grep 'jupyter' | awk '{print $$1}' | xargs -I@ kill @
