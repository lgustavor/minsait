INPUT = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Processamento Batch",
    "description": "Processamento Batch.",
    "required": ["uuid"],
    "properties": {
        "uuid": {
            "type": "string",
            "maxLength": 9,
            "pattern": "[0-9]{9}"
        }
    },
}