From python:3.11-slim
WORKDIR /app
COPY . /app
RUN python --version
RUN pip install -r requirement.txt
RUN pip list 
CMD ["python","obs_scene_switch.py"]
