class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self._valor_litro = valor_litro
        self._quantidade_disponivel = quantidade_disponivel
    
    def abastecer_por_valor(self, valor):
        if valor <= 0:
            return -1
        
        litros = valor / self._valor_litro
        if litros > self._quantidade_disponivel:
            return -1
        
        self._quantidade_disponivel -= litros
        return litros
    
    def abastecer_por_litro(self, litros):
        if litros <= 0:
            return -1
        
        valor = litros * self._valor_litro
        if litros > self._quantidade_disponivel:
            return -1
        
        self._quantidade_disponivel -= litros
        return valor
    
    @property
    def valor_litro(self):
        return self._valor_litro
    
    @valor_litro.setter
    def valor_litro(self, valor):
        self._valor_litro = valor
    
    @property
    def quantidade_disponivel(self):
        return self._quantidade_disponivel
    
    @quantidade_disponivel.setter
    def quantidade_disponivel(self, quantidade):
        self._quantidade_disponivel = quantidade


class BombaEtanol(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)


class BombaGasolina(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)
    
    def abastecer_por_valor_com_aditivo(self, valor):
        if valor <= 0:
            return -1
        
        valor_litro_aditivo = self._valor_litro * 1.05
        litros = valor / valor_litro_aditivo
        if litros > self._quantidade_disponivel:
            return -1
        
        self._quantidade_disponivel -= litros
        return litros
    
    def abastecer_por_litro_com_aditivo(self, litros):
        if litros <= 0:
            return -1
        
        valor_litro_aditivo = self._valor_litro * 1.05
        valor = litros * valor_litro_aditivo
        if litros > self._quantidade_disponivel:
            return -1
        
        self._quantidade_disponivel -= litros
        return valor
