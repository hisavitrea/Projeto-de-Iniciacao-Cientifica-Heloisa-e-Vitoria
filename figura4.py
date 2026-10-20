import matplotlib.pyplot as plt

categorias = ['Inconsistentes\n(prob. baixa + sep. >2")', 'Demais casos\n(consistentes)']
quantidades = [3385, 28775]
cores = ['#b71c1c', '#2e7d32']

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.linewidth': 1.0
})

fig, ax = plt.subplots(figsize=(8, 6))

barras = ax.bar(categorias, quantidades, color=cores, edgecolor='black', linewidth=0.8, width=0.5)

ax.set_title('Confiabilidade real dos pares classificados como "D"', fontsize=13, pad=15)
ax.set_ylabel('Número de pares com match_grade = D', fontsize=12)

ax.set_ylim(0, max(quantidades) * 1.15)

for barra, qtd in zip(barras, quantidades):
    altura = barra.get_height()
    pct = (qtd / 32160) * 100
    ax.text(barra.get_x() + barra.get_width()/2., altura + 500,
            f'{qtd}\n({pct:.2f}%)',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.savefig('figura4_inconsistencias_D.png', dpi=300, bbox_inches='tight')
plt.savefig('figura4_inconsistencias_D.pdf', bbox_inches='tight')

plt.show()