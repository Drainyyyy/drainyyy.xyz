# -*- coding: utf-8 -*-

#  Covered by The MIT License
#
#  Copyright 2021 Jörg R.
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

from flask import Flask, redirect, render_template
from markupsafe import escape

from website import config

app = Flask(__name__)

# Non-login pages


@app.route("/")
def index():
    """TODO docs"""
    return render_template("index.html", base=config.BASE_URL)


@app.route("/about")
def about():
    """TODO docs"""
    return "About me"


@app.route("/contact")
def contact():
    """TODO docs"""
    return render_template("contact.html", base=config.BASE_URL, dc_server_id=config.DC_SERVER_ID, dc_user_id=config.DC_USER_ID,
                           contact_email=config.EMAIL_ADDRESS)


@app.route("/blog")
def blog():
    """TODO docs"""
    return "Personal blog"


@app.route("/blog/<article>")
def blog_article(article: str):
    """TODO docs"""
    # TODO check first if article exists and then show reading preview before showing the whole article
    article = article[:-5] if article.endswith(".html") else article
    return render_template(f"blog/{article}.html")


@app.route("/projects")
def projects():
    """TODO docs"""
    return "Overview about all projects"


@app.route("/projects/<specific_project>")
def project(specific_project: str):
    """TODO docs"""
    known_projects = {  # TODO move to database
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
    if escape(specific_project) not in known_projects:
        return redirect("/projects")
    return known_projects[escape(specific_project)]["full_name"]


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


@app.route("/r/<to>")
def dynamic_redirect(to: str):
    """TODO docs"""
    known_redirects = {  # TODO move to database
        "example": {"url": "https://www.example.com/", "third_party_service": None},
        "status": {"url": "https://stats.uptimerobot.com/qp0w9S1PzL", "third_party_service": "UptimeRobot"},
        "discord": {"url": "https://discord.gg/JR7tSXgM7Y", "third_party_service": "Discord"}
    }
    if to not in known_redirects or None:
        return redirect(config.BASE_URL)

    destination = known_redirects[to]
    if destination["third_party_service"] is not None:
        return render_template("redirect-warning.html", base=config.BASE_URL, url=destination["url"], service=destination["third_party_service"])
    return redirect(destination["url"])


# Login pages

@app.route("/login")
def login():
    """TODO docs"""
    # TODO add reCaptcha for login
    return "Login page"


@app.route("/", subdomain="aoi")
def aoi():
    """TODO docs"""
    return "administrative operations interface"


@app.route("/status", subdomain="aoi")
def aoi_status():
    """TODO docs"""
    # TODO get information from uptime robot api and project it on graphs -> Information from srv1 and srv2 and not only homepage
    return "aoi status page"


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
    if config.FLASK_SSH_ENABLED is True:
        app.config["ssl_context"] = "adhoc"


if __name__ == "__main__":
    init_app()
    app.run(**config.FLASK_RUN_CONFIG)
