import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'axes.linewidth': 1.5
})

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(12, 6))

# Painel A: Campo pouco denso
ax_a.set_xlim(0, 10)
ax_a.set_ylim(0, 10)
ax_a.set_xticks([])
ax_a.set_yticks([])
ax_a.set_title("(a) Campo pouco denso", fontsize=12, fontweight='bold', pad=10)

x_true_a, y_true_a = 5, 5
x_meas_a, y_meas_a = 5.2, 5.1

ellipse_a = patches.Circle((x_true_a, y_true_a), radius=1.0, 
                           edgecolor='blue', facecolor='lightblue', alpha=0.3, label='Elipse de erro')
ax_a.add_patch(ellipse_a)

raio_a = patches.Circle((x_meas_a, y_meas_a), radius=2.0, 
                        edgecolor='gray', facecolor='none', linestyle='--', linewidth=2, label='Raio de busca fixo')
ax_a.add_patch(raio_a)

ax_a.plot(x_true_a, y_true_a, 'kx', markersize=10, markeredgewidth=2, label='Centroide verdadeiro')
ax_a.plot(x_meas_a, y_meas_a, 'ro', markersize=6, label='Centroide medido')

np.random.seed(42)
fundo_x_a = np.random.uniform(1, 9, 5)
fundo_y_a = np.random.uniform(1, 9, 5)
for fx, fy in zip(fundo_x_a, fundo_y_a):
    if np.hypot(fx-x_true_a, fy-y_true_a) > 3:
        ax_a.plot(fx, fy, 'ko', markersize=4, alpha=0.5)

ax_a.legend(loc='upper right', fontsize=9, framealpha=0.9)

# Painel B: Campo denso com confusão astrométrica
ax_b.set_xlim(0, 10)
ax_b.set_ylim(0, 10)
ax_b.set_xticks([])
ax_b.set_yticks([])
ax_b.set_title("(b) Campo denso (Confusão Astrométrica)", fontsize=12, fontweight='bold', pad=10)

x_true_b, y_true_b = 5, 5
x_viz, y_viz = 6.5, 6.2
x_meas_b, y_meas_b = 5.8, 5.6

ellipse_alvo = patches.Circle((x_true_b, y_true_b), radius=1.2, 
                              edgecolor='blue', facecolor='lightblue', alpha=0.4)
ellipse_viz = patches.Circle((x_viz, y_viz), radius=1.2, 
                             edgecolor='green', facecolor='lightgreen', alpha=0.4)
ax_b.add_patch(ellipse_alvo)
ax_b.add_patch(ellipse_viz)

raio_b = patches.Circle((x_meas_b, y_meas_b), radius=1.5, 
                        edgecolor='gray', facecolor='none', linestyle='--', linewidth=2)
ax_b.add_patch(raio_b)

ax_b.plot(x_true_b, y_true_b, 'kx', markersize=10, markeredgewidth=2)
ax_b.plot(x_meas_b, y_meas_b, 'ro', markersize=6)

ax_b.annotate('', xy=(x_meas_b, y_meas_b), xytext=(x_true_b, y_true_b),
              arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

fundo_x_b = np.random.uniform(1, 9, 15)
fundo_y_b = np.random.uniform(1, 9, 15)
for fx, fy in zip(fundo_x_b, fundo_y_b):
    ax_b.plot(fx, fy, 'ko', markersize=4, alpha=0.5)

ax_b.text(5.1, 4.5, "Deslocamento\ndo centroide", color='red', fontsize=9, ha='left')
ax_b.text(x_viz + 0.2, y_viz - 0.5, "Fonte vizinha", color='green', fontsize=9)

plt.tight_layout()
plt.subplots_adjust(wspace=0.1)

plt.savefig('figura1_confusao_astrometrica.png', dpi=300, bbox_inches='tight')
plt.savefig('figura1_confusao_astrometrica.pdf', bbox_inches='tight')

plt.show()