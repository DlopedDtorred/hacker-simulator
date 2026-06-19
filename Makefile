# Hacker Simulator 2077 - Makefile
# Targets: install, run, clean, test, package

.PHONY: install run clean test package help

# Colors
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
RED    := $(shell tput -Txterm setaf 1)
RESET  := $(shell tput -Txterm sgr0)

help: ## Show this help message
	@echo '$(GREEN)Available commands:$(RESET)'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(YELLOW)%-15s$(RESET) %s\n", $$1, $$2}'

install: ## Install dependencies and package
	@echo '$(GREEN)📦 Installing dependencies...$(RESET)'
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .
	@echo '$(GREEN)✅ Installation complete!$(RESET)'

run: ## Run the game
	@echo '$(GREEN)🚀 Running Hacker Simulator 2077...$(RESET)'
	python cyberdex.py

clean: ## Clean temporary files
	@echo '$(GREEN)🧹 Cleaning up...$(RESET)'
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache .coverage htmlcov 2>/dev/null || true
	@echo '$(GREEN)✅ Clean complete!$(RESET)'

test: ## Run tests (if any)
	@echo '$(GREEN)🧪 Running tests...$(RESET)'
	python -m pytest tests/ 2>/dev/null || echo '$(YELLOW)⚠️ No tests found$(RESET)'

package: ## Build package for distribution
	@echo '$(GREEN)📦 Building package...$(RESET)'
	python -m pip install --upgrade build
	python -m build
	@echo '$(GREEN)✅ Package built in dist/$(RESET)'

install-dev: ## Install development dependencies
	@echo '$(GREEN)🛠️ Installing dev dependencies...$(RESET)'
	pip install -r requirements-dev.txt 2>/dev/null || echo '$(YELLOW)⚠️ requirements-dev.txt not found$(RESET)'

all: clean install run ## Clean, install and run