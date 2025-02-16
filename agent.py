fn=[
    {
        "type":"function",
        "function":{
            "name":"differentiate",
            "description":"Differentiates the given function",
            "parameters":{
                "type":"object",
                "properties":{
                    "function":{
                        "type":"string",
                        "description":"The function to differentiate"
                    }
                }
            },
            "required":["function"],
            "additionalProperties":False
            }
        }
]