from alpha.src.FooDBalpha import FooDB


mydb = FooDB("./mydb.db")
mydb.set("name", "Muad'Dib")
mydb.get("name")