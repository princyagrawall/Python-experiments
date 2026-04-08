try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)

    num = int(content.strip())
    print("Number:", num)

    result = 100 // num
    print("Result:", result)

except FileNotFoundError as e:
    print("Error:", e)
except PermissionError as e:
    print("Error:", e)
except ValueError as e:
    print("Error:", e)
except ZeroDivisionError as e:
    print("Error:", e)
except IOError as e:
    print("Error:", e)
finally:
    try:
        f.close()
    except:
        pass