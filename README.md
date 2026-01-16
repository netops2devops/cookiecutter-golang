# Cookiecutter Golang

A production-ready [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Go projects with built-in support for Docker, CI/CD pipelines, and code quality tools.

## Features

- **Go 1.25** - Latest Go version with module support
- **Makefile** - Build automation with lint, build, clean, and run targets
- **Docker Support** - Optional multi-stage Dockerfile with minimal secure base image
- **CI/CD Pipelines** - Optional GitHub Actions or GitLab CI configuration
- **Pre-commit Hooks** - Code quality enforcement with gosec, gitleaks, and standard checks
- **Git Integration** - Optional automatic repository initialization with initial commit
- **Environment Management** - direnv support via `.envrc`

## Requirements

- [Cookiecutter](https://cookiecutter.readthedocs.io/) (`pip install cookiecutter`)
- [pre-commit](https://pre-commit.com)
- Python 3.10+
- Go 1.25+ (for the generated project)

## Quick Start

### Generate a new project

```bash
cookiecutter github.com/netops2devops/cookiecutter-golang
```

Or from a local clone:

```bash
git clone https://github.com/kagraw/cookiecutter-golang.git
cookiecutter cookiecutter-golang/
```

### Answer the prompts

```text
project_name [my-go-project]: my-awesome-app
module_name [github.com/username/my-awesome-app]: github.com/username/my-awesome-app
description [A Go project]: A REST API service
author_name [Your Name]: Jane Doe
create_git_repo [yes]: yes
ci_platform [none]: github
include_dockerfile [yes]: yes
```

### Start developing

```bash
cd my-awesome-app
make build    # Compile the project
make run      # Build and run
make lint     # Run linters (go fmt, go vet, go mod tidy)
```

## Template Options

| Option | Default | Description |
| ------ | ------- | ----------- |
| `project_name` | `my-go-project` | Name of your Go project |
| `module_name` | `github.com/username/{{project_name}}` | Go module path |
| `description` | `A Go project` | Brief project description |
| `author_name` | `Your Name` | Author name for documentation |
| `create_git_repo` | `yes` | Initialize a Git repository |
| `ci_platform` | `none` | CI/CD platform: `none`, `github`, or `gitlab` |
| `include_dockerfile` | `yes` | Include Docker containerization |

## Generated Project Structure

```text
my-go-project/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions (if selected)
├── .gitlab-ci.yml          # GitLab CI (if selected)
├── .gitignore
├── .envrc                   # direnv environment file
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
├── Dockerfile               # Multi-stage Docker build (if selected)
├── Makefile                 # Build automation
├── README.md                # Project documentation
├── go.mod                   # Go module definition
└── main.go                  # Application entry point
```

## Makefile Targets

| Target | Description |
| ------ | ----------- |
| `make build` | Compile the Go binary |
| `make run` | Clean, build, and run the application |
| `make lint` | Run `go fmt`, `go vet`, and `go mod tidy` |
| `make clean` | Remove binaries and clear Go cache |
| `make all` | Alias for `run` |

## Docker Support

When Docker support is enabled, the template generates a multi-stage Dockerfile:

- **Build stage**: Uses `golang:1.25.5-trixie` to compile a static binary with CGO disabled
- **Runtime stage**: Uses `chainguard/wolfi-base:latest` for a minimal, security-focused container

```bash
# Build the image
docker build -t my-awesome-app .

# Run the container
docker run my-awesome-app
```

## CI/CD Pipelines

### GitHub Actions

Automatically runs on push to `main`/`master` and pull requests:

- Sets up Go 1.25
- Builds the project
- Runs tests

### GitLab CI

Two-stage pipeline:

- **Build**: Compiles the application and stores artifacts
- **Test**: Runs unit tests

## Pre-commit Hooks

The template includes pre-configured hooks for code quality:

- **Standard checks**: YAML validation, trailing whitespace, end-of-file fixes
- **gitleaks**: Prevents committing secrets and credentials
- **gosec**: Security scanner for Go code (high-severity issues)

Install hooks in your generated project:

```bash
pip install pre-commit
pre-commit install
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
