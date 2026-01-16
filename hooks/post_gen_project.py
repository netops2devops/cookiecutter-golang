#!/usr/bin/env python
"""Post-generation hooks for cookiecutter template."""

import os
import shutil
import subprocess

def init_git():
    """Initialize git repository if requested."""
    if "{{ cookiecutter.create_git_repo }}" == "yes":
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
        print("Git repository initialized with initial commit.")

def remove_unused_ci_files():
    """Remove CI files that aren't needed based on selected platform.

    If create_git_repo is 'no', CI platform is forced to 'none' since
    CI/CD pipelines require a git repository.
    """
    create_git_repo = "{{ cookiecutter.create_git_repo }}"
    ci_platform = "{{ cookiecutter.ci_platform }}"

    # CI makes no sense without a git repo - force to 'none'
    if create_git_repo != "yes":
        ci_platform = "none"

    if ci_platform != "github":
        github_dir = ".github"
        if os.path.exists(github_dir):
            shutil.rmtree(github_dir)

    if ci_platform != "gitlab":
        gitlab_file = ".gitlab-ci.yml"
        if os.path.exists(gitlab_file):
            os.remove(gitlab_file)

def remove_dockerfile_if_not_needed():
    """Remove Dockerfile if not requested."""
    if "{{ cookiecutter.include_dockerfile }}" != "yes":
        dockerfile = "Dockerfile"
        if os.path.exists(dockerfile):
            os.remove(dockerfile)

def main():
    remove_unused_ci_files()
    remove_dockerfile_if_not_needed()
    init_git()
    print("Project {{ cookiecutter.project_name }} created successfully!")

if __name__ == "__main__":
    main()
