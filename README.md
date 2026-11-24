# Supermarket Sales Analysis

A data analysis project that explores supermarket sales data in two ways: SQL KPI queries on a sales database, and a Python analysis with statistics and visualizations.

## Repository structure

```
data/sales.csv                      - the sales dataset used by the SQL project (1000 transactions)
sql/creation_queries.sql            - creates the sales table and loads the data
sql/sales_and_revenue_kpis.sql      - Use Case 1: total revenue and average basket size per city and branch
sql/customer_behavior_kpis.sql      - Use Case 2: customer footfall, loyalty, gender split, big spenders
sql/product_performance_kpis.sql    - Use Case 3: top-selling products and categories, overall and per store
analysis/supermarket_sales_analysis.py - Python analysis: descriptive statistics and charts
```

## SQL project

The SQL queries analyze a `sales` table of supermarket transactions across three cities (New York, Los Angeles, Chicago) and two branches. Each KPI file contains the queries plus the findings and business conclusions drawn from the results:

- **Sales and revenue**: total revenue by city and branch, average basket size.
- **Customer behavior**: footfall per store, membership percentage, gender split, number of transactions over $100.
- **Product performance**: top-selling products and product categories, overall and per store.

To run: load `sql/creation_queries.sql` into MySQL (it creates and populates the `sales` table from the same data as `data/sales.csv`), then run any of the KPI query files.

## Python analysis

`analysis/supermarket_sales_analysis.py` is a pandas/matplotlib/seaborn analysis covering:

- Descriptive statistics of the `Total` column (mean, median, mode, range, variance, standard deviation)
- Visualizations: branch sales count, rating vs total scatter, total distribution histogram, box plot, payment methods pie chart
- Value counts for product lines, payment methods, and branches

### Requirements

```
pip install pandas numpy matplotlib seaborn
```

### Run

```
cd analysis
python supermarket_sales_analysis.py
```

The script expects a `supermarket_sales.csv` file in its working directory with the classic supermarket sales dataset columns (Branch, Product line, Total, Payment, Rating). Place the CSV next to the script before running.
