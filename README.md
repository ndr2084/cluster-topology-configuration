# cluster-topology-configuration

A simple way to add racks to a cluster. Compatible with [qzweng/kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator).

## Overview

**cluster-topology-configuration** provides a straightforward method to define and configure rack topology for clusters. This project is designed to work seamlessly with the [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator), enabling enhanced scheduling and simulation based on topology-aware rack information.

## Features

- **Simple Configuration:** Easily specify rack and node relationships using Python.
- **Compatibility:** Integrates with [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator).
- **Extensible:** Designed to support future topology extensions.

## Quick-Start
```
cd kubernetes-simulator-dockerfile
docker build -t simulator-with-ui .
docker run -p 8501:8501 simulator-with-ui
```


# Streamlit Web UI (app.py)

app.py has been added to provide a modern web interface for running and customizing cluster topology and simulation experiments.
```
Features: 
    ✅Streamlit-based GUI: Easily accessible interface for configuring racks, skew, pod lists, and scheduler policies.
    ✅Interactive Sidebar: Select the number of racks and skew value.
    ✅Pod List & Policy Selection: Dropdown menus to choose configuration options
    ✅Process Topology: One-click button executes process_openb_dir.py with your chosen options
    ✅Run Simulation: Launches a full simulation pipeline
```
## Usage
```
Use the web interface to:
    ✅Select pod list, scheduling policy, and other options.
    ✅Customize racks and skew (enable in sidebar).
    ✅Click "Process Topology" to generate topology data.
    ✅Click "Run Simulation" to launch a full simulation and see results live.
```
## License

This project is licensed under the MIT License.

## Acknowledgements

- [qzweng/kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator) for providing the simulator framework.

---
