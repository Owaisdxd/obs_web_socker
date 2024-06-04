# import obswebsocket.requests as obsrequests
import obs ,time , logging
from obswebsocket import obsws, requests, exceptions


def start_streaming(client):
    try:
        logging.info("Starting streaming")
        client.call(requests.StartStream())
        print("Started streaming")
        time.sleep(15)
    except Exception as e:
        logging.error(f"Error starting streaming: {e}")

def stop_streaming(client):
    try:
        logging.info("Stopping streaming in 15 seconds")
        time.sleep(10)
        client.call(requests.StopStream())
        print("Stopped streaming successfully")
        time.sleep(5)
        print("Successfully disconnected from the OBS server")
    except Exception as e:
        logging.error(f"Error stopping streaming: {e}")
def list_of_scenes( client):
    try:
        print("Please find the list of scenes below")
        scenes_list = client.call(requests.GetSceneList())
        scenes = scenes_list
        for s in scenes.getScenes():
            print(f"Input devices available : {s['sceneName']}")
            time.sleep(15)
    except exceptions.ConnectionFailure as e:
        logging.error(f"Connection failure: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def recording_streaming():
    try:
        print("We are going to recorde the streaming")
        request_recording = requests.StartRecord()
        client.call(request_recording)
        print("we are now recording the video")
        time.sleep(5)
        print("Video will be stopped after 30 seconds")
        time.sleep(30)
        print("We are not going to stop the video right now ")
        if client.call(requests.StopRecord()) :
            print("We have stopped the video")
        else:
            print("please refer to the issue bleow")
    except Exception as e:
        print("Issue -->", e)


def switching_scenes(client, scene):
    try:

        response = client.call(requests.SetCurrentProgramScene(sceneName=scene))
        print(f"Switching to scene: {scene}")
        if response.status:
            logging.info("Switched to scene successfully")
        else:
            logging.error(f"Failed to switch to the scene: {response.getError()}")
    except Exception as e:
        logging.error(f"An error occurred during scene switching: {e}")

host = "192.168.56.1"
port = 4455
#please provide  the path to password file for obs server
with open('./password', 'r') as file:
    password = file.read().strip()

logging.basicConfig(level=logging.DEBUG)

client = obsws(host, port, password)
print("Connecting to the OBS server")
time.sleep(3)
try:
    client.connect()
    version = client.call(requests.GetVersion())
    print(f"Version for the OBS server : {version}")
    logging.info("Connected to the OBS server")
    print("Connected to the server successfully")
    scene = "_scene_one"


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

    if client.connect:
        client.disconnect()
        print("Disconnected from the server")
        print("\n\t\t\tHellow World\t\t\t\n")



































































































































