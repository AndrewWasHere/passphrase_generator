# Pwgen

A passphrase generator based on website scrapes. Because, why not?

## Use

There are two steps to generating passphrases: creating a word database to 
choose  from and generating a password from that list.

### Build

Use this command to generate a word database based on scraping websites.

```
$ python pwgen.py build --out words.pwgen http://someurl
```

Alternatively, pass in a file path to scrape multiple URLs. The input file is
a plain text file formatted one URL per line.

```
$ python pwgen.py build --out shakespeare.pwgen complete_works_urls.txt
```

### Generate

Use this command to generate a passphrase from a database built with the `build`
command. You can specify the minimum number of characters a chosen word should
have, the maximum number of characters a chosen word should have, the minimum 
number of words in the passphrase, the minimum number of characters in the 
passphrase, and whether to camel case the generated passphrase.

```
$ python pwgen.py generate --min 1 --max 10 --camelcase -n 5 words.pwgen
```

## License

Copyright 2017, Andrew Lin.
All rights reserved.

This software is released under the BSD 3-clause license. See
LICENSE.txt or https://opensource.org/licenses/BSD-3-Clause for more
information.
