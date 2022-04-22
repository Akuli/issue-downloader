# Issue downloader

This repo contains a script that downloads code from GitHub issues
and saves it to files in `code_snippets/`.
Running two different versions of a tool on these code snippets
helps identify issues that have been fixed or unfixed.
See also [hauntsaninja/mypy_primer](https://github.com/hauntsaninja/mypy_primer/).

Currently issues from the following repositories are checked daily at midnight UTC:
- https://github.com/python/mypy
- https://github.com/python/typeshed
- https://github.com/python/typing
