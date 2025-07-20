from flask_socketio import SocketIO
from openai import OpenAI
from flask_cors import CORS

socketio = SocketIO(cors_allowed_origins="*")
openai_client = OpenAI()
cors = CORS()
