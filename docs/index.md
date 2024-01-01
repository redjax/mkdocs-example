# Home

## Description

This is an example project, meant to demonstrate an auto-documented Python app. The code for the app is in the `src/` directory of the repository.

!!! note
    This project doesn't actually do anything, it's just meant to show features of `mkdocs`, `mkdocstring`, and a simple Python app.

## Requirements

This is where the requirements for the app would go.

## Installation

This is where details about installing the project would go.

## Usage

This is where instructions for using the app would go.

Example of a Python snippet:

``` py title="example.py"
from pathlib import Path
from datetime import datetime

now = datetime.now()
cwd = Path.cwd() # (1)
```

1. This is a code annotation! You can use the `.cwd()` method of the `pathlib.Path` object to get the current working directory.
