# M4-B2 — Squelette repo (vision PCB Defect — binôme async)

> **Repo template GitHub.** Le membre désigné du binôme clique sur
> **« Use this template »** → nomme `M4-B2-pcb-<binome>` → invite l'autre.

---

## 🧭 Votre brief en un coup d'œil

**Ce README est votre document de pilotage unique** — tout ce qu'il faut faire,
dans l'ordre, avec le bon appui. Les autres supports ont chacun un rôle précis :

| Support | Rôle |
|---|---|
| **Simplonline** | Le contrat : contexte client, livrables, critères de performance |
| **Ce README** | Le pilotage : quoi faire, quand, avec quel mini-cours |
| [`ressources/`](./ressources/) | Les 6 mini-cours d'appui (index dans [`ressources/README.md`](./ressources/README.md)) |
| **Discord `fil-M4-B2`** | Annonces + questions ; MP binôme pour la coordination |

### Les 2 jours async (7 h cumulées binôme)

| Quand | Tâche | Durée | Appui |
|---|---|---|---|
| Jeudi | 0. **Choisir votre approche** (avant de coder) | 30 min | [`06_Grille_decision_approche`](./ressources/06_Grille_decision_approche_essentiel.md) |
| Jeudi | 1. Coordination kick-off (MP Discord) | 30 min | [`05_Pair_coding_async`](./ressources/05_Pair_coding_async_essentiel.md) |
| Jeudi | 2. EDA dataset PCB (partagé) | ~1h | — |
| Jeudi | 3. Implémentation de l'option choisie (partagé) | ~4h | [`01`](./ressources/01_CNN_from_scratch_essentiel.md) / [`02`](./ressources/02_Transfer_learning_essentiel.md) / [`03`](./ressources/03_Zero_shot_CLIP_essentiel.md) selon l'option |
| Vendredi | 4. Comparaison économique (1 mesuré + 2 estimés) | ~1h30 | [`04_Comparaison_economique`](./ressources/04_Comparaison_economique_essentiel.md) |
| Vendredi | 5. Verdict + recommandation | ~30 min | — |
| Vendredi | 6. README + préparation restitution duo | ~1h | — |
| Vendredi | 7. Finition + **test croisé du repo** | ~30 min | [`05`](./ressources/05_Pair_coding_async_essentiel.md) |

> 💡 **Une seule option implémentée** jusqu'à l'inférence — les 2 autres sont
> **estimées** (lisez leurs mini-cours pour pouvoir estimer).

### ✅ Checklist livrables (avant vendredi 17h)

- [ ] `notebooks/` : notebook exécuté de bout en bout
- [ ] `src/option_<x>_*.py` : l'option choisie implémentée
- [ ] `models/` : modèle entraîné **poussé ou régénérable** (script + seed)
- [ ] `decisions.md` : choix d'approche + répartition binôme tracés
- [ ] `economic_comparison.md` : comparatif 3 approches avec sources
- [ ] `verdict.md` : recommandation 8 lignes max, chiffrée
- [ ] Test croisé fait : chacun a cloné et fait tourner le code de l'autre

→ Compétences visées : **C1 — adapter** renforcé + **C4 — adapter** renforcé.

---

## 🚀 Démarrage (5 commandes)

```bash
git clone git@github.com:<owner>/M4-B2-pcb-<binome>.git
cd M4-B2-pcb-<binome>

python -m venv .venv && source .venv/bin/activate
# (variante uv : uv venv .venv && source .venv/bin/activate)

# ⚠️ PyTorch CPU pèse ~200 Mo
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
# (variante uv : uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
#                uv pip install -r requirements.txt)
```

