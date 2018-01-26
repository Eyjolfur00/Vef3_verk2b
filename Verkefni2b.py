from bottle import *
import os

@route("/")
def index():
    return """
        <title>Verkefni2b</title>
        <meta charset="utf-8">
        <h1>Verkefni2b</h1>
        <h2>Veldu uppáhalds stafin þinn</h2>
        <a href="/1"><img src="pix/A.png"></a>
        <a href="/2"><img src="pix/B.png"></a>
        <a href="/3"><img src="pix/C.png"></a>
            """
@route('/pix/<filename>')
def server_static(filename):
    return static_file(filename, root="./pix")

@route('/<nr>')
def index(nr):
    if nr=='1':
        return """
            <title>Verkefni2b</title>
            <meta charset="utf-8">
            <h1>Verkefni2b</h1>
            <h2>Minn uppáhalds bókstafur er</h2>
            <img src="pix/A.png">
               """

    if nr=='2':
        return """
            <title>Verkefni2b</title>
            <meta charset="utf-8">
            <h1>Verkefni2b</h1>
            <h2>Minn uppáhalds bókstafur er</h2>
            <img src="pix/B.png">
               """
    if nr=='3':
        return """
            <title>Verkefni2b</title>
            <meta charset="utf-8">
            <h1>Verkefni2b</h1>
            <h2>Minn uppáhalds bókstafur er</h2>
            <img src="pix/C.png">
               """


run(host="0.0.0.0", port=os.environ.get('PORT'))
