# **Loan Risk & Customer Profiling Analysis — Nettoyage, Feature Engineering & Visualisation**

Ce projet analyse des données de prêts et de clients afin d’évaluer les profils d’emprunteurs, de segmenter les risques et de visualiser les tendances financières.
Réalisé dans un cadre **personnel d’apprentissage**, il met en pratique des compétences clés en **Python**, **pandas**, **feature engineering**, **statistiques**, et **visualisation avancée**.


## 🎯 Objectifs du projet

* Nettoyer et fusionner les données clients et prêts
* Créer des **fonctions métier** pour catégoriser l’usage du prêt, le risque emprunteur et le score FICO
* Enrichir les données avec des features dérivées (risk level, fico category…)
* Visualiser les répartitions des prêts, risques, revenus et scores
* Identifier les profils à risque et comprendre les critères qui les caractérisent


## 🧰 Stack Technique

* **Python 3**
* **pandas** (nettoyage, manipulation, feature engineering)
* **Matplotlib** (visualisations)
* **Seaborn** (plots statistiques)
* Fichiers Excel / CSV en entrée


## 📊 Données utilisées

**1. loan_data (Excel)**
Contient :

* montant du prêt
* score FICO
* debt-to-income ratio (dti)
* historique de délinquance
* taux d'intérêt
* motif du prêt

**2. customer_data (CSV)**
Contient :

* informations d’identification
* historique financier
* déclarations publiques
* revenus

Fusionnées via :

```python
pd.merge(loan_data, customer_data, left_on='customerid', right_on='id')
```


## 🧹 Étapes de préparation & nettoyage

### ✔ Vérification et suppression :

* des **valeurs manquantes**
* des **doublons**
* cohérence des colonnes fusionnées

### ✔ Application de règles métiers via fonctions personnalisées :

#### Catégorisation du “purpose”

```python
if purpose in ['credit_card', 'debt_consolidation']: → Financial
```

#### Évaluation du risque emprunteur

Règle : `dti > 20`, `delinq.2yrs > 2` et `revol.util > 60`
→ High Risk

#### Segmentation du score FICO

* 800–850 → Excellent
* 740–799 → Very Good
* 670–739 → Good
* 580–669 → Fair
* < 580 → Poor

#### Identification des emprunteurs avec anomalies

* Nombre d’enquêtes > moyenne
* Dossiers publics > moyenne


## 🧠 Feature Engineering

Création de nouvelles colonnes :

* `purpose_category`
* `Risk Level`
* `FICO Category`
* `High_Inquieries_and_Public_Records`

Utilisation de fonctions, conditions, `apply()` et calculs dynamiques.


## 📈 Visualisations proposées

### 📌 Distribution des prêts par motif

Analyse du volume emprunté par motif (credit card, debt consolidation, etc.)

### 📌 Scatterplot : revenu annuel vs ratio d’endettement

Permet d’identifier les emprunteurs ayant un DTI anormalement élevé par rapport à leurs revenus.

### 📌 Distribution du score FICO

Analyse de la qualité du portefeuille d’emprunteurs.

### 📌 Subplots combinés

Quatre visuels regroupés :

1. Loan purpose distribution
2. FICO vs DTI
3. Histogramme des FICO
4. Boxplot du taux d'intérêt par niveau de risque


## 📂 Structure du projet

```
loan_risk_analysis/
 ├── loandataset.xlsx
 ├── customer_data.csv
 ├── loan_analysis.py
 ├── README.md
```


## 🧠 Compétences démontrées

✔ Nettoyage structuré de données réelles
✔ Fusion multi-sources (Excel & CSV)
✔ Feature engineering avec règles métiers
✔ Fonctions personnalisées + apply
✔ Utilisation de classes Python pour statistiques
✔ Analyse statistique (FICO, DTI, risk scoring)
✔ Visualisation professionnelle (Seaborn, Matplotlib)
✔ Détection d’emprunteurs à risque
✔ Analyse financière & scoring simplifié


## 🔧 Améliorations possibles

* Ajout d’un modèle prédictif (logistic regression pour prédire le défaut)
* Dashboard Power BI / Tableau
* Analyse temporelle (niveaux de risque dans le temps)
* Optimisation avec pipeline sklearn
* Détection d'anomalies via clustering


## 👤 À propos

Projet réalisé par **Alex Alkhatib**, passionné par l’analyse, la modélisation et la visualisation de données.


## 📄 Licence
MIT License
Copyright (c) 2025 Alex Alkhatib
