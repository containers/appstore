# Ollama & Open WebUI

Ollama is an open-source project which provides an easy interface for running and interacting with LLMs (Large Language Models).
One way to use Ollama is to access it through the Open WebUI, which provides a web interface which resembles the ChatGPT site.

This quadlet runs Ollama as a rootless container, however runs without SELinux confinement.  It mounts a volume to store the data and the models so they can be persisted between restarts.  It also contains the required configuration for NVIDIA CUDA and ROCm support, so you can benefit from GPU acceleration.

Unfortunately the Open WebUI does not support defining default credentials, so users must first sign-up when accessing the site for the first time.

## Installation

To install the Ollama quadlet to your user's systemd services, copy the `ollama.network`, `ollama.volume`, `ollama-webui.volume`, `ollama-webui.container` and `ollama.container` files to either of the following directories:

- `$HOME/.config/containers/systemd/`
- `/etc/containers/systemd/users/`

If you wish to use GPU acceleration with CUDA or ROCm, you should also copy over the respective `.conf` files inside the `ollama.container.d` directory.  These options will be automatically merged with the container configuration when the service is generated.

## Usage

To start the Ollama and Open WebUI services, you can generate the systemd service files and execute the services:

```bash
$ systemctl --user daemon-reload
$ systemctl --user start ollama-web
```

This will bring up the Ollama service and the Open WebUI service.  You can then access the Open WebUI by navigating to `http://localhost:8080` in your web browser.
