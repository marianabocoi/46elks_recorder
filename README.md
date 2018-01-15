# Recording utility for [46elks](https://46elks.com/) phone nr. redirection

For a project I needed to record an automatic response I got from a robot. 
I redirected my phone through [46elks](https://46elks.com/) and that allowed 
me to configure a phone nr. that would redirect to my number. 

I would still have to answer the phone in order to get the recording.

## Tech 

- [46elks](https://46elks.com/) phone nr. redirection
- [Flask](http://flask.pocoo.org/) localhost server
- [jinja](http://jinja.pocoo.org/) templating
- [ngrok](https://ngrok.com/) expose the local server to the internet

## Setup

Create the phone nr. in [46elks](https://46elks.com/) and configure it with:
```
{"connect":"+467XXXXXXXX","recordcall":"http://XYZ.ngrok.io/record"}
```

Start this server locally running:
```
ELKS_USER="..." ELKS_KEY="..." python3 run.py

```

Run ngrok to get a link:
```
ngrok http 127.0.0.1:5000
```

Done!

## Listing/Downloading wav files: 

Just visit http://127.0.0.1:5000 or whatever link ngrok provided you.
