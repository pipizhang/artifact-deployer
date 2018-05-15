SHELL := /bin/bash

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "  clean              Clean venv"
	@echo "  install            Init venv"
	@echo "  test               Run tests"
	@echo "  run                Execute run command"
	@echo "  list               Execute list command"
	@echo ""

.PHONY:clean
clean:
	@exec rm -rf ./venv

.PHONY:install
install:
	@exec virtualenv --no-site-packages venv

.PHONY:test
test:
	@exec pytest

.PHONY:run
run:
	@exec python ardeployer.py run

.PHONY:list
list:
	@exec python ardeployer.py list

.PHONY:docker-build
docker-build:
	exec docker build --no-cache -t peterzhang/artifact-deployer .

.PHONY:docker-run
docker-run:
	exec docker run  -it --rm --env-file=".env" peterzhang/artifact-deployer

