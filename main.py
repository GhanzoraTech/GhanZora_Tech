from flask import Flask, render_template, Response, request

app = Flask(__name__)


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# SITEMAP
# =========================

@app.route("/sitemap.xml")
def sitemap():

    base_url = request.url_root.rstrip("/")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>{base_url}/</loc>
    </url>

</urlset>
"""

    return Response(
        sitemap_xml,
        mimetype="application/xml"
    )


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    app.run(debug=True)