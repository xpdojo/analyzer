.PHONY: all
all: clean install oracle-session

.PHONY: clean
clean:
	rm -rf venv

.PHONY: install
install:
	python3 -m venv venv
	venv/bin/pip install -Ur requirements.txt

.PHONY: oracle-session
oracle-session:
	@echo "Running main.py"
	@venv/bin/python3 main.py
