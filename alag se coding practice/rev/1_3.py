extention=input("input the name of the file : ").lower().strip()

if "."in extention:
    extention=extention.rsplit(".",1)[1]
    match extention:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "zip":
            print("application/zip")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")