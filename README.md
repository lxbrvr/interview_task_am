## Description

A simple Categories API that stores category tree to database and returns category
parents, children and siblings by category id.

## Solution

The tree is stored in the database as nested sets.

Some approaches used for efficient inserting:
- for inserting a node used bulk_create;
- uniqueness names check occurs on one database query;

As a result, we get effective reading and inserting.

## Stack

- python 3.8
- django 2.2.7

## Requirements

- docker
- docker-compose

## API

There are two endpoints:

- `POST /categories/` - accepts json body and saves categories to database;
- `GET /categories/{id}/` - retrieves category name, parents, children and siblings by primary key in json format.

## Commands

Commands are run from the root directory.
    
`make up` - runs the development server at 0.0.0.0:8000

`make test` - runs project tests

`make down` - removes containers and volumes

