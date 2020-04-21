REQUIREMENTS=requirements.txt

env:
	virtualenv -p python3 $@
	$(MAKE) pip_install REQUIREMENTS=$(REQUIREMENTS)

pip_install:
	env/bin/pip install -r ${REQUIREMENTS}
