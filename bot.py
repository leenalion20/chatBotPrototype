from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import openai

openai.api_key = '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'

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    ai=openai.Completion.create(
        engine='davinci', 
        prompt="\nHumano: "+incoming_msg+"\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n","Humano:", "AI: "]
        )
    
    msg.body(ai.choices[0].text.strip())
    
    return str(resp)


if __name__ == '__main__':
    app.run()
    