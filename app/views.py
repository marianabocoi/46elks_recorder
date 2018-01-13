import os
import time

import requests
from flask import render_template, request, send_from_directory
from requests.auth import HTTPBasicAuth

from app import application


def maybe_make_static_dir():
    if not os.path.exists(application.static_folder):
        os.makedirs(application.static_folder)


@application.route('/record', methods=['POST'])
def index():
    print("Incoming message...")
    print("Keys:", list(request.form.keys()))

    callid = request.form.get("callid")
    to_nr = request.form.get("to")
    creation_datetime = request.form.get("created")
    wav = request.form.get("wav")

    print("callid:", callid)
    print("to:", to_nr)
    print("creation time:", creation_datetime)
    print("wav url:", wav)

    user = os.environ['ELKS_USER']
    password = os.environ['ELKS_KEY']

    print("Retrieving wav file {} ...".format(wav))
    maybe_make_static_dir()
    local_filename = callid + "_" + to_nr + "_" + creation_datetime + ".wav".replace(" ", "-")
    r = requests.get(wav, stream=True, auth=HTTPBasicAuth(user, password))
    with open(application.static_folder + "/" + local_filename, 'wb') as f:
        print("\tGetting chunks ...")
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                print("\t\twriting chunk ...")

    print("Done!")
    return "Thanks"


@application.route('/recordings/<path:filename>')
def download_file(filename):
    print("You wanna get:", filename, "from:", application.static_folder)
    return send_from_directory(application.static_folder, filename, as_attachment=True)


@application.route('/')
def show_time():
    maybe_make_static_dir()
    return render_template(
        'recordings.html',
        now=time.strftime("%c"),
        wavs=os.listdir(application.static_folder)
    )
