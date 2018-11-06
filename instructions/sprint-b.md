# Introduction to Seeding
Database seeding is the act of inserting data into a database to satisfy a
use-case, many of which can be reduced to two scenarios:

1. Adding data that will be used in the application
2. Adding data that will be used to test the application

The first scenario may include tasks such as adding countries to a countries
table to populate form drop-downs. Applications may rely on all kinds of data
and the data has to come from somewhere. If it isn't collected directly, it is
likely seeded as tables of semi-static data are introduced. These can include
countries, color names, planet names, ingredients available at a single
pizzeria, etc....The second scenario involves verify the expected
behavior of a database given appropriate inputs or determining behavior given
unexpected data.

For this assignment, we'll use mimesis to create synthetic data to populate a
test database to verify it accepts expected inputs.


## Readings
- [mimesis quick start](https://mimesis.readthedocs.io/quickstart.html)

# Instructions
1. Install mimesis.
2. Create tables for each of the following tables below.
3. Seed 50 users with random data from mimesis.
4. Seed 10 records per table for each of the 50 seeded users with random data from mimesis.
5. Create tests to verify all 500 seeded records were created.


  | Table       | Columns                                                                                                  |
  |-------------|----------------------------------------------------------------------------------------------------------|
  | User        | id, username, password, email address                                                                    |
  | Accounts    | id, user id, social media url                                                                            |
  | Addresses   | id, user id, street address, street address two, city, state, postal code, country, start date, end date |
  | Education   | id, user id, school, start date, end date, graduated, gpa                                                |
  | Employments | id, user id, company, occupation, start date, end date                                                   |
  | Languages   | id, user id, language                                                                                    |
  | Profiles    | id, user id, nationality                                                                                 |
  | Telephones  | id, user id, telephone number                                                                            |
  | Vitals      | id, user id, height, weight                                                                              |


The table above is an unconventional style of defining tables used for clarity.
The example below is the conventional notation for designing relational
databases and should be used when defining tables.



```text
users (id, username, password, email
accounts (id, user_id, url
addresses (id, user_id, street_address, street_address_two, city, state, postal_code, country, start_date, end_date
education (id, user_id, school, start_date, end_date, graduated, gpa  
employments (id, user_id, company, occupation, start_date, end_date
languages (id, user_id, language
profiles (id, user_id, nationality
telephones (id, user_id, number
vitals (id, user_id, height, weight
```
