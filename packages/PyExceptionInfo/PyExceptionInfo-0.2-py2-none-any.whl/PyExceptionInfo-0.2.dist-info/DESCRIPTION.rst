PyExceptionInfo: Easily lookup your errors on the web
=====================================================

# Exceptions happen

Exceptions do happen and we all have seen it more than once while we are
developing our code. Mostly we would want to know more about the exception or
error that we generated and the logical step that follows up is to inspect our
code and still if we are stuck, we might lookup on the internet.

PyExceptionInfo helps you on the last part. Use it in your exception handling,
and it will automatically lookup the exception on Google for you.

## Installation

Use pip for Installation

    pip install PyExceptionInfo

## Example

Look up the test.py source code for usage

    import PyExceptionInfo

    try:
        # Some exception here
    except Exception as e:
        PyExceptionInfo.getInfo(e)

Thanks!


