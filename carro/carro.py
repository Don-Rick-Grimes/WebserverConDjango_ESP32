class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            self.carro=self.session["carro"] = {}
        else:
            self.carro = carro

    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            # self.carro[producto.id]["cantidad"] = self.carro[producto.id]["cantidad"] + 1
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = float(value["precio"])+producto.precio
                    break

        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        if str(producto.id) in self.carro.keys():
            del self.carro[str(producto.id)]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                if value["cantidad"]>1:
                    value["cantidad"] = value["cantidad"]-1
                    value["precio"] = float(value["precio"])-producto.precio
                else:
                      self.eliminar(producto)  
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified = True
