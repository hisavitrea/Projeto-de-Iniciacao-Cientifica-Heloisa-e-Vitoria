import matplotlib.pyplot as plt
import numpy as np

categorias = ['<1"', '1-2"', '>2"']
prob_alta = [14099, 2, 0]
prob_media = [7494, 5696, 563]
prob_baixa = [217, 1280, 6420]

cores = ['#2e7d32', '#d4af37', '#b71c1c']

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.linewidth': 1.0
})

x = np.arange(len(categorias))
largura = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

barras_alta = ax.bar(x - largura, prob_alta, largura, label='Prob. alta (>=0.99)', color=cores[0], edgecolor='black', linewidth=0.8)
barras_media = ax.bar(x, prob_media, largura, label='Prob. média (0.9-0.99)', color=cores[1], edgecolor='black', linewidth=0.8)
barras_baixa = ax.bar(x + largura, prob_baixa, largura, label='Prob. baixa (<0.9)', color=cores[2], edgecolor='black', linewidth=0.8)

ax.set_title('Separação angular × Probabilidade de match', fontsize=13, pad=15)
ax.set_xlabel('Separação angular', fontsize=12)
ax.set_ylabel('Número de pares', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categorias)

ax.legend(loc='upper right', fontsize=10)

ax.set_ylim(0, max(prob_alta) * 1.15)

def adicionar_rotulos(barras):
    for barra in barras:
        altura = barra.get_height()
        if altura > 0:
            ax.text(barra.get_x() + barra.get_width()/2., altura + 200,
                    f'{int(altura)}',
                    ha='center', va='bottom', fontsize=9)

adicionar_rotulos(barras_alta)
adicionar_rotulos(barras_media)
adicionar_rotulos(barras_baixa)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.savefig('figura3_separacao_probabilidade.png', dpi=300, bbox_inches='tight')
plt.savefig('figura3_separacao_probabilidade.pdf', bbox_inches='tight')

plt.show()