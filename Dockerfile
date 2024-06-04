From python:3.11-slim
WORKDIR /app
COPY . /app
RUN python --version
RUN pip install -r requirement.txt
RUN pip list 
RUN python /app/obs_scene_switch.py
