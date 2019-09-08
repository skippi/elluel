from hypothesis.strategies import (lists, tuples, just, text, integers)

bgm_info_field = (
    tuples(just("description"), text())
    | tuples(just("filename"), text())
    | tuples(just("mark"), text())
    | tuples(just("youtube"), text())
)

metadata_field = (
    tuples(just("album-artist"), text())
    | tuples(just("artist"), text())
    | tuples(just("title"), text())
    | tuples(just("year"), integers().map(str))
)
