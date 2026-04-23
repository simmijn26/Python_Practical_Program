x = input("Enter value: ")

try:
    val = int(x)
    print("Integer:", val)
except:
    try:
        val = float(x)
        print("Float:", val)
    except:
        try:
            val = complex(x)
            print("Complex:", val)
        except:
            print("String:", x)