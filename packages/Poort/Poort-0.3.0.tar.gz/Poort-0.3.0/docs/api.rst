.. _api:

API
===

.. py:currentmodule:: poort


Gate
----

.. autoclass:: Gate

   .. automethod:: setup


Request
-------

.. autoclass:: Request

   .. automethod:: as_dict
   .. automethod:: get_cookie


Response
--------


.. autoclass:: Response

   .. automethod:: set_cookie
   .. automethod:: del_cookie
   .. automethod:: __call__
   .. automethod:: get_status
   .. automethod:: get_body
   .. automethod:: prepare_response
   .. automethod:: respond

.. autoclass:: JsonResponse
.. autoclass:: HtmlResponse
.. autoclass:: TemplateResponse
.. autoclass:: WrappedTemplateResponse
.. autoclass:: FileResponse

   .. autoattribute:: size
   .. autoattribute:: mtime
   .. autoattribute:: etag

.. autofunction:: template_or_json_response
.. autofunction:: wrapped_template_or_json_response


CLI
---

.. autofunction:: poort.cli.start
.. autofunction:: poort.cli.stop
.. autofunction:: poort.cli.reload
.. autofunction:: poort.cli.scale
.. autofunction:: poort.cli.status
