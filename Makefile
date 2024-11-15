install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

all-install:build publish package-install

brain-games:
	poetry run brain-games

git-add-commit:
	git add .
	git commit -m "$m"

lint:	
	poetry run flake8 brain_games

