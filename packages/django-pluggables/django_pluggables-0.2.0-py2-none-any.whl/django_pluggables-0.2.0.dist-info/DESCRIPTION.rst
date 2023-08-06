Django-Pluggables is a design pattern that endows reusable applications with a few additional features:

#. Applications can exist at multiple URL locations (e.g. http://example.com/foo/app/ and http://example.com/bar/app/).
#. Applications can be "parented" to other applications or objects which can then deliver specialized context information.
#. Posting form data and error handling can happen in locations that make sense to the user, as opposed to the common practice of using templatetags and standalone error or preview pages for form data processing.
#. Views and templates remain generic and reusable.

