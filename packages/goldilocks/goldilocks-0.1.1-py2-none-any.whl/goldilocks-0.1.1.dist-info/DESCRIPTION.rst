==========
Goldilocks
==========

.. image:: https://badge.fury.io/py/goldilocks.png
    :target: http://badge.fury.io/py/goldilocks

.. image:: https://travis-ci.org/SamStudio8/goldilocks.png?branch=master
        :target: https://travis-ci.org/SamStudio8/goldilocks

.. image:: https://coveralls.io/repos/SamStudio8/goldilocks/badge.png?branch=master
        :target: https://coveralls.io/r/SamStudio8/goldilocks

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/SamStudio8/goldilocks
   :target: https://gitter.im/SamStudio8/goldilocks?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Locating genomic regions that are "just right".

* Documentation: http://goldilocks.readthedocs.org.


What is it?
-----------

**Goldilocks** is a Python package providing functionality for locating 'interesting'
genomic regions for some definition of 'interesting'. You can import it to your
scripts, pass it sequence data and search for subsequences that match some criteria
across one or more samples.

Goldilocks was developed to support our work in the investigation of quality
control for genetic sequencing. It was used to quickly locate
regions on the human genome that expressed a desired level of variability,
which were "just right" for later variant calling and comparison.

The package has since been made more flexible and can be used to find regions
of interest based on other criteria such as GC-content, density of target k-mers,
defined confidence metrics and missing nucleotides.


What can I use it for?
----------------------

Given some genetic sequences (from one or more samples, comprising of one or more
chromosomes), Goldilocks will shard each chromosome in to subsequences of a
desired size which may or may not overlap as required. For each chromosome from
each sample, each subsequence or 'region' is passed to the user's chosen strategy.

The strategy simply defines what is of interest to the user in a language that
Goldilocks can understand. Goldilocks is currently packaged with the following
strategies:

============================      ==================
Strategy                          Census Description
============================      ==================
GCRatioStrategy                   Calculate GC-ratio for subregions across the
                                  genome.
NucleotideCounterStrategy         Count given nucleotides for subregions across
                                  the genome.
MotifCounterStrategy              Search for one or more particular motifs of
                                  interest of any and varying size in subregions
                                  across the genome.
ReferenceConsensusStrategy        Calculate the (dis)similarity to a given
                                  reference across the genome.
PositionCounterStrategy           Given a list of base locations, calculate
                                  density of those locations over subregions
                                  across the genome.
============================      ==================

Once all regions have been 'censused', the results may be sorted by one of four
mathematical operations: `max`, `min`, `median` and `mean`. So you may be interested
in subregions of your sequence(s) that feature the most missing nucleotides, or
subregions that contain the mean or median number of SNPs or the lowest GC-ratio.


Why should I use it?
--------------------

Goldilocks is hardly the first tool capable of calculating GC-content across a
genome, or to find k-mers of interest, or SNP density, so why should you use it
as part of your bioinformatics pipeline?

Whilst not the first program to be able to conduct these tasks, it is the first
to be capable of doing them all together, sharing the same interfaces. Every strategy
can quickly be swapped with another by changing one line of your code. Every strategy
returns regions in the same format and so you need not waste time munging data to
fit the rest of your pipeline.

Strategies are also customisable and extendable, those even vaguely familiar with
Python should be able to construct a strategy to meet their requirements.

Goldilocks is maintained, documented and tested, rather than that hacky perl
script that you inherited years ago from somebody who has now left your lab.


Requirements
------------
To use;

* numpy
* matplotlib (for plotting)

To test;

* tox
* pytest

For coverage;

* nose
* python-coveralls

Installation
------------

::

    $ pip install goldilocks


Citation
--------

Please cite us so we can continue to make useful software! ::

    Nicholls, S. M., Clare, A., & Randall, J. C. (2016). Goldilocks: a tool for identifying genomic regions that are "just right." Bioinformatics (2016) 32 (13): 2047-2049. doi:10.1093/bioinformatics/btw116

