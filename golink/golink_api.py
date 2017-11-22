#!/usr/bin/env python
from golink import golink
from flask import Flask, redirect


application = Flask(__name__)
golinkobj = golink()

@application.route('/', defaults={'path': ''}, methods=['GET'])
@application.route('/<path:path>', methods=['GET'])
def redirecturl(path):
    sanpath = path.strip("/")
    linkto = golinkobj.fetch(sanpath)
    print linkto
    if not linkto:
        return "No link found for go link {0}".format(sanpath)
    else:
        return redirect(linkto)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)
