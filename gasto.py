class Gasto:
    def __init__(self, descripcion, monto, categoria="otros"):
        self.descripcion = descripcion
        self.monto = float(monto)
        self.categoria = categoria or "otros"

    def a_diccionario(self):
        return {
            "descripcion": self.descripcion,
            "monto": self.monto,
            "categoria": self.categoria,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["descripcion"], datos["monto"], datos["categoria"])

    def __str__(self):
        return f"{self.descripcion}: {self.monto} € [{self.categoria}]"
