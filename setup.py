[coverage:run]
branch = True

[flake8]
accept-encodings = utf-8
max-complexity = 6
statistics = False
max-line-length = 80
doctests = True
enable-extensions = G
isort-show-traceback = True

# clean default ignore list
ignore =

per-file-ignores =
  # it is possibble to have prints in scripts
    hexlet_python_package/scripts/*.py: WPS421

    [tool:pytest]
    norecursedirs = __pycache__
    addopts = --strict-markers

    [isort]
    # See https://github.com/timothycrosley/isort#multi-line-output-modes
    multi_line_output = 3
    include_trailing_comma = true
    default_section = FIRSTPARTY
    # Should be: 80 - 1
    line_length = 79
