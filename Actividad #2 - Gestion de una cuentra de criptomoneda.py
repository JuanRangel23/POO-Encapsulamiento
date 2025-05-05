class CarteraCripto:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__saldo_btc = 0.0  # saldo inicial en BTC

    def consultar_saldo(self):
        print(f"Saldo de {self.__usuario}: {self.__saldo_btc:.8f} BTC")
        return self.__saldo_btc

    def comprar_btc(self, monto_usd, precio_actual_btc):
        if precio_actual_btc <= 0:
            print("El precio del BTC debe ser mayor a 0.")
            return
        btc_comprado = monto_usd / precio_actual_btc
        self.__saldo_btc += btc_comprado
        print(f"{self.__usuario} compró {btc_comprado:.8f} BTC")

    def vender_btc(self, monto_btc, precio_actual_btc):
        if monto_btc > self.__saldo_btc:
            print("No tienes suficiente BTC para vender.")
            return
        if monto_btc <= 0:
            print("El monto de BTC a vender debe ser positivo.")
            return
        usd_recibido = monto_btc * precio_actual_btc
        self.__saldo_btc -= monto_btc
        print(f"{self.__usuario} vendió {monto_btc:.8f} BTC y recibió ${usd_recibido:.2f} USD")
        return usd_recibido

# Ejemplo de uso
mi_cartera = CarteraCripto("Alice")

# Consultar saldo inicial
mi_cartera.consultar_saldo()

# Comprar BTC (ejemplo: 1000 USD con BTC a 50,000 USD)
mi_cartera.comprar_btc(1000, 50000)

# Consultar saldo después de la compra
mi_cartera.consultar_saldo()

# Vender una parte de BTC
mi_cartera.vender_btc(0.01, 55000)

# Consultar saldo final
mi_cartera.consultar_saldo()
