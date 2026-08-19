# Comparatif économique 3 approches — PCB Defect

> Document remis à **Inès Tabet** (Mistral) qui relaie à **TechniMatic**.
> Auteurs : `<prénom1>` × `<prénom2>` — Date : `<date>`

## Méthodologie

- **Option implémentée** : mesures **réelles** sur train + inférence
- **2 options non implémentées** : estimations argumentées via sources
  publiques (benchmarks PCB Defect, doc HuggingFace, articles cités)
- ⚠️ **Ordres de grandeur uniquement** : latence, temps d'entraînement et coût
  dépendent fortement du **hardware** (CPU/GPU, RAM, machine). On compare des
  **échelles relatives**, pas des vérités absolues.

## Tableau

| Critère | Option A (CNN scratch) | Option B (Transfer ResNet-18) | Option C (Zero-shot CLIP) |
|---|---|---|---|
| **Données d'entraînement requises** | ~1500 (train) | ~1500 (train) | **0** |
| **Temps train (CPU)** | 72,3 s (8 epochs) | ... | **0** |
| **Latence inférence / image (CPU)** | 2,73 ms | ... | ~80-200 ms (estimé) |
| **Mémoire modèle (Mo)** | 2,1 Mo | ... | ~150 Mo (poids) / ~600 Mo (RAM) (estimé) |
| **Accuracy attendue** | 59,0 % test (mesuré) | ... | ~30-60 % (estimé, dépend fortement des prompts) |
| **Coût € (training cloud)** | ~$0 (CPU local) | ~$0 (CPU local) | $0 |
| **Coût € (API)** | $0 (modèle local) | $0 | $0 (modèle local) |
| **Maintenance** | Réentraîner régulièrement | Réentraîner régulièrement | Aucune (prompts à raffiner) |

**Légende** :
- **Mesuré** : valeur obtenue dans notre implémentation
- **Estimé** : valeur extrapolée de sources publiques (citer)

## Sources des estimations

> Pour les 2 options non implémentées, cite tes sources.

- Option C (Zero-shot CLIP) : selon `ressources/03_Zero_shot_CLIP_essentiel.md` (modèle `openai/clip-vit-base-patch32`, HuggingFace)

## Comparaison qualitative

| Aspect | Option A | Option B | Option C |
|---|---|---|---|
| **Quand préférer** | Beaucoup de données disponibles (10k+/classe idéalement) | ... | MVP rapide sans données labellisées, classes descriptibles en mots |
| **Quand éviter** | Peu de données (< 1k/classe) ; délai court (itérer archi/hyperparamètres prend du temps) ; précision critique (généralise moins bien qu'un backbone pré-entraîné) | ... | Domaine très spécifique ; précision critique (CLIP n'a jamais vu ce type d'image à l'entraînement, il devine sans certitude) ; production temps réel (~80-200 ms/image, bien plus lent qu'un modèle entraîné pour la tâche) |
| **Domaine adapté** | Gros volume de données, domaine très spécifique sans backbone pertinent | ... | Sujets courants trouvés sur internet (objets du quotidien, animaux, paysages) — pas des cartes électroniques en gros plan, trop éloignées de ce que CLIP a appris |

---

*Comparatif produit en binôme — `<date>`.*
