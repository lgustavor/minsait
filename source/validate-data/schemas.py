INPUT = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Processamento Batch",
    "description": "Processamento Batch.",
    "required": ["uuid", "country", "itemType", "salesChannel", "orderPriority", "orderDate", "region", "shipDate"],
    "properties": {
        "uuid": {
            "type": "string",
            "maxLength": 9,
        },
        "country": {
            "type": "string",
            "maxLength": 50,
        },
        "itemType": {
            "type": "string",
            "maxLength": 30,
        },
        "salesChannel": {
            "type": "string",
            "maxLength": 10,
        },
        "orderPriority": {
            "type": "string",
            "maxLength": 5,
        },
        "orderDate": {
            "type": "string",
            "maxLength": 10,
        },
        "region": {
            "type": "string",
            "maxLength": 100,
        },
        "shipDate": {
            "type": "string",
            "maxLength": 10,
        }
    },
}