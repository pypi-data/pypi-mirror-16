[![Build Status](https://travis-ci.org/kespindler/albatross.svg?branch=master)](https://travis-ci.org/kespindler/albatross)

# Albatross

A modern, fast, simple, natively-async web framework. (Python3.5 only)

```python
from albatross import Server
import asyncio


class Handler:
    async def on_get(self, req, res):
        await asyncio.sleep(0.1)
        res.write('Hello, %s' % req.args['name'])


app = Server()
app.add_route('/(?P<name>[a-z]+)', Handler())
app.serve()
```

### Notes for Usage

For now (pre 1.0.0), I'm not guaranteeing the API stays the same. In particular, the add_route will
likely change from regex to `{arg}`-based. But reach out if you want to use this, as I'm happy to
incorporate your feedback!

## Install

    pip3 install albatross3

## Features

- You can read the entire codebase in about 30 minutes.

- It's natively async

- This works with the `uvloop` project, to make your server fast!


