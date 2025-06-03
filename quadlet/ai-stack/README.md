# AI Stack with Podman Quadlets

A complete AI stack using Podman Quadlets to deploy Ollama, Open WebUI and associated services.

## Architecture

- **Ollama**: LLM model server with NVIDIA GPU support
- **Open WebUI**: Web interface to interact with models
- **Tika**: Content extraction for RAG (Retrieval-Augmented Generation)
- **EdgeTTS**: OpenAI-compatible Text-to-Speech service
- **Valkey**: Redis-compatible cache for WebSocket

## Prerequisites

### NVIDIA GPU (optional but recommended)

#### Option 1: Use Fedora AI/ML COPR (Recommended)
```bash
# Install CUDA drivers and NVIDIA Container Toolkit
sudo dnf install -y cuda-drivers
sudo dnf copr enable @ai-ml/nvidia-container-toolkit
sudo dnf install nvidia-container-toolkit nvidia-container-toolkit-selinux

# Configure CDI for Podman
sudo mkdir -p /etc/cdi
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place

# Remove OCI hook (avoid conflicts with CDI)
sudo rm -f /usr/share/containers/oci/hooks.d/oci-nvidia-hook.json

# Restart Podman
systemctl --user restart podman.service
```
#### Option 2: Manual SELinux Configuration

The official NVIDIA repo causes SELinux denials in rootless mode because:

Device labeling: NVIDIA GPU devices are labeled as xserver_misc_device_t:
`/dev/nvidia0, /dev/nvidiactl, /dev/nvidia-uvm → xserver_misc_device_t`
`/dev/dri/renderD* → dri_device_t`

Container context: Ollama containers run with container_t context:
`system_u:system_r:container_t:s0:c381,c953`

Missing SELinux rules: The official NVIDIA package lacks allow rules for container_t to access xserver_misc_device_t devices.

Solution provided by ai-ml repo:

The nvidia-container-toolkit-selinux.rpm includes a SELinux module defining nvidia_container_t with the crucial rule:

allow nvidia_container_t xserver_misc_device_t:chr_file { append getattr ioctl lock map open read write };

This enables GPU device access for containerized workloads. The ai-ml version essentially provides the missing SELinux policies that should be part of the official NVIDIA container toolkit for rootless scenarios.

## Installation

1. Clone repository to `~/.config/containers/systemd/`
2. Adjust environment variables if needed
3. Start the stack:

```bash
# Rootless mode (recommended)
systemctl --user daemon-reload
systemctl --user status ollama.service
systemctl --user start ollama.service
```

## Port Configuration

The pod exposes the following ports:
- **4080** → Open WebUI (only port that needs public exposure)
- **11434** → Ollama API (internal use)
- **9998** → Tika (internal use)
- **5050** → EdgeTTS (internal use)

> **Note**: Only port 4080 (Open WebUI) needs to be exposed on the host. Other services communicate via the pod's internal network.

## Access

- Web Interface: `http://localhost:4080`
- Ollama API (internal): `http://ollama:11434`

## Management

```bash
# Service status
systemctl --user status ollama.service

# Logs
podman logs -f open-webui
podman logs -f ollama

# Automatic image updates
systemctl --user start podman-auto-update.service
```

## Volume Structure

- `ollama`: Downloaded LLM models
- `openwebui`: Open WebUI configuration and data
- `valkey`: Persistent cache
