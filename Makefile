MODULES = $(PWD)/_build/modules
TOOLS = $(PWD)/_build/tools
SRC = $(PWD)/src
PYTHONPATH = $(MODULES)/site-packages:$(TOOLS)/site-packages
PYTHON_VERSION = python3
PYTHON := PYTHONPATH="$(PYTHONPATH)" $(PYTHON_VERSION)


.PHONY: deps unit test coverage shell clean

deps: $(MODULES) $(TOOLS) requirements.txt
	@echo "Pulling in dependencies..."

$(MODULES):
	@mkdir -p $(MODULES)
	@pip install -I --prefix=$(MODULES) -r requirements.txt
	@ln -s $(MODULES)/lib/python*/site-packages $(MODULES)/site-packages

$(TOOLS):
	@mkdir -p $(TOOLS)
	@pip install -I --prefix=$(TOOLS) pytest-cov
	@ln -s $(TOOLS)/lib/python*/site-packages $(TOOLS)/site-packages

clean:
	@echo "Cleaning all artifacts..."
	@-rm -rf _build

unit test: deps $(TOOLS)
	@cd $(SRC);\
	$(PYTHON) -m pytest ../tests

coverage: deps $(TOOLS)
	@cd $(SRC);\
	$(PYTHON) -m pytest ../tests --cov $(SRC) --cov-report=term-missing ../tests

shell: deps
	@cd $(SRC); $(PYTHON)

run: deps
	@cd $(SRC); $(PYTHON) $(SRC)/main.py

depclean::
	@-rm -rf $(MODULES)
	@-rm -rf $(TOOLS)
	@-find . -name "*.py[oc]" -delete
	@-find . -name "__pycache__" -delete
