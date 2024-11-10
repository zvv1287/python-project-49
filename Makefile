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

git-add-commot-push:
	git add .
	git commit -m "$m"
	git push
