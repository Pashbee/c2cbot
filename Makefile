GIT_HASH=$(shell git rev-parse --short HEAD)

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
base_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

setup: clean
	pip install -e .

setup-dev: clean
	pip install -e .[dev]

clean:
	rm -rf c2cbot.egg-info/

.PHONY: test
test:
	echo "Soon TM"	