export AWS_DEFAULT_REGION=eu-west-2

.PHONY: test
test:
	sam validate

.PHONY: build
build:
	pipenv run pip freeze >requirements.txt
	sam build --use-container
	rm requirements.txt

.PHONY: deploy
deploy: build
	sam deploy

logs:
	sam logs --stack-name Django-Test-App --name HelloWorldFunction
tail:
	sam logs --stack-name Django-Test-App --name HelloWorldFunction --tail
