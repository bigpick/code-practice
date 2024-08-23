SHELL := /usr/bin/env TZ=UTC bash

ifndef verbose
.SILENT:
endif

all: package

### Meta related
check-venv::
	@echo "++ $@"
	if [[ -z "$${SKIP_VENV_CHECK:-}" ]] ; then \
	    if [[ "$$VIRTUAL_ENV" == "" ]] || [[ ! -d "$$VIRTUAL_ENV" ]] ; then \
	        echo "You do not appear to be in a virtualenv, make sure your direnv setup is correct" >&2 && \
	        exit 44;  \
	    fi; \
	fi

show-venv:: | check-venv
	@echo "++ $@"
	@echo "$(VIRTUAL_ENV)"

show-installed-deps::
	@echo "++ $@"
	poetry show


### Actual building
install-deps:: | check-venv
	@echo "++ $@"
	# will install deps in this venv
	python -m pip install poetry --ignore-installed virtualenv
	poetry install

package:: install-deps test-all | check-venv
	@echo "++ $@"
	poetry build

publish:: package | check-venv
	@echo "++ $@"
	#poetry publish


### Clean related
clean::
	@echo "++ $@"

distclean::
	@echo "++ $@"
	-cd $(CURDIR) && \
	find . \( -name "__pycache__" -or -path "./build*" -or -path "./.pytest_cache*" -or -path "./dist" \) -and -not -path "./.direnv*" -exec rm -Rf {} +

pristine::
	@echo "++ $@"
	-direnv deny .envrc
	@echo "***** Your direnv-managed Python venv has been removed and direnv disabled. To re-enable, execute: 'direnv allow', then: 'make install-deps'"


### Testing
test-all:: test-unit # test-integration
check:: test-all
test:: test-all

test-unit:: | check-venv
	@echo "++ $@"
	pytest -m "not integration"

# test-integration:: | check-venv
# 	@echo "++ $@"
# 	pytest -m "integration"

# these targets are declared "phony" so that make won't skip them if a file named after the target exists
python-phonies := check-venv show-venv set-pyproject-vers clean distclean install-deps pristine check test test-all test-integration test-unit package publish
