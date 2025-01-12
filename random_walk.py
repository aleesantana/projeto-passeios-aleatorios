from random import choice

class RandomWalk:
    """Classe para gerar passeios aleatórios simulando movimento Browniano"""

    def __init__(self, num_points=500):
        """Inicializa atributos de um passeio"""
        self.num_points = num_points

        # Todos os passeios começam em (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """
        Determina a direção e a distância de um único passo do movimento.
        
        Returns:
            int: O tamanho do passo (positivo ou negativo) representando
                a mudança na coordenada x ou y.
        """
        # Escolhe a direção do movimento (1 para direita/cima, -1 para esquerda/baixo)
        direction = choice([1, -1])

        # Escolhe a distância do movimento (0 a 4 unidades)
        distance = choice([0, 1, 2, 3, 4])

        # Calcula o passo multiplicando direção pela distância
        step = direction * distance

        return step
        

    def fill_walk(self):
        """Calcula todos os pontos do passeio"""       
        # Continua dando passos até que o passeio atinja o comprimento desejado
        while len(self.x_values) < self.num_points:
            # Obtém os passos nas direções x e y usando o novo método
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejeita movimentos que não vão a lugar algum
            if x_step == 0 and y_step == 0:
                continue

            # Calcula a nova posição 
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            