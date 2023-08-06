# Stampery Python
 Stampery API for Python. Notarize all your data using the blockchain!

# Usage
```python

from stampery import Stampery

client = Stampery('2d4cdee7-38b0-4a66-da87-c1ab05b43768', 'prod')

def on_ready():
    digest = client.hash("Hello, blockchain!")
    client.stamp(digest)

def on_proof(hash, proof):
    print("Received proof for")
    print(hash)
    print("Proof")
    print(proof)

def on_error(err):
    print("Woot: %s" % err)

client.on("error", on_error)
client.on("proof", on_proof)
client.on("ready", on_ready)

client.start()


 ```
## Installation
```python
pip install stampery
```

# Official implementations
- [NodeJS](https://github.com/stampery/node)
- [PHP](https://github.com/stampery/php)
- [Ruby](https://github.com/stampery/ruby)
- [Python](https://github.com/stampery/python)
- [Elixir](https://github.com/stampery/elixir)

# Feedback

Ping us at support@stampery.com and we’ll help you! 😃


## License

Code released under
[the MIT license](https://github.com/stampery/js/blob/master/LICENSE).

Copyright 2016 Stampery
