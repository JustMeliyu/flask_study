# encoding:utf-8

from config import app
import os

print "===getcwd:", os.getcwd()
print "===realpath:", os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
