# M4-B2 — Détection de défauts sur cartes PCB

TechniMatic, fabricant de cartes électroniques, veut une détection automatique de défauts qualité
sur ses cartes PCB. Le dataset compte 2 100 images 64×64 en niveaux de gris, réparties en
7 classes : 6 types de défauts (`open`, `short`, `mousebite`, `spur`, `copper`, `pin_hole`) et une
classe `ok`.

Trois approches ont été comparées. Deux sont implémentées jusqu'à l'inférence, la troisième est
estimée à partir de sources publiques.

## Résultats mesurés

| | Option A (CNN from scratch) | Option B (Transfer ResNet-18) |
|---|---|---|
| Accuracy test | 59,0 % | 80,0 % |
| Temps d'entraînement (CPU) | 72,3 s (8 epochs) | 756,3 s (5 epochs) |
| Latence inférence | 2,73 ms/image | 28,58 ms/image |
| Taille du modèle | 2,1 Mo | 42,7 Mo |

Les deux options partagent le même split (`seed=42`), donc les accuracies sont comparables.
L'option C (CLIP zero-shot) est estimée, non implémentée.

La recommandation chiffrée est dans [`verdict.md`](./verdict.md), le comparatif complet des trois
approches dans [`economic_comparison.md`](./economic_comparison.md).

## Fichiers remplis

### `src/option_a_cnn.py`

- Le modèle entraîné depuis zéro
- Les fonctions qui l'entraînent et le testent

### `src/option_b_transfer.py`

- Le modèle ResNet-18 déjà entraîné, adapté à nos 7 classes
- La préparation des images au format qu'il attend

### `notebooks/M4-B2_template.ipynb`

- Ce que contient le jeu de données : combien d'images par classe, à quoi elles ressemblent
- L'entraînement des deux modèles et leurs résultats
- Le temps que met chaque modèle pour traiter une image, puis la sauvegarde des modèles

### `decisions.md`

- Pourquoi nous avons choisi le transfer learning
- Pourquoi nous avons aussi fait le CNN

### `economic_comparison.md`

- Ce que coûte chaque approche : données, temps, mémoire, précision, maintenance
- Dans quel cas choisir laquelle

### `verdict.md`

- L'approche que nous recommandons, et ce qui nous ferait changer d'avis

`src/option_c_clip.py` reste au stade template : l'option C est estimée à partir de
[`ressources/03_Zero_shot_CLIP_essentiel.md`](./ressources/03_Zero_shot_CLIP_essentiel.md).

## Reproduire les résultats

```bash
python -m venv venv && source venv/bin/activate

# PyTorch CPU pèse environ 200 Mo
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt

# Génère les 2 100 images dans data/pcb_defect_sample/ (déterministe, seed 42, environ 30 s)
python scripts/generate_dataset.py

jupyter notebook notebooks/M4-B2_template.ipynb
```

`data/` et `models/` sont gitignorés. Les images se régénèrent avec le script ci-dessus, les
modèles en exécutant le notebook. Le CPU suffit : les images sont petites et le volume modeste.

## Structure du repo

```
M4-B2-pcb-alex-franck/
├── scripts/
│   └── generate_dataset.py              # génère les images PCB (seed 42)
├── data/                                # gitignored
│   └── pcb_defect_sample/               # produit par le script
│       ├── ok/ open/ short/ ...         # 7 classes
├── notebooks/
│   └── M4-B2_template.ipynb
├── src/
│   ├── load_data.py                     # Dataset PyTorch + dataloaders
│   ├── option_a_cnn.py                  # CNN from scratch — implémenté
│   ├── option_b_transfer.py             # ResNet-18 transfer — implémenté
│   └── option_c_clip.py                 # CLIP zero-shot — estimé, non implémenté
├── models/                              # gitignored
│   ├── option_a_cnn.pt
│   └── option_b_transfer.pt
├── ressources/                          # 6 mini-cours d'appui
├── decisions.md                         # choix d'approche + répartition binôme
├── economic_comparison.md               # comparatif des 3 approches
├── verdict.md                           # recommandation chiffrée
├── requirements.txt
└── .gitignore
```

## Auteurs

Alexandre × Franck.
