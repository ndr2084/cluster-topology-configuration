# cluster-topology-configuration

A simple way to add racks to a cluster. Compatible with [qzweng/kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator).

## Overview

**cluster-topology-configuration** provides a straightforward method to define and configure rack topology for clusters. This project is designed to work seamlessly with the [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator), enabling enhanced scheduling and simulation based on topology-aware rack information.

## Features

- **Simple Configuration:** Easily specify rack and node relationships using Python.
- **Compatibility:** Integrates with [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator).
- **Extensible:** Designed to support future topology extensions.

## Quick-Start
- **In your terminal:** $ python3 process_openb_dir.py ./openb_pod_list_cpu037/ --rack-mod 8 --max-skew 2

### Prerequisites

- Python 3.7+
- [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator)


### Integration

To use with [kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator), 

## License

This project is licensed under the MIT License.

## Acknowledgements

- [qzweng/kubernetes-scheduler-simulator](https://github.com/qzweng/kubernetes-scheduler-simulator) for providing the simulator framework.

---
