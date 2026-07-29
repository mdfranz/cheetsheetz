# Lists
- [awesome-AI-sandbox](https://github.com/webcoyote/awesome-AI-sandbox) - Curated list of AI sandbox environments, runtimes, and isolation frameworks.
- [awesome-agent-runtime-security](https://github.com/bureado/awesome-agent-runtime-security) - Collection of resources for secure AI agent execution, sandboxing, and runtime isolation.

# Vendor 
- [openshell](https://github.com/nvidia/openshell) - NVIDIA runtime providing isolated sandbox environments for AI agents using lightweight k3s.

# Easy Drop In Wrappers for Agents
- [cplt](https://ki-utvikling.nav.no/cplt) - CLI tool for running agent workloads inside lightweight isolated environments.
- [nono](https://github.com/nolabs-ai/nono) - Simple agent sandboxing tool designed for zero-config isolated code execution.

# Requires Some Tweaking
- [agentsh](https://github.com/canyonroad/agentsh) - Shell wrapper providing restricted, monitored execution environments for autonomous agents.
- [mxc](https://github.com/microsoft/mxc) - Microsoft experimental container sandbox for isolation of agent workflows.
- [landstrip](https://github.com/landstrip/landstrip) - Lightweight Linux security wrapper for stripping permissions from agent subprocesses.

# Lightweight Isolation (Linux Only)
- [microbox](https://github.com/hqarroum/microbox) - Minimal Linux sandbox tool leveraging namespaces and cgroups for process isolation.
- [sandlock](https://github.com/multikernel/sandlock) - Linux process isolation tool using [landlock](https://landlock.io/) LSM for unprivileged filesystem sandboxing.

# Plumbing
- [bubblewrap](https://github.com/containers/bubblewrap) - Unprivileged sandbox implementation using Linux namespaces for restricted command execution.

# Requires Docker
- [shai](https://shai.run/) - Docker-backed secure execution sandbox for AI agent code and tools.
- [leash](https://github.com/strongdm/leash) - Containerized sandbox runtime developed by StrongDM for controlling agent execution.

# Requires KVM
- [gondolin](https://github.com/earendil-works/gondolin) - MicroVM-based agent sandbox environment built on hardware virtualization.
- [matchlock](https://github.com/jingkaihe/matchlock) - Lightweight MicroVM sandbox wrapping [firecracker](https://github.com/firecracker-microvm/firecracker), tested on low-end Intel and ARM hardware.
