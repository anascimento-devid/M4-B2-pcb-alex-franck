"""Option B — Transfer learning (ResNet-18 pré-entraîné).

À IMPLÉMENTER si votre binôme choisit l'option B.
Stratégie : freeze backbone + fine-tune classifier head.
Mini-cours d'appui : ressources/02_Transfer_learning_essentiel.md

Note : ResNet attend des images **3 canaux** en **224×224**, normalisées
avec les statistiques ImageNet. Vos PNG sont en niveaux de gris 64×64 :
vos transforms doivent combler cet écart.
"""

from __future__ import annotations

import torch  # noqa: F401 — à utiliser dans ton implémentation
import torch.nn as nn  # noqa: F401
from torchvision import models, transforms  # noqa: F401

from src.load_data import CLASSES


def get_transfer_transforms(image_size: int = 224):
    """Transforms d'entrée pour ResNet.

    À faire (cf. mini-cours 02) : composer les transforms qui amènent un
    PNG niveaux de gris 64×64 au format attendu par ResNet (taille, canaux,
    normalisation — les valeurs ImageNet sont dans la doc torchvision).

    Returns:
        transforms.Compose prêt à passer au Dataset.
    """
    # TODO — composer les transforms ResNet
    raise NotImplementedError(
        "TODO — transforms ResNet (taille, canaux, normalisation)"
    )


def build_resnet18_classifier(
    n_classes: int = len(CLASSES), freeze_backbone: bool = True
):
    """Construit un ResNet-18 pré-entraîné adapté à nos classes.

    Objectif : backbone ImageNet (gelé si `freeze_backbone`), nouvelle tête
    de classification vers `n_classes`.

    Args:
        n_classes: nombre de classes finales.
        freeze_backbone: si True, seule la tête de classification est fine-tunée.

    Returns:
        nn.Module prêt à l'entraînement.
    """
    # TODO — implémenter le transfer learning
    #        (cf. ressources/02_Transfer_learning_essentiel.md)
    raise NotImplementedError("TODO — construire le ResNet-18 + nouvelle tête")


# Pour l'entraînement / l'évaluation, réutilise les boucles `train_one_epoch`
# et `evaluate` que tu écris dans src/option_a_cnn.py (même logique).
