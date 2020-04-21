# A quick and dirty toy database

Written in Python 3.7 this database uses a CSV based backend and allows simple
CRUD (INSERT, SELECT, UPDATE, DELETE) operations.

Data is held in memory and persisted back to the CSV file on INSERT, UPDATE or 
DELETE.

## Getting started

 * Clone the repo and run python3 demo.py

 * Monitor the testdb/people.csv file for changes

 * Profit

## Usage

Don't use this! It's awfully basic and has many many problems. That said if you
must please bear in mind the following:

 * The database folder must exist BEFORE use. There is no support for defining 
 new tables or for building a database schema from scratch - that's what Excel
 if for
 
 * Ensure you pass the path to the database files into the class initilisation

 * Column names are not case sensitive. Values _are_ case sensitive

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
