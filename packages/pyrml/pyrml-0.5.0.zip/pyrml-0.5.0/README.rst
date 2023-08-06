Python RainBot Module Library
=============================

Proper documentation and specifications will be coming with RainBot v0.5.0 (This includes a working link to library web page)

To install
----------

.. code:: python

    pip install pyrml

To generate a simple scaffold (assuming rainbot is installed)

.. code:: python

    rainbot -m py YourModuleName

Example Usage
-------------

#### Simple

.. code:: python

    from pyrml import Module

    m = Module("Echo", "A simple echo module")

    @m.command("echo")
    def echo(msg, args):
        m.say(msg["Params"][0], " ".join(args))

    m.register()

.. code:: python

    from pyrml import Module

    class Echo(Module):
        def __init__(self, name, desc):
            Module.__init__(self, name, desc)

        def echo(self, msg, args):
            self.say(msg["Args"][0], " ".join(args))

    if __name__ == '__main__':
        m = Echo("Echo", "An echo mdoule")

        m.add_command("echo", {
            "Help": "Repeats arguments",
            "Fun": m.echo
        })

        m.register()
