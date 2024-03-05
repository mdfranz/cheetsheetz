# Python Architecture Patterns by Jaime Buelta

See - https://www.packtpub.com/product/python-architecture-patterns/9781801819992 and https://github.com/PacktPublishing/Python-Architecture-Patterns

## 1 - Intro to Software Architecture 

Software structure and organizations, teams, and individuals

### Structure

Architectural Considerations

- Business Vision
- Technical Requirements - users count, latency 
- Security, Reliability, and other y's 
- Division of Labor across teams
- Technical constraints 

Defines boundaries 

Challenge of existing systems that must be evolved and avoid 2nd system 

## 2 - API Design 

Pattern is to have `resource` and `action`

CRUD 

REST Interfaces 

```
pen = Pen()
pen.open()
pen.write("Something")
pen.close()
```

which would be in REST

```
# Create a new pen with id 1
POST /pens
# Create a new open pen for pen 1
POST /pens/1/open
# Update the new open text for the open pen 1
PUT /pens/1/open/1/text
# Delete the open pen, closing the pen
DELETE /pens/1/open/1
```

Resources & Parameters

Pagination 

## 3 - Data Modeling

Types of Databases

Transactions

## 4 - Data Layer

- ORM 
- Unit of Work 
* CQRS -  Command (write operations) and Query (read operations) are separated. The pattern is not unique to event-driven structures; they are typically seen in these systems because their nature is to detach the input data from the output data.

Migrations 
- Data Change
- Schema Change 
