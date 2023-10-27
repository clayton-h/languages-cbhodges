#Makefile
.phony: all
all:
	@echo "All done..."

.PHONY: run
run:
	python main.py

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis

# a. Rule for local unit test
.PHONY: local-unit-test
local-unit-test:
	pytest --verbose .

# b. Rule for local Kattis test on sample input/output files
.PHONY: local-kattis-test
local-kattis-test:
	@cat sample_input.in | python main.py | diff - sample_output.ans
	@echo "Local Kattis tests passed..."

# c. Rule for checking styles using flake8
.PHONY: style-check
style-check:
	flake8 .

# d. Rule for fixing styles using autopep8
.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .

# e. Rule for checking types with mypy
.PHONY: type-check
type-check:
	mypy --strict .

# f. Rule to submit problem to Kattis using Kattis CLI
.PHONY: submit-kattis
submit-kattis:
	kattis -f main.py -p hvertskalmaeta
