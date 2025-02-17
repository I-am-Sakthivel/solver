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
        },
        {
            "type":"function",
            "function":{
                "name":"addition",
                "description":"used to add two numbers. Choose if the limeric needs addition",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "a":{
                            "type":"number",
                            "description":"The first number"
                        },
                        "b":{
                            "type":"number",
                            "description":"The second number"
                        }
                    }
                },
                "required":["a","b"],
                "additionalProperties":False
            }
        }
]