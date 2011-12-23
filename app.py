import os
import mimetypes

import flask


app = flask.Flask(__name__)

fst = lambda (x, y): x
get_mime_info = lambda x: mimetypes.guess_type('fake.%s' % x)
get_mime = lambda x: fst(get_mime_info(x))
render = lambda x, y: '%s\n' % (x if x else y)

usage = (lambda: 'Please do\n'
                 '    GET /extension\n'
                 'You may provide `?default=unknown` parameter for me to '
                 'render it if I\'ve no idea what your extension is.')


@app.route('/')
def home():
    return usage()


@app.route('/<extension>')
def doit_baby(extension):
    default = flask.request.args.get('default', 'unknown')
    return render(get_mime(extension), default)


if __name__ == '__main__':
    mimetypes.init()
    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', False))
    app.run(host='0.0.0.0', port=port, debug=debug)
