init:
	npm install -g serverless
	pipenv --python 3.7
	pipenv install

deploy:
	serverless deploy -v

invoke:
	serverless invoke -f $(FUNC) -l

logs:
	serverless logs -f $(FUNC) -t

remove:
	serverless remove

freeze: ## Freeze the packages to .txt
	pipenv lock -r > requirements.txt