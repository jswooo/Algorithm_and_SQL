SELECT warehouse_id, warehouse_name, address, coalesce(freezer_yn, 'N') as freezer_yn
FROM food_warehouse
WHERE address like '경기도%'
ORDER BY warehouse_id;