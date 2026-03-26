CREATE TABLE transactions (
    card_number STRING,
    amount DOUBLE,
    timestamp STRING,
    merchant STRING,
    merchant_category STRING,
    device_type STRING
) WITH (
    'connector' = 'kafka',
    'topic' = 'credit_card_transactions',
    'properties.bootstrap.servers' = 'localhost:9092',
    'format' = 'json'
);

SELECT
    merchant_category,
    COUNT(*) AS transaction_count
FROM transactions
WHERE amount > 500
GROUP BY merchant_category;