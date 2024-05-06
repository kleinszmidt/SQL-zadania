import polars as pl
import sys

db_path = 'C:/sql-tutorial/db/penguins-python5.db'
uri = "sqlite:///{db_path}"
query = "select species, count(*) as num from penguins group by species;"
df = pl.read_database_uri(query, uri, engine="adbc")
print(df)