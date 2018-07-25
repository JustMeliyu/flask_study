#!/usr/bin/env python

from config import app


@app.before_request
def a():
    print("111===111")
