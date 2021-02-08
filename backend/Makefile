APP := blogger

VER := 0.1.0
SRC := $(shell find . -name "*.py" -type f)
WHL := dist/${APP}-${VER}-py3-none-any.whl

REPO := localhost:5000/tclasen

.PHONY: all
all: clean test build

.PHONY: test
test:
	poetry run pytest --mypy --flake8 --isort --black --bandit

.PHONY: build
build: build-wheel build-docker

.PHONY: build-wheel
build-wheel: ${WHL}

${WHL}: ${SRC}
	poetry version ${VER}
	poetry build -f wheel

.PHONY: build-docker
build-docker: ${WHL}
	docker build -f Dockerfile -t ${REPO}/${APP}:${VER} dist/
	docker push ${REPO}/${APP}:${VER}

.PHONY: clean
clean:
	rm -rf dist/
	find . -name "*.pyc" -delete
	find . -type d -name  "__pycache__" -exec rm -r {} +
	find . -type d -name  ".mypy_cache" -exec rm -r {} +