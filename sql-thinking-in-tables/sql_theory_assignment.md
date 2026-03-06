# 														SQL Theory Assignment											#
#########################################################################################################################		

## 1. Importance of Databases in Real-World AI Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Databases are critical in AI systems because they provide a structured, reliable, and scalable storage for large volumes of data.
AI models depend on clean, organized datasets for training and inference.
Without databases, managing this data would be chaotic and error-prone.

>>>>>> Examples of data stored:
-----------------------------------------
  -> User profiles (names, emails, preferences)
  -> Transaction records (orders, payments, invoices)
  -> Logs and historical data ( various system events, activity tracking)

>>>>>> Structured storage ensures:
------------------------------------------
-->Consistency (data follows predecided rules and formats)
-->Efficiency (fast retrieval and updates)
-->Scalability (handling millions of records without confusion)

                             =========================================================================




## 2. Relational Database Mental Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Relational databases organize data into tables. Each table represents a single entity (example Users, Orders).

- Table --> Represents an entity (like "Customers").
- Row (Tuple) --> Represents one record (e.g. a single customer record).
- Column (Attribute) --> Represents a property of the entity (e.g. Name, Email,age).

Example:

| CustomerID | Name       | Email              |
|============|============|====================|
| 1          | Alice      | alice@email.com    |
| 2          | Bob        | bob@email.com      |

Each table should represent only one entity to avoid confusion and redundancy else while fetching them issues may occur
with lots of irrelevant data.

							============================================================================
## 3. Primary Key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A primary key is a column (or set of columns) that uniquely identifies each row in a table.

->> Must be unique --> No two rows can share the same primary key.
->> Must be non-null --> Every record must have a valid identifier.

Example:
#####################
| CustomerID (PK) | Name   | Email            |
|-----------------|--------|------------------|
| 1               | Alice  | alice@email.com  |
| 2               | Bob    | bob@email.com    |

Here, CustomerID is the primary key. It ensures we can always identify Alice or Bob without confusion using their IDs.

                            ===============================================================================

## 4. Database Schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A schema defines the structure of the database. It describes:
- Tables
- Columns and their data types
- Constraints (primary keys, foreign keys, uniqueness)
- Relationships between tables

Schemas are important because they:
- Maintain consistency across data
- Prevent errors (e.g., storing text in a numeric column)
- Provide a blueprint for developers and AI systems

							============================================================================


## 5. Relationships Between Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Relational databases allow tables to be connected using foreign keys.

- Foreign Key --> A column in one table that references the primary key of another table.
- This creates relationships such as one-to-many or many-to-many.

Example:

Users Table
---------------

| UserID (PK) | Name         |
|-------------|--------------|
| 1           | Ajay         |
| 2           | Brijendra    |

Orders Table
-------------

| OrderID (PriKey) | UserID (Foregin Key) | Product   |
|------------------|----------------------|-----------|
| 101              | 1                    | Laptop    |
| 102              | 2                    | Phone     |

Here:
- UserID in Orders is a foreign key referencing UserID in Users.
- This means Ajay placed order 101, and Brijendra placed order 102.

							============================================================================
									

# 									Summary
########################################################################
- Databases provide structured storage for AI systems.
- Relational databases use tables, rows, and columns to represent entities.
- Primary keys uniquely identify records.
- Schemas define the structure and rules of the database.
- Relationships connect multiple tables using foreign keys.
							============================================================================