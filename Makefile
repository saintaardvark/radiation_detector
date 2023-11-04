run:
	. ./.secret.sh && \
		$(VENV)/python ./detector.py

include Makefile.venv
