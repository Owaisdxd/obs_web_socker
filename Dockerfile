From python:3.11-slim
WORKDIR /app
COPY . /app
CMD python --version
CMD pip install -r requirement.txt
CMD pip list 
CMD python obs_scene_switch.py
