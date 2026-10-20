import matplotlib.pyplot as plt

categorias = ['<1"', '1-2"', '>2"']
quantidades = [21810, 6978, 6983]
porcentagens = [60.97, 19.51, 19.52]
cores = ['#2e7d32', '#d4af37', '#b71c1c']

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.linewidth': 1.0
})

fig, ax = plt.subplots(figsize=(8, 6))

barras = ax.bar(categorias, quantidades, color=cores, edgecolor='black', linewidth=0.8)

ax.set_title('Distribuição da separação angular (35.771 pares)', fontsize=13, pad=15)
ax.set_xlabel('Separação angular', fontsize=12)
ax.set_ylabel('Número de pares', fontsize=12)

ax.set_ylim(0, max(quantidades) * 1.15)

for barra, qtd, pct in zip(barras, quantidades, porcentagens):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., altura + 500,
            f'{qtd}\n({pct}%)',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.savefig('figura2_separacao_angular.png', dpi=300, bbox_inches='tight')
plt.savefig('figura2_separacao_angular.pdf', bbox_inches='tight')

plt.show()