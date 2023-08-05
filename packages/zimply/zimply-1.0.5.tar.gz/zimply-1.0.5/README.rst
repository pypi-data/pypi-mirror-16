**ZIMply** is an easy to use, offline reader for `Wikipedia <https://www.wikipedia.org>`__ which provides access to the offline `Wikipedia <https://www.wikipedia.org>`__ through any ordinary browser. **ZIMply** is written entirely in `Python <https://www.python.org>`__ and, as the name implies, relies on `ZIM files <http://www.openzim.org/wiki/OpenZIM>`__. Each ZIM file is a bundle containing thousands of articles, images, etc. as found on websites such as `Wikipedia <https://www.wikipedia.org>`__. The format is made popular by `Kiwix <http://www.kiwix.org>`__, which is a program to read such files offline on your device. As indicated, **ZIMply** differs from `Kiwix <http://www.kiwix.org>`__ in that it provides access through the browser. It accomplishes this by running its own HTTP server. This furthermore makes it easy to install **ZIMply** on one device (a *server*, such as a `Raspberry Pi <https://www.raspberrypi.org/products/>`__) and access it on others (the *clients*). To install Python3 on a `Raspbian lite distribution <https://www.raspberrypi.org/downloads/raspbian/>`__ it suffices to install the following packages:

.. code:: bash

    sudo apt-get -qq python3 python3-setuptools python3-dev python3-pip

**ZIMply** depends on `gevent <http://www.gevent.org>`__ (for networking), `falcon <https://falconframework.org>`__ (for the web service), and `mako <http://www.makotemplates.org>`__ (for templating). The easiest way to install these dependencies is by using:

.. code:: bash

    sudo pip install gevent falcon mako

When you have both Python 2.* and Python 3.* installed on your system, you may need to replace `pip` with `pip3` depending on your setup.

**ZIMply** can be used as-is and does not require any configuration out of the box. It suffices to delete the `wiki.zim` file and replace it with your ZIM file of choice which you rename to `wiki.zim` (**do delete the index.idx** if it has already been created). A large collection of ZIM files is available from http://download.kiwix.org/zim/ . If you run **ZIMply** on your local system, you can access it by visiting http://localhost:9454 - spelling out as :WIKI on a keypad. To access **ZIMply** from another system, you need to know the IP address of the system that is running **ZIMply**. You can then easily access it by visiting http://ip_address:9454 where you replace ip_address with the actual IP address.

The first time you run **ZIMply** the index file is created. **This can take some time**. Unless you see error messages, you can assume that it all works as planned and **ZIMply** will notify you as soon as the index is fully created. The largest ZIM file (the full English Wikipedia) takes about half an hour to index on a core i7 processor, and can take over half a day on a Raspberry Pi Zero. Creating the index is a step that only needs to be done once though, and subsequent restarts of **ZIMply** will only take a matter of seconds. **ZIMply** is heavily optimised, and *will* run comfortably on a Raspberry Pi Zero.

To modify the standard parameters, or use **ZIMply** in your own project, you need to modify or delete the last rule in `zimply.py` which is used to start the server. **ZIMply** comes with a very permissive license, so you can do whatever you want with the source code as long as you keep the copyright notice intact.