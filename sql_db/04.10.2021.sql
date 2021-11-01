USE dump;

SELECT 
    *
FROM
    student
WHERE
    date_of_birth > '1991-10-04'
        AND (lastname LIKE '%ov'
        OR lastname LIKE '%ova'
        OR lastname LIKE '%ev'
        OR lastname LIKE '%eva'
        OR lastname LIKE '%in'
        OR lastname LIKE '%ina')
 
