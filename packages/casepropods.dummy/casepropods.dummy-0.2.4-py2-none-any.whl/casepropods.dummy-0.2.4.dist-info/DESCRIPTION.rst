casepropods.dummy
==================

Example casepro data pod returning statically configured data.

Install
~~~~~~~

.. code-block::

  $ pip install casepropods.dummy

Usage
~~~~~

In casepro's settings file, add the pod as an installed app, and configure the pods that you would like to show in the UI:

.. code-block:: python

  INSTALLED_APPS += ('casepropods.dummy.plugin.DummyPodPlugin',)

  PODS = [{
      # maps this pod to the dummy pod type
      'label': 'dummy_pod',

      # title of the pod to show in the ui
      'title': 'Maternal Health Info',

      # static data to show as item in the ui for this pod
      # (only relevant to the dummy pod type)
      'data': {
          'items': [{
              'name': 'EDD',
              'value': '2015-07-18'
          }, {
              'name': 'Clinic Code',
              'value': '2034 6524 6421'
          }]
      }
  }]


