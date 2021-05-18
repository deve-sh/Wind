# Wind Database

This is a try at a good File-Based Cloud Database.

Implementation Features include:

1. Python for interacting with the database.
2. Node.js or another framework for the REST API.

With Features such as:

1. Projects
2. Users
3. Collections
4. Rows

The functionalities in v1 are supposed to be:

1. Creation of Collections
2. Addition of Rows.
3. Updation of Rows.
4. Deletion of Rows.
5. Querying of Rows.

Options for the format of storage of data:

1. Plain JSON
2. Binary JSON (Preferrable)
3. Fixed Binary Engine (In case we need a fixed schema model.)

Wind V1 Architecure:

![Wind V1 Architecure](./Wind-Architecture-V1.jpg)

## New Thoughts and Ideas

I was working on the storage, retrieval and write structure for tables in BSON Format where something struck me. Most Regular DB Engines store data for an entire table in a single file (Kind of what Wind is doing right now with `.bson` files), which causes the following complications:

- The entire table's contents have to be read in order to perform even the most basic and expected-to-be-fast operations, like querying by a unique ID. Yes, Indexing helps, but in case of large tables, the time it requires in order to read the entire table, is a bottleneck.

- For writes, any change to a row has to be reflected in the file containing the data, for unshifting/adding a row at the beginning, the file has to be read, transformed into appropriate data structures from binary representation on disk, the row has to be added and then written back into the database. In this case, precious compute is being wasted to write the contents to the file that were already there, `append`s are much faster since they only have to add the data to the end of the row-list/file. Even then, the file still needs to have the redundant contents re-written.

#### Possible Workaround:

A possible workaround of it is to have a folder/directory associated with the table and store the rows as documents (Literally picking up the 'document' terminology from NoSQL), have the row's unique ID be the identifier for it.


```
"Table Name"
    |
    |-{DocumentId/RowId}.bson
    |-{DocumentId/RowId}.bson
    |-{DocumentId/RowId}.bson
```

The benefit of this approach is:
- Counting of rows becomes easier since it's just the number of files in the table's directory.
- The `updatedAt` and `createdAt` fields are stored right in the metadata of the files itself.
- The searching for rows by uniqueIDs becomes an O(1) operation, since the unique id is the file name itself.
- Indexing references becomes easier as well, certain field values can be referenced to different documents having them and direct access to those files can be done without having to read an entire table file to get to that row.
- Writes become faster, just open the document to write, and save it post modifying. Appending is O(1) and so is adding to the top of the table (Logically, in this approach, there is no top of the table, the document that appears at the top by the default order of file sort is the top of the table.)
- Distribution of the data becomes easier across multiple servers, since now you aren't limited to storing all the data in a single file.

Querying by filters, however, migth take a hit considering every file has to be read, but that can be managed by asynchronously unpacking all files, reading for matches, waiting for all of the read promises to resolve and then providing the rows/documents that matched.