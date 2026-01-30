# pynxtools-foo - NORTH Jupyter tool

This directory contains the NORTH tool configuration and Docker image for a Jupyter-based tool in NOMAD NORTH.

## Quick start

The foo NORTH tool provides a containerized JupyterLab environment for interactive analysis with thepynxtools-foo plugin.

## Building and testing

Build the Docker image locally:

```bash
docker build -f src/pynxtools_foo/north_tools/foo/Dockerfile \
	-t ghcr.io/RubelMozumder/pynxtools-foo:latest .
```

Test the image:

```bash
docker run -p 8888:8888 ghcr.io/RubelMozumder/pynxtools-foo:latest
```

Access JupyterLab at `http://localhost:8888`.

## Documentation

For comprehensive guidance, see the main docs and the single source of truth for NORTHTool and NorthToolEntryPoint. These resources cover entry point configuration, image structure, and dependency management.

- [NOMAD NORTH tools](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html)
- [Reference for NorthToolEntryPoint](https://fairmat-nfdi.github.io/nomad-docs/reference/plugins.html#northtoolentrypoint)
- [Reference for NORTHTool](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html#north-tool-entry-point)