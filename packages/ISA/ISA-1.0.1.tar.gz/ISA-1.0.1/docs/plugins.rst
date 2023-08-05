.. _plugins:

=======
Plugins
=======

There are a lot of measurement tools for specific servers. Therefore, ISA has a plugin structure so that it is easy to add new monitors. A plugin file is named as follows: `plugin_pluginname.py`. Then, you can call ISA with a list of plugins and you can add `pluginname` to the comma separated list of the plugins argument of ISA.

`````````
Structure
`````````
It is very easy to create a new plugin. The plugin script should have the following structure:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin(...)

   class MyPlugin(Plugin):
      def collect(self, server):
         server.execute(...)

The plugin is first initialized. You can use arguments from the original ISA call. For example, suppose ISA is called as follows:

.. code-block:: text

   isa nodes.ini --timeout 3

Then you can use `args.timeout` to refer to the `timeout` argument:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin(args.timeout)

   class MyPlugin(Plugin):
      def __init__(self, timeout):
         print("I am called with timeout=%s" % timeout)

      def collect(self, server):
         server.execute(...)

The `collect` method should return either a list of dictionaries or a dictionary which specifies the collected data in key-value pairs:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin()

   class MyPlugin(Plugin):
      def collect(self, server):
         return {
            'temperature': 25.0
         }

Or you can use a list:
.. code-block:: python

   def plugin_init(args):
      return MyPlugin()

   class MyPlugin(Plugin):
      def collect(self, server):
         return [{
            'sensor': 'A',
            'temperature': 15.0
         }, {
            'sensor': 'B',
            'temperature': 35.0
         }]