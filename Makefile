.PHONY: test-server-code test-dev-run test-docker-compose

test-server-code:
	@cookiecutter . --no-input
	@cd demo-project && make test && poetry env remove python3
	@rm -rf demo-project

test-dev-run:
	@cookiecutter . --no-input
	@cd demo-project && make dev &
	@sleep 5
	@curl -s -o /dev/null -w "%{http_code}" http://localhost:8888/health | grep 200 && echo "OK"
	@pkill -f "app.server:app"
	@docker stop mongodb
	@cd demo-project && poetry env remove python3
	@rm -rf demo-project

test-docker-compose:
	@cookiecutter . --no-input
	@cd demo-project && make docker-compose-up
	@sleep 5
	@curl -s -o /dev/null -w "%{http_code}" http://localhost:8888/health | grep 200 && echo "OK"
	@cd demo-project && make docker-compose-down && poetry env remove python3
	@rm -rf demo-project
