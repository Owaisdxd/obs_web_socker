import os
import time
import logging
from obswebsocket import obsws, requests, exceptions

def start_streaming(client):
    """
    Starts the streaming session on the OBS server.
    
    Args:
        client (obsws): The OBS WebSocket client instance.
    
    Logs the process of starting the stream and handles exceptions that may occur.
    """
    try:
        logging.info("Starting streaming")
        client.call(requests.StartStream())
        print("Started streaming")
        time.sleep(15)
    except Exception as e:
        logging.error(f"Error starting streaming: {e}")

def stop_streaming(client):
    """
    Stops the streaming session on the OBS server after a delay.
    
    Args:
        client (obsws): The OBS WebSocket client instance.
    
    Logs the process of stopping the stream and handles exceptions that may occur.
    """
    try:
        logging.info("Stopping streaming in 15 seconds")
        time.sleep(10)
        client.call(requests.StopStream())
        print("Stopped streaming successfully")
        time.sleep(5)
        print("Successfully disconnected from the OBS server")
    except Exception as e:
        logging.error(f"Error stopping streaming: {e}")

def list_of_scenes(client):
    """
    Retrieves and prints the list of available scenes from the OBS server.
    
    Args:
        client (obsws): The OBS WebSocket client instance.
    
    Handles connection failures and other exceptions.
    """
    try:
        print("Please find the list of scenes below")
        scenes_list = client.call(requests.GetSceneList())
        scenes = scenes_list
        for s in scenes.getScenes():
            print(f"Scene available: {s['sceneName']}")
            time.sleep(15)
    except exceptions.ConnectionFailure as e:
        logging.error(f"Connection failure: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def recording_streaming(client):
    """
    Starts recording the stream and stops it after a specified duration.
    
    Args:
        client (obsws): The OBS WebSocket client instance.
    
    Handles the process of starting and stopping recording, and logs any issues that occur.
    """
    try:
        print("Starting recording the stream")
        client.call(requests.StartRecord())
        print("Recording the video")
        time.sleep(5)
        print("Video will be stopped after 30 seconds")
        time.sleep(30)
        print("Stopping the recording")
        if client.call(requests.StopRecord()):
            print("Stopped the recording successfully")
        else:
            print("Please refer to the issue below")
    except Exception as e:
        print("Issue -->", e)

def switching_scenes(client, scene):
    """
    Switches to the specified scene on the OBS server.
    
    Args:
        client (obsws): The OBS WebSocket client instance.
        scene (str): The name of the scene to switch to.
    
    Logs the result of the scene switch and handles any errors.
    """
    try:
        response = client.call(requests.SetCurrentProgramScene(sceneName=scene))
        print(f"Switching to scene: {scene}")
        if response.status:
            logging.info("Switched to scene successfully")
        else:
            logging.error(f"Failed to switch to the scene: {response.getError()}")
    except Exception as e:
        logging.error(f"An error occurred during scene switching: {e}")

# Configuration for OBS WebSocket
host = os.getenv("OBS_HOST", "localhost")  # Default to 'localhost' if environment variable is not set
port = int(os.getenv("OBS_PORT", 4455))  # Default to 4455 if environment variable is not set
password = os.getenv("OBS_PASSWORD", "")  # Password should be set in environment variables

logging.basicConfig(level=logging.DEBUG)

# Initialize OBS WebSocket client
client = obsws(host, port, password)
print("Connecting to the OBS server")
time.sleep(3)

try:
    client.connect()
    version = client.call(requests.GetVersion())
    print(f"Version for the OBS server: {version}")
    logging.info("Connected to the OBS server")
    print("Connected to the server successfully")

    scene = "_scene_one"

    # Perform operations
    start_streaming(client)
    list_of_scenes(client)
    switching_scenes(client, scene)
    recording_streaming()
    time.sleep(30)
    stop_streaming(client)

except exceptions.ConnectionFailure as e:
    logging.error(f"Failed to connect to OBS: {e}")

except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")

finally:
    if client.is_connected():
        client.disconnect()
        print("Disconnected from the server")
        print("\n\t\t\tHello World\t\t\t\n")
