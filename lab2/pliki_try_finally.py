try:
    file=open("namesfile","w")
    file.write("tekst")
finally:
    file.close()