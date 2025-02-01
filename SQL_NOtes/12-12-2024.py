https://cloud.google.com/blog/topics/developers-practitioners/bigquery-explained-working-joins-nested-repeated-data

S3: After finding the min year for each product, I am joining the cte result with the main table and selecting the required fields.

WITH
  min_year_finiding AS(
  SELECT
    product_id,
    MIN(year) AS firt_year -- product_id | first_year | quantity | price
  FROM
    pacific-ethos-441506-a1.sql_practice.Sales
  GROUP BY
    1)
SELECT
  a.product_id,
  b.year as first_year,
  b.quantity,
  b.price
FROM
  min_year_finiding a
JOIN
  pacific-ethos-441506-a1.sql_practice.Sales AS b
ON
  a.product_id = b.product_id
  AND a.firt_year = b.year
  
  
Questions:
----------
1. What is a temporary table in sql?
2. What is CTE?
3. What is Recursive CTE?
4. What is the difference between CTE and Temp Table?
5. What is Sub-Query?
6. What is scalar Sub-Query?