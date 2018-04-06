SHELL := /bin/bash

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "  clean              Clean venv"
	@echo "  install            Init venv"
	@echo ""

.PHONY: clean
clean:
	@exec rm -rf ./venv

.PHONY: install
install:
	@exec virtualenv --no-site-packages venv


