from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, flash
from GetMapsFromLayer import getMapsFromLayer
import pandas as pd
import json

views = Blueprint(__name__, "views")



@views.route("/")
def home():
    return render_template("index.html")

@views.route("/trigger_script", methods=["GET", "Post"])
def trigger_script():
    global service_dict
    global token
    global service_lst

    if request.method == "POST":
        portal_url = request.form.get("PortalURL")
        username = request.form.get("Username")
        pw = request.form.get("Password")
        url = request.form.get("URL")
        if 'service_dict' not in locals():
            service_dict, token = getMapsFromLayer(portal_url, username, pw)
        session.permanent = True
        session["service_dict"] = service_dict


        service_lst = sorted(list(service_dict.keys()))

        if url in service_dict:
            layer_dependencies = service_dict[url]#next(iter(service_dict))]


            df = pd.DataFrame(layer_dependencies)
            df.to_csv("downloads\\Results.csv")

            return render_template(
                "index.html",
                data=layer_dependencies, service_dict=service_dict, token=token)
        else:
            return render_template(
                "index.html",
                services=service_lst, service_dict=service_dict)

    else:
        return render_template("index.html")
    #return jsonify(layer_dependencies)

@views.route("/filter", methods=["GET", "Post"])
def filter():
    if request.method == "POST":
        url = request.form.get("service")
        #service_dict = json.loads(request.form.get("service_dict"))
        layer_dependencies = service_dict[url]
        return render_template(
            "index.html",
            data=layer_dependencies, services=service_lst, selected_service=url)
    return render_template(
            "index.html")