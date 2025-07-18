import streamlit as st
import subprocess

# ✅ Full list of pod list options
pod_lists = [
    "openb_pod_list_cpu050",
    "openb_pod_list_cpu100",
    "openb_pod_list_cpu200",
    "openb_pod_list_cpu250",
    "openb_pod_list_default",
    "openb_pod_list_gpushare40",
    "openb_pod_list_gpushare60",
    "openb_pod_list_gpushare80",
    "openb_pod_list_gpushare100",
    "openb_pod_list_gpuspec10",
    "openb_pod_list_gpuspec20",
    "openb_pod_list_gpuspec25",
    "openb_pod_list_gpuspec33",
    "openb_pod_list_multigpu10",
    "openb_pod_list_multigpu20",
    "openb_pod_list_multigpu30",
    "openb_pod_list_multigpu40",
    "openb_pod_list_multigpu50",
]

# ✅ Policies (schedulers)
policies = [
    "Random",
    "DotProd",
    "GpuClustering",
    "GpuPacking",
    "BestFit",
    "FGD",
]

# ✅ GPU selection options
gpu_modes = ["<none>", "random", "best", "FGD"]
dimext_modes = ["<none>", "merge", "share"]
norm_modes = ["<none>", "max"]

# ============================
# ✅ Sidebar (left side)
# ============================
st.sidebar.title("Topology Processing Options")

enable_topology = st.sidebar.radio(
    "Enable Rack & Skew Customization?",
    ["No", "Yes"],
    index=0
)

DEFAULT_RACKS = 10
DEFAULT_SKEW = 1

if enable_topology == "Yes":
    # ✅ Real sliders (interactive)
    rack_mod = st.sidebar.slider("Number of Racks", 1, 50, DEFAULT_RACKS)
    max_skew = st.sidebar.slider("Skew Value", 1, 10, DEFAULT_SKEW)
else:
    # ✅ Show fake greyed-out values (NOT interactive)
    st.sidebar.write("**Number of Racks:**")
    st.sidebar.progress(0)  # visual indicator
    st.sidebar.caption(f"(disabled)")

    st.sidebar.write("**Skew Value:**")
    st.sidebar.progress(0)
    st.sidebar.caption(f"(disabled)")

    # Force defaults internally
    rack_mod = DEFAULT_RACKS
    max_skew = DEFAULT_SKEW

# ============================
# ✅ Main UI (right side)
# ============================
st.title("Kubernetes Scheduler Simulator Runner")

# Dropdown UI
pod_list = st.selectbox("Select Pod List", pod_lists)
policy = st.selectbox("Select Scheduling Policy", policies)
gpu_sel = st.selectbox("GPU Selection", gpu_modes)
dimext = st.selectbox("Dimension Extension", dimext_modes)
norm = st.selectbox("Normalization", norm_modes)

# ---------------------------------------
# Topology Processing Button
# ---------------------------------------
if st.button("Process Topology (Add Racks & Constraints)"):
    # Build command to call your topology script
    cmd = [
        "python3", "process_openb_dir.py",
        f"data/{pod_list}",
        "--rack-mod", str(rack_mod),
        "--max-skew", str(max_skew)
    ]

    st.write("### Running Topology Processor:")
    st.code(" ".join(cmd))

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    st.write("### Topology Processor Output")
    if result.stdout:
        st.code(result.stdout)
    if result.stderr:
        st.error(result.stderr)

st.markdown("---")

# ---------------------------------------
# Scheduler Simulation Button
# ---------------------------------------
if st.button("Run Simulation"):
    # ✅ Experiment directory
    expdir = f"experiments/2023_0511/{pod_list}/{policy}/1.3/42"
    mkdir_cmd = f'mkdir -p "{expdir}" && touch "{expdir}/terminal.out"'

    # ✅ Base CLI command
    cli = (
        f'python3 scripts/generate_config_and_run.py '
        f'-d "{expdir}" -e -b -f data/{pod_list} -{policy} 1000'
    )

    # ✅ Add optional params dynamically
    if gpu_sel != "<none>":
        cli += f" -gpusel {gpu_sel}"
    if dimext != "<none>":
        cli += f" -dimext {dimext}"
    if norm != "<none>":
        cli += f" -norm {norm}"

    cli += f' -tune 1.3 -tuneseed 42 --shuffle-pod=true -z "{expdir}/snapshot/ds01"'

    # ✅ Append analysis step
    analysis = f'python3 scripts/analysis.py -f -g {expdir}'

    # ✅ Combine into one full command
    full_cmd = f'{mkdir_cmd} && {cli} | tee -a "{expdir}/terminal.out" && {analysis} | tee -a "{expdir}/terminal.out"'

    # ✅ Show the generated command
    st.write("### Generated Command")
    st.code(full_cmd)

    # ✅ Run directly (we’re already in simulator root)
    result = subprocess.run(
        full_cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    # ✅ Show output
    st.write("### Simulation Output")
    if result.stdout:
        st.code(result.stdout)
    if result.stderr:
        st.error(result.stderr)
    st.success("Simulation completed successfully!")