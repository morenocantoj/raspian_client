import websocket
import json
import engage_light
import turnoff_light

try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    response_json = json.loads(message)
    if response_json['action'] == 'light':
        if response_json['value'] == True:
            # turn on light
            engage_light.engage(response_json['port'])
        else:
            # turn off light
            turnoff_light.turnoff(response_json['port'])
                
def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(json.dumps({'type': 'CONNECTION', 'msg': '1'}))
        print("Conexion establecida con el servidor")
        while True:
            ws.send(json.dumps({'type': 'PING', 'msg': 'Keep alive Heroku!!'}))
            time.sleep(30)
        time.sleep(1)
        ws.send(json.dumps({'type': 'CLOSE', 'msg': '1'}))
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://mighty-reef-55430.herokuapp.com/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
