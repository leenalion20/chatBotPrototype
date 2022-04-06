from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import openai as ai

#Llave de acceso a la API de OpenAI
ai.api_key = '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'

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    mensaje_recibido = request.values.get('Body', '').lower()
    respuesta = MessagingResponse()
    mensaje = respuesta.message()
    
    robot=ai.Completion.create(
        engine='davinci', 
        prompt="\nHumano: "+mensaje_recibido+"\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n","Humano:", "AI: "]
        )
    
    mensaje.body(robot.choices[0].text.strip())
    
    return str(respuesta)


if __name__ == '__main__':
    app.run()
    