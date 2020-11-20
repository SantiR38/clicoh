# Clicoh
=============

E-commerce for a beloved enterprise.


## Setting up on your local machine

For running this project it will be necesary to **download and install** the following things:

  1. [Python 3.6 32-bit](https://www.python.org/downloads/).
  2. [PostgreSQL](https://www.postgresql.org/download/).
  3. [Git](https://git-scm.com/download/win).
  4. [Pip](https://www.neoguias.com/como-instalar-pip-python/#Como_instalar_PIP_en_Windows).

Next steps:

  5. **Clone this project** in your local machine: Use `git clone` and the url of this project.

  6. **Create the database in postgres** with the data in config.

  7. Create the **virtual enviroment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

  8. Install dependencies ```pip install requirements.txt```

  9. Migrate to your database: `$ python manage.py migrate`.

  10. Next, you have to **create a superuser**: `$ python manage.py createsuperuser`.


## Endpoints

| Resource           | POST            | GET               | PUT             | DELETE          |
| :----              |     :-----:     |      :-----:      |     :-----:     |     :-----:     |
| {host}/product/    | Create product* | List Products     |                 |                 |
| {host}/product/123 |                 | Retrieve Product  | Update product  | Delete product  |
| {host}/sales/      | Create sales*#  | List sales        |                 |                 |
| {host}/sales/123   |                 | Retrieve sale     | Update sale#    | Delete sale     |

[*] For post, the JSON structure is the following:

**Create Product:**
```json
{
    "id": "B12MX",
    "name": "Product name",
    "price": 100
}
```

**Create Sale:**
```json
{
    "date_time": "2020-09-09 08:00",
    "details": [
        {
            "cuantity": 1,
            "product_id": "1"
        },
        {
            "cuantity": 2,
            "product_id": "2"
        }
    ]
}
```
[#] The endpoint is not working properly at the moment.