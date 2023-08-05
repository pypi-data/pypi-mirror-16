.. _examples:

Examples
========

Simple setup
------------


.. code-block:: python

    import poort

    gate = poort.Gate()

    def application(environ, start_response):
        with gate(environ):
            request = gate.request

            if request.path == '/':
                response = poort.Response('Hallo world!')
            else:
                response = poort.Response('Not found.', status_code=404)

            return response(request, start_response)


Setup with router
-----------------


.. code-block:: python

    import avenue
    import pandora
    import poort


    router = avenue.Avenue()
    laborer = pandora.Laborer()
    gate = poort.Gate()


    @laborer.provider('params')
    def provide_params(kwargs):
        return gate.request.params


    @router.attach(path='/')
    def get(params):
        return poort.HtmlResponse('<p>Hallo %s.</p>' % params.get('name'))


    def application(environ, start_response):
        with gate(environ):
            response = router.solve(wrap=laborer.provide,
                                    **gate.request.as_dict())

            response(gate.request, start_response)
