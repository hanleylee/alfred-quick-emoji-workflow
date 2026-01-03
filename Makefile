SHELL:=/usr/bin/env bash
a:
	@echo "a is $$0"
b:
	@echo "b is $$0"
pack:
	shopt -s globstar
	uv pip install . --target ./src/libs
