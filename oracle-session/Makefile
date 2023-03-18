.PHONY: all
all: clean install run

.PHONY: clean
clean:
	rm -rf venv

.PHONY: install
install:
	python3 -m venv venv
	venv/bin/pip install -Ur requirements.txt

.PHONY: run
run:
	@echo "Running main.py"
	@venv/bin/python3 main.py
