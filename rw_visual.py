import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from random_walk import RandomWalk

def create_random_walk():
    """Cria e preenche um novo passeio aleatório."""
    rw = RandomWalk()
    rw.fill_walk()
    return rw

def setup_plot():
    """Configura o estilo e cria a figura do matplotlib."""
    plt.style.use('seaborn-v0_8-pastel')
    fig, ax = plt.subplots(figsize=(15, 10), dpi=128)
    return fig, ax

def create_gradient_line(rw, ax):
    """Cria a linha com efeito de degradê que representa o movimento."""
    # Prepara os pontos para o degradê
    points = np.array([rw.x_values, rw.y_values]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    # Configura a normalização e cria a coleção de linhas
    norm = plt.Normalize(0, len(rw.x_values))
    lc = LineCollection(segments, cmap='Blues', norm=norm)
    lc.set_array(np.arange(len(rw.x_values)))
    lc.set_linewidth(1.3)
    
    # Adiciona ao gráfico e retorna para uso posterior
    return ax.add_collection(lc)

def customize_plot(ax, rw, line):
    """Personaliza a aparência do gráfico."""
    # Configura os limites e proporções
    ax.set_xlim(min(rw.x_values), max(rw.x_values))
    ax.set_ylim(min(rw.y_values), max(rw.y_values))
    ax.set_aspect('equal')
    
    # Adiciona título e marca pontos especiais
    ax.set_title("Movimento Browniano de um Grão de Pólen", fontsize=24)
    ax.plot(0, 0, c='green', marker='o', markersize=10, label='Início')
    ax.plot(rw.x_values[-1], rw.y_values[-1], c='red', marker='o', markersize=10, label='Fim')
    
    # Configurações finais
    ax.legend()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.colorbar(line, ax=ax, label='Progressão do movimento')

def main():
    """Função principal que coordena a visualização do passeio aleatório."""
    while True:
        # Cria e visualiza um novo passeio aleatório
        rw = create_random_walk()
        fig, ax = setup_plot()
        line = create_gradient_line(rw, ax)
        customize_plot(ax, rw, line)
        
        plt.show()
        
        # Verifica se o usuário quer continuar
        if input("Criar outro passeio aleatório? (s/n): ").lower() == 'n':
            break

if __name__ == '__main__':
    main()
    