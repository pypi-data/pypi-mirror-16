
mscxyz.py
=========

.. code-block::

  usage: mscxyz.py [-h] [-b] [-g GLOB] [-p PICK] [-c CYCLE_LENGTH] [-v]
                   {clean,meta,lyrics,rename,export,help} ... path
  
  A command line tool to manipulate the XML based *.mscX and *.mscZ files of the
  notation software MuseScore.
  
  positional arguments:
    path                  Path to a *.mscx file or a folder which contains
                          *.mscx files. In conjunction with the subcommand
                          "help" this positional parameter accepts the names of
                          all other subcommands or the word "all".
  
  optional arguments:
    -h, --help            show this help message and exit
    -b, --backup          Create a backup file.
    -g GLOB, --glob GLOB  Handle only files which matches against Unix style
                          glob patterns (e. g. "*.mscx", "* - *"). If you omit
                          this option, the standard glob pattern "*.mscx" is
                          used.
    -p PICK, --pick PICK  The --pick option can be used to run multiple
                          mscxyz.py commands in parallel on multiple consoles.
                          If you like so, using this option a "poor man's
                          multithreading" can be accomplished. Multicore CPUs
                          can be used to full capacity. By default every fourth
                          file gets picked up. The option "-p N" begins the
                          picking on the Nth file of a cycle. The corresponding
                          option is named "-c" or "--cycle-length".
    -c CYCLE_LENGTH, --cycle-length CYCLE_LENGTH
                          This option specifies the distance between the picked
                          files. The option "-c N" picks every Nth file. The
                          corresponding options is named "-p" or "--pick".
    -v, --verbose         Make commands more verbose. You can specifiy multiple
                          arguments (. g.: -vvv) to make the command more
                          verbose.
  
  Subcommands:
    {clean,meta,lyrics,rename,export,help}
                          Run "subcommand --help" for more informations.
      clean               Clean and reset the formating of the *.mscx file
      meta                Synchronize the values of the first vertical frame
                          (title, composer, lyricist) with the corresponding
                          metadata fields.
      lyrics              Extract lyrics. Without any option this subcommand
                          extracts all lyrics verses into separate mscx files.
                          This generated mscx files contain only one verse. The
                          old verse number is appended to the file name, e. g.:
                          score_1.mscx.
      rename              Rename the *.mscx files.
      export              Export the scores to PDFs or to the specified
                          extension.
      help                Show help. Use "mscxyz.py help all" to show help
                          messages of all subcommands. Use "mscxyz.py help
                          <subcommand>" to show only help messages for the given
                          subcommand.
  

Subcommands
===========


mscxyz.py rename
----------------

.. code-block::

  usage: mscxyz.py rename [-h] [-d] [-f FORMAT] [-a] [-n]
  
  Tokens you can use in the format string (-f, --format):
  
  	- %title%
  	- %title_1char%  The first character of the token 'title'.
  	- %title_2char%  The first two characters of the token 'title'
  	- %subtitle%
  	- %composer%
  	- %lyricist%
  
  optional arguments:
    -h, --help            show this help message and exit
    -d, --dry-run         Do not rename the scores
    -f FORMAT, --format FORMAT
                          Format string.
    -a, --ascii           Use only ASCII characters.
    -n, --no-whitespace   Replace all whitespaces with dashes or sometimes
                          underlines.
  

mscxyz.py help
--------------

.. code-block::

  usage: mscxyz.py help [-h] [-m] [-r]
  
  optional arguments:
    -h, --help      show this help message and exit
    -m, --markdown  Show help in markdown format. This option enables to
                    generate the README file directly form the command line
                    output.
    -r, --rst       Show help in reStructuresText format. This option enables to
                    generate the README file directly form the command line
                    output.
  

mscxyz.py lyrics
----------------

.. code-block::

  usage: mscxyz.py lyrics [-h] [-n NUMBER] [-r REMAP]
  
  optional arguments:
    -h, --help            show this help message and exit
    -n NUMBER, --number NUMBER
                          The lyric verse number to extract.
    -r REMAP, --remap REMAP
                          Remap lyrics. Example: "--remap 3:2,5:3". This example
                          remaps lyrics verse 3 to verse 2 and verse 5 to 3. Use
                          commas to specify multiple remap pairs. One remap pair
                          is separated by a colon in this form: "old:new": "old"
                          stands for the old verse number. "new" stands for the
                          new verse number.
  

mscxyz.py meta
--------------

.. code-block::

  usage: mscxyz.py meta [-h] [-j] [-s]
  
  # XML structure of a meta tag:
  
  	<metaTag name="tag"></metaTag>
  
  # All meta tags:
  
  	- arranger
  	- composer
  	- copyright
  	- creationDate
  	- lyricist
  	- movementNumber
  	- movementTitle
  	- originalFormat
  	- platform
  	- poet
  	- source
  	- translator
  	- workNumber
  	- workTitle
  
  # XML structure of a vbox tag:
  
  	<VBox>
  	  <Text>
  	    <style>Title</style>
  	    <text>Some title text</text>
  	    </Text>
  
  # All vbox tags:
  
  	- Title
  	- Subtitle
  	- Composer
  	- Lyricis
  
  optional arguments:
    -h, --help  show this help message and exit
    -j, --json  Additionally write the metadata to a json file.
    -s, --show  Show all metadata.
  

mscxyz.py export
----------------

.. code-block::

  usage: mscxyz.py export [-h] [-e EXTENSION]
  
  optional arguments:
    -h, --help            show this help message and exit
    -e EXTENSION, --extension EXTENSION
                          Extension to export. If this option is omitted, then
                          the default extension is "pdf".
  

mscxyz.py clean
---------------

.. code-block::

  usage: mscxyz.py clean [-h] [-s STYLE]
  
  optional arguments:
    -h, --help            show this help message and exit
    -s STYLE, --style STYLE
                          Load a *.mss style file and include the contents of
                          this file.
  
