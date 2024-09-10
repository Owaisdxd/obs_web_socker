# OBS Python Integration

This repository contains a Python script that interacts with Open Broadcaster Software (OBS) using the OBS WebSocket API. The script includes functionalities to start and stop streaming, list available scenes, record the stream, and switch between scenes. This can be particularly useful for streamers and content creators looking to automate their OBS setup.

## Features

- **Start Streaming**: Initiates a streaming session.
- **Stop Streaming**: Stops the current streaming session.
- **List Scenes**: Retrieves and displays a list of available scenes.
- **Record Streaming**: Starts and stops recording of the stream.
- **Switch Scenes**: Changes to a specified scene.

## Installation

### Prerequisites

- Python 3.6 or higher
- OBS Studio with the OBS WebSocket plugin installed

### Dependencies

Install the required Python libraries using `pip`:

```bash
pip install obs-websocket-py
