# -*- coding: utf-8 -*-

#  Covered by The MIT License (MIT)
#
#  Copyright 2021 Jörg Reinhardt (Drainyyy)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
#  (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
#  publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
#  CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

from flask import Flask, redirect

from website import config

app = Flask(__name__)

# Non-login pages


@app.route("/")
def index():
    """TODO docs"""
    return "Welcome to my website."


@app.route("/about")
def about():
    """TODO docs"""
    return "About me"


@app.route("/contact")
def contact():
    """TODO docs"""
    return "Contact me"


@app.route("/blog")
def blog():
    """TODO docs"""
    return "Personal blog"


@app.route("/projects")
def projects():
    """TODO docs"""
    return "Overview about all projects"


@app.route("/projects/<specific_project>")
def project(specific_project: str):
    """TODO docs"""
    known_projects = {
        "example": {"full_name": "The example project",
                    "keywords": ["example", "example.com", "example project"],
                    "short_desc": "An example project",
                    "long_desc": "A very detailed example project by myself.",
                    "source_url": "https://github.com/drainyyyy/example",
                    "project_website": "https://www.example.com",
                    "download_url": "https://www.example.com/download",
                    "maintained": True,
                    "languages": ["Css", "Html"],
                    "license": {"name": "MIT-License",
                                "url": "https://opensource.org/licenses/MIT"},
                    "creators": {"John Doe": "https://john-doe.example.com",
                                 "Johnny Doe": "https://johnny-doe.example.com"},
                    }
    }
    if specific_project not in known_projects:
        return redirect("/projects")
    return known_projects[specific_project]["full_name"]


@app.route("/status")
def status():
    """TODO docs"""
    return "uptime robot status"


@app.route("/imprint")
def imprint():
    """TODO docs"""
    return "imprint"


@app.route("/privacy-policy")
def privacy():
    """TODO docs"""
    return "privacy policy"


@app.route("/<to>", subdomain="re")  # TODO NOT WORKING -> redirect if unknown only to re.localhost instead of localhost
def dynamic_redirect(to: str):
    """TODO docs"""
    known_redirects = {
        "example": {"url": "https://www.example.com/"}
    }
    if to not in known_redirects:
        return redirect("/")
    return redirect(known_redirects[to]["url"])


# Login pages

@app.route("/login")
def login():
    """TODO docs"""
    return "Login page"


@app.route("/", subdomain="aoi")
def aoi():
    """TODO docs"""
    return "administrative operations interface"


@app.route("/", subdomain="cms")
def content_management_system():
    """TODO docs"""
    return "cms with integrated cdn"


@app.route("/chat", subdomain="ypc")
def chat():
    """TODO docs"""
    return "redirect to ypc instance of I ever get it finished"


def init_app():
    """TODO docs"""
    app.config["SERVER_NAME"] = f"{config.FLASK_RUN_CONFIG['host']}:{config.FLASK_RUN_CONFIG['port']}"


if __name__ == "__main__":
    init_app()
    app.run(**config.FLASK_RUN_CONFIG)
