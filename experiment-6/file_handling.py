with open("filename.txt","w") as f:
    f.write("hello world ")
    f.writelines(["Second Line\n", "Third Line\n"])

with open("filename.txt","r") as f:
    text=f.read()
    print(text)

with open("filename.txt","r") as f:
    text=f.readlines()
    print(text)


with open("pointer.txt", "w+") as f:
  f.write("Python File Handling")
  print("Pointer position:", f.tell())

  f.seek(0)
  print("After seek:", f.read())
  f.flush()