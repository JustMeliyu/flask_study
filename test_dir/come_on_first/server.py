#!/usr/bin/env python


from config import app
# from werkzeug.contrib.fixers import LighttpdCGIRootFix
# app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# end
