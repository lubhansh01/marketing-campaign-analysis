-- Campaign response rate
SELECT 
    AVG(Response) AS response_rate
FROM customers;

-- Response by high spender
SELECT 
    High_Spender,
    AVG(Response) AS response_rate
FROM customers
GROUP BY High_Spender;

-- Channel engagement of high-value customers
SELECT 
    AVG(NumWebVisitsMonth) AS avg_web_visits
FROM customers
WHERE High_Spender = 1;
