# Lab 2 Solution - UrlCount

## Solution

UrlCount scans the two Wikipedia pages, pulls out every `href="..."` link, and prints the
ones that appear more than 5 times with their counts. `UrlMapper` finds each link and
outputs it with a count of 1. It uses the regular expression `href="([^"]*)"`, which
captures the URL inside the quotation marks and can find multiple links on the same
line. Hadoop then sorts and groups matching links together, and `UrlReducer` adds their
counts and filters out any links that appeared 5 times or less. In the Java version,
the combiner only creates partial sums; the final filtering is left to the reducer so
counts coming from different mapper tasks are not accidentally discarded. The Java
and Python streaming versions follow the same overall process and produce the same
type of output.

## Software needed

Hadoop 3.3.6 (or whatever is on the `dataproc` image), a JDK to compile the Java
version, and Python 3 for the streaming version. No outside libraries, just
`java.util.regex` and `re`. Run `make prepare` first, then `make urlrun` for the Java
version or `make urlstream` for the streaming one. `make urltest` pipes the mapper and
reducer together by hand, which is handy for debugging. The Makefile automatically
uses Dataproc's Hadoop streaming jar when it is running on the cluster.

## Resources used

The Hadoop MapReduce tutorial for 3.3.6, Michael Noll's "Writing an Hadoop MapReduce
Program in Python" for the streaming API, the Java `Pattern` and `Matcher` documentation,
and the provided `WordCount1.java`, `Mapper.py`, and `Reducer.py` as starting points.
Collaborators: TODO.

## Execution time comparison

Both tests used `e2-standard-2` machines and the same two Wikipedia input files. The
Java version took 78.42 seconds with 2 workers and 74.85 seconds with 4 workers, while
the Python streaming version took 99.44 seconds with 2 workers and 100.51 seconds with
4 workers. All four runs produced the same output. Adding workers only made the Java
run about 3.57 seconds faster and made the streaming run slightly slower. This was not
too surprising because the input was small: job startup and task scheduling took up
most of the time, and the Java job had only two map tasks, so it could not make much
use of the extra workers. The larger cluster also started more reducer tasks, which
added overhead for very little data.
