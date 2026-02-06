setup:
	pip install --upgrade pip pytest

test:
	pytest

docker-test:
	docker build -t chimera-test .
	docker run chimera-test

spec-check:
	@echo "Checking specs existence..."
	test -d specs || exit 1
	test -f specs/technical.md || exit 1
