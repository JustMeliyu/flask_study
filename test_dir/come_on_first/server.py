#!/usr/bin/env python


from config import app
import os
from app_before import a
print "===getcwd:", os.getcwd()
print "===realpath:", os.path.dirname(os.path.realpath(__file__))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


# end
