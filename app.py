from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from comparabot import ask, append_interaction_to_chat_log

app = Flask(__name__)

# if for some reason your conversation with ComparaBot gets weird, change the secret key
app.config['SECRET_KEY'] = 'naKlRJsgw8'


@app.route('/comparabot', methods=['POST'])
def comparabot():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log[:1500])
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log[:1500])
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)


if __name__ == '__main__':
    app.run(debug=True)
