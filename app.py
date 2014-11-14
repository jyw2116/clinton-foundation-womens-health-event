from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient

app = Flask(__name__)
twilio_account_sid = "ACCOUNT_SID"
twilio_token = "TOKEN"
client = TwilioRestClient(twilio_account_sid, twilio_token)

@app.route('/')
def ReturnForm():
  return render_template('form.html')

@app.route('/', methods=['POST'])
def FormPost():
  message = client.sms.messages.create(to="RECIPIENT_NUMBER", from_="SENDER_NUMBER",
                                     body=request.form['Message'])
  return render_template('success.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

