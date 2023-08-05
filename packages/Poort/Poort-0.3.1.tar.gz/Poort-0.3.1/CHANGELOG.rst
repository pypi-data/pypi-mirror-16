Changelog
=========


Version 0.3.0
-------------

Released on Jul 4th 2016

- Added more documentation.
- Added `TemplateResponse.configure`.
- Added `TemplateResponse.get_template`.
- Added `TemplateResponse.render`.
- Fixed broken examples.
- Renamed `TemplateResponse.jinja` to `TemplateResponse.renderer`, **breaking change**.
- Updated requirements.
- Updated changelog.


Version 0.2.3
-------------

Released on Jun 30th 2016

- Added some documentation.
- Added `Request.ssl`.
- Updated `Request` to build from an empty enivonment.



Version 0.2.2
-------------

Released on Jun 30th 2016

- Updated cli to handle package configuration.


Version 0.2.1
-------------

Released on Jun 30th 2016

- Added **cli** support.
- Updated requirements.
- Fixed Flake8 problems.
- Fixed file headers.


Version 0.2.0
-------------

Released on Jun 24th 2016

- Added `WrappedTemplate`.
- Added *coveralls* badge.
- Added `mock` and `build_environ`.
- Updated some tests to be a bit more *generic*.
- Updated requirements.
- Fixed Flake8 problems.
- Fixed file headers.


Version 0.1.4
-------------

Released on Feb 8th 2016

- Added `json_default` with better JSON automation in `JsonResponse`.
- Updated tests.
- Fixed `'wsgi.input'` bug.


Version 0.1.3
-------------

Released on Feb 8th 2016

- Broken partial release, see `0.1.4`.


Version 0.1.2
-------------

Released on Feb 7th 2016

- Added `Gate`.
- Added `environ_from_dict`, replaces `environ_from_yaml`.
- Refactored `poort.py` into `request.py` and `response.py`.
- Updated tests, large overhaul with better code coverage.
- Updated requirements.
- Removed `environ_from_yaml`.
- Fixed auto-creation of `'wsgi.input'` on manual constructed environment.
- Fixed Python 2 & Python 3 coverage.


Version 0.1.1
-------------

Released on Feb 1st 2016

- Added tests and code coverage.
- Added `copy_request_environ`.
- Added `environ_from_yaml`.
- Updated requirements.


Version 0.1.0
-------------

Released on Feb 1st 2016

- Initial release
