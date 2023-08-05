Tools to work help with inspecting function calls
-------------------------------------------------

The functions `update_wrapper` and `wraps` improve on
`functools.update_wrapper` and `functools.wraps` by persisting information
about function signatures. The function `get_argspec` is similar to
`inspect.get_argspec`, except it first tries to use the metadata provided
by `update_wrapper`.

The function `get_callargs` is similar to `inspect.getcallargs`, except
that

* it can access the metadata created by `update_wrapper`
* it does not raise when a call is illegal but rather makes a best
  guess, which makes it suitable for logging and error handling in
  decorators.
