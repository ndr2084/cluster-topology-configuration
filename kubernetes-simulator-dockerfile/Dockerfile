FROM qzweng/kubernetes-scheduler-simulator:atc23

# Install Streamlit + YAML deps
RUN apt-get update && apt-get install -y python3-pip vim && \
    pip install --no-cache-dir streamlit pyyaml

# Copy your app code
COPY app.py /root/kubernetes-scheduler-simulator/app.py
COPY process_openb_dir.py /root/kubernetes-scheduler-simulator/process_openb_dir.py

# Debug: show contents during build
RUN ls -l /root/kubernetes-scheduler-simulator

# Set working directory so CMD runs in the correct folder
WORKDIR /root/kubernetes-scheduler-simulator

# Run Streamlit explicitly inside the correct folder
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

