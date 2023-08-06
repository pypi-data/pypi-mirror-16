The :py:mod:`protostrings` distribution provides string-like objects with functional aspects, integrating well with the standard string type. Each :py:mod:`protostring` simply wraps a function dictating specific behaviours within the overarching constraints of the type. Due to their dynamic nature, features such as length or indexing are not supported. Memoizing variants of each :py:mod:`protostring` type are provided. The :py:mod:`inspect` module is required only for visualing :py:mod:`protostrings` (:py:meth:`~.LazyString.__str__`, :py:meth:`~.LazyString.__repr__`, :py:meth:`~.LazyString.pprint`), and is thus a soft requirement.

>>> protostring = "alpha " + ((lazy_str + context_str_right) + context_str_both) + " omega"
>>> protostring.pprint(False)
LazyString                      (...)
    LazyString                  (...)
        str                     'alpha '
        LazyString              (...)
            ContextString       (...)
                LazyString      ()
                ContextString   (...)
            ContextString       (...)
    str                         ' omega'
>>> str(protostring)
'alpha @@everything else@@ omega'
>>> "...alpha " + (context_str_right + context_str_both) + " omega..."
'...alpha (everything else) omega...'

