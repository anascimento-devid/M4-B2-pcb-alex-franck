# Verdict — Recommandation TechniMatic via Mistral

> 8 lignes maximum.
> Auteurs : Alexandre × Franck — Date : 2026-08-19

**Recommandation** : option B, transfer learning ResNet-18, pour la détection de défauts sur cartes PCB chez TechniMatic.

**Raison principale (chiffrée)** : 80,0 % d'accuracy test contre 59,0 % pour le CNN from scratch, sur le même split. Sur un contrôle qualité, un défaut manqué part en production : l'accuracy prime sur la latence et sur la taille du modèle.

**Condition de changement d'avis** :
- si la latence ou la mémoire deviennent contraignantes (inspection en ligne sur la chaîne), alors CNN from scratch — 2,1 Mo contre 42,7 Mo ;
- si TechniMatic labellisait 10k+ images par classe, alors CNN from scratch aussi — il rattraperait l'accuracy en gardant l'avantage en latence et en coût d'entraînement ;
- si aucune donnée labellisée n'était disponible, alors CLIP zero-shot en MVP, sans en attendre plus de 30 à 60 %.

---

*Verdict binôme — 2026-08-19.*
