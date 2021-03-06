HERE := $(shell pwd)
VENV := $(shell pipenv --venv)
PYTHONPATH := ${HERE}/src
TEST_PARAMS := --verbosity 2 --pythonpath ${PYTHONPATH}
PSQL_PARAMS := --host=localhost --username=ay2ya --password


ifeq ($(origin PIPENV_ACTIVE), undefined)
	PY := pipenv run
endif

ifeq ($(ENV_FOR_DYNACONF), travis)
	PY :=
	TEST_PARAMS := --failfast --keepdb --verbosity 0 --pythonpath ${PYTHONPATH}
	PSQL_PARAMS := --host=localhost --username=postgres --no-password
else ifeq ($(ENV_FOR_DYNACONF), heroku)
	PY :=
endif


MANAGE := ${PY} python src/manage.py


.PHONY: format
format:
	${PY} isort --virtual-env ${VENV} --recursive --apply ${HERE}
	${PY} black ${HERE}


.PHONY: run
run: static
	${MANAGE} runserver


.PHONY: static
static:
	${MANAGE} collectstatic --noinput --clear -v0


.PHONY: migrations
migrations:
	${MANAGE} makemigrations


.PHONY: migrate
migrate:
	${MANAGE} migrate


.PHONY: su
su:
	${MANAGE} createsuperuser


.PHONY: sh
sh:
	${MANAGE} shell


.PHONY: test
test:
	ENV_FOR_DYNACONF=test \
	${PY} coverage run \
		src/manage.py test ${TEST_PARAMS} \
			apps \
			project \

	${PY} coverage report
	${PY} isort --virtual-env ${VENV} --recursive --check-only ${HERE}
	${PY} black --check ${HERE}


.PHONY: report
report:
	${PY} coverage html --directory=${HERE}/htmlcov --fail-under=0
	open "${HERE}/htmlcov/index.html"


.PHONY: venv
venv:
	pipenv install --dev


.PHONY: clean
clean:
	${PY} coverage erase
	rm -rf htmlcov
	find . -type d -name "__pycache__" | xargs rm -rf
	rm -rf ./.static/


.PHONY: resetdb
resetdb:
	psql ${PSQL_PARAMS} \
		--dbname=postgres \
		--echo-all \
		--file=${HERE}/ddl/reset_db.sql \
		--no-psqlrc \
		--no-readline \


.PHONY: initdb
initdb: resetdb migrate
