#!/bin/bash

pyenv:
	if [ ! -d "~/.pyenv/versions/3.10.11/" ]; then \
		pyenv install 3.10.11; \
	elif [ ! -d "~/.pyenv/versions/3.7.12/" ]; then \
		pyenv install 3.7.12; \
	elif [ ! -d "~/.pyenv/versions/3.8.16/" ]; then \
		pyenv install 3.8.16; \
	else \
		echo "Python development versions already installed."; \
	fi
test:
	python -m pytest --cov=./ --cov-config=.coveragerc --cov-fail-under=0 --cov-report=xml
