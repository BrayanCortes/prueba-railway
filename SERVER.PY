import socketio
from prueba import probando


sio = socketio.Server(cors_allowed_origins='https://repo-prueba-vercel-omega.vercel.app/')
app = socketio.WSGIApp(sio)


"""
"""

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def message(sid, data):
    
    sio.emit('response', "XD", room=sid)

if __name__ == '__main__':
    import eventlet
    import eventlet.wsgi
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)