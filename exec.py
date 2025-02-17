def exec(func,args):
    match func:
        case "addition":
            return args["a"]+args["b"]
        