# Backend Code Challenge

This project represents a web application written in Django. The application is able to seed it's database with CSV files from [here](https://data.gov.uk/dataset/4c9b7641-cf73-4fd9-869a-4bfeed6d440e/hm-land-registry-price-paid-data).

### Project Setup

Make sure you have Python `3.8+` installed on your machine.
I recommend to also create a virtual environment in order to isolate project dependencies.

To install project dependencies just run
```
make install
```

After that, check if all the tests are green
```
make test
```
The project uses `black` for code formatting, and to format the code, just run
```
make lint
```
To start the development server on your machine, run
```
make run
```

As I mentioned, the project database needs to be seeded with data. For this, we have a download a CSV file from [here](https://data.gov.uk/dataset/4c9b7641-cf73-4fd9-869a-4bfeed6d440e/hm-land-registry-price-paid-data). Any CSV file will do.

After that, just run
```
python manage.py seed_db --file_path=your_path_to_downloaded_file 
```
This command will read the file and will insert all it's contents into the database. All of this is done with the power of SQL 💪.

### Endpoints

At the moment, there are only two endpoints available.

 - `/api/v1/house-prices` is the endpoint where data is grouped by month for each property type.
    
    For filtering of the data, there are a few query params available:
    - `from_date`, a string of the format `YYYY-MM-DD` representing from which date the data should be filtered.
    - `to_date`, a string of the format `YYYY-MM-DD` representing to which date the data should be filtered.
    - `postcode`, a string representing the postcode of the region where the land is located.
 - `/api/v1/transactions` is the endpoint where transactions are grouped by price range types.
 
    For filtering of the data, there are a few query params available:
    - `from_date`, a string of the format `YYYY-MM-DD` representing from which date the data should be filtered.
    - `to_date`, a string of the format `YYYY-MM-DD` representing to which date the data should be filtered.
    - `postcode`, a string representing the postcode of the region where the land is located.
    
    
### DB Tweaks

The SQL queries that are aggregating the data are relatively simple, but because of tha amount of data to aggregate, they are slow.
Because of this, I've added to `registry_api_landtransaction` two indexes, for `postcode` and `price` columns. After I've added these two indexes, I've seen a quite big jump in terms of speed, especially when filtering by postcode. 
There is one more issue, filtering by date range is quite slow in my opinion, and I wasn't able to find a decent solution 😞.

### Decisions

As you might have noticed, I haven't used Django ORM at all. Now, there are a few reasons why:
 - First, I could use the ORM when reading the file and storing data into DB, but, it would be very slow and doing the same action using SQL adds a big performance benefit.
 - When aggregating data, I decided to go with SQL because SQL is very good at aggregating big amount of data and the ORM would just be an intermediate layer I decided to skip.

I know this may be a controversy decision, when to use and when to now use the ORM, but, if the task would be to build a CRUD API, I would definitely choose to use the ORM, but in this particular case, I decided to go with SQL because it's just better for this kind of job.
