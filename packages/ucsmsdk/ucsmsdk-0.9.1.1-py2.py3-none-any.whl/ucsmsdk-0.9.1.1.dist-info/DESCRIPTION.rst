[![](https://img.shields.io/travis/CiscoUcs/ucsmsdk.svg)](https://travis-ci.org/CiscoUcs/ucsmsdk)
[![](https://ucspython.herokuapp.com/badge.svg)](https://ucspython.herokuapp.com)
[![](https://img.shields.io/pypi/v/ucsmsdk.svg)](https://pypi.python.org/pypi/ucsmsdk)
[![Code Health](https://landscape.io/github/CiscoUcs/ucsmsdk/master/landscape.svg?style=flat)](https://landscape.io/github/CiscoUcs/ucsmsdk/master)
[![Code Climate](https://codeclimate.com/github/CiscoUcs/ucsmsdk/badges/gpa.svg)](https://codeclimate.com/github/CiscoUcs/ucsmsdk)

# Python SDK for Cisco UCS

* Apache License, Version 2.0 (the "License") 
* Documentation: https://CiscoUcs.github.io/ucsmsdk_docs/

## Installation

The SDK can be installed using any of ways below,

### From pip:

Installs the last released version,

```
    pip install ucsmsdk
```

### From github:

Installs the latest top of the tree development version,

```
    # Install pip (skip if pip is already available):
    wget https://bootstrap.pypa.io/get-pip.py
    python get-pip.py

    git clone https://github.com/CiscoUcs/ucsmsdk.git
    cd ucsmsdk
    make install
```

## Documentation

* We have an extensive list of samples at https://github.com/ciscoucs/ucsmsdk_samples
* We encourage contriutions to the samples repository


## Community:

* We are on Slack - slack requires registration, but the ucspython team is open invitation to
  anyone to register [here](https://ucspython.herokuapp.com) 




History
-------

0.9.1.1 (2016-06-12)
---------------------

* Support for UCSM 2.2.7
* Simplified event handlers to a single `wait_for_event` method. `UcsEventHandler` internals are hidden from user.
* Support for showing progress for upload/download operations
* Support for multi-threading in SDK. An application can run multiple threads that can use SDK methods in parallel.
* Support for multiple parallel transactions via the `tag` parameter in `add_mo`, `set_mo`, `remove_mo`, `commit_mo`
* Fix for `convert_to_ucs_python` exception in some scenarios
* Fix for `convert_to_ucs_python` not displaying python script for Java6u45
* Fix for event handlers not trigerring for some events
* Added more unit and system tests
* Better Documentation

0.9.1.0 (2016-05-25)
---------------------

* Support for UCSM 3.1.1
* Support for Python 3.x
* Support for Comparing and Syncing Objects across Ucs Domains - `compare_ucs_mo` `sync_ucs_mo`
* Support for `filter_str` in `query_children` method
* Support to drill down into Managed Object Meta and Property Meta details - `get_meta_info`
* Support to monitor **any/all** change(s) in a ManagedObject with `UcsEventHandler`
* Fix for Unable to make unsecured connection when redirection was enabled on the server
* Fix for issues with the usage of force parameter in `Login` method
* Fix for `not` filter not generating filter request
* Fix for TechSupport not getting removed from server even when `remove_from_ucs=True`
* Fix for convert_to_ucs_python not redirecting output to a file
* Fix for convert_to_ucs_python not working correctly when `gui_log=True`
* More PEP8 compliance related fixes

0.9.0.0 (2015-01-11)
---------------------

* Python SDK for UCS server management and related automation
* Supports every Managed Object exposed by Ucs
* APIs for CRUD operations simplified
* Support for server side filters made simpler
* Support for eventhandlers
* Runtime memory usage is reduced
* Nosetests for unit testing
* Samples directory for more real world use cases
* Integrating the sphinx framework for documentation
* PEP8 Compliance


