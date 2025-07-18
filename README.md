# cluster-topology-configuration

A simple way to add racks to a cluster. Compatible with [qzweng/kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator).

## Overview

**cluster-topology-configuration** provides a straightforward method to define and configure rack topology for clusters. This project is designed to work seamlessly with the [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator), enabling enhanced scheduling and simulation based on topology-aware rack information.

## Features

- **Simple Configuration:** Easily specify rack and node relationships using Python.
- **Compatibility:** Integrates with [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator).
- **Extensible:** Designed to support future topology extensions.

## Quick-Start
- **Enter In Terminal:** $ python3 process_openb_dir.py ./openb_pod_list_cpu037/ --rack-mod 8 --max-skew 2

## Prerequisites

- Python 3.7+
- [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator)

# Streamlit Web UI (app.py)

app.py has been added to provide a modern web interface for running and customizing cluster topology and simulation experiments.
Features

    Streamlit-based GUI: Easily accessible interface for configuring racks, skew, pod lists, and scheduler policies.
    Interactive Sidebar: Select the number of racks and skew value using sliders (can be enabled/disabled).
    Pod List & Policy Selection: Dropdown menus to choose pod list, scheduling policy, GPU selection mode, dimension extension, and normalization.
    Process Topology: One-click button executes process_openb_dir.py with your chosen options, displaying output in the browser.
    Run Simulation: Launches a full simulation pipeline, including directory setup, config generation, execution, and analysis, with output shown in the app.

Usage

    Install Streamlit if not yet done:
    Code

pip install streamlit

Start the app in your terminal:
Code

    streamlit run app.py

    Use the web interface to:
        Select pod list, scheduling policy, and other options.
        Customize racks and skew (enable in sidebar).
        Click "Process Topology" to generate topology data.
        Click "Run Simulation" to launch a full simulation and see results live.

Requirements

    Python 3.7+
    streamlit
    kubernetes-scheduler-simulator


## Integration

To use with [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator), 

## License

This project is licensed under the MIT License.

## Acknowledgements

- [qzweng/kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator) for providing the simulator framework.

---