> 🛠️ **Dépannage** : `No module named pip` après `uv venv` → utiliser `uv pip install …`
> (un venv créé par uv n'embarque pas pip).

```bash

# Génère les ~2 100 images PCB (déterministe, seed 42, ~30 s)
python scripts/generate_dataset.py

jupyter notebook notebooks/M4-B2_template.ipynb
```

> 📦 Les ~2 100 images PCB (7 classes = 6 défauts + 1 OK, 64×64) sont **générées par
> `scripts/generate_dataset.py`** dans `data/pcb_defect_sample/`. Synthétiques,
> déterministes (seed 42) → tout le monde a le même jeu. Git-ignorées (on ne
> commite pas la donnée, on la régénère).

---

## 📁 Structure du repo

```
M4-B2-pcb-<binome>/
├── scripts/
│   └── generate_dataset.py              # génère les images PCB (seed 42)
├── data/                                # gitignored
│   └── pcb_defect_sample/               # produit par le script
│       ├── ok/ open/ short/ ...         # 7 classes
├── notebooks/
│   └── M4-B2_template.ipynb
├── src/
│   ├── load_data.py                     # Dataset PyTorch + dataloaders
│   ├── option_a_cnn.py                  # CNN from scratch (TODO si choisi)
│   ├── option_b_transfer.py             # ResNet-18 transfer (TODO si choisi)
│   └── option_c_clip.py                 # CLIP zero-shot (TODO si choisi)
├── models/                              # gitignored
├── ressources/                          # 📚 6 mini-cours
│   ├── README.md
│   ├── 01_CNN_from_scratch_essentiel.md
│   ├── 02_Transfer_learning_essentiel.md
│   ├── 03_Zero_shot_CLIP_essentiel.md
│   ├── 04_Comparaison_economique_essentiel.md
│   ├── 05_Pair_coding_async_essentiel.md
│   ├── 06_Grille_decision_approche_essentiel.md
│   └── liens_officiels.md
├── decisions.md                         # binôme — choix + répartition
├── economic_comparison.md               # comparatif 3 approches
├── verdict.md                           # recommandation 8 lignes
├── requirements.txt
└── .gitignore
```

---

## ⭐ Extensions optionnelles (« cas client avancé »)

> Non notées (bonus qualitatif). **Seulement si le socle est bouclé.** Les 3
> approches restent imposées — c'est la **façon de les implémenter** qui s'ouvre.
> Toute décision ⭐ se justifie dans `decisions.md`.

- ⭐ **CNN** : conçois ton archi (≥ 2 conv + 1 pooling) et **justifie le flatten**.
- ⭐ **Transfer** : choisis ton backbone (ResNet18 / MobileNet / EfficientNet) et justifie.
- ⭐ **CLIP** : prompts libres + explique ta stratégie de prompt engineering.
- ⭐ **Sensibilité au dataset** : change 1-2 paramètres du générateur (bruit dans `augment`, taille/contraste des défauts dans `apply_defect`), régénère, observe comment tes 3 chiffres bougent → les perfs dépendent de la **distribution des données**, pas que du modèle. Aucun résultat imposé ; ne touche pas au dataset figé de ton verdict principal.
- ⭐ **Fine-tuning partiel (option B)** : entraîne le ResNet-18 une première fois backbone **entièrement gelé**, puis dé-gèle **le dernier bloc** (`layer4`) avec un learning rate réduit (ex. `1e-4`) et re-mesure. Que gagne-t-on, que paie-t-on (accuracy, temps de train, risque d'overfitting sur ~1 500 images) ? Documente le delta dans `economic_comparison.md` — c'est un vrai arbitrage d'ingénieur, pas un tuning gratuit.

---

## ✅ Conventions de code

- Python 3.11+, type hints
- `Co-authored-by:` sur les commits significatifs
- Branches nominatives `<prénom>/<feature>`
- Test croisé : chacun clone et fait tourner le code de l'autre

---

## 🆘 Bloqué·e·s ?

1. Relisez le mini-cours de l'option choisie.
2. **Sur PyTorch** : `device = "cpu"` est OK (volume limité). Pas besoin
   de GPU.
3. **Sur CLIP** : ~150 Mo de téléchargement au 1ᵉʳ appel — patience.
4. **Si binôme stuck à 2** : un fait un mini-prototype et MP voix, l'autre
   prend le clavier. Switch.
5. Demande sur Discord (`fil-M4-B2`).
