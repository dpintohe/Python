import sqlite3
class almacen():
    def formatearVista(self, Consumible):
        print("+{:-<14}+{:-<12}+{:-<10}+{:-<10}+{:-<10}+{:-<10}+".format("", "", "", "", "", ""))
        print("|{:^14}|{:^12}|{:^10}|{:^10}|{:^10}|{:^10}|".format("Origen", "Referencia", "Nombre", "Cantidad", "Precio","Posicion"))
        print("+{:-<14}+{:-<12}+{:-<10}+{:-<10}+{:-<10}+{:-<10}+".format("", "", "", "", "", ""))

        for i in Consumible:
            print("|{:^14}|{:^12}|{:^10}|{:^10}|{:^10}|{:^10}|".format(i[0], i[1], i[2], i[3], i[4],i[5]))
        
        print("+{:-<14}+{:-<12}+{:-<10}+{:-<10}+{:-<10}+{:-<10}+".format("", "", "", "", "", ""))
    def crear(self):
        conexion = sqlite3.connect("almacen.db")
        c = conexion.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Consumibles (Origen VARCHAR(10),
                                                            Referencia INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            Nombre VARCHAR (10), 
                                                            Cantidad INTEGER, 
                                                            PRECIO REAL, 
                                                            POSICION VARCHAR (5))''')
        conexion.commit()
        conexion.close()    
    def ver(self, Ref):
        conexion = sqlite3.connect("almacen.db")
        c = conexion.cursor()
        c.execute("SELECT * FROM Consumibles WHERE Referencia = ?", (Ref,)) 
        Consumible = c.fetchall()
        self.formatearVista(Consumible)
        conexion.close()
    def Introducir(self, datos):
        conexion = sqlite3.connect("almacen.db")
        c = conexion.cursor()
        c.execute("INSERT INTO Consumibles VALUES (?,NULL,?,?,?,?)", datos)
        conexion.commit()
        conexion.close()
    def modificar(self, concepto, referencia):
        if concepto == 1:
            valor = float(input("Introduzca nuevo valor: "))
            columna = "Cantidad"
        elif concepto == 2:
            valor = float(input("Introduzca nuevo valor: "))
            columna = "PRECIO"
        else:
            valor = input("Introduzca nuevo valor: ")
            columna = "POSICION"
        conexion = sqlite3.connect("almacen.db")
        c = conexion.cursor()
        Sentencia = "UPDATE Consumibles SET " + columna + "= ? WHERE Referencia = ?"
        c.execute(Sentencia, (valor,referencia))
        conexion.commit()
        conexion.close()
    def listar(self):
        conexion = sqlite3.connect("almacen.db")
        c = conexion.cursor()
        c.execute("SELECT * FROM Consumibles ORDER BY Referencia")
        Consumible = c.fetchall()
        self.formatearVista(Consumible)
        conexion.close()
    def stock(self, minimo):
        conexion = sqlite3.connect("almacen.db")
        c = conexion.cursor()
        c.execute("SELECT * FROM Consumibles WHERE Cantidad <= ? ORDER BY Cantidad",(minimo,))
        Consumible = c.fetchall()
        self.formatearVista(Consumible)
        conexion.close()
    def valor(self):
        conexion = sqlite3.connect("almacen.db")
        c = conexion.cursor()
        c.execute("SELECT Cantidad, Precio FROM Consumibles ")
        resultado = c.fetchall()
        valor_total = 0
        for i in resultado:
            valor = i[0]*i[1]
            valor_total = valor_total + valor
        print("El valor total del stock es de " + str(valor) + "euros")
        conexion.close()

    