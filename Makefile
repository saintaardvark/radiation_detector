SHELL=/bin/bash

run: venv
	source ./.secret.sh && \
		$(VENV)/python ./detector.py

include Makefile.venv
