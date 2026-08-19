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

def SimpleTransferModel():
    return build_resnet18_classifier()

def get_transfer_transforms(image_size: int = 224):
    """Transforms d'entrée pour ResNet.

    À faire (cf. mini-cours 02) : composer les transforms qui amènent un
    PNG niveaux de gris 64×64 au format attendu par ResNet (taille, canaux,
    normalisation — les valeurs ImageNet sont dans la doc torchvision).

    Returns:
        transforms.Compose prêt à passer au Dataset.
    """
    return transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.Grayscale(num_output_channels=3),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])


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
    model = models.resnet18(
        weights=models.ResNet18_Weights.IMAGENET1K_V1
    )

    if freeze_backbone:
        for param in model.parameters():
            param.requires_grad = False

    model.fc = nn.Linear(
        model.fc.in_features,
        n_classes,
    )

    return model


# Pour l'entraînement / l'évaluation, réutilise les boucles `train_one_epoch`
# et `evaluate` que tu écris dans src/option_a_cnn.py (même logique).
def train_one_epoch(model, loader, optimizer, criterion, device):
    """Boucle d'entraînement d'1 epoch."""
    model.train()
    total_loss = 0.0
    correct = 0
    total = 0
    for X, y in loader:
        X, y = X.to(device), y.to(device)
        optimizer.zero_grad()
        logits = model(X)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()

        total_loss += loss.item() * X.size(0)
        preds = logits.argmax(dim=1)
        correct += (preds == y).sum().item()
        total += X.size(0)
    return total_loss / total, correct / total


def evaluate(model, loader, criterion, device):
    """Évaluation sur un loader (val ou test)."""
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for X, y in loader:
            X, y = X.to(device), y.to(device)
            logits = model(X)
            loss = criterion(logits, y)
            total_loss += loss.item() * X.size(0)
            preds = logits.argmax(dim=1)
            correct += (preds == y).sum().item()
            total += X.size(0)
    return total_loss / total, correct / total