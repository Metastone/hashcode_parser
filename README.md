# Assumptions

- When there is a list in the input file, its size is always given before the list 

# Subjects

## 2015

```
(
    nb_rows : int,
    nb_slots : int,
    nb_unavailable_slots : int,
    nb_pools : int,
    nb_servers : int,

    unavailable_slots : nb_unavailable_slots $ [
        row : int,
        slot : int
    ],

    servers : nb_servers $ [
        size : int,
        capacity : int
    ]
)
```

## 2016

```
(
    nb_rows : int,
    nb_columns : int,
    nb_drones : int,
    nb_turns : int,
    max_payload : int,

    nb_product_types : int,
    product_type_weights : nb_product_types $ [
        weight : int
    ],

    nb_warehouses : int,
    warehouses : nb_warehouses $ [
        row : int,
        column : int,
        quantities : nb_product_types $ [
            quantity : int
        ]
    ],

    nb_orders : int,
    orders : nb_order $ [
        row : int,
        column : int,
        nb_ordered : int,
        product_types : nb_ordered $ [
            type : int
        ]
    ]
)
```

## 2017

```
(
    nb_videos : int,
    nb_endpoints : int,
    nb_requests : int,
    nb_caches : int,
    caches_size : int,

    videos : nb_videos $ [
        size : int
    ],

    endpoints : nb_endpoints $ [
        latency : int,
        nb_caches : int,
        connections : nb_caches $ [
            cache : int,
            latency : int
        ]
    ],

    requests : nb_requests $ [
        quantity : int,
        video : int,
        endpoint : int
    ]
)
```

## 2018

## 2019

## 2020

