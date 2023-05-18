def command(param):
    match(param):
        case "help":
            print("All coommands avaiable")
        case "out":
            return 1
        case "__":
            print("No comman insert.")