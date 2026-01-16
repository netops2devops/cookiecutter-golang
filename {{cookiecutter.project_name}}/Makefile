# Variables
APP_NAME={{ cookiecutter.project_name }}
ENV_FILE= .envrc

ENV_FILE= .envrc

# Targets
.PHONY: all lint build clean run

default: build

all: run

lint:
	@echo "🧹 Linting..."
	go fmt ./...
	go vet ./...
	go mod tidy

build:
	@echo "⚙️ Building Go program..."
	go build -o $(APP_NAME) .

clean:
	@echo "Removing compiled binary and cleaning cache..."
	@if [ -f $(APP_NAME) ]; then \
		rm $(APP_NAME); \
	fi
	@go clean -cache

run: clean build
	@echo "🚀 Running..."
	@eval $$(cat $(ENV_FILE) | grep -v "^#" | xargs -I {} echo {}) ./$(APP_NAME)
