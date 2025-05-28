















class Cliente:

    def __init__(self, cod_empresa: str, cod_cliente: str):
        self.cod_empresa: str = cod_empresa
        self.cod_cliente: str = cod_cliente
    


    @property
    def info_cliente(self):
        
        return f"{self.cod_cliente} - {self.cod_empresa}"
    
    
    

o1 = Cliente(1000, "001")

print(o1.cod_empresa)
print(o1.info_cliente)