::

    @article{Nicholls01072016,
        author = {Nicholls, Samuel M. and Clare, Amanda and Randall, Joshua C.}, 
        title = {Goldilocks: a tool for identifying genomic regions that are ‘just right’},
        volume = {32}, 
        number = {13}, 
        pages = {2047-2049}, 
        year = {2016}, 
        doi = {10.1093/bioinformatics/btw116}, 
        URL = {http://bioinformatics.oxfordjournals.org/content/32/13/2047.abstract}, 
        eprint = {http://bioinformatics.oxfordjournals.org/content/32/13/2047.full.pdf+html}, 
        journal = {Bioinformatics} 
    }

License
-------
Goldilocks is distributed under the MIT license, see LICENSE.


History
=======

0.1.1 (2016-07-07)
------------------
* Updated citation.
    Please cite us! <3
* [PR:ar0ch] Add lowercase matching in GCRatioStrategy
    Fixes 'feature' where lowercase letters are ignored by GCRatioStrategy.

0.1.0 (2016-03-08)
------------------
* Goldilocks is published software!

0.0.83-beta
-------------------
* `-l` and `-s` CLI arguments and corresponding `length` and `stride` parameters
  to `Goldilocks` constructor now support SI suffixes: `K`, `M`, `G`, `T`.
  `util` module contains `parse_si_bp` used to parse option strings and return
  the number of bases for length and stride.
* Add length and stride to x-axis label of plots.
* Add `ignore_query` option to `plot` to override new default behaviour of plot
  that only plots points for regions remaining after a call to `query`.
* Remove `profile` function, use `plot` with `bins=N` instead.
* Add binning to `plot` to reduce code duplication.
* Add `chrom` kwarg to `plot` to allow plotting of a single chromosome across
  multiple input genomes.
* Fix support for plotting data from multiple contigs or chromosomes of a single
  input genome when provided as a FASTA.
* Add `ignore_query` kwarg to `plot` for ignoring the results of a query on
  the `Goldilocks` object when performing a plot afterwards.
* Bins no longer have to be specified manually, use `bins=N`, this will create
  N+1 bins (a special 0 bin is reserved) between 0 and the largest observed
  value unless `bin_max` is also provided.
* Bins may have a hard upper limit set with `bin_max`. This will override the
  default of the largest observed value regardless of whether `bin_max` is smaller.
* Plots can now be plotted proportionally with `prop=True`.
* Improve labels for plotting.
* Reduce duplication of plotting code inside `plot`.
* Share Y axis across plot panels to prevent potentially misleading default plots.
* Reduce duplication of code used for outputting metadata:
* Add `fmt` kwarg to `export_meta` that permits one of:
    * bed
        BED format (compulsory fields only)
    * circos
        A format compatible with the circos plotting tool
    * melt
        A format that will suit import to an R dataframe without the need
        for additional munging with reshape2
    * table
        A plain tabular format that will suit for quick outputs with
        some munging
* Remove `print_melt`, use `export_meta` with `fmt=melt`.
* Add `is_pos_file` kwarg to Goldilocks, allows user to specify position based
  variants in the format `CHR\tPOS` or `CHR:POS` in a newline delimited file.
* Changed required `idx` key to `file` in sequence dictionaries.
* Added custom strategy and plotting examples to the documentation.
* The `Goldilocks` class is now imported as `from goldilocks import Goldilocks`.
* The `textwrap.wrap` function is used to write out FASTA more cleanly.
* A serious regression in the parsing of FASTA files introduced by v0.0.80 has
  been closed.
* Improved plotting functionality for co-plotting groups, tracks of chromosome
  has been introduced. Tracks can now be plotted together on the same panel by
  providing their names as a list to the `tracks` keyword.
* `reset_candidates` allows users to "reset" the Goldilocks object after a
  query or sort has been performed on the regions.

0.0.82 (2016-01-29)
-------------------
* Changed example to use `MotifCounterStrategy` over removed `KMerCounterStrategy`.
* Fix runtime `NameError` preventing `PositionCounterStrategy` from executing correctly.
* Fix runtime `NameError` preventing `ReferenceConsensusStrategy` from executing correctly.
* Add default `count` track to `PositionCounterStrategy` to prevent accidental
  multiple counting issue encountered when couting with the `default` track.
* Add LICENSE
* Paper accepted for press!

0.0.81 (2016-01-29)
-------------------
* Fix versioning error.

0.0.80 (2015-08-10)
-------------------
* Added multiprocessing capabilities during census step.
* Added a simple command line interface.
* Removed prepare-evaluate paradigm from strategies and now perform counts
  directly on input data in one step.
* Skip slides (and set all counts to 0) if their `end_pos` falls outside of
  the region on that particular genome's chromosome/contig.
* Rename `KMerCounterStrategy` to `MotifCounterStrategy`
* Fixed bug causing `use_and` to not work as expected for chromosomes not
  explicitly listed in the `exceptions` dict when also using `use_chrom`.
* Support use of FASTA files which must be supplied with a `samtools faidx` style index.
* Stopped supporting Python 3 due to incompatability with `buffer` and `memoryview`.
* Prevent `query` from deep copying itself on return. Note this means that a query
  will alter the original Goldilocks object.
* Now using a 3D numpy matrix to store counters with memory shared to
  support multiprocessing during census.
* Removed `StrategyValue` as these cannot be stored in shared memory. This makes
  ratio-based strategies a bit of a hack currently (but still work...)
* tldr; Goldilocks is at least 2-4x faster than previously, even without multiprocessing

0.0.71 (2015-07-11)
-------------------
* Officially add MIT license to repository.
* Deprecate `_filter`.
* Update and tidy `examples.py`.
* `is_seq` argument to initialisation removed and replaced with `is_pos`.
* Use `is_pos` to indicate the expected input is positional, not sequence.
* Force use of `PositionCounterStrategy` when `is_pos` is True.
* Sequence data now read in to 0-indexed arrays to avoid the overhead of string
    re-allocation by having to append a padding character to the beginning of very
    long strings.
* Region metadata continues to use 1-indexed positions for user output.
* `VariantCounterStrategy` now `PositionCounterStrategy`.
* `PositionCounterStrategy` expects 1-indexed lists of positions;
    `prepare` populates the listed locations with 1 and then `evaluate`
    returns the sum as before.
* `test_regression2` updated to account for converting 1-index to 0-index when
    manually handling the sequence for expected results.
* `query` accepts `gmax` and `gmin` arguments to filter candidate regions by
  the group-track value.
* `CandidateList` removed and replaced with simply returning a new `Goldilocks`.

0.0.6 (2015-06-23)
------------------
* `Goldilocks.sorted_regions` stores a list of region ids to represent the result
  of a sorting operation following a call to `query`.
* Regions in `Goldilocks.regions` now always have a copy of their "id" as a key.
* `__check_exclusions` now accepts a `group` and `track` for more complex
  exclusion-based operations.
* `region_group_lte` and `region_group_gte` added to usable exclusion fields to
  remove regions where the value of the desired group/track combination is
  less/greater than or equal to the value of the group/track set by the
  current `query`.
* `query` now returns a new `Goldilocks` instance, rather than a `CandidateList`.
* `Goldilocks.candidates` property now allows access to regions, this property
  will maintain the order of `sorted_regions` if it has one.
* `export_meta` now allows `group=None`
* `CandidateList` class deleted.
* Test data that is no longer used has been deleted.
* Scripts for generating test data added to `test_gen/` directory.
* Tests updated to reflect the fact `CandidateList` lists are no longer returned
  by `query`.
* `_filter` is to be deprecated in favour of `query` by 0.0.7

Beta (2014-10-08)
---------------------
* Massively updated! Compatability with previous versions very broken.
* Software retrofitted to be much more flexible to support a wider range of problems.

0.0.2 (2014-08-18)
---------------------

* Remove incompatible use of `print`

0.0.1 (2014-08-18)
---------------------

* Initial package


