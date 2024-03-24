try:
    var=890
    var2=0
    print(var/0)
    print(var2+"!!!!!")
except(TypeError,ValueError):
    print("bład")

except(ZeroDivisionError):
    print("bład dzielenia przez zero")