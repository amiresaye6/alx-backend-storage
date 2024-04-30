# NoSQL Database Overview

This README provides an overview of NoSQL databases, including what NoSQL means, the differences between SQL and NoSQL, ACID properties, document storage, NoSQL types, benefits of NoSQL databases, querying information, and basic CRUD operations using MongoDB.

## Table of Contents
1. [What is NoSQL?](#what-is-nosql)
2. [Differences Between SQL and NoSQL](#differences-between-sql-and-nosql)
3. [ACID Properties](#acid-properties)
4. [Document Storage](#document-storage)
5. [Types of NoSQL Databases](#types-of-nosql-databases)
6. [Benefits of NoSQL Databases](#benefits-of-nosql-databases)
7. [Querying NoSQL Databases](#querying-nosql-databases)
8. [CRUD Operations in MongoDB](#crud-operations-in-mongodb)

---

## What is NoSQL?

NoSQL, which stands for "Not Only SQL," is a type of database management system that provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases.

## Differences Between SQL and NoSQL

### SQL
- Relational database management system (RDBMS).
- Structured data model.
- Uses SQL (Structured Query Language) for defining and manipulating data.
- ACID properties are maintained.
- Examples: MySQL, PostgreSQL, Oracle.

### NoSQL
- Non-relational database management system.
- Flexible and schema-less data model.
- Query languages vary (e.g., MongoDB uses JavaScript-like query language).
- Relaxation of ACID properties for scalability.
- Examples: MongoDB, Cassandra, Redis.

## ACID Properties

ACID stands for Atomicity, Consistency, Isolation, and Durability. It ensures that database transactions are processed reliably.

## Document Storage

Document storage is a NoSQL database model where data is stored in flexible, semi-structured documents (e.g., JSON, BSON) instead of traditional row-column format.

## Types of NoSQL Databases

1. **Key-Value Stores**: Store data as key-value pairs (e.g., Redis).
2. **Document Stores**: Store data as documents (e.g., MongoDB).
3. **Column Stores**: Store data in columns rather than rows (e.g., Cassandra).
4. **Graph Databases**: Store data as graph structures (e.g., Neo4j).

## Benefits of NoSQL Databases

- Scalability: Easily scale horizontally.
- Flexibility: Schema-less design allows for dynamic changes.
- Performance: Optimized for specific use cases, such as high read/write throughput.
- Availability: High availability and fault tolerance.

## Querying NoSQL Databases

Querying in NoSQL databases depends on the type of database. For example, in MongoDB, you can use the `find()` method to query documents.

```javascript
// Find documents in MongoDB
db.collection.find({ field: value });
```

## CRUD Operations in MongoDB

MongoDB supports CRUD operations: Create, Read, Update, and Delete.

### Insert
```javascript
// Insert document into collection
db.collection.insertOne({ field: value });
```

### Update
```javascript
// Update document in collection
db.collection.updateOne({ field: value }, { $set: { fieldToUpdate: newValue } });
```

### Delete
```javascript
// Delete document from collection
db.collection.deleteOne({ field: value });
```
