# Matador

Matador, a data engineering/integration metadata store.
Holds information about sources, transforms/mappings and downstreams.
Ultimately I wanted a tool that was simpler than the full blown metadata management services like amundsen or datahub but could still be used to record and produce documentation related to data/integration flows I am producing.

## schemas

### dataset

A dataset is used to group a collection of attributes together.

* name - pkey
* type
* owner - nullable

| name           | type | owner       |
|----------------|------|-------------|
| abc patient    | fhir | some system |
| medicare items | csv  | medicare    |

### attribute

An attribute represents a field of a dataset, or a column of a table.

* dataset
* name
* datatype
* optional
* primary key

| dataset     | name       | datatype | optional | primary key |
|-------------|------------|----------|----------|-------------|
| abc patient | first_name | string   | false    | false       |
| abc patient | last_name  | string   | false    | false       |
| abc patient | uid        | integer  | false    | true        |

### mapping

A mapping describes a simple transformation from one value to another.

* codeset
* value_in
* value out

| codeset | value_in | value_out |
|---------|----------|-----------|
| gender  | M        | male      |
| gender  | F        | female    |
| gender  | Female   | female    |
| gender  | *null*   | other     |
| status  | disabled | *null*    |

### attribute encoding

An attribute encoding descibes how a dataset will be serialised, these are expressed at the attribute level.

* dataset
* attribute
* path
* mapping

| dataset     | attribute  | path                    | mapping  |
|-------------|------------|-------------------------|----------|
| abc patient | gender     | $.gender                | gender   |
| abc patient | last_name  | $.name[0].family        | false    |
| abc patient | uid        | $.identifiers[0].value  | false    |
