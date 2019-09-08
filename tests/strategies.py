from datetime import date
from hypothesis.strategies import lists, tuples, just, text, integers, dates

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

source_field = (
    tuples(just("client"), text())
    | tuples(just("date"), dates().map(date.isoformat))
    | tuples(just("structure"), text())
    | tuples(just("version"), text())
)
