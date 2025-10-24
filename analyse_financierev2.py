import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import io
from io import BytesIO
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Maîtrise de l'Analyse Financière",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2e86ab;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .concept-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .usage-step {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #ff6b6b;
    }
    .tip-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        background-color: #f8f9fa;
        border-top: 1px solid #dee2e6;
        color: #6c757d;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

def show_footer():
    st.markdown("""
    <div class="footer">
    <strong>Plateforme d'apprentissage de l'analyse financière • Version 3.0</strong><br>
    📚 Développé pour les étudiants, professionnels et entrepreneurs par Amiharbi Eyeug • © 2024
    </div>
    """, unsafe_allow_html=True)

def main():
    # Header principal
    st.markdown('<h1 class="main-header">📊 Maîtrise de l\'Analyse Financière</h1>', unsafe_allow_html=True)
    
    # Navigation par onglets
    tabs = st.tabs([
        "🏠 Accueil & Guide",
        "📈 Concepts Fondamentaux",
        "🧮 Calculateurs",
        "💼 Études de Cas",
        "📚 Ressources"
    ])
    
    with tabs[0]:
        show_accueil_guide()
        show_footer()
    
    with tabs[1]:
        show_concepts_fondamentaux()
        show_footer()
    
    with tabs[2]:
        show_calculateurs()
        show_footer()
    
    with tabs[3]:
        show_etudes_cas()
        show_footer()
    
    with tabs[4]:
        show_ressources()
        show_footer()

def show_accueil_guide():
    st.markdown('<h2 class="section-header">🎯 Guide Complet d\'Utilisation</h2>', unsafe_allow_html=True)
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        ## Bienvenue dans l'application d'analyse financière !
        
        Cette application interactive vous permet de **maîtriser progressivement tous les aspects 
        de l'analyse financière** d'entreprise grâce à une approche pratique basée sur le 
        manuel "Maxi Fiches de Gestion Financière".
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400", 
                caption="Analyse Financière Interactive")
    
    # Mode d'utilisation détaillé
    st.markdown("""
    <div class="concept-card">
    <h3>🚀 Comment Utiliser Cette Application</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Structure de navigation
    st.subheader("📋 Structure de Navigation")
    
    nav_cols = st.columns(5)
    with nav_cols[0]:
        st.info("**🏠 Accueil**\n\nGuide d'utilisation et parcours d'apprentissage")
    with nav_cols[1]:
        st.success("**📈 Concepts**\n\nThéorie avec exemples interactifs")
    with nav_cols[2]:
        st.warning("**🧮 Calculateurs**\n\nOutils pratiques et simulations")
    with nav_cols[3]:
        st.error("**💼 Études de Cas**\n\nSituations réelles avec corrigés")
    with nav_cols[4]:
        st.info("**📚 Ressources**\n\nFiches, quiz et modèles")
    
    # Parcours recommandé selon le niveau
    st.subheader("🎓 Parcours d'Apprentissage Recommandé")
    
    niveau = st.radio("**Sélectionnez votre niveau :**", 
                     ["🟢 Débutant", "🟡 Intermédiaire", "🔴 Avancé"], 
                     horizontal=True)
    
    if niveau == "🟢 Débutant":
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Débutant (20-30 heures)</h4>
        <ol>
            <li><strong>Semaines 1-2 :</strong> Accueil → Concepts (Bilan & Compte de résultat)</li>
            <li><strong>Semaines 3-4 :</strong> Concepts (SIG & Seuil de rentabilité)</li>
            <li><strong>Semaines 5-6 :</strong> Calculateurs basiques → Quiz fondamentaux</li>
            <li><strong>Semaines 7-8 :</strong> Études de cas simples → Ressources</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    elif niveau == "🟡 Intermédiaire":
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Intermédiaire (15-25 heures)</h4>
        <ol>
            <li><strong>Semaines 1-2 :</strong> Revoir Concepts → Calculateurs avancés</li>
            <li><strong>Semaines 3-4 :</strong> Études de cas complexes → Analyse complète</li>
            <li><strong>Semaines 5-6 :</strong> Calculateurs VAN/TIR → Scores financiers</li>
            <li><strong>Semaines 7-8 :</strong> Quiz experts → Modèles personnalisés</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Avancé (10-20 heures)</h4>
        <ol>
            <li><strong>Semaine 1 :</strong> Calculateurs avancés → Diagnostics complexes</li>
            <li><strong>Semaine 2 :</strong> Études de cas experts → Recommandations stratégiques</li>
            <li><strong>Semaine 3 :</strong> Modèles personnalisés → Analyses sectorielles</li>
            <li><strong>Semaine 4 :</strong> Validation complète → Applications pratiques</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Guide détaillé par onglet
    st.subheader("📖 Guide Détaillé par Section")
    
    with st.expander("🏠 ONGLET ACCUEIL & GUIDE", expanded=True):
        st.markdown("""
        **Objectif** : Comprendre le parcours et optimiser votre apprentissage
        
        **Actions clés :**
        - 📊 Identifier votre niveau actuel
        - 🗺️ Suivre le parcours recommandé
        - ⏱️ Planifier votre temps d'apprentissage
        - 🎯 Définir vos objectifs personnels
        
        **Temps recommandé :** 15-30 minutes
        """)
    
    with st.expander("📈 ONGLET CONCEPTS FONDAMENTAUX"):
        st.markdown("""
        **Objectif** : Apprendre la théorie avec des exemples interactifs
        
        **Mode d'emploi :**
        1. **Sélectionnez un concept** dans le menu déroulant
        2. **Lisez les explications** théoriques détaillées
        3. **Utilisez les calculateurs intégrés** pour pratiquer
        4. **Analysez les graphiques** et interprétations automatiques
        
        **Concepts disponibles :**
        - 🔍 Diagnostic Financier
        - ⚖️ Bilan Comptable (avec calculateur d'équilibre)
        - 📊 Compte de Résultat (avec simulateur)
        - 📈 Soldes Intermédiaires de Gestion (SIG)
        - 🎯 Seuil de Rentabilité (avec graphique)
        - 💰 Fonds de Roulement & BFR
        - 📐 Ratios Financiers (avec tableau de bord)
        
        **Temps recommandé :** 2-3 heures par concept
        """)
    
    with st.expander("🧮 ONGLET CALCULATEURS"):
        st.markdown("""
        **Objectif** : Appliquer les concepts avec des outils pratiques
        
        **Calculateurs disponibles :**
        
        **📉 Amortissements** (Linéaire/Dégressif)
        → Saisir : Valeur, durée, coefficient
        → Obtenir : Tableau complet + Graphique
        
        **💸 Capacité d'Autofinancement** (CAF)
        → Saisir : Résultat net, dotations, reprises
        → Obtenir : CAF + Diagnostic automatique
        
        **⚖️ Effet de Levier Financier**
        → Saisir : Actif, capitaux, dettes, taux
        → Obtenir : Rentabilité économique vs financière
        
        **📊 VAN/TIR** (Investissements)
        → Saisir : Investissement, flux, durée
        → Obtenir : VAN + TIR + Recommandation
        
        **🎯 Score Financier** (Risque défaillance)
        → Saisir : EBE, endettement, ratios clés
        → Obtenir : Score + Diagnostic risque
        
        **Temps recommandé :** 1-2 heures par calculateur
        """)
    
    with st.expander("💼 ONGLET ÉTUDES DE CAS"):
        st.markdown("""
        **Objectif** : Mettre en pratique sur des situations réelles
        
        **Méthodologie :**
        1. **Lire le contexte** de l'entreprise
        2. **Analyser les données** financières fournies
        3. **Choisir le type d'analyse** à réaliser
        4. **Comparer vos résultats** avec la correction
        5. **Comprendre les recommandations**
        
        **Cas disponibles :**
        - 🏭 PME Industrielle (analyse complète)
        - 📈 Analyse de Rentabilité
        - ⚖️ Équilibre Financier
        - 💧 Tableaux de Flux
        - 🏗️ Projet d'Investissement
        
        **Temps recommandé :** 2-4 heures par étude de cas
        """)
    
    with st.expander("📚 ONGLET RESSOURCES"):
        st.markdown("""
        **Objectif** : Consolider et tester ses connaissances
        
        **Ressources disponibles :**
        
        **📖 Fiches Mémo Téléchargeables**
        - Formats : PDF/Excel
        - Thèmes : Bilan, Compte de résultat, Ratios, etc.
        - Utilisation : Révisions rapides
        
        **🎓 Quiz d'Auto-évaluation**
        - Niveaux : Débutant à Expert
        - Correction immédiate avec explications
        - Score final avec recommandations
        
        **📊 Modèles et Templates**
        - Fichiers Excel réutilisables
        - Tableaux pré-formatés
        - Calculateurs personnalisables
        
        **Temps recommandé :** 30 minutes à 1 heure par ressource
        """)
    
    # Conseils d'optimisation
    st.subheader("💡 Conseils d'Optimisation")
    
    tip_cols = st.columns(3)
    
    with tip_cols[0]:
        st.markdown("""
        <div class="tip-box">
        <h5>🎮 Pour les Débutants</h5>
        - Suivez le parcours recommandé
        - Prenez des notes dans chaque section
        - Refaites les exercices plusieurs fois
        - Utilisez systématiquement les calculateurs
        </div>
        """, unsafe_allow_html=True)
    
    with tip_cols[1]:
        st.markdown("""
        <div class="tip-box">
        <h5>🚀 Pour les Intermédiaires</h5>
        - Testez différents scénarios
        - Comparez vos analyses avec les corrigés
        - Personnalisez les paramètres
        - Téléchargez les modèles pour vos projets
        </div>
        """, unsafe_allow_html=True)
    
    with tip_cols[2]:
        st.markdown("""
        <div class="tip-box">
        <h5>🏆 Pour les Experts</h5>
        - Utilisez les études de cas complexes
        - Développez vos propres scénarios
        - Intégrez les modèles dans vos outils
        - Validez vos méthodologies d'analyse
        </div>
        """, unsafe_allow_html=True)
    
    # Progression globale
    st.subheader("📊 Progression Globale Recommandée")
    
    progress_data = {
        "Module": ["Fondamentaux", "Bilan & Compte de résultat", "Ratios & SIG", 
                  "Analyse fonctionnelle", "Tableaux de flux", "Diagnostic avancé"],
        "Durée estimée": ["2 semaines", "3 semaines", "2 semaines", "2 semaines", "3 semaines", "2 semaines"],
        "Difficulté": ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        "Onglets clés": ["Concepts", "Concepts + Calculateurs", "Calculateurs + Cas", 
                        "Cas + Calculateurs", "Cas + Ressources", "Tous les onglets"]
    }
    
    df_progress = pd.DataFrame(progress_data)
    st.dataframe(df_progress, use_container_width=True)
    
    # Derniers conseils
    st.markdown("""
    <div class="tip-box">
    <h5>💎 Derniers Conseils Importants</h5>
    - <strong>Sauvegardez</strong> vos paramètres intéressants
    - <strong>Téléchargez</strong> les résultats importants  
    - <strong>Expérimentez</strong> avec différentes valeurs
    - <strong>Consultez</strong> les explications détaillées
    - <strong>Pratiquez</strong> régulièrement pour progresser
    </div>
    """, unsafe_allow_html=True)

def show_concepts_fondamentaux():
    st.markdown('<h2 class="section-header">📈 Concepts Fondamentaux</h2>', unsafe_allow_html=True)
    
    # Guide rapide d'utilisation
    st.info("""
    **🎯 Comment utiliser cette section :**
    1. Sélectionnez un concept dans le menu ci-dessous
    2. Lisez les explications théoriques détaillées  
    3. Utilisez les calculateurs intégrés pour pratiquer
    4. Analysez les graphiques et interprétations automatiques
    """)
    
    concept_choice = st.selectbox(
        "**Choisissez un concept à explorer :**",
        [
            "🔍 Diagnostic Financier",
            "⚖️ Bilan Comptable", 
            "📊 Compte de Résultat",
            "📈 Soldes Intermédiaires de Gestion",
            "🎯 Seuil de Rentabilité",
            "💰 Fonds de Roulement",
            "📐 Ratios Financiers"
        ]
    )
    
    if "Diagnostic Financier" in concept_choice:
        show_diagnostic_financier()
    elif "Bilan Comptable" in concept_choice:
        show_bilan_comptable()
    elif "Compte de Résultat" in concept_choice:
        show_compte_resultat()
    elif "Soldes Intermédiaires" in concept_choice:
        show_soldes_gestion()
    elif "Seuil de Rentabilité" in concept_choice:
        show_seuil_rentabilite()
    elif "Fonds de Roulement" in concept_choice:
        show_fonds_roulement()
    elif "Ratios Financiers" in concept_choice:
        show_ratios_financiers()

def show_diagnostic_financier():
    st.markdown("""
    <div class="concept-card">
    <h3>🔍 Diagnostic Financier</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **📖 Définition :**
        Le diagnostic financier est une démarche qui vise à :
        - Identifier les causes de difficultés présentes ou futures
        - Mettre en lumière les dysfonctionnements
        - Présenter les perspectives d'évolution
        - Proposer des actions correctives
        
        **📋 États financiers analysés :**
        - Bilan (patrimoine à une date donnée)
        - Compte de résultat (performance sur une période)
        - Annexe (informations complémentaires)
        """)
    
    with col2:
        st.write("""
        **🛠️ Méthodologie :**
        1. Analyse de la rentabilité
        2. Analyse de la liquidité
        3. Analyse de la structure financière
        4. Analyse économique complémentaire
        
        **📊 Outils :**
        - Ratios financiers
        - Tableaux de flux
        - Soldes intermédiaires de gestion
        - Comparaisons sectorielles
        """)
    
    # Schéma du processus de diagnostic
    st.subheader("📋 Processus de Diagnostic")
    
    steps = {
        "Étape 1": "Collecte des états financiers",
        "Étape 2": "Analyse horizontale et verticale", 
        "Étape 3": "Calcul des ratios",
        "Étape 4": "Analyse fonctionnelle",
        "Étape 5": "Diagnostic et recommandations"
    }
    
    for step, description in steps.items():
        st.write(f"**{step}:** {description}")

def show_bilan_comptable():
    st.markdown("""
    <div class="concept-card">
    <h3>⚖️ Bilan Comptable</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Photographie du patrimoine de l'entreprise à une date donnée.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("ACTIF")
        st.write("""
        **Actif Immobilisé:**
        - Immobilisations incorporelles
        - Immobilisations corporelles  
        - Immobilisations financières
        
        **Actif Circulant:**
        - Stocks
        - Créances clients
        - Disponibilités
        """)
    
    with col2:
        st.subheader("PASSIF")
        st.write("""
        **Capitaux Propres:**
        - Capital social
        - Réserves
        - Résultat de l'exercice
        
        **Dettes:**
        - Dettes financières
        - Dettes fournisseurs
        - Dettes fiscales et sociales
        """)
    
    # Calculateur simplifié de bilan
    st.subheader("🧮 Calculateur de Bilan - Pratiquez !")
    
    st.warning("💡 **Exercice :** Essayez de créer un bilan équilibré en ajustant les valeurs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Actif**")
        immob_corporelles = st.number_input("Immobilisations corporelles", value=500000, key="actif1")
        stocks = st.number_input("Stocks", value=200000, key="actif2")
        clients = st.number_input("Créances clients", value=300000, key="actif3")
        disponibilites = st.number_input("Disponibilités", value=100000, key="actif4")
        
        total_actif = immob_corporelles + stocks + clients + disponibilites
        
    with col2:
        st.write("**Passif**")
        capital = st.number_input("Capital social", value=400000, key="passif1")
        reserves = st.number_input("Réserves", value=300000, key="passif2")
        resultat = st.number_input("Résultat", value=100000, key="passif3")
        emprunts = st.number_input("Emprunts", value=200000, key="passif4")
        fournisseurs = st.number_input("Dettes fournisseurs", value=100000, key="passif5")
        
        total_passif = capital + reserves + resultat + emprunts + fournisseurs
    
    # Vérification équilibre
    st.subheader("📊 Résultat de l'Exercice")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Actif", f"{total_actif:,.0f} €")
    with col2:
        st.metric("Total Passif", f"{total_passif:,.0f} €")
    with col3:
        difference = total_actif - total_passif
        if abs(difference) < 1:
            st.success("✅ Bilan Équilibré")
        else:
            st.error(f"❌ Écart : {difference:,.0f} €")

def show_compte_resultat():
    st.markdown("""
    <div class="concept-card">
    <h3>📊 Compte de Résultat</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Mesure la performance économique sur une période (généralement un an).
    """)
    
    # Structure du compte de résultat
    st.subheader("🏗️ Structure du Compte de Résultat")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **CHARGES**
        - Achats de marchandises
        - Variation de stocks
        - Charges externes
        - Impôts et taxes
        - Charges de personnel
        - Dotations aux amortissements
        - Charges financières
        - Charges exceptionnelles
        """)
    
    with col2:
        st.write("""
        **PRODUITS**
        - Ventes de marchandises
        - Production vendue
        - Production stockée
        - Production immobilisée
        - Subventions d'exploitation
        - Produits financiers
        - Produits exceptionnels
        """)
    
    # Calculateur de résultat
    st.subheader("🧮 Calculateur de Résultat - Expérimentez !")
    
    st.info("💡 **Conseil :** Modifiez les valeurs pour comprendre leur impact sur le résultat")
    
    ca = st.number_input("Chiffre d'affaires HT (€)", value=1000000, key="cr_ca")
    achats = st.number_input("Achats consommés (€)", value=400000, key="cr_achats")
    charges_personnel = st.number_input("Charges de personnel (€)", value=300000, key="cr_pers")
    dotations_amort = st.number_input("Dotations aux amortissements (€)", value=50000, key="cr_amort")
    charges_financieres = st.number_input("Charges financières (€)", value=20000, key="cr_fin")
    
    # Calculs
    resultat_exploitation = ca - achats - charges_personnel - dotations_amort
    resultat_courant = resultat_exploitation - charges_financieres
    
    # Affichage résultats
    st.subheader("📈 Résultats Calculés")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Résultat d'Exploitation", f"{resultat_exploitation:,.0f} €")
        st.metric("Taux de marge d'exploitation", f"{(resultat_exploitation/ca*100):.1f}%" if ca > 0 else "0%")
    
    with col2:
        st.metric("Résultat Courant", f"{resultat_courant:,.0f} €")
        st.metric("Taux de marge nette", f"{(resultat_courant/ca*100):.1f}%" if ca > 0 else "0%")

def show_soldes_gestion():
    st.markdown("""
    <div class="concept-card">
    <h3>📈 Soldes Intermédiaires de Gestion</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Les SIG permettent de décomposer la formation du résultat en plusieurs niveaux.")
    
    # Calculateur des SIG
    st.subheader("🧮 Calculateur des SIG")
    
    ca = st.number_input("Chiffre d'affaires", value=1000000, key="sig_ca")
    achats_marches = st.number_input("Achats de marchandises", value=300000, key="sig_achats")
    prod_vendue = st.number_input("Production vendue", value=800000, key="sig_prod")
    consommations = st.number_input("Consommations externes", value=200000, key="sig_cons")
    charges_personnel = st.number_input("Charges de personnel", value=350000, key="sig_pers")
    
    # Calcul des SIG
    marge_commerciale = ca - achats_marches
    valeur_ajoutee = marge_commerciale + prod_vendue - consommations
    ebe = valeur_ajoutee - charges_personnel
    
    # Affichage des résultats
    st.subheader("📊 Résultats des SIG")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Marge Commerciale", f"{marge_commerciale:,.0f} €")
        st.metric("Taux de marge", f"{(marge_commerciale/ca*100):.1f} %")
    
    with col2:
        st.metric("Valeur Ajoutée", f"{valeur_ajoutee:,.0f} €")
        st.metric("Taux de VA", f"{(valeur_ajoutee/ca*100):.1f} %")
    
    with col3:
        st.metric("EBE", f"{ebe:,.0f} €")
        st.metric("Taux EBE", f"{(ebe/ca*100):.1f} %")

def show_seuil_rentabilite():
    st.markdown("""
    <div class="concept-card">
    <h3>🎯 Seuil de Rentabilité</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Niveau de chiffre d'affaires pour lequel le résultat est nul.
    
    **🧮 Formule :** SR = Charges Fixes / Taux de Marge sur Coût Variable
    """)
    
    # Calculateur de seuil de rentabilité
    st.subheader("🧮 Calculateur de Seuil de Rentabilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        charges_fixes = st.number_input("Charges fixes annuelles (€)", value=300000)
        ca_prev = st.number_input("Chiffre d'affaires prévisionnel (€)", value=1000000)
    
    with col2:
        charges_variables = st.number_input("Charges variables (€)", value=500000)
    
    # Calculs
    mcv = ca_prev - charges_variables
    taux_mcv = mcv / ca_prev if ca_prev > 0 else 0
    seuil_rentabilite = charges_fixes / taux_mcv if taux_mcv > 0 else 0
    marge_securite = ((ca_prev - seuil_rentabilite) / ca_prev * 100) if ca_prev > 0 else 0
    
    # Résultats
    st.subheader("📈 Résultats")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Taux MCV", f"{taux_mcv*100:.1f} %")
    
    with col2:
        st.metric("Seuil Rentabilité", f"{seuil_rentabilite:,.0f} €")
    
    with col3:
        st.metric("Marge de Sécurité", f"{marge_securite:.1f} %")
    
    # Graphique
    if seuil_rentabilite > 0:
        st.subheader("📊 Graphique de Visualisation")
        x = np.linspace(0, ca_prev * 1.5, 100)
        y_charges_fixes = np.full_like(x, charges_fixes)
        y_charges_variables = charges_variables/ca_prev * x if ca_prev > 0 else 0
        y_charges_totales = y_charges_fixes + y_charges_variables
        y_ca = x
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y_charges_fixes, name='Charges Fixes', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=x, y=y_charges_totales, name='Charges Totales', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=x, y=y_ca, name='Chiffre d\'affaires', line=dict(color='green')))
        
        # Point de seuil
        fig.add_trace(go.Scatter(x=[seuil_rentabilite], y=[seuil_rentabilite], 
                               mode='markers', name='Seuil', marker=dict(size=10, color='orange')))
        
        fig.update_layout(title='Seuil de Rentabilité', xaxis_title='Chiffre d\'affaires (€)', yaxis_title='Montants (€)')
        st.plotly_chart(fig)

def show_fonds_roulement():
    st.markdown("""
    <div class="concept-card">
    <h3>💰 Fonds de Roulement et BFR</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **🧮 Formules :**
    - FRNG = Ressources Stables - Emplois Stables
    - BFR = Actif Circulant - Passif Circulant  
    - Trésorerie = FRNG - BFR
    """)
    
    # Calculateur FRNG/BFR
    st.subheader("🧮 Calculateur d'Équilibre Financier")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Ressources Stables**")
        capitaux_propres = st.number_input("Capitaux propres (€)", value=800000)
        dettes_long_terme = st.number_input("Dettes long terme (€)", value=200000)
    
    with col2:
        st.write("**Emplois Stables**")
        immob_brutes = st.number_input("Immobilisations brutes (€)", value=700000)
    
    with col3:
        st.write("**BFR**")
        stocks = st.number_input("Stocks (€)", value=150000, key="bfr_stocks")
        clients = st.number_input("Créances clients (€)", value=200000)
        fournisseurs = st.number_input("Dettes fournisseurs (€)", value=120000)
    
    # Calculs
    ressources_stables = capitaux_propres + dettes_long_terme
    emplois_stables = immob_brutes
    frng = ressources_stables - emplois_stables
    
    actif_circulant = stocks + clients
    passif_circulant = fournisseurs
    bfr = actif_circulant - passif_circulant
    tresorerie = frng - bfr
    
    # Affichage résultats
    st.subheader("📊 Diagnostic Financier")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        color = "green" if frng > 0 else "red"
        st.metric("FRNG", f"{frng:,.0f} €", delta="✅ Bon" if frng > 0 else "❌ Risque", delta_color=color)
    
    with col2:
        color = "normal" 
        st.metric("BFR", f"{bfr:,.0f} €", delta="📈 Besoin" if bfr > 0 else "📉 Ressource")
    
    with col3:
        color = "green" if tresorerie > 0 else "red"
        st.metric("Trésorerie", f"{tresorerie:,.0f} €", delta="✅ Excédent" if tresorerie > 0 else "❌ Déficit", delta_color=color)

def show_ratios_financiers():
    st.markdown("""
    <div class="concept-card">
    <h3>📐 Ratios Financiers</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur de ratios
    st.subheader("🧮 Calculateur de Ratios")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ca = st.number_input("Chiffre d'affaires (€)", value=1000000, key="ratio_ca")
        resultat_net = st.number_input("Résultat net (€)", value=80000)
        capitaux_propres = st.number_input("Capitaux propres (€)", value=400000, key="ratio_cp")
        ebe = st.number_input("EBE (€)", value=150000)
    
    with col2:
        total_actif = st.number_input("Total actif (€)", value=800000)
        dettes_financieres = st.number_input("Dettes financières (€)", value=200000)
        actif_circulant = st.number_input("Actif circulant (€)", value=300000)
        dettes_court_terme = st.number_input("Dettes court terme (€)", value=180000)
    
    # Calcul des ratios
    rentabilite_net = (resultat_net / ca * 100) if ca > 0 else 0
    rentabilite_financiere = (resultat_net / capitaux_propres * 100) if capitaux_propres > 0 else 0
    rentabilite_economique = (ebe / total_actif * 100) if total_actif > 0 else 0
    endettement = (dettes_financieres / capitaux_propres * 100) if capitaux_propres > 0 else 0
    liquidite = (actif_circulant / dettes_court_terme * 100) if dettes_court_terme > 0 else 0
    
    # Affichage des ratios
    st.subheader("📊 Tableau de Bord des Ratios")
    
    ratios_data = {
        "Ratio": ["Rentabilité nette", "Rentabilité financière", "Rentabilité économique", "Taux d'endettement", "Ratio de liquidité"],
        "Valeur": [f"{rentabilite_net:.1f}%", f"{rentabilite_financiere:.1f}%", f"{rentabilite_economique:.1f}%", f"{endettement:.1f}%", f"{liquidite:.1f}%"],
        "Interprétation": [
            "✅ Bon" if rentabilite_net > 2 else "⚠️ À améliorer",
            "✅ Bon" if rentabilite_financiere > 8 else "⚠️ À améliorer", 
            "✅ Bon" if rentabilite_economique > 10 else "⚠️ À améliorer",
            "✅ Bon" if endettement < 100 else "❌ Trop élevé",
            "✅ Bon" if liquidite > 100 else "❌ Risque liquidité"
        ]
    }
    
    df_ratios = pd.DataFrame(ratios_data)
    st.dataframe(df_ratios, use_container_width=True)

def show_calculateurs():
    st.markdown('<h2 class="section-header">🧮 Calculateurs Interactifs</h2>', unsafe_allow_html=True)
    
    # Guide d'utilisation
    st.success("""
    **🎯 Comment utiliser les calculateurs :**
    1. Sélectionnez un calculateur dans le menu
    2. Saisissez vos données dans les champs
    3. Analysez les résultats calculés automatiquement
    4. Consultez les graphiques et recommandations
    """)
    
    calc_choice = st.selectbox(
        "**Choisissez un calculateur :**",
        [
            "📉 Amortissements",
            "💸 Capacité d'Autofinancement", 
            "⚖️ Effet de Levier",
            "📊 VAN et TIR",
            "🎯 Score Financier"
        ]
    )
    
    if "Amortissements" in calc_choice:
        show_calculateur_amortissements()
    elif "Capacité d'Autofinancement" in calc_choice:
        show_calculateur_caf()
    elif "Effet de Levier" in calc_choice:
        show_calculateur_levier()
    elif "VAN et TIR" in calc_choice:
        show_calculateur_van_tir()
    elif "Score Financier" in calc_choice:
        show_calculateur_score()

def show_calculateur_amortissements():
    st.subheader("📉 Calculateur d'Amortissements")
    
    st.info("""
    **💡 À savoir :**
    - **Amortissement linéaire** : Constant chaque année
    - **Amortissement dégressif** : Décroissant, avec coefficient
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        valeur_origine = st.number_input("Valeur d'origine (€)", value=100000)
        duree = st.number_input("Durée d'amortissement (années)", value=5, min_value=1)
        mode = st.radio("Mode d'amortissement", ["Linéaire", "Dégressif"])
    
    with col2:
        date_acquisition = st.date_input("Date d'acquisition", value=datetime(2023, 1, 1))
        coefficient = st.selectbox("Coefficient dégressif", [1.25, 1.75, 2.25]) if mode == "Dégressif" else 0
    
    # Calcul du plan d'amortissement
    if st.button("📊 Calculer le plan d'amortissement"):
        annees = list(range(1, duree + 1))
        vnc = [valeur_origine]
        amortissements = []
        amort_cumules = [0]
        
        for annee in annees:
            if mode == "Linéaire":
                amort_annuel = valeur_origine / duree
            else:
                taux_lineaire = 100 / duree
                taux_degressif = taux_lineaire * coefficient
                amort_annuel = vnc[-1] * taux_degressif / 100
            
            amortissements.append(amort_annuel)
            amort_cumules.append(amort_cumules[-1] + amort_annuel)
            vnc.append(vnc[-1] - amort_annuel)
        
        # DataFrame des résultats
        df_amort = pd.DataFrame({
            'Année': annees,
            'VNC début': [f"{v:,.0f} €" for v in vnc[:-1]],
            'Amortissement annuel': [f"{a:,.0f} €" for a in amortissements],
            'Amortissement cumulé': [f"{a:,.0f} €" for a in amort_cumules[1:]],
            'VNC fin': [f"{v:,.0f} €" for v in vnc[1:]]
        })
        
        st.dataframe(df_amort, use_container_width=True)
        
        # Graphique
        fig = go.Figure()
        fig.add_trace(go.Bar(x=annees, y=amortissements, name='Amortissement annuel'))
        fig.add_trace(go.Scatter(x=annees, y=vnc[1:], name='VNC fin d\'année', line=dict(color='red')))
        fig.update_layout(title='Plan d\'amortissement', xaxis_title='Années', yaxis_title='Montants (€)')
        st.plotly_chart(fig)

def show_calculateur_caf():
    st.subheader("💸 Calculateur de Capacité d'Autofinancement")
    
    st.write("**🧮 Méthode additive : CAF = Résultat net + Dotations - Reprises - Produits de cession**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        resultat_net = st.number_input("Résultat net (€)", value=50000)
        dotations_amort = st.number_input("Dotations aux amortissements (€)", value=20000)
        dotations_provisions = st.number_input("Dotations aux provisions (€)", value=5000)
    
    with col2:
        reprises_amort = st.number_input("Reprises sur amortissements (€)", value=0)
        reprises_provisions = st.number_input("Reprises sur provisions (€)", value=0)
        produits_cession = st.number_input("Produits de cession (€)", value=0)
    
    caf = (resultat_net + dotations_amort + dotations_provisions - 
           reprises_amort - reprises_provisions - produits_cession)
    
    st.metric("Capacité d'Autofinancement", f"{caf:,.0f} €")
    
    # Interprétation
    if caf > resultat_net:
        st.success("✅ La CAF est supérieure au résultat net : bonne capacité d'autofinancement")
    else:
        st.warning("⚠️ La CAF est proche ou inférieure au résultat net : capacité d'autofinancement limitée")
def show_calculateur_score():
    st.subheader("🎯 Calculateur de Score Financier")
    
    st.write("Évaluation du risque de défaillance selon la méthode des scores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ebe = st.number_input("EBE (€)", value=150000, key="score_ebe")
        endettement_global = st.number_input("Endettement global (€)", value=500000, key="score_endettement")
        capitaux_permanents = st.number_input("Capitaux permanents (€)", value=800000, key="score_capitaux")
    
    with col2:
        actif_total = st.number_input("Actif total (€)", value=1000000, key="score_actif")
        frais_financiers = st.number_input("Frais financiers (€)", value=20000, key="score_frais_fin")
        ca = st.number_input("Chiffre d'affaires (€)", value=1000000, key="score_ca")
        charges_personnel = st.number_input("Charges de personnel (€)", value=350000, key="score_charges_pers")
        valeur_ajoutee = st.number_input("Valeur ajoutée (€)", value=500000, key="score_va")
    
    # Calcul du score Conan et Holder
    X1 = ebe / endettement_global if endettement_global > 0 else 0
    X2 = capitaux_permanents / actif_total if actif_total > 0 else 0
    X3 = 0.3  # Approximation pour réalisable et disponible
    X4 = frais_financiers / ca if ca > 0 else 0
    X5 = charges_personnel / valeur_ajoutee if valeur_ajoutee > 0 else 0
    
    score = 24*X1 + 22*X2 + 16*X3 - 87*X4 - 10*X5
    
    st.metric("Score financier", f"{score:.2f}")
    
    # Interprétation
    if score > 9.5:
        st.success("✅ Situation financière saine")
    elif score > -4.5:
        st.warning("⚠️ Situation à surveiller")
    else:
        st.error("❌ Situation risquée - Attention !")

def show_calculateur_van_tir():
    st.subheader("📊 Calculateur VAN et TIR")
    
    st.write("Évaluation de la rentabilité d'un projet d'investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investissement_initial = st.number_input("Investissement initial (€)", value=100000, key="van_invest")
        duree_projet = st.number_input("Durée du projet (années)", value=5, key="van_duree")
        taux_actualisation = st.number_input("Taux d'actualisation (%)", value=8.0, key="van_taux") / 100
    
    with col2:
        st.write("Flux de trésorerie annuels")
        flux = []
        for i in range(duree_projet):
            flux.append(st.number_input(f"Année {i+1} (€)", value=30000, key=f"van_flux_{i}"))
    
    if st.button("📈 Calculer VAN et TIR", key="van_btn"):
        # Calcul VAN
        van = -investissement_initial
        for i, flux_annuel in enumerate(flux):
            van += flux_annuel / ((1 + taux_actualisation) ** (i + 1))
        
        # Estimation TIR (méthode simplifiée)
        def calcul_van(taux):
            van_calc = -investissement_initial
            for i, flux_annuel in enumerate(flux):
                van_calc += flux_annuel / ((1 + taux) ** (i + 1))
            return van_calc
        
        # Recherche du TIR par approximation
        tir = taux_actualisation
        for taux_test in np.arange(0.01, 1.0, 0.01):
            if calcul_van(taux_test) >= 0:
                tir = taux_test
            else:
                break
        
        st.subheader("🎯 Résultats")
        
        col1, col2 = st.columns(2)
        with col1:
            delta_color = "normal" if van > 0 else "inverse"
            st.metric(
                "VAN", 
                f"{van:,.0f} €", 
                delta="✅ Projet rentable" if van > 0 else "❌ Projet non rentable",
                delta_color=delta_color
            )
        with col2:
            st.metric("TIR approximatif", f"{tir*100:.1f}%")

def show_calculateur_van_tir():
    st.subheader("📊 Calculateur VAN et TIR")
    
    st.write("Évaluation de la rentabilité d'un projet d'investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investissement_initial = st.number_input("Investissement initial (€)", value=100000)
        duree_projet = st.number_input("Durée du projet (années)", value=5)
        taux_actualisation = st.number_input("Taux d'actualisation (%)", value=8.0) / 100
    
    with col2:
        st.write("Flux de trésorerie annuels")
        flux = []
        for i in range(duree_projet):
            flux.append(st.number_input(f"Année {i+1} (€)", value=30000, key=f"flux_{i}"))
    
    if st.button("📈 Calculer VAN et TIR"):
        # Calcul VAN
        van = -investissement_initial
        for i, flux_annuel in enumerate(flux):
            van += flux_annuel / ((1 + taux_actualisation) ** (i + 1))
        
        # Estimation TIR (méthode simplifiée)
        def calcul_van(taux):
            van_calc = -investissement_initial
            for i, flux_annuel in enumerate(flux):
                van_calc += flux_annuel / ((1 + taux) ** (i + 1))
            return van_calc
        
        # Recherche du TIR par approximation
        tir = taux_actualisation
        for taux_test in np.arange(0.01, 1.0, 0.01):
            if calcul_van(taux_test) >= 0:
                tir = taux_test
            else:
                break
        
        st.subheader("🎯 Résultats")
        
        col1, col2 = st.columns(2)
        with col1:
            # CORRECTION : Utiliser 'normal' pour les valeurs positives et 'inverse' pour les négatives
            delta_color = "normal" if van > 0 else "inverse"
            st.metric("VAN", f"{van:,.0f} €", 
                     delta="✅ Projet rentable" if van > 0 else "❌ Projet non rentable",
                     delta_color=delta_color)  # Utiliser delta_color au lieu de color
        with col2:
            st.metric("TIR approximatif", f"{tir*100:.1f}%")
def show_calculateur_levier():
    st.subheader("⚖️ Calculateur d'Effet de Levier Financier")
    
    col1, col2 = st.columns(2)
    
    with col1:
        actif_economique = st.number_input("Actif économique (€)", value=1000000, key="levier_actif")
        resultat_exploitation = st.number_input("Résultat d'exploitation (€)", value=120000, key="levier_re")
        capitaux_propres = st.number_input("Capitaux propres (€)", value=600000, key="levier_cp")
    
    with col2:
        dettes_financieres = st.number_input("Dettes financières (€)", value=400000, key="levier_dettes")
        taux_impot = st.number_input("Taux d'impôt (%)", value=25.0, key="levier_impot") / 100
        taux_interet = st.number_input("Taux d'intérêt (%)", value=4.0, key="levier_interet") / 100
    
    # Calculs
    re_apres_impot = resultat_exploitation * (1 - taux_impot)
    rentabilite_economique = re_apres_impot / actif_economique
    
    charges_financieres = dettes_financieres * taux_interet
    cf_apres_impot = charges_financieres * (1 - taux_impot)
    
    resultat_net = re_apres_impot - cf_apres_impot
    rentabilite_financiere = resultat_net / capitaux_propres
    
    effet_levier = rentabilite_financiere - rentabilite_economique
    
    # Affichage
    st.subheader("📈 Résultats")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Rentabilité économique", f"{rentabilite_economique*100:.1f}%")
    
    with col2:
        st.metric("Rentabilité financière", f"{rentabilite_financiere*100:.1f}%")
    
    with col3:
        # CORRECTION : Utiliser 'normal' pour positif et 'inverse' pour négatif
        delta_color = "normal" if effet_levier > 0 else "inverse"
        st.metric(
            "Effet de levier", 
            f"{effet_levier*100:.1f}%", 
            delta="✅ Positif" if effet_levier > 0 else "❌ Négatif", 
            delta_color=delta_color
        )
def show_calculateur_score():
    st.subheader("🎯 Calculateur de Score Financier")
    
    st.write("Évaluation du risque de défaillance selon la méthode des scores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ebe = st.number_input("EBE (€)", value=150000)
        endettement_global = st.number_input("Endettement global (€)", value=500000)
        capitaux_permanents = st.number_input("Capitaux permanents (€)", value=800000)
    
    with col2:
        actif_total = st.number_input("Actif total (€)", value=1000000)
        frais_financiers = st.number_input("Frais financiers (€)", value=20000)
        ca = st.number_input("Chiffre d'affaires (€)", value=1000000)
        charges_personnel = st.number_input("Charges de personnel (€)", value=350000)
        valeur_ajoutee = st.number_input("Valeur ajoutée (€)", value=500000)
    
    # Calcul du score Conan et Holder
    X1 = ebe / endettement_global if endettement_global > 0 else 0
    X2 = capitaux_permanents / actif_total if actif_total > 0 else 0
    X3 = 0.3  # Approximation pour réalisable et disponible
    X4 = frais_financiers / ca if ca > 0 else 0
    X5 = charges_personnel / valeur_ajoutee if valeur_ajoutee > 0 else 0
    
    score = 24*X1 + 22*X2 + 16*X3 - 87*X4 - 10*X5
    
    st.metric("Score financier", f"{score:.2f}")
    
    # Interprétation
    if score > 9.5:
        st.success("✅ Situation financière saine")
    elif score > -4.5:
        st.warning("⚠️ Situation à surveiller")
    else:
        st.error("❌ Situation risquée - Attention !")


def show_etudes_cas():
    st.markdown('<h2 class="section-header">💼 Études de Cas Pratiques</h2>', unsafe_allow_html=True)
    
    st.success("""
    **🎯 Méthodologie recommandée :**
    1. **Lire** attentivement le contexte de l'entreprise
    2. **Analyser** les données financières fournies  
    3. **Choisir** le type d'analyse à réaliser
    4. **Comparer** vos résultats avec la correction
    5. **Comprendre** les recommandations stratégiques
    """)
    
    cas_choice = st.selectbox(
        "**Choisissez une étude de cas :**",
        [
            "🏭 Diagnostic PME industrielle",
            "📈 Analyse de rentabilité", 
            "⚖️ Équilibre financier",
            "💧 Tableau de flux",
            "🏗️ Projet d'investissement"
        ]
    )
    
    if "PME industrielle" in cas_choice:
        show_cas_pme()
    elif "rentabilité" in cas_choice:
        show_cas_rentabilite()
    elif "Équilibre financier" in cas_choice:
        show_cas_equilibre()
    elif "Tableau de flux" in cas_choice:
        show_cas_flux()
    elif "Projet d'investissement" in cas_choice:
        show_cas_investissement()

def show_cas_pme():
    st.subheader("🏭 Diagnostic d'une PME Industrielle")
    
    st.write("""
    **📋 Contexte :** Société DUBOIS, fabricant de composants électroniques
    - Chiffre d'affaires : 2,5 M€
    - Effectif : 45 personnes
    - Marché en croissance mais concurrence forte
    """)
    
    # Données financières
    st.subheader("📊 Données financières")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Compte de résultat (k€)**")
        data_compte = {
            'Poste': ['Chiffre d\'affaires', 'Achats consommés', 'Charges personnel', 'EBE', 'Dotations amortissement', 'Résultat exploitation'],
            'N': [2500, 1200, 800, 500, 150, 200],
            'N-1': [2300, 1150, 750, 400, 140, 150]
        }
        df_compte = pd.DataFrame(data_compte)
        st.dataframe(df_compte, use_container_width=True)
    
    with col2:
        st.write("**Bilan simplifié (k€)**")
        data_bilan = {
            'Poste': ['Actif immobilisé', 'Stocks', 'Clients', 'Disponibilités', 'Capitaux propres', 'Dettes financières', 'Fournisseurs'],
            'N': [1800, 450, 600, 150, 1200, 800, 1000],
            'N-1': [1700, 400, 550, 200, 1100, 700, 1050]
        }
        df_bilan = pd.DataFrame(data_bilan)
        st.dataframe(df_bilan, use_container_width=True)
    
    # Analyse interactive
    st.subheader("🔍 Analyse à réaliser")
    
    analyse_choice = st.radio(
        "**Sélectionnez l'analyse à effectuer :**",
        ["Ratios de rentabilité", "Structure financière", "Liquidité", "Diagnostic global"]
    )
    
    if analyse_choice == "Ratios de rentabilité":
        show_analyse_rentabilite_cas()
    elif analyse_choice == "Structure financière":
        show_analyse_structure_cas()
    elif analyse_choice == "Liquidité":
        show_analyse_liquidite_cas()
    else:
        show_diagnostic_global_cas()

def show_analyse_rentabilite_cas():
    st.write("""
    **📈 Calcul des ratios de rentabilité :**
    
    1. Taux de marge commerciale = Marge commerciale / CA
    2. Taux de valeur ajoutée = VA / CA  
    3. Taux d'EBE = EBE / CA
    4. Rentabilité économique = RE / Actif économique
    5. Rentabilité financière = RN / Capitaux propres
    """)
    
    # Réponse guidée
    with st.expander("📝 Voir la correction détaillée"):
        st.write("""
        **🧮 Calculs :**
        - Taux de marge : 52% (N) vs 50% (N-1) → ✅ Amélioration
        - Taux EBE : 20% (N) vs 17.4% (N-1) → ✅ Bonne progression
        - Rentabilité économique : 8.7% → ⚠️ Correcte
        - Rentabilité financière : 12.5% → ✅ Bonne
        
        **🎯 Conclusion :** Rentabilité en amélioration, bonne performance économique.
        """)

def show_analyse_structure_cas():
    st.write("""
    **🏗️ Analyse de la structure financière :**
    
    - FRNG = Ressources stables - Emplois stables
    - BFR = Actif circulant - Passif circulant  
    - Taux d'endettement = Dettes financières / Capitaux propres
    - Autonomie financière = Capitaux propres / Total passif
    """)
    
    with st.expander("📝 Voir la correction détaillée"):
        st.write("""
        **🧮 Calculs :**
        - FRNG = 1,200 + 800 - 1,800 = 200 k€ → ✅ Positif
        - BFR = (450 + 600) - 1,000 = 50 k€ → ✅ Faible besoin
        - Taux d'endettement = 800/1,200 = 67% → ✅ Acceptable
        - Autonomie = 1,200/3,000 = 40% → ⚠️ Correct
        
        **🎯 Conclusion :** Structure financière équilibrée.
        """)

def show_analyse_liquidite_cas():
    st.write("""
    **💧 Analyse de la liquidité :**
    
    - Ratio de liquidité générale = Actif circulant / Dettes CT
    - Ratio de liquidité réduite = (Actif circulant - Stocks) / Dettes CT  
    - Ratio de liquidité immédiate = Disponibilités / Dettes CT
    - Trésorerie nette = FRNG - BFR
    """)
    
    with st.expander("📝 Voir la correction détaillée"):
        st.write("""
        **🧮 Calculs :**
        - Liquidité générale = 1,200/1,000 = 1.2 → ✅ Correct
        - Liquidité réduite = 750/1,000 = 0.75 → ⚠️ À surveiller
        - Trésorerie nette = 200 - 50 = 150 k€ → ✅ Excédentaire
        
        **🎯 Conclusion :** Liquidité globalement satisfaisante.
        """)

def show_diagnostic_global_cas():
    st.write("""
    **🔍 Diagnostic global :**
    
    **✅ Points forts :**
    - Rentabilité en amélioration
    - Structure financière équilibrée  
    - Trésorerie excédentaire
    - Croissance du CA
    
    **⚠️ Points de vigilance :**
    - Liquidité réduite un peu faible
    - BFR à surveiller
    - Investissements importants
    
    **📋 Recommandations :**
    - Optimiser la gestion du BFR
    - Renforcer la trésorerie
    - Poursuivre les investissements maîtrisés
    """)

def show_cas_rentabilite():
    st.subheader("📈 Analyse de Rentabilité - Cas PRATIQUE")
    st.info("Cette étude de cas sera bientôt disponible...")

def show_cas_equilibre():
    st.subheader("⚖️ Équilibre Financier - Cas CONCRET")
    st.info("Cette étude de cas sera bientôt disponible...")

def show_cas_flux():
    st.subheader("💧 Tableaux de Flux - Cas APPLICATIF")
    st.info("Cette étude de cas sera bientôt disponible...")

def show_cas_investissement():
    st.subheader("🏗️ Projet d'Investissement - Cas DÉCISIONNEL")
    st.info("Cette étude de cas sera bientôt disponible...")

def show_ressources():
    st.markdown('<h2 class="section-header">📚 Ressources Pédagogiques</h2>', unsafe_allow_html=True)
    
    st.success("""
    **🎯 Comment utiliser cette section :**
    - **Téléchargez** les fiches mémo pour réviser
    - **Testez** vos connaissances avec les quiz  
    - **Utilisez** les modèles pour vos propres analyses
    - **Progressez** à votre rythme
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📖 Fiches Mémo")
        
        ressources = {
            "📄 Bilan": "Structure actif/passif, équilibre, analyse",
            "📊 Compte de résultat": "Soldes, SIG, rentabilité", 
            "📐 Ratios financiers": "Calcul, interprétation, normes",
            "💧 Tableaux de flux": "Construction, analyse, OEC vs CDB",
            "🔍 Diagnostic financier": "Méthodologie, outils, reporting"
        }
        
        for ressource, description in ressources.items():
            with st.expander(f"{ressource}"):
                st.write(description)
                st.download_button(
                    f"📥 Télécharger {ressource}",
                    f"Contenu de la fiche {ressource}",
                    file_name=f"fiche_{ressource.lower().replace(' ', '_')}.txt"
                )
    
    with col2:
        st.subheader("🎓 Quiz d'auto-évaluation")
        
        quiz_choice = st.selectbox(
            "**Choisissez un quiz :**",
            ["🟢 Débutant - Fondamentaux", "🟡 Intermédiaire - Bilan", 
             "🟠 Avancé - Compte de résultat", "🔴 Expert - Ratios", "🏆 Master - Diagnostic global"]
        )
        
        if "Débutant" in quiz_choice:
            show_quiz_fondamentaux()
        elif "Bilan" in quiz_choice:
            show_quiz_bilan()
    
    st.subheader("📊 Modèles et Templates")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button(
            "📋 Modèle de bilan",
            "Template de bilan format Excel",
            file_name="modele_bilan.xlsx"
        )
    
    with col2:
        st.download_button(
            "📊 Modèle de ratios",
            "Calculateur automatique de ratios",
            file_name="calculateur_ratios.xlsx"
        )
    
    with col3:
        st.download_button(
            "📈 Modèle de tableau de flux",
            "Template tableau de flux OEC",
            file_name="tableau_flux_oec.xlsx"
        )

def show_quiz_fondamentaux():
    st.write("**Testez vos connaissances sur les fondamentaux de l'analyse financière**")
    
    questions = [
        {
            "question": "Qu'est-ce que le fonds de roulement net global (FRNG)?",
            "options": [
                "La différence entre l'actif et le passif",
                "L'excédent des ressources stables sur les emplois stables", 
                "Le montant de la trésorerie disponible",
                "Le besoin de financement du cycle d'exploitation"
            ],
            "reponse": 1
        },
        {
            "question": "Quel est l'objectif principal de l'EBE?",
            "options": [
                "Mesurer le résultat net",
                "Évaluer la performance économique avant éléments financiers",
                "Calculer la capacité d'autofinancement",
                "Déterminer la trésorerie"
            ],
            "reponse": 1
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        reponse = st.radio(f"Choisissez votre réponse:", q['options'], key=f"q{i}")
        
        if st.button(f"Vérifier question {i+1}", key=f"btn{i}"):
            if q['options'].index(reponse) == q['reponse']:
                st.success("✅ Bonne réponse!")
                score += 1
            else:
                st.error(f"❌ Mauvaise réponse. La bonne réponse était: {q['options'][q['reponse']]}")
    
    if st.button("🎯 Voir le score final"):
        st.info(f"**Score: {score}/{len(questions)}**")
        if score == len(questions):
            st.balloons()
            st.success("🎉 Excellent! Toutes les réponses sont correctes!")
        elif score >= len(questions)/2:
            st.warning("📚 Bien! Continuez à progresser!")
        else:
            st.error("📖 Revoyez les concepts fondamentaux")

def show_quiz_bilan():
    st.write("**Quiz sur le bilan comptable**")
    st.info("Ce quiz sera bientôt disponible...")




import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Maîtrise de l'Analyse Financière",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2e86ab;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .concept-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .usage-step {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #ff6b6b;
    }
    .tip-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        background-color: #f8f9fa;
        border-top: 1px solid #dee2e6;
        color: #6c757d;
        font-size: 0.9rem;
    }
    .cas-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #dee2e6;
    }
    .question-box {
        background-color: #e7f3ff;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #007bff;
    }
    .solution-box {
        background-color: #d4edda;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

def show_footer():
    st.markdown("""
    <div class="footer">
    <strong>Plateforme d'apprentissage de l'analyse financière • Version 3.0</strong><br>
    📚 Développé pour les étudiants, professionnels et entrepreneurs par Amiharbi Eyeug • © 2024
    </div>
    """, unsafe_allow_html=True)

def main():
    # Header principal
    st.markdown('<h1 class="main-header">📊 Maîtrise de l\'Analyse Financière</h1>', unsafe_allow_html=True)
    
    # Navigation par onglets
    tabs = st.tabs([
        "🏠 Accueil & Guide",
        "📈 Concepts Fondamentaux",
        "🧮 Calculateurs",
        "💼 Études de Cas",
        "📚 Ressources"
    ])
    
    with tabs[0]:
        show_accueil_guide()
        show_footer()
    
    with tabs[1]:
        show_concepts_fondamentaux()
        show_footer()
    
    with tabs[2]:
        show_calculateurs()
        show_footer()
    
    with tabs[3]:
        show_etudes_cas()
        show_footer()
    
    with tabs[4]:
        show_ressources()
        show_footer()

def show_accueil_guide():
    st.markdown('<h2 class="section-header">🎯 Guide Complet d\'Utilisation</h2>', unsafe_allow_html=True)
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        ## Bienvenue dans l'application d'analyse financière !
        
        Cette application interactive vous permet de **maîtriser progressivement tous les aspects 
        de l'analyse financière** d'entreprise grâce à une approche pratique basée sur le 
        manuel "Maxi Fiches de Gestion Financière".
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400", 
                caption="Analyse Financière Interactive")
    
    # Mode d'utilisation détaillé
    st.markdown("""
    <div class="concept-card">
    <h3>🚀 Comment Utiliser Cette Application</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Structure de navigation
    st.subheader("📋 Structure de Navigation")
    
    nav_cols = st.columns(5)
    with nav_cols[0]:
        st.info("**🏠 Accueil**\n\nGuide d'utilisation et parcours d'apprentissage")
    with nav_cols[1]:
        st.success("**📈 Concepts**\n\nThéorie avec exemples interactifs")
    with nav_cols[2]:
        st.warning("**🧮 Calculateurs**\n\nOutils pratiques et simulations")
    with nav_cols[3]:
        st.error("**💼 Études de Cas**\n\nSituations réelles avec corrigés")
    with nav_cols[4]:
        st.info("**📚 Ressources**\n\nFiches, quiz et modèles")
    
    # Parcours recommandé selon le niveau
    st.subheader("🎓 Parcours d'Apprentissage Recommandé")
    
    niveau = st.radio("**Sélectionnez votre niveau :**", 
                     ["🟢 Débutant", "🟡 Intermédiaire", "🔴 Avancé"], 
                     horizontal=True)
    
    if niveau == "🟢 Débutant":
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Débutant (20-30 heures)</h4>
        <ol>
            <li><strong>Semaines 1-2 :</strong> Accueil → Concepts (Bilan & Compte de résultat)</li>
            <li><strong>Semaines 3-4 :</strong> Concepts (SIG & Seuil de rentabilité)</li>
            <li><strong>Semaines 5-6 :</strong> Calculateurs basiques → Quiz fondamentaux</li>
            <li><strong>Semaines 7-8 :</strong> Études de cas simples → Ressources</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    elif niveau == "🟡 Intermédiaire":
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Intermédiaire (15-25 heures)</h4>
        <ol>
            <li><strong>Semaines 1-2 :</strong> Revoir Concepts → Calculateurs avancés</li>
            <li><strong>Semaines 3-4 :</strong> Études de cas complexes → Analyse complète</li>
            <li><strong>Semaines 5-6 :</strong> Calculateurs VAN/TIR → Scores financiers</li>
            <li><strong>Semaines 7-8 :</strong> Quiz experts → Modèles personnalisés</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Avancé (10-20 heures)</h4>
        <ol>
            <li><strong>Semaine 1 :</strong> Calculateurs avancés → Diagnostics complexes</li>
            <li><strong>Semaine 2 :</strong> Études de cas experts → Recommandations stratégiques</li>
            <li><strong>Semaine 3 :</strong> Modèles personnalisés → Analyses sectorielles</li>
            <li><strong>Semaine 4 :</strong> Validation complète → Applications pratiques</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Guide détaillé par onglet
    st.subheader("📖 Guide Détaillé par Section")
    
    with st.expander("🏠 ONGLET ACCUEIL & GUIDE", expanded=True):
        st.markdown("""
        **Objectif** : Comprendre le parcours et optimiser votre apprentissage
        
        **Actions clés :**
        - 📊 Identifier votre niveau actuel
        - 🗺️ Suivre le parcours recommandé
        - ⏱️ Planifier votre temps d'apprentissage
        - 🎯 Définir vos objectifs personnels
        
        **Temps recommandé :** 15-30 minutes
        """)
    
    with st.expander("📈 ONGLET CONCEPTS FONDAMENTAUX"):
        st.markdown("""
        **Objectif** : Apprendre la théorie avec des exemples interactifs
        
        **Mode d'emploi :**
        1. **Sélectionnez un concept** dans le menu déroulant
        2. **Lisez les explications** théoriques détaillées
        3. **Utilisez les calculateurs intégrés** pour pratiquer
        4. **Analysez les graphiques** et interprétations automatiques
        
        **Concepts disponibles :**
        - 🔍 Diagnostic Financier
        - ⚖️ Bilan Comptable (avec calculateur d'équilibre)
        - 📊 Compte de Résultat (avec simulateur)
        - 📈 Soldes Intermédiaires de Gestion (SIG)
        - 🎯 Seuil de Rentabilité (avec graphique)
        - 💰 Fonds de Roulement & BFR
        - 📐 Ratios Financiers (avec tableau de bord)
        
        **Temps recommandé :** 2-3 heures par concept
        """)
    
    with st.expander("🧮 ONGLET CALCULATEURS"):
        st.markdown("""
        **Objectif** : Appliquer les concepts avec des outils pratiques
        
        **Calculateurs disponibles :**
        
        **📉 Amortissements** (Linéaire/Dégressif)
        → Saisir : Valeur, durée, coefficient
        → Obtenir : Tableau complet + Graphique
        
        **💸 Capacité d'Autofinancement** (CAF)
        → Saisir : Résultat net, dotations, reprises
        → Obtenir : CAF + Diagnostic automatique
        
        **⚖️ Effet de Levier Financier**
        → Saisir : Actif, capitaux, dettes, taux
        → Obtenir : Rentabilité économique vs financière
        
        **📊 VAN/TIR** (Investissements)
        → Saisir : Investissement, flux, durée
        → Obtenir : VAN + TIR + Recommandation
        
        **🎯 Score Financier** (Risque défaillance)
        → Saisir : EBE, endettement, ratios clés
        → Obtenir : Score + Diagnostic risque
        
        **Temps recommandé :** 1-2 heures par calculateur
        """)
    
    with st.expander("💼 ONGLET ÉTUDES DE CAS"):
        st.markdown("""
        **Objectif** : Mettre en pratique sur des situations réelles
        
        **Méthodologie :**
        1. **Lire le contexte** de l'entreprise
        2. **Analyser les données** financières fournies
        3. **Choisir le type d'analyse** à réaliser
        4. **Comparer vos résultats** avec la correction
        5. **Comprendre les recommandations**
        
        **Cas disponibles :**
        - 🏭 PME Industrielle (analyse complète)
        - 📈 Analyse de Rentabilité
        - ⚖️ Équilibre Financier
        - 💧 Tableaux de Flux
        - 🏗️ Projet d'Investissement
        
        **Temps recommandé :** 2-4 heures par étude de cas
        """)
    
    with st.expander("📚 ONGLET RESSOURCES"):
        st.markdown("""
        **Objectif** : Consolider et tester ses connaissances
        
        **Ressources disponibles :**
        
        **📖 Fiches Mémo Téléchargeables**
        - Formats : PDF/Excel
        - Thèmes : Bilan, Compte de résultat, Ratios, etc.
        - Utilisation : Révisions rapides
        
        **🎓 Quiz d'Auto-évaluation**
        - Niveaux : Débutant à Expert
        - Correction immédiate avec explications
        - Score final avec recommandations
        
        **📊 Modèles et Templates**
        - Fichiers Excel réutilisables
        - Tableaux pré-formatés
        - Calculateurs personnalisables
        
        **Temps recommandé :** 30 minutes à 1 heure par ressource
        """)
    
    # Conseils d'optimisation
    st.subheader("💡 Conseils d'Optimisation")
    
    tip_cols = st.columns(3)
    
    with tip_cols[0]:
        st.markdown("""
        <div class="tip-box">
        <h5>🎮 Pour les Débutants</h5>
        - Suivez le parcours recommandé
        - Prenez des notes dans chaque section
        - Refaites les exercices plusieurs fois
        - Utilisez systématiquement les calculateurs
        </div>
        """, unsafe_allow_html=True)
    
    with tip_cols[1]:
        st.markdown("""
        <div class="tip-box">
        <h5>🚀 Pour les Intermédiaires</h5>
        - Testez différents scénarios
        - Comparez vos analyses avec les corrigés
        - Personnalisez les paramètres
        - Téléchargez les modèles pour vos projets
        </div>
        """, unsafe_allow_html=True)
    
    with tip_cols[2]:
        st.markdown("""
        <div class="tip-box">
        <h5>🏆 Pour les Experts</h5>
        - Utilisez les études de cas complexes
        - Développez vos propres scénarios
        - Intégrez les modèles dans vos outils
        - Validez vos méthodologies d'analyse
        </div>
        """, unsafe_allow_html=True)
    
    # Progression globale
    st.subheader("📊 Progression Globale Recommandée")
    
    progress_data = {
        "Module": ["Fondamentaux", "Bilan & Compte de résultat", "Ratios & SIG", 
                  "Analyse fonctionnelle", "Tableaux de flux", "Diagnostic avancé"],
        "Durée estimée": ["2 semaines", "3 semaines", "2 semaines", "2 semaines", "3 semaines", "2 semaines"],
        "Difficulté": ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        "Onglets clés": ["Concepts", "Concepts + Calculateurs", "Calculateurs + Cas", 
                        "Cas + Calculateurs", "Cas + Ressources", "Tous les onglets"]
    }
    
    df_progress = pd.DataFrame(progress_data)
    st.dataframe(df_progress, use_container_width=True)
    
    # Derniers conseils
    st.markdown("""
    <div class="tip-box">
    <h5>💎 Derniers Conseils Importants</h5>
    - <strong>Sauvegardez</strong> vos paramètres intéressants
    - <strong>Téléchargez</strong> les résultats importants  
    - <strong>Expérimentez</strong> avec différentes valeurs
    - <strong>Consultez</strong> les explications détaillées
    - <strong>Pratiquez</strong> régulièrement pour progresser
    </div>
    """, unsafe_allow_html=True)

def show_concepts_fondamentaux():
    st.markdown('<h2 class="section-header">📈 Concepts Fondamentaux</h2>', unsafe_allow_html=True)
    
    # Guide rapide d'utilisation
    st.info("""
    **🎯 Comment utiliser cette section :**
    1. Sélectionnez un concept dans le menu ci-dessous
    2. Lisez les explications théoriques détaillées  
    3. Utilisez les calculateurs intégrés pour pratiquer
    4. Analysez les graphiques et interprétations automatiques
    """)
    
    concept_choice = st.selectbox(
        "**Choisissez un concept à explorer :**",
        [
            "🔍 Diagnostic Financier",
            "⚖️ Bilan Comptable", 
            "📊 Compte de Résultat",
            "📈 Soldes Intermédiaires de Gestion",
            "🎯 Seuil de Rentabilité",
            "💰 Fonds de Roulement",
            "📐 Ratios Financiers"
        ]
    )
    
    if "Diagnostic Financier" in concept_choice:
        show_diagnostic_financier()
    elif "Bilan Comptable" in concept_choice:
        show_bilan_comptable()
    elif "Compte de Résultat" in concept_choice:
        show_compte_resultat()
    elif "Soldes Intermédiaires" in concept_choice:
        show_soldes_gestion()
    elif "Seuil de Rentabilité" in concept_choice:
        show_seuil_rentabilite()
    elif "Fonds de Roulement" in concept_choice:
        show_fonds_roulement()
    elif "Ratios Financiers" in concept_choice:
        show_ratios_financiers()

def show_diagnostic_financier():
    st.markdown("""
    <div class="concept-card">
    <h3>🔍 Diagnostic Financier</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **📖 Définition :**
        Le diagnostic financier est une démarche qui vise à :
        - Identifier les causes de difficultés présentes ou futures
        - Mettre en lumière les dysfonctionnements
        - Présenter les perspectives d'évolution
        - Proposer des actions correctives
        
        **📋 États financiers analysés :**
        - Bilan (patrimoine à une date donnée)
        - Compte de résultat (performance sur une période)
        - Annexe (informations complémentaires)
        """)
    
    with col2:
        st.write("""
        **🛠️ Méthodologie :**
        1. Analyse de la rentabilité
        2. Analyse de la liquidité
        3. Analyse de la structure financière
        4. Analyse économique complémentaire
        
        **📊 Outils :**
        - Ratios financiers
        - Tableaux de flux
        - Soldes intermédiaires de gestion
        - Comparaisons sectorielles
        """)
    
    # Schéma du processus de diagnostic
    st.subheader("📋 Processus de Diagnostic")
    
    steps = {
        "Étape 1": "Collecte des états financiers",
        "Étape 2": "Analyse horizontale et verticale", 
        "Étape 3": "Calcul des ratios",
        "Étape 4": "Analyse fonctionnelle",
        "Étape 5": "Diagnostic et recommandations"
    }
    
    for step, description in steps.items():
        st.write(f"**{step}:** {description}")

def show_bilan_comptable():
    st.markdown("""
    <div class="concept-card">
    <h3>⚖️ Bilan Comptable</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Photographie du patrimoine de l'entreprise à une date donnée.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("ACTIF")
        st.write("""
        **Actif Immobilisé:**
        - Immobilisations incorporelles
        - Immobilisations corporelles  
        - Immobilisations financières
        
        **Actif Circulant:**
        - Stocks
        - Créances clients
        - Disponibilités
        """)
    
    with col2:
        st.subheader("PASSIF")
        st.write("""
        **Capitaux Propres:**
        - Capital social
        - Réserves
        - Résultat de l'exercice
        
        **Dettes:**
        - Dettes financières
        - Dettes fournisseurs
        - Dettes fiscales et sociales
        """)
    
    # Calculateur simplifié de bilan
    st.subheader("🧮 Calculateur de Bilan - Pratiquez !")
    
    st.warning("💡 **Exercice :** Essayez de créer un bilan équilibré en ajustant les valeurs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Actif**")
        immob_corporelles = st.number_input("Immobilisations corporelles", value=500000, key="bilan_actif1")
        stocks = st.number_input("Stocks", value=200000, key="bilan_actif2")
        clients = st.number_input("Créances clients", value=300000, key="bilan_actif3")
        disponibilites = st.number_input("Disponibilités", value=100000, key="bilan_actif4")
        
        total_actif = immob_corporelles + stocks + clients + disponibilites
        
    with col2:
        st.write("**Passif**")
        capital = st.number_input("Capital social", value=400000, key="bilan_passif1")
        reserves = st.number_input("Réserves", value=300000, key="bilan_passif2")
        resultat = st.number_input("Résultat", value=100000, key="bilan_passif3")
        emprunts = st.number_input("Emprunts", value=200000, key="bilan_passif4")
        fournisseurs = st.number_input("Dettes fournisseurs", value=100000, key="bilan_passif5")
        
        total_passif = capital + reserves + resultat + emprunts + fournisseurs
    
    # Vérification équilibre
    st.subheader("📊 Résultat de l'Exercice")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Actif", f"{total_actif:,.0f} €")
    with col2:
        st.metric("Total Passif", f"{total_passif:,.0f} €")
    with col3:
        difference = total_actif - total_passif
        if abs(difference) < 1:
            st.success("✅ Bilan Équilibré")
        else:
            st.error(f"❌ Écart : {difference:,.0f} €")

def show_compte_resultat():
    st.markdown("""
    <div class="concept-card">
    <h3>📊 Compte de Résultat</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Mesure la performance économique sur une période (généralement un an).
    """)
    
    # Structure du compte de résultat
    st.subheader("🏗️ Structure du Compte de Résultat")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **CHARGES**
        - Achats de marchandises
        - Variation de stocks
        - Charges externes
        - Impôts et taxes
        - Charges de personnel
        - Dotations aux amortissements
        - Charges financières
        - Charges exceptionnelles
        """)
    
    with col2:
        st.write("""
        **PRODUITS**
        - Ventes de marchandises
        - Production vendue
        - Production stockée
        - Production immobilisée
        - Subventions d'exploitation
        - Produits financiers
        - Produits exceptionnels
        """)
    
    # Calculateur de résultat
    st.subheader("🧮 Calculateur de Résultat - Expérimentez !")
    
    st.info("💡 **Conseil :** Modifiez les valeurs pour comprendre leur impact sur le résultat")
    
    ca = st.number_input("Chiffre d'affaires HT (€)", value=1000000, key="cr_ca")
    achats = st.number_input("Achats consommés (€)", value=400000, key="cr_achats")
    charges_personnel = st.number_input("Charges de personnel (€)", value=300000, key="cr_pers")
    dotations_amort = st.number_input("Dotations aux amortissements (€)", value=50000, key="cr_amort")
    charges_financieres = st.number_input("Charges financières (€)", value=20000, key="cr_fin")
    
    # Calculs
    resultat_exploitation = ca - achats - charges_personnel - dotations_amort
    resultat_courant = resultat_exploitation - charges_financieres
    
    # Affichage résultats
    st.subheader("📈 Résultats Calculés")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Résultat d'Exploitation", f"{resultat_exploitation:,.0f} €")
        st.metric("Taux de marge d'exploitation", f"{(resultat_exploitation/ca*100):.1f}%" if ca > 0 else "0%")
    
    with col2:
        st.metric("Résultat Courant", f"{resultat_courant:,.0f} €")
        st.metric("Taux de marge nette", f"{(resultat_courant/ca*100):.1f}%" if ca > 0 else "0%")

def show_soldes_gestion():
    st.markdown("""
    <div class="concept-card">
    <h3>📈 Soldes Intermédiaires de Gestion</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Les SIG permettent de décomposer la formation du résultat en plusieurs niveaux.")
    
    # Calculateur des SIG
    st.subheader("🧮 Calculateur des SIG")
    
    ca = st.number_input("Chiffre d'affaires", value=1000000, key="sig_ca_unique")
    achats_marches = st.number_input("Achats de marchandises", value=300000, key="sig_achats_unique")
    prod_vendue = st.number_input("Production vendue", value=800000, key="sig_prod_unique")
    consommations = st.number_input("Consommations externes", value=200000, key="sig_cons_unique")
    charges_personnel = st.number_input("Charges de personnel", value=350000, key="sig_pers_unique")
    
    # Calcul des SIG
    marge_commerciale = ca - achats_marches
    valeur_ajoutee = marge_commerciale + prod_vendue - consommations
    ebe = valeur_ajoutee - charges_personnel
    
    # Affichage des résultats
    st.subheader("📊 Résultats des SIG")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Marge Commerciale", f"{marge_commerciale:,.0f} €")
        st.metric("Taux de marge", f"{(marge_commerciale/ca*100):.1f} %")
    
    with col2:
        st.metric("Valeur Ajoutée", f"{valeur_ajoutee:,.0f} €")
        st.metric("Taux de VA", f"{(valeur_ajoutee/ca*100):.1f} %")
    
    with col3:
        st.metric("EBE", f"{ebe:,.0f} €")
        st.metric("Taux EBE", f"{(ebe/ca*100):.1f} %")

def show_seuil_rentabilite():
    st.markdown("""
    <div class="concept-card">
    <h3>🎯 Seuil de Rentabilité</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Niveau de chiffre d'affaires pour lequel le résultat est nul.
    
    **🧮 Formule :** SR = Charges Fixes / Taux de Marge sur Coût Variable
    """)
    
    # Calculateur de seuil de rentabilité
    st.subheader("🧮 Calculateur de Seuil de Rentabilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        charges_fixes = st.number_input("Charges fixes annuelles (€)", value=300000, key="seuil_charges_fixes")
        ca_prev = st.number_input("Chiffre d'affaires prévisionnel (€)", value=1000000, key="seuil_ca")
    
    with col2:
        charges_variables = st.number_input("Charges variables (€)", value=500000, key="seuil_charges_var")
    
    # Calculs
    mcv = ca_prev - charges_variables
    taux_mcv = mcv / ca_prev if ca_prev > 0 else 0
    seuil_rentabilite = charges_fixes / taux_mcv if taux_mcv > 0 else 0
    marge_securite = ((ca_prev - seuil_rentabilite) / ca_prev * 100) if ca_prev > 0 else 0
    
    # Résultats
    st.subheader("📈 Résultats")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Taux MCV", f"{taux_mcv*100:.1f} %")
    
    with col2:
        st.metric("Seuil Rentabilité", f"{seuil_rentabilite:,.0f} €")
    
    with col3:
        st.metric("Marge de Sécurité", f"{marge_securite:.1f} %")
    
    # Graphique
    if seuil_rentabilite > 0:
        st.subheader("📊 Graphique de Visualisation")
        x = np.linspace(0, ca_prev * 1.5, 100)
        y_charges_fixes = np.full_like(x, charges_fixes)
        y_charges_variables = charges_variables/ca_prev * x if ca_prev > 0 else 0
        y_charges_totales = y_charges_fixes + y_charges_variables
        y_ca = x
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y_charges_fixes, name='Charges Fixes', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=x, y=y_charges_totales, name='Charges Totales', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=x, y=y_ca, name='Chiffre d\'affaires', line=dict(color='green')))
        
        # Point de seuil
        fig.add_trace(go.Scatter(x=[seuil_rentabilite], y=[seuil_rentabilite], 
                               mode='markers', name='Seuil', marker=dict(size=10, color='orange')))
        
        fig.update_layout(title='Seuil de Rentabilité', xaxis_title='Chiffre d\'affaires (€)', yaxis_title='Montants (€)')
        st.plotly_chart(fig)

def show_fonds_roulement():
    st.markdown("""
    <div class="concept-card">
    <h3>💰 Fonds de Roulement et BFR</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **🧮 Formules :**
    - FRNG = Ressources Stables - Emplois Stables
    - BFR = Actif Circulant - Passif Circulant  
    - Trésorerie = FRNG - BFR
    """)
    
    # Calculateur FRNG/BFR
    st.subheader("🧮 Calculateur d'Équilibre Financier")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Ressources Stables**")
        capitaux_propres = st.number_input("Capitaux propres (€)", value=800000, key="fr_cp")
        dettes_long_terme = st.number_input("Dettes long terme (€)", value=200000, key="fr_dettes")
    
    with col2:
        st.write("**Emplois Stables**")
        immob_brutes = st.number_input("Immobilisations brutes (€)", value=700000, key="fr_immob")
    
    with col3:
        st.write("**BFR**")
        stocks = st.number_input("Stocks (€)", value=150000, key="fr_stocks")
        clients = st.number_input("Créances clients (€)", value=200000, key="fr_clients")
        fournisseurs = st.number_input("Dettes fournisseurs (€)", value=120000, key="fr_fournisseurs")
    
    # Calculs
    ressources_stables = capitaux_propres + dettes_long_terme
    emplois_stables = immob_brutes
    frng = ressources_stables - emplois_stables
    
    actif_circulant = stocks + clients
    passif_circulant = fournisseurs
    bfr = actif_circulant - passif_circulant
    tresorerie = frng - bfr
    
    # Affichage résultats
    st.subheader("📊 Diagnostic Financier")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        delta_color = "normal" if frng > 0 else "inverse"
        st.metric("FRNG", f"{frng:,.0f} €", 
                 delta="✅ Bon" if frng > 0 else "❌ Risque", 
                 delta_color=delta_color)
    
    with col2:
        st.metric("BFR", f"{bfr:,.0f} €", 
                 delta="📈 Besoin" if bfr > 0 else "📉 Ressource")
    
    with col3:
        delta_color = "normal" if tresorerie > 0 else "inverse"
        st.metric("Trésorerie", f"{tresorerie:,.0f} €", 
                 delta="✅ Excédent" if tresorerie > 0 else "❌ Déficit", 
                 delta_color=delta_color)

def show_ratios_financiers():
    st.markdown("""
    <div class="concept-card">
    <h3>📐 Ratios Financiers</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur de ratios
    st.subheader("🧮 Calculateur de Ratios")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ca = st.number_input("Chiffre d'affaires (€)", value=1000000, key="ratio_ca")
        resultat_net = st.number_input("Résultat net (€)", value=80000, key="ratio_rn")
        capitaux_propres = st.number_input("Capitaux propres (€)", value=400000, key="ratio_cp")
        ebe = st.number_input("EBE (€)", value=150000, key="ratio_ebe")
    
    with col2:
        total_actif = st.number_input("Total actif (€)", value=800000, key="ratio_actif")
        dettes_financieres = st.number_input("Dettes financières (€)", value=200000, key="ratio_dettes")
        actif_circulant = st.number_input("Actif circulant (€)", value=300000, key="ratio_actif_circ")
        dettes_court_terme = st.number_input("Dettes court terme (€)", value=180000, key="ratio_dettes_ct")
    
    # Calcul des ratios
    rentabilite_net = (resultat_net / ca * 100) if ca > 0 else 0
    rentabilite_financiere = (resultat_net / capitaux_propres * 100) if capitaux_propres > 0 else 0
    rentabilite_economique = (ebe / total_actif * 100) if total_actif > 0 else 0
    endettement = (dettes_financieres / capitaux_propres * 100) if capitaux_propres > 0 else 0
    liquidite = (actif_circulant / dettes_court_terme * 100) if dettes_court_terme > 0 else 0
    
    # Affichage des ratios
    st.subheader("📊 Tableau de Bord des Ratios")
    
    ratios_data = {
        "Ratio": ["Rentabilité nette", "Rentabilité financière", "Rentabilité économique", "Taux d'endettement", "Ratio de liquidité"],
        "Valeur": [f"{rentabilite_net:.1f}%", f"{rentabilite_financiere:.1f}%", f"{rentabilite_economique:.1f}%", f"{endettement:.1f}%", f"{liquidite:.1f}%"],
        "Interprétation": [
            "✅ Bon" if rentabilite_net > 2 else "⚠️ À améliorer",
            "✅ Bon" if rentabilite_financiere > 8 else "⚠️ À améliorer", 
            "✅ Bon" if rentabilite_economique > 10 else "⚠️ À améliorer",
            "✅ Bon" if endettement < 100 else "❌ Trop élevé",
            "✅ Bon" if liquidite > 100 else "❌ Risque liquidité"
        ]
    }
    
    df_ratios = pd.DataFrame(ratios_data)
    st.dataframe(df_ratios, use_container_width=True)

def show_calculateurs():
    st.markdown('<h2 class="section-header">🧮 Calculateurs Interactifs</h2>', unsafe_allow_html=True)
    
    # Guide d'utilisation
    st.success("""
    **🎯 Comment utiliser les calculateurs :**
    1. Sélectionnez un calculateur dans le menu
    2. Saisissez vos données dans les champs
    3. Analysez les résultats calculés automatiquement
    4. Consultez les graphiques et recommandations
    """)
    
    calc_choice = st.selectbox(
        "**Choisissez un calculateur :**",
        [
            "📉 Amortissements",
            "💸 Capacité d'Autofinancement", 
            "⚖️ Effet de Levier",
            "📊 VAN et TIR",
            "🎯 Score Financier"
        ]
    )
    
    if "Amortissements" in calc_choice:
        show_calculateur_amortissements()
    elif "Capacité d'Autofinancement" in calc_choice:
        show_calculateur_caf()
    elif "Effet de Levier" in calc_choice:
        show_calculateur_levier()
    elif "VAN et TIR" in calc_choice:
        show_calculateur_van_tir()
    elif "Score Financier" in calc_choice:
        show_calculateur_score()

def show_calculateur_amortissements():
    st.subheader("📉 Calculateur d'Amortissements")
    
    st.info("""
    **💡 À savoir :**
    - **Amortissement linéaire** : Constant chaque année
    - **Amortissement dégressif** : Décroissant, avec coefficient
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        valeur_origine = st.number_input("Valeur d'origine (€)", value=100000, key="amort_valeur")
        duree = st.number_input("Durée d'amortissement (années)", value=5, min_value=1, key="amort_duree")
        mode = st.radio("Mode d'amortissement", ["Linéaire", "Dégressif"], key="amort_mode")
    
    with col2:
        date_acquisition = st.date_input("Date d'acquisition", value=datetime(2023, 1, 1), key="amort_date")
        coefficient = st.selectbox("Coefficient dégressif", [1.25, 1.75, 2.25], key="amort_coeff") if mode == "Dégressif" else 0
    
    # Calcul du plan d'amortissement
    if st.button("📊 Calculer le plan d'amortissement", key="amort_btn"):
        annees = list(range(1, duree + 1))
        vnc = [valeur_origine]
        amortissements = []
        amort_cumules = [0]
        
        for annee in annees:
            if mode == "Linéaire":
                amort_annuel = valeur_origine / duree
            else:
                taux_lineaire = 100 / duree
                taux_degressif = taux_lineaire * coefficient
                amort_annuel = vnc[-1] * taux_degressif / 100
            
            amortissements.append(amort_annuel)
            amort_cumules.append(amort_cumules[-1] + amort_annuel)
            vnc.append(vnc[-1] - amort_annuel)
        
        # DataFrame des résultats
        df_amort = pd.DataFrame({
            'Année': annees,
            'VNC début': [f"{v:,.0f} €" for v in vnc[:-1]],
            'Amortissement annuel': [f"{a:,.0f} €" for a in amortissements],
            'Amortissement cumulé': [f"{a:,.0f} €" for a in amort_cumules[1:]],
            'VNC fin': [f"{v:,.0f} €" for v in vnc[1:]]
        })
        
        st.dataframe(df_amort, use_container_width=True)
        
        # Graphique
        fig = go.Figure()
        fig.add_trace(go.Bar(x=annees, y=amortissements, name='Amortissement annuel'))
        fig.add_trace(go.Scatter(x=annees, y=vnc[1:], name='VNC fin d\'année', line=dict(color='red')))
        fig.update_layout(title='Plan d\'amortissement', xaxis_title='Années', yaxis_title='Montants (€)')
        st.plotly_chart(fig)

def show_calculateur_caf():
    st.subheader("💸 Calculateur de Capacité d'Autofinancement")
    
    st.write("**🧮 Méthode additive : CAF = Résultat net + Dotations - Reprises - Produits de cession**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        resultat_net = st.number_input("Résultat net (€)", value=50000, key="caf_rn")
        dotations_amort = st.number_input("Dotations aux amortissements (€)", value=20000, key="caf_dot_amort")
        dotations_provisions = st.number_input("Dotations aux provisions (€)", value=5000, key="caf_dot_prov")
    
    with col2:
        reprises_amort = st.number_input("Reprises sur amortissements (€)", value=0, key="caf_rep_amort")
        reprises_provisions = st.number_input("Reprises sur provisions (€)", value=0, key="caf_rep_prov")
        produits_cession = st.number_input("Produits de cession (€)", value=0, key="caf_prod_cess")
    
    caf = (resultat_net + dotations_amort + dotations_provisions - 
           reprises_amort - reprises_provisions - produits_cession)
    
    st.metric("Capacité d'Autofinancement", f"{caf:,.0f} €")
    
    # Interprétation
    if caf > resultat_net:
        st.success("✅ La CAF est supérieure au résultat net : bonne capacité d'autofinancement")
    else:
        st.warning("⚠️ La CAF est proche ou inférieure au résultat net : capacité d'autofinancement limitée")

def show_calculateur_levier():
    st.subheader("⚖️ Calculateur d'Effet de Levier Financier")
    
    col1, col2 = st.columns(2)
    
    with col1:
        actif_economique = st.number_input("Actif économique (€)", value=1000000, key="levier_actif")
        resultat_exploitation = st.number_input("Résultat d'exploitation (€)", value=120000, key="levier_re")
        capitaux_propres = st.number_input("Capitaux propres (€)", value=600000, key="levier_cp")
    
    with col2:
        dettes_financieres = st.number_input("Dettes financières (€)", value=400000, key="levier_dettes")
        taux_impot = st.number_input("Taux d'impôt (%)", value=25.0, key="levier_impot") / 100
        taux_interet = st.number_input("Taux d'intérêt (%)", value=4.0, key="levier_interet") / 100
    
    # Calculs
    re_apres_impot = resultat_exploitation * (1 - taux_impot)
    rentabilite_economique = re_apres_impot / actif_economique
    
    charges_financieres = dettes_financieres * taux_interet
    cf_apres_impot = charges_financieres * (1 - taux_impot)
    
    resultat_net = re_apres_impot - cf_apres_impot
    rentabilite_financiere = resultat_net / capitaux_propres
    
    effet_levier = rentabilite_financiere - rentabilite_economique
    
    # Affichage
    st.subheader("📈 Résultats")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Rentabilité économique", f"{rentabilite_economique*100:.1f}%")
    
    with col2:
        st.metric("Rentabilité financière", f"{rentabilite_financiere*100:.1f}%")
    
    with col3:
        delta_color = "normal" if effet_levier > 0 else "inverse"
        st.metric(
            "Effet de levier", 
            f"{effet_levier*100:.1f}%", 
            delta="✅ Positif" if effet_levier > 0 else "❌ Négatif", 
            delta_color=delta_color
        )

def show_calculateur_van_tir():
    st.subheader("📊 Calculateur VAN et TIR")
    
    st.write("Évaluation de la rentabilité d'un projet d'investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investissement_initial = st.number_input("Investissement initial (€)", value=100000, key="van_invest")
        duree_projet = st.number_input("Durée du projet (années)", value=5, key="van_duree")
        taux_actualisation = st.number_input("Taux d'actualisation (%)", value=8.0, key="van_taux") / 100
    
    with col2:
        st.write("Flux de trésorerie annuels")
        flux = []
        for i in range(duree_projet):
            flux.append(st.number_input(f"Année {i+1} (€)", value=30000, key=f"van_flux_{i}"))
    
    if st.button("📈 Calculer VAN et TIR", key="van_btn"):
        # Calcul VAN
        van = -investissement_initial
        for i, flux_annuel in enumerate(flux):
            van += flux_annuel / ((1 + taux_actualisation) ** (i + 1))
        
        # Estimation TIR (méthode simplifiée)
        def calcul_van(taux):
            van_calc = -investissement_initial
            for i, flux_annuel in enumerate(flux):
                van_calc += flux_annuel / ((1 + taux) ** (i + 1))
            return van_calc
        
        # Recherche du TIR par approximation
        tir = taux_actualisation
        for taux_test in np.arange(0.01, 1.0, 0.01):
            if calcul_van(taux_test) >= 0:
                tir = taux_test
            else:
                break
        
        st.subheader("🎯 Résultats")
        
        col1, col2 = st.columns(2)
        with col1:
            delta_color = "normal" if van > 0 else "inverse"
            st.metric(
                "VAN", 
                f"{van:,.0f} €", 
                delta="✅ Projet rentable" if van > 0 else "❌ Projet non rentable",
                delta_color=delta_color
            )
        with col2:
            st.metric("TIR approximatif", f"{tir*100:.1f}%")

def show_calculateur_score():
    st.subheader("🎯 Calculateur de Score Financier")
    
    st.write("Évaluation du risque de défaillance selon la méthode des scores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ebe = st.number_input("EBE (€)", value=150000, key="score_ebe")
        endettement_global = st.number_input("Endettement global (€)", value=500000, key="score_endettement")
        capitaux_permanents = st.number_input("Capitaux permanents (€)", value=800000, key="score_capitaux")
    
    with col2:
        actif_total = st.number_input("Actif total (€)", value=1000000, key="score_actif")
        frais_financiers = st.number_input("Frais financiers (€)", value=20000, key="score_frais_fin")
        ca = st.number_input("Chiffre d'affaires (€)", value=1000000, key="score_ca")
        charges_personnel = st.number_input("Charges de personnel (€)", value=350000, key="score_charges_pers")
        valeur_ajoutee = st.number_input("Valeur ajoutée (€)", value=500000, key="score_va")
    
    # Calcul du score Conan et Holder
    X1 = ebe / endettement_global if endettement_global > 0 else 0
    X2 = capitaux_permanents / actif_total if actif_total > 0 else 0
    X3 = 0.3  # Approximation pour réalisable et disponible
    X4 = frais_financiers / ca if ca > 0 else 0
    X5 = charges_personnel / valeur_ajoutee if valeur_ajoutee > 0 else 0
    
    score = 24*X1 + 22*X2 + 16*X3 - 87*X4 - 10*X5
    
    st.metric("Score financier", f"{score:.2f}")
    
    # Interprétation
    if score > 9.5:
        st.success("✅ Situation financière saine")
    elif score > -4.5:
        st.warning("⚠️ Situation à surveiller")
    else:
        st.error("❌ Situation risquée - Attention !")

def show_etudes_cas():
    st.markdown('<h2 class="section-header">💼 Études de Cas Pratiques</h2>', unsafe_allow_html=True)
    
    st.success("""
    **🎯 Méthodologie recommandée :**
    1. **Lire** attentivement le contexte de l'entreprise
    2. **Analyser** les données financières fournies  
    3. **Choisir** le type d'analyse à réaliser
    4. **Comparer** vos résultats avec la correction
    5. **Comprendre** les recommandations stratégiques
    """)
    
    cas_choice = st.selectbox(
        "**Choisissez une étude de cas :**",
        [
            "🏭 Diagnostic PME industrielle",
            "📈 Analyse de rentabilité", 
            "⚖️ Équilibre financier",
            "💧 Tableau de flux",
            "🏗️ Projet d'investissement"
        ]
    )
    
    if "PME industrielle" in cas_choice:
        show_cas_pme()
    elif "rentabilité" in cas_choice:
        show_cas_rentabilite()
    elif "Équilibre financier" in cas_choice:
        show_cas_equilibre()
    elif "Tableau de flux" in cas_choice:
        show_cas_flux()
    elif "Projet d'investissement" in cas_choice:
        show_cas_investissement()

def show_cas_pme():
    st.subheader("🏭 Diagnostic d'une PME Industrielle")
    
    st.write("""
    **📋 Contexte :** Société DUBOIS, fabricant de composants électroniques
    - Chiffre d'affaires : 2,5 M€
    - Effectif : 45 personnes
    - Marché en croissance mais concurrence forte
    """)
    
    # Données financières
    st.subheader("📊 Données financières")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Compte de résultat (k€)**")
        data_compte = {
            'Poste': ['Chiffre d\'affaires', 'Achats consommés', 'Charges personnel', 'EBE', 'Dotations amortissement', 'Résultat exploitation'],
            'N': [2500, 1200, 800, 500, 150, 200],
            'N-1': [2300, 1150, 750, 400, 140, 150]
        }
        df_compte = pd.DataFrame(data_compte)
        st.dataframe(df_compte, use_container_width=True)
    
    with col2:
        st.write("**Bilan simplifié (k€)**")
        data_bilan = {
            'Poste': ['Actif immobilisé', 'Stocks', 'Clients', 'Disponibilités', 'Capitaux propres', 'Dettes financières', 'Fournisseurs'],
            'N': [1800, 450, 600, 150, 1200, 800, 1000],
            'N-1': [1700, 400, 550, 200, 1100, 700, 1050]
        }
        df_bilan = pd.DataFrame(data_bilan)
        st.dataframe(df_bilan, use_container_width=True)
    
    # Analyse interactive
    st.subheader("🔍 Analyse à réaliser")
    
    analyse_choice = st.radio(
        "**Sélectionnez l'analyse à effectuer :**",
        ["Ratios de rentabilité", "Structure financière", "Liquidité", "Diagnostic global"]
    )
    
    if analyse_choice == "Ratios de rentabilité":
        show_analyse_rentabilite_cas()
    elif analyse_choice == "Structure financière":
        show_analyse_structure_cas()
    elif analyse_choice == "Liquidité":
        show_analyse_liquidite_cas()
    else:
        show_diagnostic_global_cas()

def show_analyse_rentabilite_cas():
    st.markdown("""
    <div class="question-box">
    <h4>📈 Calcul des ratios de rentabilité</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Questions :**
    1. Calculez les ratios de rentabilité pour N et N-1
    2. Analysez l'évolution de la rentabilité
    3. Identifiez les points forts et les points faibles
    """)
    
    if st.button("📝 Voir la correction détaillée", key="correction_rentabilite"):
        st.markdown("""
        <div class="solution-box">
        <h4>🧮 Correction - Ratios de Rentabilité</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **Calculs détaillés :**
        
        **N-1 :**
        - Taux de marge commerciale = (2.300 - 1.150) / 2.300 = 50,0%
        - Taux EBE = 400 / 2.300 = 17,4%
        - Rentabilité économique = 150 / (1.700 + 400 + 550 + 200) = 5,3%
        - Rentabilité financière = 150 / 1.100 = 13,6%
        
        **N :**
        - Taux de marge commerciale = (2.500 - 1.200) / 2.500 = 52,0%
        - Taux EBE = 500 / 2.500 = 20,0%
        - Rentabilité économique = 200 / (1.800 + 450 + 600 + 150) = 6,7%
        - Rentabilité financière = 200 / 1.200 = 16,7%
        
        **🎯 Analyse :**
        - ✅ **Amélioration de la rentabilité** sur tous les indicateurs
        - ✅ **Taux de marge en hausse** de 50% à 52%
        - ✅ **EBE en forte progression** (+25%)
        - ✅ **Rentabilité financière améliorée** (+3,1 points)
        
        **📋 Recommandations :**
        - Poursuivre les efforts de maîtrise des coûts
        - Maintenir la stratégie de croissance
        - Renforcer la profitabilité
        """)

def show_analyse_structure_cas():
    st.markdown("""
    <div class="question-box">
    <h4>🏗️ Analyse de la structure financière</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Questions :**
    1. Calculez le FRNG, BFR et Trésorerie nette
    2. Analysez l'équilibre financier
    3. Évaluez la structure de financement
    """)
    
    if st.button("📝 Voir la correction détaillée", key="correction_structure"):
        st.markdown("""
        <div class="solution-box">
        <h4>🧮 Correction - Structure Financière</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **Calculs détaillés :**
        
        **FRNG = Ressources stables - Emplois stables**
        - N-1 : (1.100 + 700) - 1.700 = 100 k€
        - N : (1.200 + 800) - 1.800 = 200 k€
        
        **BFR = Actif circulant - Passif circulant**
        - N-1 : (400 + 550) - 1.050 = -100 k€
        - N : (450 + 600) - 1.000 = 50 k€
        
        **Trésorerie nette = FRNG - BFR**
        - N-1 : 100 - (-100) = 200 k€
        - N : 200 - 50 = 150 k€
        
        **Taux d'endettement = Dettes financières / Capitaux propres**
        - N-1 : 700 / 1.100 = 63,6%
        - N : 800 / 1.200 = 66,7%
        
        **🎯 Analyse :**
        - ✅ **FRNG positif et en amélioration**
        - ⚠️ **BFR devient positif** (besoin de financement apparu)
        - ✅ **Trésorerie nette excédentaire** mais en baisse
        - ⚠️ **Endettement en légère hausse** mais acceptable
        
        **📋 Recommandations :**
        - Surveiller l'évolution du BFR
        - Optimiser le cycle d'exploitation
        - Maintenir une politique d'investissement maîtrisée
        """)

def show_analyse_liquidite_cas():
    st.markdown("""
    <div class="question-box">
    <h4>💧 Analyse de la liquidité</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Questions :**
    1. Calculez les ratios de liquidité
    2. Analysez la capacité à faire face aux dettes court terme
    3. Évaluez le risque de liquidité
    """)
    
    if st.button("📝 Voir la correction détaillée", key="correction_liquidite"):
        st.markdown("""
        <div class="solution-box">
        <h4>🧮 Correction - Analyse de Liquidité</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **Calculs détaillés :**
        
        **Ratio de liquidité générale = Actif circulant / Dettes CT**
        - N-1 : (400 + 550 + 200) / 1.050 = 1,10
        - N : (450 + 600 + 150) / 1.000 = 1,20
        
        **Ratio de liquidité réduite = (Actif circulant - Stocks) / Dettes CT**
        - N-1 : (550 + 200) / 1.050 = 0,71
        - N : (600 + 150) / 1.000 = 0,75
        
        **Ratio de liquidité immédiate = Disponibilités / Dettes CT**
        - N-1 : 200 / 1.050 = 0,19
        - N : 150 / 1.000 = 0,15
        
        **🎯 Analyse :**
        - ✅ **Liquidité générale satisfaisante** (>1)
        - ⚠️ **Liquidité réduite faible** (<1)
        - ⚠️ **Liquidité immédiate insuffisante**
        - 📈 **Amélioration globale** des ratios
        
        **📋 Recommandations :**
        - Renforcer la trésorerie disponible
        - Optimiser la gestion des stocks
        - Négocier des délais fournisseurs
        """)

def show_diagnostic_global_cas():
    st.markdown("""
    <div class="question-box">
    <h4>🔍 Diagnostic global</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Questions :**
    1. Synthétisez le diagnostic financier
    2. Identifiez les points forts et les risques
    3. Proposez des recommandations stratégiques
    """)
    
    if st.button("📝 Voir la correction détaillée", key="correction_global"):
        st.markdown("""
        <div class="solution-box">
        <h4>🎯 Correction - Diagnostic Global</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **📊 SYNTHÈSE DU DIAGNOSTIC**
        
        **✅ POINTS FORTS :**
        - Rentabilité en nette amélioration
        - Croissance du chiffre d'affaires (+8,7%)
        - Structure financière équilibrée (FRNG positif)
        - Trésorerie excédentaire
        - Bonne profitabilité (EBE en hausse)
        
        **⚠️ POINTS DE VIGILANCE :**
        - Dégradation de la liquidité immédiate
        - Apparition d'un BFR positif
        - Endettement en légère hausse
        - Liquidité réduite faible
        
        **🔴 RISQUES IDENTIFIÉS :**
        - Risque de tension de trésorerie
        - Dépendance accrue au financement externe
        - Sensibilité à la conjoncture
        
        **📋 RECOMMANDATIONS STRATÉGIQUES :**
        
        **À court terme (6 mois) :**
        - Renforcer la trésorerie disponible
        - Optimiser le BFR (délais clients/fournisseurs)
        - Réviser la politique de stocks
        
        **À moyen terme (1-2 ans) :**
        - Maintenir les investissements productifs
        - Diversifier les sources de financement
        - Renforcer la rentabilité opérationnelle
        
        **À long terme (3-5 ans) :**
        - Poursuivre la croissance maîtrisée
        - Développer de nouveaux marchés
        - Optimiser la structure financière
        """)

def show_cas_rentabilite():
    st.subheader("📈 Analyse de Rentabilité - Cas PRATIQUE")
    
    st.markdown("""
    <div class="cas-container">
    <h3>🏢 Société TEXTILIA - Spécialiste du textile technique</h3>
    
    **Contexte :**
    - Entreprise familiale créée en 1995
    - Spécialisée dans les textiles techniques
    - 120 collaborateurs
    - Marché en croissance mais concurrence internationale forte
    </div>
    """, unsafe_allow_html=True)
    
    # Données financières
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Compte de résultat (k€)")
        data_cr = {
            'Poste': ['Chiffre d\'affaires', 'Coût des ventes', 'Marge brute', 'Frais commerciaux', 
                     'Frais administratifs', 'EBE', 'Dotations amortissements', 'Résultat exploitation',
                     'Charges financières', 'Résultat courant', 'Impôt sur les sociétés', 'Résultat net'],
            'N': [8500, 5100, 3400, 800, 900, 1700, 400, 1300, 150, 1150, 345, 805],
            'N-1': [7800, 4830, 2970, 750, 850, 1370, 380, 990, 140, 850, 255, 595]
        }
        df_cr = pd.DataFrame(data_cr)
        st.dataframe(df_cr, use_container_width=True)
    
    with col2:
        st.subheader("📈 Ratios à calculer")
        st.write("""
        **Questions :**
        1. Calculez les ratios de rentabilité
        2. Analysez la formation du résultat
        3. Identifiez les leviers d'amélioration
        4. Proposez des actions correctives
        """)
        
        st.markdown("""
        <div class="question-box">
        <h5>📋 Travail à réaliser</h5>
        - Taux de marge brute
        - Taux de charges d'exploitation
        - Rentabilité économique
        - Rentabilité financière
        - Effet de levier
        </div>
        """, unsafe_allow_html=True)
    
    # Calculateur interactif
    st.subheader("🧮 Calculateur de Ratios")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ca = st.number_input("CA (k€)", value=8500, key="renta_ca")
        cout_ventes = st.number_input("Coût des ventes (k€)", value=5100, key="renta_cout")
        frais_exploitation = st.number_input("Frais d'exploitation (k€)", value=1700, key="renta_frais")
        resultat_exploitation = st.number_input("Résultat exploitation (k€)", value=1300, key="renta_re")
        resultat_net = st.number_input("Résultat net (k€)", value=805, key="renta_rn")
    
    with col2:
        capitaux_propres = st.number_input("Capitaux propres (k€)", value=4500, key="renta_cp")
        dettes_financieres = st.number_input("Dettes financières (k€)", value=1800, key="renta_dettes")
        actif_economique = st.number_input("Actif économique (k€)", value=7200, key="renta_actif")
        charges_financieres = st.number_input("Charges financières (k€)", value=150, key="renta_charges_fin")
    
    if st.button("📈 Calculer les ratios", key="btn_renta"):
        # Calculs
        marge_brute = (ca - cout_ventes) / ca * 100
        taux_frais_exploitation = frais_exploitation / ca * 100
        rentabilite_economique = resultat_exploitation / actif_economique * 100
        rentabilite_financiere = resultat_net / capitaux_propres * 100
        taux_endettement = dettes_financieres / capitaux_propres * 100
        
        # Affichage résultats
        st.subheader("📊 Résultats des Ratios")
        
        ratios_data = {
            'Ratio': ['Marge brute', 'Taux frais exploitation', 'Rentabilité économique', 
                     'Rentabilité financière', 'Taux d\'endettement'],
            'Valeur': [f"{marge_brute:.1f}%", f"{taux_frais_exploitation:.1f}%", 
                      f"{rentabilite_economique:.1f}%", f"{rentabilite_financiere:.1f}%", 
                      f"{taux_endettement:.1f}%"],
            'Analyse': [
                "✅ Bon" if marge_brute > 35 else "⚠️ Faible",
                "✅ Maîtrisé" if taux_frais_exploitation < 25 else "❌ Élevé",
                "✅ Bonne" if rentabilite_economique > 15 else "⚠️ À améliorer",
                "✅ Excellente" if rentabilite_financiere > 15 else "✅ Correcte",
                "✅ Acceptable" if taux_endettement < 50 else "❌ Élevé"
            ]
        }
        
        df_resultats = pd.DataFrame(ratios_data)
        st.dataframe(df_resultats, use_container_width=True)
    
    # Correction détaillée
    if st.button("🎯 Voir la correction complète", key="btn_correction_renta"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Correction Détaillée - Analyse de Rentabilité</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **🧮 CALCULS DÉTAILLÉS :**
        
        **1. Taux de marge brute :**
        - N-1 : (7.800 - 4.830) / 7.800 = 38,1%
        - N : (8.500 - 5.100) / 8.500 = 40,0%
        → **Amélioration de la marge** (+1,9 points)
        
        **2. Taux de charges d'exploitation :**
        - N-1 : (750 + 850) / 7.800 = 20,5%
        - N : (800 + 900) / 8.500 = 20,0%
        → **Maîtrise des charges** (-0,5 point)
        
        **3. Rentabilité économique :**
        - N-1 : 990 / 6.500 = 15,2%
        - N : 1.300 / 7.200 = 18,1%
        → **Forte amélioration** (+2,9 points)
        
        **4. Rentabilité financière :**
        - N-1 : 595 / 4.200 = 14,2%
        - N : 805 / 4.500 = 17,9%
        → **Excellente progression** (+3,7 points)
        
        **🎯 DIAGNOSTIC :**
        - ✅ **Entreprise très rentable**
        - ✅ **Amélioration sur tous les indicateurs**
        - ✅ **Bonne maîtrise des charges**
        - ✅ **Effet de levier positif**
        
        **📋 RECOMMANDATIONS :**
        - Poursuivre la stratégie de croissance rentable
        - Maintenir la discipline sur les coûts
        - Investir dans l'innovation produit
        - Explorer de nouveaux marchés à forte marge
        """)

def show_cas_equilibre():
    st.subheader("⚖️ Équilibre Financier - Cas CONCRET")
    
    st.markdown("""
    <div class="cas-container">
    <h3>🏗️ Société BATIPRO - Entreprise de BTP</h3>
    
    **Contexte :**
    - Entreprise de construction créée en 2008
    - Spécialisée dans la rénovation énergétique
    - 85 collaborateurs
    - Forte croissance mais tensions de trésorerie
    </div>
    """, unsafe_allow_html=True)
    
    # Données du bilan
    st.subheader("📋 Bilan Financier (k€)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**ACTIF**")
        data_actif = {
            'Poste': ['Actif immobilisé', 'Stocks', 'Créances clients', 'Disponibilités', 'TOTAL ACTIF'],
            'N': [4200, 1800, 3200, 450, 9650],
            'N-1': [3800, 1500, 2800, 600, 8700]
        }
        df_actif = pd.DataFrame(data_actif)
        st.dataframe(df_actif, use_container_width=True)
    
    with col2:
        st.write("**PASSIF**")
        data_passif = {
            'Poste': ['Capitaux propres', 'Dettes financières LT', 'Dettes financières CT', 
                     'Dettes fournisseurs', 'Autres dettes', 'TOTAL PASSIF'],
            'N': [3800, 2200, 800, 2500, 350, 9650],
            'N-1': [3500, 1800, 600, 2400, 400, 8700]
        }
        df_passif = pd.DataFrame(data_passif)
        st.dataframe(df_passif, use_container_width=True)
    
    # Analyse de l'équilibre financier
    st.subheader("🔍 Analyse de l'Équilibre Financier")
    
    st.markdown("""
    <div class="question-box">
    <h5>📋 Questions à résoudre</h5>
    1. Calculez le FRNG, BFR et Trésorerie nette
    2. Analysez l'évolution de la structure financière
    3. Identifiez les déséquilibres éventuels
    4. Proposez des solutions de financement
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur d'équilibre financier
    st.subheader("🧮 Calculateur d'Équilibre Financier")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Ressources Stables**")
        cp = st.number_input("Capitaux propres (k€)", value=3800, key="equi_cp")
        dettes_lt = st.number_input("Dettes LT (k€)", value=2200, key="equi_dettes_lt")
    
    with col2:
        st.write("**Emplois Stables**")
        actif_immob = st.number_input("Actif immobilisé (k€)", value=4200, key="equi_immob")
    
    with col3:
        st.write("**BFR**")
        stocks = st.number_input("Stocks (k€)", value=1800, key="equi_stocks")
        creances = st.number_input("Créances clients (k€)", value=3200, key="equi_creances")
        dettes_court = st.number_input("Dettes CT (k€)", value=2850, key="equi_dettes_ct")
    
    if st.button("📊 Calculer l'équilibre", key="btn_equilibre"):
        # Calculs
        ressources_stables = cp + dettes_lt
        emplois_stables = actif_immob
        frng = ressources_stables - emplois_stables
        
        actif_circulant = stocks + creances
        bfr = actif_circulant - dettes_court
        tresorerie = frng - bfr
        
        # Diagnostic
        st.subheader("📈 Résultats de l'Analyse")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            delta_color = "normal" if frng > 0 else "inverse"
            st.metric("FRNG", f"{frng:,.0f} k€", 
                     delta="✅ Équilibre" if frng > 0 else "❌ Déséquilibre", 
                     delta_color=delta_color)
        
        with col2:
            st.metric("BFR", f"{bfr:,.0f} k€", 
                     delta="📈 Besoin" if bfr > 0 else "📉 Ressource")
        
        with col3:
            delta_color = "normal" if tresorerie > 0 else "inverse"
            st.metric("Trésorerie", f"{tresorerie:,.0f} k€", 
                     delta="✅ Excédent" if tresorerie > 0 else "❌ Déficit", 
                     delta_color=delta_color)
    
    # Correction détaillée
    if st.button("🎯 Voir l'analyse complète", key="btn_analyse_equilibre"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Analyse Complète - Équilibre Financier</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **🧮 CALCULS DÉTAILLÉS :**
        
        **N-1 :**
        - FRNG = (3.500 + 1.800) - 3.800 = 1.500 k€
        - BFR = (1.500 + 2.800) - (2.400 + 400) = 1.500 k€
        - Trésorerie = 1.500 - 1.500 = 0 k€
        
        **N :**
        - FRNG = (3.800 + 2.200) - 4.200 = 1.800 k€
        - BFR = (1.800 + 3.200) - (2.500 + 350) = 2.150 k€
        - Trésorerie = 1.800 - 2.150 = -350 k€
        
        **🎯 DIAGNOSTIC FINANCIER :**
        
        **✅ ASPECTS POSITIFS :**
        - FRNG positif et en augmentation
        - Capacité d'autofinancement suffisante
        - Structure financière globalement saine
        
        **🔴 PROBLÈMES IDENTIFIÉS :**
        - **Déficit de trésorerie** apparu (-350 k€)
        - **BFR en forte augmentation** (+650 k€)
        - **Croissance du besoin de financement**
        - **Tension sur la liquidité**
        
        **📋 PLAN D'ACTION RECOMMANDÉ :**
        
        **Actions immédiates (1-3 mois) :**
        - Renégocier les délais fournisseurs
        - Accélérer le recouvrement clients
        - Mettre en place une ligne de trésorerie
        
        **Actions à moyen terme (3-12 mois) :**
        - Optimiser la gestion des stocks
        - Réviser la politique commerciale
        - Renforcer les capitaux propres
        
        **Actions stratégiques (1-3 ans) :**
        - Diversifier les sources de financement
        - Améliorer la rentabilité opérationnelle
        - Développer un fonds de roulement permanent
        """)

def show_cas_flux():
    st.subheader("💧 Tableaux de Flux - Cas APPLICATIF")
    
    st.markdown("""
    <div class="cas-container">
    <h3>⚡ Société ENERG-TECH - Énergies renouvelables</h3>
    
    **Contexte :**
    - Start-up créée en 2018 dans les énergies solaires
    - Forte croissance avec besoins d'investissement importants
    - 65 collaborateurs
    - Phase de développement accéléré
    </div>
    """, unsafe_allow_html=True)
    
    # Tableaux de flux
    st.subheader("📊 Tableaux des Flux de Trésorerie (k€)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**FLUX D'EXPLOITATION**")
        data_exploitation = {
            'Poste': ['Résultat net', 'Dotations aux amortissements', 'Variation BFR exploitation', 
                     'Intérêts payés', 'Impôts payés', 'FLUX NET EXPLOITATION'],
            'N': [650, 420, -380, 95, 210, 805],
            'N-1': [480, 350, -220, 75, 145, 480]
        }
        df_exploitation = pd.DataFrame(data_exploitation)
        st.dataframe(df_exploitation, use_container_width=True)
    
    with col2:
        st.write("**FLUX D'INVESTISSEMENT**")
        data_investissement = {
            'Poste': ['Acquisitions immobilisations', 'Cessions immobilisations', 
                     'Acquisitions titres', 'FLUX NET INVESTISSEMENT'],
            'N': [-1250, 120, -80, -1210],
            'N-1': [-980, 90, -50, -940]
        }
        df_investissement = pd.DataFrame(data_investissement)
        st.dataframe(df_investissement, use_container_width=True)
    
    st.write("**FLUX DE FINANCEMENT**")
    data_financement = {
        'Poste': ['Augmentation capital', 'Emprunts nouveaux', 'Remboursements emprunts',
                 'Dividendes versés', 'FLUX NET FINANCEMENT'],
        'N': [500, 800, -450, -180, 670],
        'N-1': [300, 600, -380, -120, 400]
    }
    df_financement = pd.DataFrame(data_financement)
    st.dataframe(df_financement, use_container_width=True)
    
    # Analyse des flux
    st.subheader("🔍 Analyse des Flux de Trésorerie")
    
    st.markdown("""
    <div class="question-box">
    <h5>📋 Questions à résoudre</h5>
    1. Analysez la génération de trésorerie d'exploitation
    2. Évaluez la politique d'investissement
    3. Commentez la stratégie de financement
    4. Synthétisez la situation de trésorerie
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur de flux
    st.subheader("🧮 Calculateur de Flux de Trésorerie")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Flux Exploitation**")
        resultat_net = st.number_input("Résultat net (k€)", value=650, key="flux_rn")
        dotations = st.number_input("Dotations (k€)", value=420, key="flux_dot")
        variation_bfr = st.number_input("Δ BFR (k€)", value=-380, key="flux_bfr")
    
    with col2:
        st.write("**Flux Investissement**")
        acquisitions = st.number_input("Acquisitions (k€)", value=-1250, key="flux_acqu")
        cessions = st.number_input("Cessions (k€)", value=120, key="flux_cess")
    
    with col3:
        st.write("**Flux Financement**")
        augmentation_capital = st.number_input("Aug. capital (k€)", value=500, key="flux_cap")
        nouveaux_emprunts = st.number_input("Nouveaux emprunts (k€)", value=800, key="flux_emp")
        remboursements = st.number_input("Remboursements (k€)", value=-450, key="flux_remb")
    
    if st.button("💰 Calculer les flux", key="btn_flux"):
        # Calculs
        flux_exploitation = resultat_net + dotations + variation_bfr
        flux_investissement = acquisitions + cessions
        flux_financement = augmentation_capital + nouveaux_emprunts + remboursements
        variation_tresorerie = flux_exploitation + flux_investissement + flux_financement
        
        # Affichage résultats
        st.subheader("📈 Synthèse des Flux")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            delta_color = "normal" if flux_exploitation > 0 else "inverse"
            st.metric("Flux Exploitation", f"{flux_exploitation:,.0f} k€", 
                     delta="✅ Positif" if flux_exploitation > 0 else "❌ Négatif", 
                     delta_color=delta_color)
        
        with col2:
            st.metric("Flux Investissement", f"{flux_investissement:,.0f} k€")
        
        with col3:
            delta_color = "normal" if flux_financement > 0 else "inverse"
            st.metric("Flux Financement", f"{flux_financement:,.0f} k€", 
                     delta="✅ Entrées" if flux_financement > 0 else "❌ Sorties", 
                     delta_color=delta_color)
        
        with col4:
            delta_color = "normal" if variation_tresorerie > 0 else "inverse"
            st.metric("Δ Trésorerie", f"{variation_tresorerie:,.0f} k€", 
                     delta="✅ Augmentation" if variation_tresorerie > 0 else "❌ Diminution", 
                     delta_color=delta_color)
    
    # Correction détaillée
    if st.button("🎯 Analyse complète des flux", key="btn_analyse_flux"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Analyse Complète - Tableaux de Flux</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **🧮 ANALYSE DES FLUX :**
        
        **FLUX D'EXPLOITATION :**
        - **Trésorerie d'exploitation positive** : 805 k€ (N) vs 480 k€ (N-1)
        - **Forte croissance** de la capacité à générer de la trésorerie (+68%)
        - **BFR exploitation consommateur** de trésorerie (-380 k€)
        - **Activité rentable** avec bonne transformation du résultat en cash
        
        **FLUX D'INVESTISSEMENT :**
        - **Investissements importants** : -1.210 k€ (N) vs -940 k€ (N-1)
        - **Politique de croissance ambitieuse**
        - **Capacité d'autofinancement insuffisante** pour couvrir les investissements
        - **Besoin de financement externe**
        
        **FLUX DE FINANCEMENT :**
        - **Recours au financement externe** : 670 k€ d'entrées nettes
        - **Augmentation de capital** significative (500 k€)
        - **Endettement maîtrisé** avec nouvel emprunt de 800 k€
        - **Politique de dividende raisonnable**
        
        **🎯 DIAGNOSTIC GLOBAL :**
        
        **✅ POINTS FORTS :**
        - Forte croissance de la trésorerie d'exploitation
        - Stratégie d'investissement cohérente
        - Financement équilibré entre fonds propres et dette
        - Bonne visibilité sur les flux futurs
        
        **⚠️ POINTS DE VIGILANCE :**
        - BFR fortement consommateur de trésorerie
        - Dépendance au financement externe
        - Croissance des investissements supérieure à la CAF
        - Risque de tension si ralentissement économique
        
        **📋 RECOMMANDATIONS :**
        
        **Gestion du BFR :**
        - Optimiser les délais de paiement clients
        - Négocier des délais fournisseurs étendus
        - Mettre en place un plan de relance client
        
        **Stratégie d'investissement :**
        - Prioriser les investissements les plus rentables
        - Échelonner les gros investissements
        - Étudier les solutions de leasing
        
        **Politique de financement :**
        - Maintenir un équilibre fonds propres/dette
        - Diversifier les sources de financement
        - Anticiper les besoins futurs
        """)

def show_cas_investissement():
    st.subheader("🏗️ Projet d'Investissement - Cas DÉCISIONNEL")
    
    st.markdown("""
    <div class="cas-container">
    <h3>🏭 Société AGRO-INNOV - Transformation alimentaire</h3>
    
    **Contexte :**
    - Projet d'investissement dans une nouvelle ligne de production
    - Investissement : 2,5 M€
    - Durée du projet : 5 ans
    - Objectif : augmentation de capacité de 40%
    </div>
    """, unsafe_allow_html=True)
    
    # Données du projet
    st.subheader("📋 Données du Projet d'Investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**INVESTISSEMENT INITIAL**")
        data_investissement = {
            'Poste': ['Machines et équipements', 'Installation et mise en route', 
                     "Frais d'études", 'Besoins en fonds de roulement', "TOTAL"],
            'Montant (k€)': [1800, 400, 150, 250, 2600]
        }
        df_invest = pd.DataFrame(data_investissement)
        st.dataframe(df_invest, use_container_width=True)
    
    with col2:
        st.write("**FLUX PRÉVISIONNELS**")
        data_flux = {
            'Année': [1, 2, 3, 4, 5],
            'CA supplémentaire (k€)': [1200, 1800, 2400, 2400, 2400],
            'Charges variables (k€)': [600, 900, 1200, 1200, 1200],
            'Charges fixes (k€)': [300, 350, 400, 400, 400]
        }
        df_flux = pd.DataFrame(data_flux)
        st.dataframe(df_flux, use_container_width=True)
    
    # Critères d'évaluation
    st.subheader("🎯 Critères d'Évaluation du Projet")
    
    st.markdown("""
    <div class="question-box">
    <h5>📋 Questions de décision</h5>
    1. Calculez la VAN du projet (taux d'actualisation : 10%)
    2. Déterminez le TRI approximatif
    3. Évaluez le délai de récupération
    4. Analysez la sensibilité du projet
    5. Prenez une décision d'investissement
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur d'investissement
    st.subheader("🧮 Calculateur de Rentabilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investissement = st.number_input("Investissement initial (k€)", value=2600, key="inv_initial")
        taux_actualisation = st.number_input("Taux d'actualisation (%)", value=10.0, key="inv_taux") / 100
        duree = st.number_input("Durée du projet (années)", value=5, key="inv_duree")
    
    with col2:
        st.write("**Flux de trésorerie annuels (k€)**")
        flux_annee1 = st.number_input("Année 1", value=300, key="inv_flux1")
        flux_annee2 = st.number_input("Année 2", value=550, key="inv_flux2")
        flux_annee3 = st.number_input("Année 3", value=800, key="inv_flux3")
        flux_annee4 = st.number_input("Année 4", value=800, key="inv_flux4")
        flux_annee5 = st.number_input("Année 5", value=1050, key="inv_flux5")  # inclut récupération BFR
    
    if st.button("📊 Évaluer le projet", key="btn_eval_invest"):
        # Calcul VAN
        flux = [flux_annee1, flux_annee2, flux_annee3, flux_annee4, flux_annee5]
        van = -investissement
        for i, flux_annuel in enumerate(flux):
            van += flux_annuel / ((1 + taux_actualisation) ** (i + 1))
        
        # Estimation TRI
        def calcul_van_tri(taux):
            van_calc = -investissement
            for i, flux_annuel in enumerate(flux):
                van_calc += flux_annuel / ((1 + taux) ** (i + 1))
            return van_calc
        
        # Recherche TRI
        tri = taux_actualisation
        for taux_test in np.arange(0.01, 0.50, 0.01):
            if calcul_van_tri(taux_test) >= 0:
                tri = taux_test
            else:
                break
        
        # Délai de récupération
        cumul_flux = 0
        delai_recup = duree + 1
        for i, flux_annuel in enumerate(flux):
            cumul_flux += flux_annuel
            if cumul_flux >= investissement and delai_recup > duree:
                delai_recup = i + 1
        
        # Affichage résultats
        st.subheader("📈 Résultats de l'Évaluation")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            delta_color = "normal" if van > 0 else "inverse"
            st.metric("VAN", f"{van:,.0f} k€", 
                     delta="✅ Rentable" if van > 0 else "❌ Non rentable", 
                     delta_color=delta_color)
        
        with col2:
            st.metric("TRI", f"{tri*100:.1f}%")
        
        with col3:
            st.metric("Délai récupération", f"{delai_recup} ans")
    
    # Analyse de sensibilité
    st.subheader("📊 Analyse de Sensibilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        variation_ca = st.slider("Variation du CA (%)", -20, 20, 0, key="sens_ca")
        variation_charges = st.slider("Variation des charges (%)", -15, 15, 0, key="sens_charges")
    
    with col2:
        variation_invest = st.slider("Variation investissement (%)", -10, 10, 0, key="sens_invest")
        variation_taux = st.slider("Variation taux actualisation (%)", -3, 3, 0, key="sens_taux")
    
    if st.button("🔄 Calculer la sensibilité", key="btn_sensibilite"):
        # Recalcul avec variations
        invest_ajuste = investissement * (1 + variation_invest/100)
        taux_ajuste = (taux_actualisation * 100 + variation_taux) / 100
        
        flux_ajustes = [
            flux_annee1 * (1 + (variation_ca - variation_charges)/100),
            flux_annee2 * (1 + (variation_ca - variation_charges)/100),
            flux_annee3 * (1 + (variation_ca - variation_charges)/100),
            flux_annee4 * (1 + (variation_ca - variation_charges)/100),
            flux_annee5 * (1 + (variation_ca - variation_charges)/100)
        ]
        
        van_sensibilite = -invest_ajuste
        for i, flux_annuel in enumerate(flux_ajustes):
            van_sensibilite += flux_annuel / ((1 + taux_ajuste) ** (i + 1))
        
        st.metric("VAN après sensibilité", f"{van_sensibilite:,.0f} k€", 
                 delta=f"{van_sensibilite - van:+.0f} k€")
    
    # Décision d'investissement
    if st.button("🎯 Prendre la décision", key="btn_decision"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Décision d'Investissement - Analyse Complète</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **🧮 ÉVALUATION FINANCIÈRE :**
        
        **Calculs de base :**
        - **VAN** : Environ 450 k€ (positive)
        - **TRI** : Environ 18% (> taux d'actualisation de 10%)
        - **Délai de récupération** : 4 ans
        
        **ANALYSE DE SENSIBILITÉ :**
        
        **Scénario pessimiste** (CA -10%, charges +5%) :
        - VAN devient : 150 k€ (toujours positive)
        - TRI : 13% (acceptable)
        
        **Scénario optimiste** (CA +10%, charges -5%) :
        - VAN devient : 750 k€ (très bonne)
        - TRI : 22% (excellent)
        
        **🎯 CRITÈRES DE DÉCISION :**
        
        **✅ ARGUMENTS POUR L'INVESTISSEMENT :**
        - VAN positive significative
        TRI supérieur au coût du capital
        - Délai de récupération acceptable
        - Potentiel de croissance important
        - Avantage concurrentiel durable
        
        **⚠️ RISQUES IDENTIFIÉS :**
        - Sensibilité aux variations du marché
        - Besoin en fonds de roulement important
        - Concurrence potentielle
        - Évolution des coûts énergétiques
        
        **📋 RECOMMANDATION :**
        
        **💡 DÉCISION : INVESTIR** 
        
        **Conditions :**
        1. Mise en place d'un plan de suivi rigoureux
        2. Définition d'indicateurs de performance
        3. Plan de contingence en cas de déviation
        4. Révision trimestrielle des hypothèses
        
        **Plan d'action :**
        - **Mois 1-3** : Négociation des équipements
        - **Mois 4-6** : Installation et formation
        - **Mois 7-9** : Démarrage progressif
        - **Mois 10-12** : Optimisation et montée en charge
        
        **Suivi post-investissement :**
        - Reporting mensuel des performances
        - Analyse trimestrielle de la rentabilité
        - Ajustement de la stratégie commerciale
        - Évaluation continue des risques
        """)

def show_ressources():
    st.markdown('<h2 class="section-header">📚 Ressources Pédagogiques</h2>', unsafe_allow_html=True)
    
    st.success("""
    **🎯 Comment utiliser cette section :**
    - **Téléchargez** les fiches mémo pour réviser
    - **Testez** vos connaissances avec les quiz  
    - **Utilisez** les modèles pour vos propres analyses
    - **Progressez** à votre rythme
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📖 Fiches Mémo")
        
        ressources = {
            "📄 Bilan": "Structure actif/passif, équilibre, analyse",
            "📊 Compte de résultat": "Soldes, SIG, rentabilité", 
            "📐 Ratios financiers": "Calcul, interprétation, normes",
            "💧 Tableaux de flux": "Construction, analyse, OEC vs CDB",
            "🔍 Diagnostic financier": "Méthodologie, outils, reporting"
        }
        
        for ressource, description in ressources.items():
            with st.expander(f"{ressource}"):
                st.write(description)
                st.download_button(
                    f"📥 Télécharger {ressource}",
                    f"Contenu de la fiche {ressource}",
                    file_name=f"fiche_{ressource.lower().replace(' ', '_')}.txt"
                )
    
    with col2:
        st.subheader("🎓 Quiz d'auto-évaluation")
        
        quiz_choice = st.selectbox(
            "**Choisissez un quiz :**",
            ["🟢 Débutant - Fondamentaux", "🟡 Intermédiaire - Bilan", 
             "🟠 Avancé - Compte de résultat", "🔴 Expert - Ratios", "🏆 Master - Diagnostic global"]
        )
        
        if "Débutant" in quiz_choice:
            show_quiz_fondamentaux()
        elif "Bilan" in quiz_choice:
            show_quiz_bilan()
    
    st.subheader("📊 Modèles et Templates")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button(
            "📋 Modèle de bilan",
            "Template de bilan format Excel",
            file_name="modele_bilan.xlsx"
        )
    
    with col2:
        st.download_button(
            "📊 Modèle de ratios",
            "Calculateur automatique de ratios",
            file_name="calculateur_ratios.xlsx"
        )
    
    with col3:
        st.download_button(
            "📈 Modèle de tableau de flux",
            "Template tableau de flux OEC",
            file_name="tableau_flux_oec.xlsx"
        )

def show_quiz_fondamentaux():
    st.write("**Testez vos connaissances sur les fondamentaux de l'analyse financière**")
    
    questions = [
        {
            "question": "Qu'est-ce que le fonds de roulement net global (FRNG)?",
            "options": [
                "La différence entre l'actif et le passif",
                "L'excédent des ressources stables sur les emplois stables", 
                "Le montant de la trésorerie disponible",
                "Le besoin de financement du cycle d'exploitation"
            ],
            "reponse": 1
        },
        {
            "question": "Quel est l'objectif principal de l'EBE?",
            "options": [
                "Mesurer le résultat net",
                "Évaluer la performance économique avant éléments financiers",
                "Calculer la capacité d'autofinancement",
                "Déterminer la trésorerie"
            ],
            "reponse": 1
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        reponse = st.radio(f"Choisissez votre réponse:", q['options'], key=f"quiz_q{i}")
        
        if st.button(f"Vérifier question {i+1}", key=f"quiz_btn{i}"):
            if q['options'].index(reponse) == q['reponse']:
                st.success("✅ Bonne réponse!")
                score += 1
            else:
                st.error(f"❌ Mauvaise réponse. La bonne réponse était: {q['options'][q['reponse']]}")
    
    if st.button("🎯 Voir le score final", key="quiz_final"):
        st.info(f"**Score: {score}/{len(questions)}**")
        if score == len(questions):
            st.balloons()
            st.success("🎉 Excellent! Toutes les réponses sont correctes!")
        elif score >= len(questions)/2:
            st.warning("📚 Bien! Continuez à progresser!")
        else:
            st.error("📖 Revoyez les concepts fondamentaux")

def show_quiz_bilan():
    st.write("**Quiz sur le bilan comptable**")
    st.info("Ce quiz sera bientôt disponible...")
    
    




import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Maîtrise de l'Analyse Financière",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2e86ab;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .concept-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .usage-step {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #ff6b6b;
    }
    .tip-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        background-color: #f8f9fa;
        border-top: 1px solid #dee2e6;
        color: #6c757d;
        font-size: 0.9rem;
    }
    .cas-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #dee2e6;
    }
    .question-box {
        background-color: #e7f3ff;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #007bff;
    }
    .solution-box {
        background-color: #d4edda;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

def show_footer():
    st.markdown("""
    <div class="footer">
    <strong>Plateforme d'apprentissage de l'analyse financière • Version 3.0</strong><br>
    📚 Développé pour les étudiants, professionnels et entrepreneurs par Amiharbi Eyeug • © 2024
    </div>
    """, unsafe_allow_html=True)

def main():
    # Header principal
    st.markdown('<h1 class="main-header">📊 Maîtrise de l\'Analyse Financière</h1>', unsafe_allow_html=True)
    
    # Navigation par onglets
    tabs = st.tabs([
        "🏠 Accueil & Guide",
        "📈 Concepts Fondamentaux",
        "🧮 Calculateurs",
        "💼 Études de Cas",
        "📚 Ressources"
    ])
    
    with tabs[0]:
        show_accueil_guide()
        show_footer()
    
    with tabs[1]:
        show_concepts_fondamentaux()
        show_footer()
    
    with tabs[2]:
        show_calculateurs()
        show_footer()
    
    with tabs[3]:
        show_etudes_cas()
        show_footer()
    
    with tabs[4]:
        show_ressources()
        show_footer()

def show_accueil_guide():
    st.markdown('<h2 class="section-header">🎯 Guide Complet d\'Utilisation</h2>', unsafe_allow_html=True)
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        ## Bienvenue dans l'application d'analyse financière !
        
        Cette application interactive vous permet de **maîtriser progressivement tous les aspects 
        de l'analyse financière** d'entreprise grâce à une approche pratique basée sur le 
        manuel "Maxi Fiches de Gestion Financière".
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400", 
                caption="Analyse Financière Interactive")
    
    # Mode d'utilisation détaillé
    st.markdown("""
    <div class="concept-card">
    <h3>🚀 Comment Utiliser Cette Application</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Structure de navigation
    st.subheader("📋 Structure de Navigation")
    
    nav_cols = st.columns(5)
    with nav_cols[0]:
        st.info("**🏠 Accueil**\n\nGuide d'utilisation et parcours d'apprentissage")
    with nav_cols[1]:
        st.success("**📈 Concepts**\n\nThéorie avec exemples interactifs")
    with nav_cols[2]:
        st.warning("**🧮 Calculateurs**\n\nOutils pratiques et simulations")
    with nav_cols[3]:
        st.error("**💼 Études de Cas**\n\nSituations réelles avec corrigés")
    with nav_cols[4]:
        st.info("**📚 Ressources**\n\nFiches, quiz et modèles")
    
    # Parcours recommandé selon le niveau
    st.subheader("🎓 Parcours d'Apprentissage Recommandé")
    
    niveau = st.radio("**Sélectionnez votre niveau :**", 
                     ["🟢 Débutant", "🟡 Intermédiaire", "🔴 Avancé"], 
                     horizontal=True)
    
    if niveau == "🟢 Débutant":
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Débutant (20-30 heures)</h4>
        <ol>
            <li><strong>Semaines 1-2 :</strong> Accueil → Concepts (Bilan & Compte de résultat)</li>
            <li><strong>Semaines 3-4 :</strong> Concepts (SIG & Seuil de rentabilité)</li>
            <li><strong>Semaines 5-6 :</strong> Calculateurs basiques → Quiz fondamentaux</li>
            <li><strong>Semaines 7-8 :</strong> Études de cas simples → Ressources</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    elif niveau == "🟡 Intermédiaire":
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Intermédiaire (15-25 heures)</h4>
        <ol>
            <li><strong>Semaines 1-2 :</strong> Revoir Concepts → Calculateurs avancés</li>
            <li><strong>Semaines 3-4 :</strong> Études de cas complexes → Analyse complète</li>
            <li><strong>Semaines 5-6 :</strong> Calculateurs VAN/TIR → Scores financiers</li>
            <li><strong>Semaines 7-8 :</strong> Quiz experts → Modèles personnalisés</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div class="usage-step">
        <h4>🎯 Parcours Avancé (10-20 heures)</h4>
        <ol>
            <li><strong>Semaine 1 :</strong> Calculateurs avancés → Diagnostics complexes</li>
            <li><strong>Semaine 2 :</strong> Études de cas experts → Recommandations stratégiques</li>
            <li><strong>Semaine 3 :</strong> Modèles personnalisés → Analyses sectorielles</li>
            <li><strong>Semaine 4 :</strong> Validation complète → Applications pratiques</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Guide détaillé par onglet
    st.subheader("📖 Guide Détaillé par Section")
    
    with st.expander("🏠 ONGLET ACCUEIL & GUIDE", expanded=True):
        st.markdown("""
        **Objectif** : Comprendre le parcours et optimiser votre apprentissage
        
        **Actions clés :**
        - 📊 Identifier votre niveau actuel
        - 🗺️ Suivre le parcours recommandé
        - ⏱️ Planifier votre temps d'apprentissage
        - 🎯 Définir vos objectifs personnels
        
        **Temps recommandé :** 15-30 minutes
        """)
    
    with st.expander("📈 ONGLET CONCEPTS FONDAMENTAUX"):
        st.markdown("""
        **Objectif** : Apprendre la théorie avec des exemples interactifs
        
        **Mode d'emploi :**
        1. **Sélectionnez un concept** dans le menu déroulant
        2. **Lisez les explications** théoriques détaillées
        3. **Utilisez les calculateurs intégrés** pour pratiquer
        4. **Analysez les graphiques** et interprétations automatiques
        
        **Concepts disponibles :**
        - 🔍 Diagnostic Financier
        - ⚖️ Bilan Comptable (avec calculateur d'équilibre)
        - 📊 Compte de Résultat (avec simulateur)
        - 📈 Soldes Intermédiaires de Gestion (SIG)
        - 🎯 Seuil de Rentabilité (avec graphique)
        - 💰 Fonds de Roulement & BFR
        - 📐 Ratios Financiers (avec tableau de bord)
        
        **Temps recommandé :** 2-3 heures par concept
        """)
    
    with st.expander("🧮 ONGLET CALCULATEURS"):
        st.markdown("""
        **Objectif** : Appliquer les concepts avec des outils pratiques
        
        **Calculateurs disponibles :**
        
        **📉 Amortissements** (Linéaire/Dégressif)
        → Saisir : Valeur, durée, coefficient
        → Obtenir : Tableau complet + Graphique
        
        **💸 Capacité d'Autofinancement** (CAF)
        → Saisir : Résultat net, dotations, reprises
        → Obtenir : CAF + Diagnostic automatique
        
        **⚖️ Effet de Levier Financier**
        → Saisir : Actif, capitaux, dettes, taux
        → Obtenir : Rentabilité économique vs financière
        
        **📊 VAN/TIR** (Investissements)
        → Saisir : Investissement, flux, durée
        → Obtenir : VAN + TIR + Recommandation
        
        **🎯 Score Financier** (Risque défaillance)
        → Saisir : EBE, endettement, ratios clés
        → Obtenir : Score + Diagnostic risque
        
        **Temps recommandé :** 1-2 heures par calculateur
        """)
    
    with st.expander("💼 ONGLET ÉTUDES DE CAS"):
        st.markdown("""
        **Objectif** : Mettre en pratique sur des situations réelles
        
        **Méthodologie :**
        1. **Lire le contexte** de l'entreprise
        2. **Analyser les données** financières fournies
        3. **Choisir le type d'analyse** à réaliser
        4. **Comparer vos résultats** avec la correction
        5. **Comprendre les recommandations**
        
        **Cas disponibles :**
        - 🏭 PME Industrielle (analyse complète)
        - 📈 Analyse de Rentabilité
        - ⚖️ Équilibre Financier
        - 💧 Tableaux de Flux
        - 🏗️ Projet d'Investissement
        
        **Temps recommandé :** 2-4 heures par étude de cas
        """)
    
    with st.expander("📚 ONGLET RESSOURCES"):
        st.markdown("""
        **Objectif** : Consolider et tester ses connaissances
        
        **Ressources disponibles :**
        
        **📖 Fiches Mémo Téléchargeables**
        - Formats : PDF/Excel
        - Thèmes : Bilan, Compte de résultat, Ratios, etc.
        - Utilisation : Révisions rapides
        
        **🎓 Quiz d'Auto-évaluation**
        - Niveaux : Débutant à Expert
        - Correction immédiate avec explications
        - Score final avec recommandations
        
        **📊 Modèles et Templates**
        - Fichiers Excel réutilisables
        - Tableaux pré-formatés
        - Calculateurs personnalisables
        
        **Temps recommandé :** 30 minutes à 1 heure par ressource
        """)
    
    # Conseils d'optimisation
    st.subheader("💡 Conseils d'Optimisation")
    
    tip_cols = st.columns(3)
    
    with tip_cols[0]:
        st.markdown("""
        <div class="tip-box">
        <h5>🎮 Pour les Débutants</h5>
        - Suivez le parcours recommandé
        - Prenez des notes dans chaque section
        - Refaites les exercices plusieurs fois
        - Utilisez systématiquement les calculateurs
        </div>
        """, unsafe_allow_html=True)
    
    with tip_cols[1]:
        st.markdown("""
        <div class="tip-box">
        <h5>🚀 Pour les Intermédiaires</h5>
        - Testez différents scénarios
        - Comparez vos analyses avec les corrigés
        - Personnalisez les paramètres
        - Téléchargez les modèles pour vos projets
        </div>
        """, unsafe_allow_html=True)
    
    with tip_cols[2]:
        st.markdown("""
        <div class="tip-box">
        <h5>🏆 Pour les Experts</h5>
        - Utilisez les études de cas complexes
        - Développez vos propres scénarios
        - Intégrez les modèles dans vos outils
        - Validez vos méthodologies d'analyse
        </div>
        """, unsafe_allow_html=True)
    
    # Progression globale
    st.subheader("📊 Progression Globale Recommandée")
    
    progress_data = {
        "Module": ["Fondamentaux", "Bilan & Compte de résultat", "Ratios & SIG", 
                  "Analyse fonctionnelle", "Tableaux de flux", "Diagnostic avancé"],
        "Durée estimée": ["2 semaines", "3 semaines", "2 semaines", "2 semaines", "3 semaines", "2 semaines"],
        "Difficulté": ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        "Onglets clés": ["Concepts", "Concepts + Calculateurs", "Calculateurs + Cas", 
                        "Cas + Calculateurs", "Cas + Ressources", "Tous les onglets"]
    }
    
    df_progress = pd.DataFrame(progress_data)
    st.dataframe(df_progress, use_container_width=True)
    
    # Derniers conseils
    st.markdown("""
    <div class="tip-box">
    <h5>💎 Derniers Conseils Importants</h5>
    - <strong>Sauvegardez</strong> vos paramètres intéressants
    - <strong>Téléchargez</strong> les résultats importants  
    - <strong>Expérimentez</strong> avec différentes valeurs
    - <strong>Consultez</strong> les explications détaillées
    - <strong>Pratiquez</strong> régulièrement pour progresser
    </div>
    """, unsafe_allow_html=True)

def show_concepts_fondamentaux():
    st.markdown('<h2 class="section-header">📈 Concepts Fondamentaux</h2>', unsafe_allow_html=True)
    
    # Guide rapide d'utilisation
    st.info("""
    **🎯 Comment utiliser cette section :**
    1. Sélectionnez un concept dans le menu ci-dessous
    2. Lisez les explications théoriques détaillées  
    3. Utilisez les calculateurs intégrés pour pratiquer
    4. Analysez les graphiques et interprétations automatiques
    """)
    
    concept_choice = st.selectbox(
        "**Choisissez un concept à explorer :**",
        [
            "🔍 Diagnostic Financier",
            "⚖️ Bilan Comptable", 
            "📊 Compte de Résultat",
            "📈 Soldes Intermédiaires de Gestion",
            "🎯 Seuil de Rentabilité",
            "💰 Fonds de Roulement",
            "📐 Ratios Financiers"
        ]
    )
    
    if "Diagnostic Financier" in concept_choice:
        show_diagnostic_financier()
    elif "Bilan Comptable" in concept_choice:
        show_bilan_comptable()
    elif "Compte de Résultat" in concept_choice:
        show_compte_resultat()
    elif "Soldes Intermédiaires" in concept_choice:
        show_soldes_gestion()
    elif "Seuil de Rentabilité" in concept_choice:
        show_seuil_rentabilite()
    elif "Fonds de Roulement" in concept_choice:
        show_fonds_roulement()
    elif "Ratios Financiers" in concept_choice:
        show_ratios_financiers()

def show_diagnostic_financier():
    st.markdown("""
    <div class="concept-card">
    <h3>🔍 Diagnostic Financier</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **📖 Définition :**
        Le diagnostic financier est une démarche qui vise à :
        - Identifier les causes de difficultés présentes ou futures
        - Mettre en lumière les dysfonctionnements
        - Présenter les perspectives d'évolution
        - Proposer des actions correctives
        
        **📋 États financiers analysés :**
        - Bilan (patrimoine à une date donnée)
        - Compte de résultat (performance sur une période)
        - Annexe (informations complémentaires)
        """)
    
    with col2:
        st.write("""
        **🛠️ Méthodologie :**
        1. Analyse de la rentabilité
        2. Analyse de la liquidité
        3. Analyse de la structure financière
        4. Analyse économique complémentaire
        
        **📊 Outils :**
        - Ratios financiers
        - Tableaux de flux
        - Soldes intermédiaires de gestion
        - Comparaisons sectorielles
        """)
    
    # Schéma du processus de diagnostic
    st.subheader("📋 Processus de Diagnostic")
    
    steps = {
        "Étape 1": "Collecte des états financiers",
        "Étape 2": "Analyse horizontale et verticale", 
        "Étape 3": "Calcul des ratios",
        "Étape 4": "Analyse fonctionnelle",
        "Étape 5": "Diagnostic et recommandations"
    }
    
    for step, description in steps.items():
        st.write(f"**{step}:** {description}")

def show_bilan_comptable():
    st.markdown("""
    <div class="concept-card">
    <h3>⚖️ Bilan Comptable</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Photographie du patrimoine de l'entreprise à une date donnée.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("ACTIF")
        st.write("""
        **Actif Immobilisé:**
        - Immobilisations incorporelles
        - Immobilisations corporelles  
        - Immobilisations financières
        
        **Actif Circulant:**
        - Stocks
        - Créances clients
        - Disponibilités
        """)
    
    with col2:
        st.subheader("PASSIF")
        st.write("""
        **Capitaux Propres:**
        - Capital social
        - Réserves
        - Résultat de l'exercice
        
        **Dettes:**
        - Dettes financières
        - Dettes fournisseurs
        - Dettes fiscales et sociales
        """)
    
    # Calculateur simplifié de bilan
    st.subheader("🧮 Calculateur de Bilan - Pratiquez !")
    
    st.warning("💡 **Exercice :** Essayez de créer un bilan équilibré en ajustant les valeurs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Actif**")
        immob_corporelles = st.number_input("Immobilisations corporelles", value=500000, key="bilan_actif1")
        stocks = st.number_input("Stocks", value=200000, key="bilan_actif2")
        clients = st.number_input("Créances clients", value=300000, key="bilan_actif3")
        disponibilites = st.number_input("Disponibilités", value=100000, key="bilan_actif4")
        
        total_actif = immob_corporelles + stocks + clients + disponibilites
        
    with col2:
        st.write("**Passif**")
        capital = st.number_input("Capital social", value=400000, key="bilan_passif1")
        reserves = st.number_input("Réserves", value=300000, key="bilan_passif2")
        resultat = st.number_input("Résultat", value=100000, key="bilan_passif3")
        emprunts = st.number_input("Emprunts", value=200000, key="bilan_passif4")
        fournisseurs = st.number_input("Dettes fournisseurs", value=100000, key="bilan_passif5")
        
        total_passif = capital + reserves + resultat + emprunts + fournisseurs
    
    # Vérification équilibre
    st.subheader("📊 Résultat de l'Exercice")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Actif", f"{total_actif:,.0f} €")
    with col2:
        st.metric("Total Passif", f"{total_passif:,.0f} €")
    with col3:
        difference = total_actif - total_passif
        if abs(difference) < 1:
            st.success("✅ Bilan Équilibré")
        else:
            st.error(f"❌ Écart : {difference:,.0f} €")

def show_compte_resultat():
    st.markdown("""
    <div class="concept-card">
    <h3>📊 Compte de Résultat</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Mesure la performance économique sur une période (généralement un an).
    """)
    
    # Structure du compte de résultat
    st.subheader("🏗️ Structure du Compte de Résultat")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **CHARGES**
        - Achats de marchandises
        - Variation de stocks
        - Charges externes
        - Impôts et taxes
        - Charges de personnel
        - Dotations aux amortissements
        - Charges financières
        - Charges exceptionnelles
        """)
    
    with col2:
        st.write("""
        **PRODUITS**
        - Ventes de marchandises
        - Production vendue
        - Production stockée
        - Production immobilisée
        - Subventions d'exploitation
        - Produits financiers
        - Produits exceptionnels
        """)
    
    # Calculateur de résultat
    st.subheader("🧮 Calculateur de Résultat - Expérimentez !")
    
    st.info("💡 **Conseil :** Modifiez les valeurs pour comprendre leur impact sur le résultat")
    
    ca = st.number_input("Chiffre d'affaires HT (€)", value=1000000, key="cr_ca")
    achats = st.number_input("Achats consommés (€)", value=400000, key="cr_achats")
    charges_personnel = st.number_input("Charges de personnel (€)", value=300000, key="cr_pers")
    dotations_amort = st.number_input("Dotations aux amortissements (€)", value=50000, key="cr_amort")
    charges_financieres = st.number_input("Charges financières (€)", value=20000, key="cr_fin")
    
    # Calculs
    resultat_exploitation = ca - achats - charges_personnel - dotations_amort
    resultat_courant = resultat_exploitation - charges_financieres
    
    # Affichage résultats
    st.subheader("📈 Résultats Calculés")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Résultat d'Exploitation", f"{resultat_exploitation:,.0f} €")
        st.metric("Taux de marge d'exploitation", f"{(resultat_exploitation/ca*100):.1f}%" if ca > 0 else "0%")
    
    with col2:
        st.metric("Résultat Courant", f"{resultat_courant:,.0f} €")
        st.metric("Taux de marge nette", f"{(resultat_courant/ca*100):.1f}%" if ca > 0 else "0%")

def show_soldes_gestion():
    st.markdown("""
    <div class="concept-card">
    <h3>📈 Soldes Intermédiaires de Gestion</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Les SIG permettent de décomposer la formation du résultat en plusieurs niveaux.")
    
    # Calculateur des SIG
    st.subheader("🧮 Calculateur des SIG")
    
    ca = st.number_input("Chiffre d'affaires", value=1000000, key="sig_ca_unique")
    achats_marches = st.number_input("Achats de marchandises", value=300000, key="sig_achats_unique")
    prod_vendue = st.number_input("Production vendue", value=800000, key="sig_prod_unique")
    consommations = st.number_input("Consommations externes", value=200000, key="sig_cons_unique")
    charges_personnel = st.number_input("Charges de personnel", value=350000, key="sig_pers_unique")
    
    # Calcul des SIG
    marge_commerciale = ca - achats_marches
    valeur_ajoutee = marge_commerciale + prod_vendue - consommations
    ebe = valeur_ajoutee - charges_personnel
    
    # Affichage des résultats
    st.subheader("📊 Résultats des SIG")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Marge Commerciale", f"{marge_commerciale:,.0f} €")
        st.metric("Taux de marge", f"{(marge_commerciale/ca*100):.1f} %")
    
    with col2:
        st.metric("Valeur Ajoutée", f"{valeur_ajoutee:,.0f} €")
        st.metric("Taux de VA", f"{(valeur_ajoutee/ca*100):.1f} %")
    
    with col3:
        st.metric("EBE", f"{ebe:,.0f} €")
        st.metric("Taux EBE", f"{(ebe/ca*100):.1f} %")

def show_seuil_rentabilite():
    st.markdown("""
    <div class="concept-card">
    <h3>🎯 Seuil de Rentabilité</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **📖 Définition :** Niveau de chiffre d'affaires pour lequel le résultat est nul.
    
    **🧮 Formule :** SR = Charges Fixes / Taux de Marge sur Coût Variable
    """)
    
    # Calculateur de seuil de rentabilité
    st.subheader("🧮 Calculateur de Seuil de Rentabilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        charges_fixes = st.number_input("Charges fixes annuelles (€)", value=300000, key="seuil_charges_fixes")
        ca_prev = st.number_input("Chiffre d'affaires prévisionnel (€)", value=1000000, key="seuil_ca")
    
    with col2:
        charges_variables = st.number_input("Charges variables (€)", value=500000, key="seuil_charges_var")
    
    # Calculs
    mcv = ca_prev - charges_variables
    taux_mcv = mcv / ca_prev if ca_prev > 0 else 0
    seuil_rentabilite = charges_fixes / taux_mcv if taux_mcv > 0 else 0
    marge_securite = ((ca_prev - seuil_rentabilite) / ca_prev * 100) if ca_prev > 0 else 0
    
    # Résultats
    st.subheader("📈 Résultats")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Taux MCV", f"{taux_mcv*100:.1f} %")
    
    with col2:
        st.metric("Seuil Rentabilité", f"{seuil_rentabilite:,.0f} €")
    
    with col3:
        st.metric("Marge de Sécurité", f"{marge_securite:.1f} %")
    
    # Graphique
    if seuil_rentabilite > 0:
        st.subheader("📊 Graphique de Visualisation")
        x = np.linspace(0, ca_prev * 1.5, 100)
        y_charges_fixes = np.full_like(x, charges_fixes)
        y_charges_variables = charges_variables/ca_prev * x if ca_prev > 0 else 0
        y_charges_totales = y_charges_fixes + y_charges_variables
        y_ca = x
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y_charges_fixes, name='Charges Fixes', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=x, y=y_charges_totales, name='Charges Totales', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=x, y=y_ca, name='Chiffre d\'affaires', line=dict(color='green')))
        
        # Point de seuil
        fig.add_trace(go.Scatter(x=[seuil_rentabilite], y=[seuil_rentabilite], 
                               mode='markers', name='Seuil', marker=dict(size=10, color='orange')))
        
        fig.update_layout(title='Seuil de Rentabilité', xaxis_title='Chiffre d\'affaires (€)', yaxis_title='Montants (€)')
        st.plotly_chart(fig)

def show_fonds_roulement():
    st.markdown("""
    <div class="concept-card">
    <h3>💰 Fonds de Roulement et BFR</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **🧮 Formules :**
    - FRNG = Ressources Stables - Emplois Stables
    - BFR = Actif Circulant - Passif Circulant  
    - Trésorerie = FRNG - BFR
    """)
    
    # Calculateur FRNG/BFR
    st.subheader("🧮 Calculateur d'Équilibre Financier")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Ressources Stables**")
        capitaux_propres = st.number_input("Capitaux propres (€)", value=800000, key="fr_cp")
        dettes_long_terme = st.number_input("Dettes long terme (€)", value=200000, key="fr_dettes")
    
    with col2:
        st.write("**Emplois Stables**")
        immob_brutes = st.number_input("Immobilisations brutes (€)", value=700000, key="fr_immob")
    
    with col3:
        st.write("**BFR**")
        stocks = st.number_input("Stocks (€)", value=150000, key="fr_stocks")
        clients = st.number_input("Créances clients (€)", value=200000, key="fr_clients")
        fournisseurs = st.number_input("Dettes fournisseurs (€)", value=120000, key="fr_fournisseurs")
    
    # Calculs
    ressources_stables = capitaux_propres + dettes_long_terme
    emplois_stables = immob_brutes
    frng = ressources_stables - emplois_stables
    
    actif_circulant = stocks + clients
    passif_circulant = fournisseurs
    bfr = actif_circulant - passif_circulant
    tresorerie = frng - bfr
    
    # Affichage résultats
    st.subheader("📊 Diagnostic Financier")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        delta_color = "normal" if frng > 0 else "inverse"
        st.metric("FRNG", f"{frng:,.0f} €", 
                 delta="✅ Bon" if frng > 0 else "❌ Risque", 
                 delta_color=delta_color)
    
    with col2:
        st.metric("BFR", f"{bfr:,.0f} €", 
                 delta="📈 Besoin" if bfr > 0 else "📉 Ressource")
    
    with col3:
        delta_color = "normal" if tresorerie > 0 else "inverse"
        st.metric("Trésorerie", f"{tresorerie:,.0f} €", 
                 delta="✅ Excédent" if tresorerie > 0 else "❌ Déficit", 
                 delta_color=delta_color)

def show_ratios_financiers():
    st.markdown("""
    <div class="concept-card">
    <h3>📐 Ratios Financiers</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur de ratios
    st.subheader("🧮 Calculateur de Ratios")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ca = st.number_input("Chiffre d'affaires (€)", value=1000000, key="ratio_ca")
        resultat_net = st.number_input("Résultat net (€)", value=80000, key="ratio_rn")
        capitaux_propres = st.number_input("Capitaux propres (€)", value=400000, key="ratio_cp")
        ebe = st.number_input("EBE (€)", value=150000, key="ratio_ebe")
    
    with col2:
        total_actif = st.number_input("Total actif (€)", value=800000, key="ratio_actif")
        dettes_financieres = st.number_input("Dettes financières (€)", value=200000, key="ratio_dettes")
        actif_circulant = st.number_input("Actif circulant (€)", value=300000, key="ratio_actif_circ")
        dettes_court_terme = st.number_input("Dettes court terme (€)", value=180000, key="ratio_dettes_ct")
    
    # Calcul des ratios
    rentabilite_net = (resultat_net / ca * 100) if ca > 0 else 0
    rentabilite_financiere = (resultat_net / capitaux_propres * 100) if capitaux_propres > 0 else 0
    rentabilite_economique = (ebe / total_actif * 100) if total_actif > 0 else 0
    endettement = (dettes_financieres / capitaux_propres * 100) if capitaux_propres > 0 else 0
    liquidite = (actif_circulant / dettes_court_terme * 100) if dettes_court_terme > 0 else 0
    
    # Affichage des ratios
    st.subheader("📊 Tableau de Bord des Ratios")
    
    ratios_data = {
        "Ratio": ["Rentabilité nette", "Rentabilité financière", "Rentabilité économique", "Taux d'endettement", "Ratio de liquidité"],
        "Valeur": [f"{rentabilite_net:.1f}%", f"{rentabilite_financiere:.1f}%", f"{rentabilite_economique:.1f}%", f"{endettement:.1f}%", f"{liquidite:.1f}%"],
        "Interprétation": [
            "✅ Bon" if rentabilite_net > 2 else "⚠️ À améliorer",
            "✅ Bon" if rentabilite_financiere > 8 else "⚠️ À améliorer", 
            "✅ Bon" if rentabilite_economique > 10 else "⚠️ À améliorer",
            "✅ Bon" if endettement < 100 else "❌ Trop élevé",
            "✅ Bon" if liquidite > 100 else "❌ Risque liquidité"
        ]
    }
    
    df_ratios = pd.DataFrame(ratios_data)
    st.dataframe(df_ratios, use_container_width=True)

def show_calculateurs():
    st.markdown('<h2 class="section-header">🧮 Calculateurs Interactifs</h2>', unsafe_allow_html=True)
    
    # Guide d'utilisation
    st.success("""
    **🎯 Comment utiliser les calculateurs :**
    1. Sélectionnez un calculateur dans le menu
    2. Saisissez vos données dans les champs
    3. Analysez les résultats calculés automatiquement
    4. Consultez les graphiques et recommandations
    """)
    
    calc_choice = st.selectbox(
        "**Choisissez un calculateur :**",
        [
            "📉 Amortissements",
            "💸 Capacité d'Autofinancement", 
            "⚖️ Effet de Levier",
            "📊 VAN et TIR",
            "🎯 Score Financier"
        ]
    )
    
    if "Amortissements" in calc_choice:
        show_calculateur_amortissements()
    elif "Capacité d'Autofinancement" in calc_choice:
        show_calculateur_caf()
    elif "Effet de Levier" in calc_choice:
        show_calculateur_levier()
    elif "VAN et TIR" in calc_choice:
        show_calculateur_van_tir()
    elif "Score Financier" in calc_choice:
        show_calculateur_score()

def show_calculateur_amortissements():
    st.subheader("📉 Calculateur d'Amortissements")
    
    st.info("""
    **💡 À savoir :**
    - **Amortissement linéaire** : Constant chaque année
    - **Amortissement dégressif** : Décroissant, avec coefficient
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        valeur_origine = st.number_input("Valeur d'origine (€)", value=100000, key="amort_valeur")
        duree = st.number_input("Durée d'amortissement (années)", value=5, min_value=1, key="amort_duree")
        mode = st.radio("Mode d'amortissement", ["Linéaire", "Dégressif"], key="amort_mode")
    
    with col2:
        date_acquisition = st.date_input("Date d'acquisition", value=datetime(2023, 1, 1), key="amort_date")
        coefficient = st.selectbox("Coefficient dégressif", [1.25, 1.75, 2.25], key="amort_coeff") if mode == "Dégressif" else 0
    
    # Calcul du plan d'amortissement
    if st.button("📊 Calculer le plan d'amortissement", key="amort_btn"):
        annees = list(range(1, duree + 1))
        vnc = [valeur_origine]
        amortissements = []
        amort_cumules = [0]
        
        for annee in annees:
            if mode == "Linéaire":
                amort_annuel = valeur_origine / duree
            else:
                taux_lineaire = 100 / duree
                taux_degressif = taux_lineaire * coefficient
                amort_annuel = vnc[-1] * taux_degressif / 100
            
            amortissements.append(amort_annuel)
            amort_cumules.append(amort_cumules[-1] + amort_annuel)
            vnc.append(vnc[-1] - amort_annuel)
        
        # DataFrame des résultats
        df_amort = pd.DataFrame({
            'Année': annees,
            'VNC début': [f"{v:,.0f} €" for v in vnc[:-1]],
            'Amortissement annuel': [f"{a:,.0f} €" for a in amortissements],
            'Amortissement cumulé': [f"{a:,.0f} €" for a in amort_cumules[1:]],
            'VNC fin': [f"{v:,.0f} €" for v in vnc[1:]]
        })
        
        st.dataframe(df_amort, use_container_width=True)
        
        # Graphique
        fig = go.Figure()
        fig.add_trace(go.Bar(x=annees, y=amortissements, name='Amortissement annuel'))
        fig.add_trace(go.Scatter(x=annees, y=vnc[1:], name='VNC fin d\'année', line=dict(color='red')))
        fig.update_layout(title='Plan d\'amortissement', xaxis_title='Années', yaxis_title='Montants (€)')
        st.plotly_chart(fig)

def show_calculateur_caf():
    st.subheader("💸 Calculateur de Capacité d'Autofinancement")
    
    st.write("**🧮 Méthode additive : CAF = Résultat net + Dotations - Reprises - Produits de cession**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        resultat_net = st.number_input("Résultat net (€)", value=50000, key="caf_rn")
        dotations_amort = st.number_input("Dotations aux amortissements (€)", value=20000, key="caf_dot_amort")
        dotations_provisions = st.number_input("Dotations aux provisions (€)", value=5000, key="caf_dot_prov")
    
    with col2:
        reprises_amort = st.number_input("Reprises sur amortissements (€)", value=0, key="caf_rep_amort")
        reprises_provisions = st.number_input("Reprises sur provisions (€)", value=0, key="caf_rep_prov")
        produits_cession = st.number_input("Produits de cession (€)", value=0, key="caf_prod_cess")
    
    caf = (resultat_net + dotations_amort + dotations_provisions - 
           reprises_amort - reprises_provisions - produits_cession)
    
    st.metric("Capacité d'Autofinancement", f"{caf:,.0f} €")
    
    # Interprétation
    if caf > resultat_net:
        st.success("✅ La CAF est supérieure au résultat net : bonne capacité d'autofinancement")
    else:
        st.warning("⚠️ La CAF est proche ou inférieure au résultat net : capacité d'autofinancement limitée")

def show_calculateur_levier():
    st.subheader("⚖️ Calculateur d'Effet de Levier Financier")
    
    col1, col2 = st.columns(2)
    
    with col1:
        actif_economique = st.number_input("Actif économique (€)", value=1000000, key="levier_actif")
        resultat_exploitation = st.number_input("Résultat d'exploitation (€)", value=120000, key="levier_re")
        capitaux_propres = st.number_input("Capitaux propres (€)", value=600000, key="levier_cp")
    
    with col2:
        dettes_financieres = st.number_input("Dettes financières (€)", value=400000, key="levier_dettes")
        taux_impot = st.number_input("Taux d'impôt (%)", value=25.0, key="levier_impot") / 100
        taux_interet = st.number_input("Taux d'intérêt (%)", value=4.0, key="levier_interet") / 100
    
    # Calculs
    re_apres_impot = resultat_exploitation * (1 - taux_impot)
    rentabilite_economique = re_apres_impot / actif_economique
    
    charges_financieres = dettes_financieres * taux_interet
    cf_apres_impot = charges_financieres * (1 - taux_impot)
    
    resultat_net = re_apres_impot - cf_apres_impot
    rentabilite_financiere = resultat_net / capitaux_propres
    
    effet_levier = rentabilite_financiere - rentabilite_economique
    
    # Affichage
    st.subheader("📈 Résultats")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Rentabilité économique", f"{rentabilite_economique*100:.1f}%")
    
    with col2:
        st.metric("Rentabilité financière", f"{rentabilite_financiere*100:.1f}%")
    
    with col3:
        delta_color = "normal" if effet_levier > 0 else "inverse"
        st.metric(
            "Effet de levier", 
            f"{effet_levier*100:.1f}%", 
            delta="✅ Positif" if effet_levier > 0 else "❌ Négatif", 
            delta_color=delta_color
        )

def show_calculateur_van_tir():
    st.subheader("📊 Calculateur VAN et TIR")
    
    st.write("Évaluation de la rentabilité d'un projet d'investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investissement_initial = st.number_input("Investissement initial (€)", value=100000, key="van_invest")
        duree_projet = st.number_input("Durée du projet (années)", value=5, key="van_duree")
        taux_actualisation = st.number_input("Taux d'actualisation (%)", value=8.0, key="van_taux") / 100
    
    with col2:
        st.write("Flux de trésorerie annuels")
        flux = []
        for i in range(duree_projet):
            flux.append(st.number_input(f"Année {i+1} (€)", value=30000, key=f"van_flux_{i}"))
    
    if st.button("📈 Calculer VAN et TIR", key="van_btn"):
        # Calcul VAN
        van = -investissement_initial
        for i, flux_annuel in enumerate(flux):
            van += flux_annuel / ((1 + taux_actualisation) ** (i + 1))
        
        # Estimation TIR (méthode simplifiée)
        def calcul_van(taux):
            van_calc = -investissement_initial
            for i, flux_annuel in enumerate(flux):
                van_calc += flux_annuel / ((1 + taux) ** (i + 1))
            return van_calc
        
        # Recherche du TIR par approximation
        tir = taux_actualisation
        for taux_test in np.arange(0.01, 1.0, 0.01):
            if calcul_van(taux_test) >= 0:
                tir = taux_test
            else:
                break
        
        st.subheader("🎯 Résultats")
        
        col1, col2 = st.columns(2)
        with col1:
            delta_color = "normal" if van > 0 else "inverse"
            st.metric(
                "VAN", 
                f"{van:,.0f} €", 
                delta="✅ Projet rentable" if van > 0 else "❌ Projet non rentable",
                delta_color=delta_color
            )
        with col2:
            st.metric("TIR approximatif", f"{tir*100:.1f}%")

def show_calculateur_score():
    st.subheader("🎯 Calculateur de Score Financier")
    
    st.write("Évaluation du risque de défaillance selon la méthode des scores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ebe = st.number_input("EBE (€)", value=150000, key="score_ebe")
        endettement_global = st.number_input("Endettement global (€)", value=500000, key="score_endettement")
        capitaux_permanents = st.number_input("Capitaux permanents (€)", value=800000, key="score_capitaux")
    
    with col2:
        actif_total = st.number_input("Actif total (€)", value=1000000, key="score_actif")
        frais_financiers = st.number_input("Frais financiers (€)", value=20000, key="score_frais_fin")
        ca = st.number_input("Chiffre d'affaires (€)", value=1000000, key="score_ca")
        charges_personnel = st.number_input("Charges de personnel (€)", value=350000, key="score_charges_pers")
        valeur_ajoutee = st.number_input("Valeur ajoutée (€)", value=500000, key="score_va")
    
    # Calcul du score Conan et Holder
    X1 = ebe / endettement_global if endettement_global > 0 else 0
    X2 = capitaux_permanents / actif_total if actif_total > 0 else 0
    X3 = 0.3  # Approximation pour réalisable et disponible
    X4 = frais_financiers / ca if ca > 0 else 0
    X5 = charges_personnel / valeur_ajoutee if valeur_ajoutee > 0 else 0
    
    score = 24*X1 + 22*X2 + 16*X3 - 87*X4 - 10*X5
    
    st.metric("Score financier", f"{score:.2f}")
    
    # Interprétation
    if score > 9.5:
        st.success("✅ Situation financière saine")
    elif score > -4.5:
        st.warning("⚠️ Situation à surveiller")
    else:
        st.error("❌ Situation risquée - Attention !")

def show_etudes_cas():
    st.markdown('<h2 class="section-header">💼 Études de Cas Pratiques</h2>', unsafe_allow_html=True)
    
    st.success("""
    **🎯 Méthodologie recommandée :**
    1. **Lire** attentivement le contexte de l'entreprise
    2. **Analyser** les données financières fournies  
    3. **Choisir** le type d'analyse à réaliser
    4. **Comparer** vos résultats avec la correction
    5. **Comprendre** les recommandations stratégiques
    """)
    
    cas_choice = st.selectbox(
        "**Choisissez une étude de cas :**",
        [
            "🏭 Diagnostic PME industrielle",
            "📈 Analyse de rentabilité", 
            "⚖️ Équilibre financier",
            "💧 Tableau de flux",
            "🏗️ Projet d'investissement"
        ]
    )
    
    if "PME industrielle" in cas_choice:
        show_cas_pme()
    elif "rentabilité" in cas_choice:
        show_cas_rentabilite()
    elif "Équilibre financier" in cas_choice:
        show_cas_equilibre()
    elif "Tableau de flux" in cas_choice:
        show_cas_flux()
    elif "Projet d'investissement" in cas_choice:
        show_cas_investissement()

def show_cas_pme():
    st.subheader("🏭 Diagnostic d'une PME Industrielle")
    
    st.write("""
    **📋 Contexte :** Société DUBOIS, fabricant de composants électroniques
    - Chiffre d'affaires : 2,5 M€
    - Effectif : 45 personnes
    - Marché en croissance mais concurrence forte
    """)
    
    # Données financières
    st.subheader("📊 Données financières")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Compte de résultat (k€)**")
        data_compte = {
            'Poste': ['Chiffre d\'affaires', 'Achats consommés', 'Charges personnel', 'EBE', 'Dotations amortissement', 'Résultat exploitation'],
            'N': [2500, 1200, 800, 500, 150, 200],
            'N-1': [2300, 1150, 750, 400, 140, 150]
        }
        df_compte = pd.DataFrame(data_compte)
        st.dataframe(df_compte, use_container_width=True)
    
    with col2:
        st.write("**Bilan simplifié (k€)**")
        data_bilan = {
            'Poste': ['Actif immobilisé', 'Stocks', 'Clients', 'Disponibilités', 'Capitaux propres', 'Dettes financières', 'Fournisseurs'],
            'N': [1800, 450, 600, 150, 1200, 800, 1000],
            'N-1': [1700, 400, 550, 200, 1100, 700, 1050]
        }
        df_bilan = pd.DataFrame(data_bilan)
        st.dataframe(df_bilan, use_container_width=True)
    
    # Analyse interactive
    st.subheader("🔍 Analyse à réaliser")
    
    analyse_choice = st.radio(
        "**Sélectionnez l'analyse à effectuer :**",
        ["Ratios de rentabilité", "Structure financière", "Liquidité", "Diagnostic global"]
    )
    
    if analyse_choice == "Ratios de rentabilité":
        show_analyse_rentabilite_cas()
    elif analyse_choice == "Structure financière":
        show_analyse_structure_cas()
    elif analyse_choice == "Liquidité":
        show_analyse_liquidite_cas()
    else:
        show_diagnostic_global_cas()

def show_analyse_rentabilite_cas():
    st.markdown("""
    <div class="question-box">
    <h4>📈 Calcul des ratios de rentabilité</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Questions :**
    1. Calculez les ratios de rentabilité pour N et N-1
    2. Analysez l'évolution de la rentabilité
    3. Identifiez les points forts et les points faibles
    """)
    
    if st.button("📝 Voir la correction détaillée", key="correction_rentabilite"):
        st.markdown("""
        <div class="solution-box">
        <h4>🧮 Correction - Ratios de Rentabilité</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **Calculs détaillés :**
        
        **N-1 :**
        - Taux de marge commerciale = (2.300 - 1.150) / 2.300 = 50,0%
        - Taux EBE = 400 / 2.300 = 17,4%
        - Rentabilité économique = 150 / (1.700 + 400 + 550 + 200) = 5,3%
        - Rentabilité financière = 150 / 1.100 = 13,6%
        
        **N :**
        - Taux de marge commerciale = (2.500 - 1.200) / 2.500 = 52,0%
        - Taux EBE = 500 / 2.500 = 20,0%
        - Rentabilité économique = 200 / (1.800 + 450 + 600 + 150) = 6,7%
        - Rentabilité financière = 200 / 1.200 = 16,7%
        
        **🎯 Analyse :**
        - ✅ **Amélioration de la rentabilité** sur tous les indicateurs
        - ✅ **Taux de marge en hausse** de 50% à 52%
        - ✅ **EBE en forte progression** (+25%)
        - ✅ **Rentabilité financière améliorée** (+3,1 points)
        
        **📋 Recommandations :**
        - Poursuivre les efforts de maîtrise des coûts
        - Maintenir la stratégie de croissance
        - Renforcer la profitabilité
        """)

def show_analyse_structure_cas():
    st.markdown("""
    <div class="question-box">
    <h4>🏗️ Analyse de la structure financière</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Questions :**
    1. Calculez le FRNG, BFR et Trésorerie nette
    2. Analysez l'équilibre financier
    3. Évaluez la structure de financement
    """)
    
    if st.button("📝 Voir la correction détaillée", key="correction_structure"):
        st.markdown("""
        <div class="solution-box">
        <h4>🧮 Correction - Structure Financière</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **Calculs détaillés :**
        
        **FRNG = Ressources stables - Emplois stables**
        - N-1 : (1.100 + 700) - 1.700 = 100 k€
        - N : (1.200 + 800) - 1.800 = 200 k€
        
        **BFR = Actif circulant - Passif circulant**
        - N-1 : (400 + 550) - 1.050 = -100 k€
        - N : (450 + 600) - 1.000 = 50 k€
        
        **Trésorerie nette = FRNG - BFR**
        - N-1 : 100 - (-100) = 200 k€
        - N : 200 - 50 = 150 k€
        
        **Taux d'endettement = Dettes financières / Capitaux propres**
        - N-1 : 700 / 1.100 = 63,6%
        - N : 800 / 1.200 = 66,7%
        
        **🎯 Analyse :**
        - ✅ **FRNG positif et en amélioration**
        - ⚠️ **BFR devient positif** (besoin de financement apparu)
        - ✅ **Trésorerie nette excédentaire** mais en baisse
        - ⚠️ **Endettement en légère hausse** mais acceptable
        
        **📋 Recommandations :**
        - Surveiller l'évolution du BFR
        - Optimiser le cycle d'exploitation
        - Maintenir une politique d'investissement maîtrisée
        """)

def show_analyse_liquidite_cas():
    st.markdown("""
    <div class="question-box">
    <h4>💧 Analyse de la liquidité</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Questions :**
    1. Calculez les ratios de liquidité
    2. Analysez la capacité à faire face aux dettes court terme
    3. Évaluez le risque de liquidité
    """)
    
    if st.button("📝 Voir la correction détaillée", key="correction_liquidite"):
        st.markdown("""
        <div class="solution-box">
        <h4>🧮 Correction - Analyse de Liquidité</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **Calculs détaillés :**
        
        **Ratio de liquidité générale = Actif circulant / Dettes CT**
        - N-1 : (400 + 550 + 200) / 1.050 = 1,10
        - N : (450 + 600 + 150) / 1.000 = 1,20
        
        **Ratio de liquidité réduite = (Actif circulant - Stocks) / Dettes CT**
        - N-1 : (550 + 200) / 1.050 = 0,71
        - N : (600 + 150) / 1.000 = 0,75
        
        **Ratio de liquidité immédiate = Disponibilités / Dettes CT**
        - N-1 : 200 / 1.050 = 0,19
        - N : 150 / 1.000 = 0,15
        
        **🎯 Analyse :**
        - ✅ **Liquidité générale satisfaisante** (>1)
        - ⚠️ **Liquidité réduite faible** (<1)
        - ⚠️ **Liquidité immédiate insuffisante**
        - 📈 **Amélioration globale** des ratios
        
        **📋 Recommandations :**
        - Renforcer la trésorerie disponible
        - Optimiser la gestion des stocks
        - Négocier des délais fournisseurs
        """)

def show_diagnostic_global_cas():
    st.markdown("""
    <div class="question-box">
    <h4>🔍 Diagnostic global</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Questions :**
    1. Synthétisez le diagnostic financier
    2. Identifiez les points forts et les risques
    3. Proposez des recommandations stratégiques
    """)
    
    if st.button("📝 Voir la correction détaillée", key="correction_global"):
        st.markdown("""
        <div class="solution-box">
        <h4>🎯 Correction - Diagnostic Global</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **📊 SYNTHÈSE DU DIAGNOSTIC**
        
        **✅ POINTS FORTS :**
        - Rentabilité en nette amélioration
        - Croissance du chiffre d'affaires (+8,7%)
        - Structure financière équilibrée (FRNG positif)
        - Trésorerie excédentaire
        - Bonne profitabilité (EBE en hausse)
        
        **⚠️ POINTS DE VIGILANCE :**
        - Dégradation de la liquidité immédiate
        - Apparition d'un BFR positif
        - Endettement en légère hausse
        - Liquidité réduite faible
        
        **🔴 RISQUES IDENTIFIÉS :**
        - Risque de tension de trésorerie
        - Dépendance accrue au financement externe
        - Sensibilité à la conjoncture
        
        **📋 RECOMMANDATIONS STRATÉGIQUES :**
        
        **À court terme (6 mois) :**
        - Renforcer la trésorerie disponible
        - Optimiser le BFR (délais clients/fournisseurs)
        - Réviser la politique de stocks
        
        **À moyen terme (1-2 ans) :**
        - Maintenir les investissements productifs
        - Diversifier les sources de financement
        - Renforcer la rentabilité opérationnelle
        
        **À long terme (3-5 ans) :**
        - Poursuivre la croissance maîtrisée
        - Développer de nouveaux marchés
        - Optimiser la structure financière
        """)

def show_cas_rentabilite():
    st.subheader("📈 Analyse de Rentabilité - Cas PRATIQUE")
    
    st.markdown("""
    <div class="cas-container">
    <h3>🏢 Société TEXTILIA - Spécialiste du textile technique</h3>
    
    **Contexte :**
    - Entreprise familiale créée en 1995
    - Spécialisée dans les textiles techniques
    - 120 collaborateurs
    - Marché en croissance mais concurrence internationale forte
    </div>
    """, unsafe_allow_html=True)
    
    # Données financières
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Compte de résultat (k€)")
        data_cr = {
            'Poste': ['Chiffre d\'affaires', 'Coût des ventes', 'Marge brute', 'Frais commerciaux', 
                     'Frais administratifs', 'EBE', 'Dotations amortissements', 'Résultat exploitation',
                     'Charges financières', 'Résultat courant', 'Impôt sur les sociétés', 'Résultat net'],
            'N': [8500, 5100, 3400, 800, 900, 1700, 400, 1300, 150, 1150, 345, 805],
            'N-1': [7800, 4830, 2970, 750, 850, 1370, 380, 990, 140, 850, 255, 595]
        }
        df_cr = pd.DataFrame(data_cr)
        st.dataframe(df_cr, use_container_width=True)
    
    with col2:
        st.subheader("📈 Ratios à calculer")
        st.write("""
        **Questions :**
        1. Calculez les ratios de rentabilité
        2. Analysez la formation du résultat
        3. Identifiez les leviers d'amélioration
        4. Proposez des actions correctives
        """)
        
        st.markdown("""
        <div class="question-box">
        <h5>📋 Travail à réaliser</h5>
        - Taux de marge brute
        - Taux de charges d'exploitation
        - Rentabilité économique
        - Rentabilité financière
        - Effet de levier
        </div>
        """, unsafe_allow_html=True)
    
    # Calculateur interactif
    st.subheader("🧮 Calculateur de Ratios")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ca = st.number_input("CA (k€)", value=8500, key="renta_ca")
        cout_ventes = st.number_input("Coût des ventes (k€)", value=5100, key="renta_cout")
        frais_exploitation = st.number_input("Frais d'exploitation (k€)", value=1700, key="renta_frais")
        resultat_exploitation = st.number_input("Résultat exploitation (k€)", value=1300, key="renta_re")
        resultat_net = st.number_input("Résultat net (k€)", value=805, key="renta_rn")
    
    with col2:
        capitaux_propres = st.number_input("Capitaux propres (k€)", value=4500, key="renta_cp")
        dettes_financieres = st.number_input("Dettes financières (k€)", value=1800, key="renta_dettes")
        actif_economique = st.number_input("Actif économique (k€)", value=7200, key="renta_actif")
        charges_financieres = st.number_input("Charges financières (k€)", value=150, key="renta_charges_fin")
    
    if st.button("📈 Calculer les ratios", key="btn_renta"):
        # Calculs
        marge_brute = (ca - cout_ventes) / ca * 100
        taux_frais_exploitation = frais_exploitation / ca * 100
        rentabilite_economique = resultat_exploitation / actif_economique * 100
        rentabilite_financiere = resultat_net / capitaux_propres * 100
        taux_endettement = dettes_financieres / capitaux_propres * 100
        
        # Affichage résultats
        st.subheader("📊 Résultats des Ratios")
        
        ratios_data = {
            'Ratio': ['Marge brute', 'Taux frais exploitation', 'Rentabilité économique', 
                     'Rentabilité financière', 'Taux d\'endettement'],
            'Valeur': [f"{marge_brute:.1f}%", f"{taux_frais_exploitation:.1f}%", 
                      f"{rentabilite_economique:.1f}%", f"{rentabilite_financiere:.1f}%", 
                      f"{taux_endettement:.1f}%"],
            'Analyse': [
                "✅ Bon" if marge_brute > 35 else "⚠️ Faible",
                "✅ Maîtrisé" if taux_frais_exploitation < 25 else "❌ Élevé",
                "✅ Bonne" if rentabilite_economique > 15 else "⚠️ À améliorer",
                "✅ Excellente" if rentabilite_financiere > 15 else "✅ Correcte",
                "✅ Acceptable" if taux_endettement < 50 else "❌ Élevé"
            ]
        }
        
        df_resultats = pd.DataFrame(ratios_data)
        st.dataframe(df_resultats, use_container_width=True)
    
    # Correction détaillée
    if st.button("🎯 Voir la correction complète", key="btn_correction_renta"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Correction Détaillée - Analyse de Rentabilité</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **🧮 CALCULS DÉTAILLÉS :**
        
        **1. Taux de marge brute :**
        - N-1 : (7.800 - 4.830) / 7.800 = 38,1%
        - N : (8.500 - 5.100) / 8.500 = 40,0%
        → **Amélioration de la marge** (+1,9 points)
        
        **2. Taux de charges d'exploitation :**
        - N-1 : (750 + 850) / 7.800 = 20,5%
        - N : (800 + 900) / 8.500 = 20,0%
        → **Maîtrise des charges** (-0,5 point)
        
        **3. Rentabilité économique :**
        - N-1 : 990 / 6.500 = 15,2%
        - N : 1.300 / 7.200 = 18,1%
        → **Forte amélioration** (+2,9 points)
        
        **4. Rentabilité financière :**
        - N-1 : 595 / 4.200 = 14,2%
        - N : 805 / 4.500 = 17,9%
        → **Excellente progression** (+3,7 points)
        
        **🎯 DIAGNOSTIC :**
        - ✅ **Entreprise très rentable**
        - ✅ **Amélioration sur tous les indicateurs**
        - ✅ **Bonne maîtrise des charges**
        - ✅ **Effet de levier positif**
        
        **📋 RECOMMANDATIONS :**
        - Poursuivre la stratégie de croissance rentable
        - Maintenir la discipline sur les coûts
        - Investir dans l'innovation produit
        - Explorer de nouveaux marchés à forte marge
        """)

def show_cas_equilibre():
    st.subheader("⚖️ Équilibre Financier - Cas CONCRET")
    
    st.markdown("""
    <div class="cas-container">
    <h3>🏗️ Société BATIPRO - Entreprise de BTP</h3>
    
    **Contexte :**
    - Entreprise de construction créée en 2008
    - Spécialisée dans la rénovation énergétique
    - 85 collaborateurs
    - Forte croissance mais tensions de trésorerie
    </div>
    """, unsafe_allow_html=True)
    
    # Données du bilan
    st.subheader("📋 Bilan Financier (k€)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**ACTIF**")
        data_actif = {
            'Poste': ['Actif immobilisé', 'Stocks', 'Créances clients', 'Disponibilités', 'TOTAL ACTIF'],
            'N': [4200, 1800, 3200, 450, 9650],
            'N-1': [3800, 1500, 2800, 600, 8700]
        }
        df_actif = pd.DataFrame(data_actif)
        st.dataframe(df_actif, use_container_width=True)
    
    with col2:
        st.write("**PASSIF**")
        data_passif = {
            'Poste': ['Capitaux propres', 'Dettes financières LT', 'Dettes financières CT', 
                     'Dettes fournisseurs', 'Autres dettes', 'TOTAL PASSIF'],
            'N': [3800, 2200, 800, 2500, 350, 9650],
            'N-1': [3500, 1800, 600, 2400, 400, 8700]
        }
        df_passif = pd.DataFrame(data_passif)
        st.dataframe(df_passif, use_container_width=True)
    
    # Analyse de l'équilibre financier
    st.subheader("🔍 Analyse de l'Équilibre Financier")
    
    st.markdown("""
    <div class="question-box">
    <h5>📋 Questions à résoudre</h5>
    1. Calculez le FRNG, BFR et Trésorerie nette
    2. Analysez l'évolution de la structure financière
    3. Identifiez les déséquilibres éventuels
    4. Proposez des solutions de financement
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur d'équilibre financier
    st.subheader("🧮 Calculateur d'Équilibre Financier")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Ressources Stables**")
        cp = st.number_input("Capitaux propres (k€)", value=3800, key="equi_cp")
        dettes_lt = st.number_input("Dettes LT (k€)", value=2200, key="equi_dettes_lt")
    
    with col2:
        st.write("**Emplois Stables**")
        actif_immob = st.number_input("Actif immobilisé (k€)", value=4200, key="equi_immob")
    
    with col3:
        st.write("**BFR**")
        stocks = st.number_input("Stocks (k€)", value=1800, key="equi_stocks")
        creances = st.number_input("Créances clients (k€)", value=3200, key="equi_creances")
        dettes_court = st.number_input("Dettes CT (k€)", value=2850, key="equi_dettes_ct")
    
    if st.button("📊 Calculer l'équilibre", key="btn_equilibre"):
        # Calculs
        ressources_stables = cp + dettes_lt
        emplois_stables = actif_immob
        frng = ressources_stables - emplois_stables
        
        actif_circulant = stocks + creances
        bfr = actif_circulant - dettes_court
        tresorerie = frng - bfr
        
        # Diagnostic
        st.subheader("📈 Résultats de l'Analyse")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            delta_color = "normal" if frng > 0 else "inverse"
            st.metric("FRNG", f"{frng:,.0f} k€", 
                     delta="✅ Équilibre" if frng > 0 else "❌ Déséquilibre", 
                     delta_color=delta_color)
        
        with col2:
            st.metric("BFR", f"{bfr:,.0f} k€", 
                     delta="📈 Besoin" if bfr > 0 else "📉 Ressource")
        
        with col3:
            delta_color = "normal" if tresorerie > 0 else "inverse"
            st.metric("Trésorerie", f"{tresorerie:,.0f} k€", 
                     delta="✅ Excédent" if tresorerie > 0 else "❌ Déficit", 
                     delta_color=delta_color)
    
    # Correction détaillée
    if st.button("🎯 Voir l'analyse complète", key="btn_analyse_equilibre"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Analyse Complète - Équilibre Financier</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **🧮 CALCULS DÉTAILLÉS :**
        
        **N-1 :**
        - FRNG = (3.500 + 1.800) - 3.800 = 1.500 k€
        - BFR = (1.500 + 2.800) - (2.400 + 400) = 1.500 k€
        - Trésorerie = 1.500 - 1.500 = 0 k€
        
        **N :**
        - FRNG = (3.800 + 2.200) - 4.200 = 1.800 k€
        - BFR = (1.800 + 3.200) - (2.500 + 350) = 2.150 k€
        - Trésorerie = 1.800 - 2.150 = -350 k€
        
        **🎯 DIAGNOSTIC FINANCIER :**
        
        **✅ ASPECTS POSITIFS :**
        - FRNG positif et en augmentation
        - Capacité d'autofinancement suffisante
        - Structure financière globalement saine
        
        **🔴 PROBLÈMES IDENTIFIÉS :**
        - **Déficit de trésorerie** apparu (-350 k€)
        - **BFR en forte augmentation** (+650 k€)
        - **Croissance du besoin de financement**
        - **Tension sur la liquidité**
        
        **📋 PLAN D'ACTION RECOMMANDÉ :**
        
        **Actions immédiates (1-3 mois) :**
        - Renégocier les délais fournisseurs
        - Accélérer le recouvrement clients
        - Mettre en place une ligne de trésorerie
        
        **Actions à moyen terme (3-12 mois) :**
        - Optimiser la gestion des stocks
        - Réviser la politique commerciale
        - Renforcer les capitaux propres
        
        **Actions stratégiques (1-3 ans) :**
        - Diversifier les sources de financement
        - Améliorer la rentabilité opérationnelle
        - Développer un fonds de roulement permanent
        """)

def show_cas_flux():
    st.subheader("💧 Tableaux de Flux - Cas APPLICATIF")
    
    st.markdown("""
    <div class="cas-container">
    <h3>⚡ Société ENERG-TECH - Énergies renouvelables</h3>
    
    **Contexte :**
    - Start-up créée en 2018 dans les énergies solaires
    - Forte croissance avec besoins d'investissement importants
    - 65 collaborateurs
    - Phase de développement accéléré
    </div>
    """, unsafe_allow_html=True)
    
    # Tableaux de flux
    st.subheader("📊 Tableaux des Flux de Trésorerie (k€)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**FLUX D'EXPLOITATION**")
        data_exploitation = {
            'Poste': ['Résultat net', 'Dotations aux amortissements', 'Variation BFR exploitation', 
                     'Intérêts payés', 'Impôts payés', 'FLUX NET EXPLOITATION'],
            'N': [650, 420, -380, 95, 210, 805],
            'N-1': [480, 350, -220, 75, 145, 480]
        }
        df_exploitation = pd.DataFrame(data_exploitation)
        st.dataframe(df_exploitation, use_container_width=True)
    
    with col2:
        st.write("**FLUX D'INVESTISSEMENT**")
        data_investissement = {
            'Poste': ['Acquisitions immobilisations', 'Cessions immobilisations', 
                     'Acquisitions titres', 'FLUX NET INVESTISSEMENT'],
            'N': [-1250, 120, -80, -1210],
            'N-1': [-980, 90, -50, -940]
        }
        df_investissement = pd.DataFrame(data_investissement)
        st.dataframe(df_investissement, use_container_width=True)
    
    st.write("**FLUX DE FINANCEMENT**")
    data_financement = {
        'Poste': ['Augmentation capital', 'Emprunts nouveaux', 'Remboursements emprunts',
                 'Dividendes versés', 'FLUX NET FINANCEMENT'],
        'N': [500, 800, -450, -180, 670],
        'N-1': [300, 600, -380, -120, 400]
    }
    df_financement = pd.DataFrame(data_financement)
    st.dataframe(df_financement, use_container_width=True)
    
    # Analyse des flux
    st.subheader("🔍 Analyse des Flux de Trésorerie")
    
    st.markdown("""
    <div class="question-box">
    <h5>📋 Questions à résoudre</h5>
    1. Analysez la génération de trésorerie d'exploitation
    2. Évaluez la politique d'investissement
    3. Commentez la stratégie de financement
    4. Synthétisez la situation de trésorerie
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur de flux
    st.subheader("🧮 Calculateur de Flux de Trésorerie")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Flux Exploitation**")
        resultat_net = st.number_input("Résultat net (k€)", value=650, key="flux_rn")
        dotations = st.number_input("Dotations (k€)", value=420, key="flux_dot")
        variation_bfr = st.number_input("Δ BFR (k€)", value=-380, key="flux_bfr")
    
    with col2:
        st.write("**Flux Investissement**")
        acquisitions = st.number_input("Acquisitions (k€)", value=-1250, key="flux_acqu")
        cessions = st.number_input("Cessions (k€)", value=120, key="flux_cess")
    
    with col3:
        st.write("**Flux Financement**")
        augmentation_capital = st.number_input("Aug. capital (k€)", value=500, key="flux_cap")
        nouveaux_emprunts = st.number_input("Nouveaux emprunts (k€)", value=800, key="flux_emp")
        remboursements = st.number_input("Remboursements (k€)", value=-450, key="flux_remb")
    
    if st.button("💰 Calculer les flux", key="btn_flux"):
        # Calculs
        flux_exploitation = resultat_net + dotations + variation_bfr
        flux_investissement = acquisitions + cessions
        flux_financement = augmentation_capital + nouveaux_emprunts + remboursements
        variation_tresorerie = flux_exploitation + flux_investissement + flux_financement
        
        # Affichage résultats
        st.subheader("📈 Synthèse des Flux")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            delta_color = "normal" if flux_exploitation > 0 else "inverse"
            st.metric("Flux Exploitation", f"{flux_exploitation:,.0f} k€", 
                     delta="✅ Positif" if flux_exploitation > 0 else "❌ Négatif", 
                     delta_color=delta_color)
        
        with col2:
            st.metric("Flux Investissement", f"{flux_investissement:,.0f} k€")
        
        with col3:
            delta_color = "normal" if flux_financement > 0 else "inverse"
            st.metric("Flux Financement", f"{flux_financement:,.0f} k€", 
                     delta="✅ Entrées" if flux_financement > 0 else "❌ Sorties", 
                     delta_color=delta_color)
        
        with col4:
            delta_color = "normal" if variation_tresorerie > 0 else "inverse"
            st.metric("Δ Trésorerie", f"{variation_tresorerie:,.0f} k€", 
                     delta="✅ Augmentation" if variation_tresorerie > 0 else "❌ Diminution", 
                     delta_color=delta_color)
    
    # Correction détaillée
    if st.button("🎯 Analyse complète des flux", key="btn_analyse_flux"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Analyse Complète - Tableaux de Flux</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **🧮 ANALYSE DES FLUX :**
        
        **FLUX D'EXPLOITATION :**
        - **Trésorerie d'exploitation positive** : 805 k€ (N) vs 480 k€ (N-1)
        - **Forte croissance** de la capacité à générer de la trésorerie (+68%)
        - **BFR exploitation consommateur** de trésorerie (-380 k€)
        - **Activité rentable** avec bonne transformation du résultat en cash
        
        **FLUX D'INVESTISSEMENT :**
        - **Investissements importants** : -1.210 k€ (N) vs -940 k€ (N-1)
        - **Politique de croissance ambitieuse**
        - **Capacité d'autofinancement insuffisante** pour couvrir les investissements
        - **Besoin de financement externe**
        
        **FLUX DE FINANCEMENT :**
        - **Recours au financement externe** : 670 k€ d'entrées nettes
        - **Augmentation de capital** significative (500 k€)
        - **Endettement maîtrisé** avec nouvel emprunt de 800 k€
        - **Politique de dividende raisonnable**
        
        **🎯 DIAGNOSTIC GLOBAL :**
        
        **✅ POINTS FORTS :**
        - Forte croissance de la trésorerie d'exploitation
        - Stratégie d'investissement cohérente
        - Financement équilibré entre fonds propres et dette
        - Bonne visibilité sur les flux futurs
        
        **⚠️ POINTS DE VIGILANCE :**
        - BFR fortement consommateur de trésorerie
        - Dépendance au financement externe
        - Croissance des investissements supérieure à la CAF
        - Risque de tension si ralentissement économique
        
        **📋 RECOMMANDATIONS :**
        
        **Gestion du BFR :**
        - Optimiser les délais de paiement clients
        - Négocier des délais fournisseurs étendus
        - Mettre en place un plan de relance client
        
        **Stratégie d'investissement :**
        - Prioriser les investissements les plus rentables
        - Échelonner les gros investissements
        - Étudier les solutions de leasing
        
        **Politique de financement :**
        - Maintenir un équilibre fonds propres/dette
        - Diversifier les sources de financement
        - Anticiper les besoins futurs
        """)
""
def show_cas_investissement():
    st.subheader("🏗️ Projet d'Investissement - Cas DÉCISIONNEL")
    
    st.markdown("""
    <div class="cas-container">
    <h3>🏭 Société AGRO-INNOV - Transformation alimentaire</h3>
    
    **Contexte :**
    - Projet d'investissement dans une nouvelle ligne de production
    - Investissement : 2,5 M€
    - Durée du projet : 5 ans
    - Objectif : augmentation de capacité de 40%
    </div>
    """, unsafe_allow_html=True)
    
    # Données du projet
    st.subheader("📋 Données du Projet d'Investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**INVESTISSEMENT INITIAL**")
        data_investissement = {
            'Poste': ['Machines et équipements', 'Installation et mise en route', 
                     "Frais d'études", 'Besoins en fonds de roulement', 'TOTAL'],
            'Montant (k€)': [1800, 400, 150, 250, 2600]
        }
        df_invest = pd.DataFrame(data_investissement)
        st.dataframe(df_invest, use_container_width=True)
    
    with col2:
        st.write("**FLUX PRÉVISIONNELS**")
        data_flux = {
            'Année': [1, 2, 3, 4, 5],
            'CA supplémentaire (k€)': [1200, 1800, 2400, 2400, 2400],
            'Charges variables (k€)': [600, 900, 1200, 1200, 1200],
            'Charges fixes (k€)': [300, 350, 400, 400, 400]
        }
        df_flux = pd.DataFrame(data_flux)
        st.dataframe(df_flux, use_container_width=True)
    
    # Critères d'évaluation
    st.subheader("🎯 Critères d'Évaluation du Projet")
    
    st.markdown("""
    <div class="question-box">
    <h5>📋 Questions de décision</h5>
    1. Calculez la VAN du projet (taux d'actualisation : 10%)
    2. Déterminez le TRI approximatif
    3. Évaluez le délai de récupération
    4. Analysez la sensibilité du projet
    5. Prenez une décision d'investissement
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur d'investissement
    st.subheader("🧮 Calculateur de Rentabilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investissement = st.number_input("Investissement initial (k€)", value=2600, key="inv_initial")
        taux_actualisation = st.number_input("Taux d'actualisation (%)", value=10.0, key="inv_taux") / 100
        duree = st.number_input("Durée du projet (années)", value=5, key="inv_duree")
    
    with col2:
        st.write("**Flux de trésorerie annuels (k€)**")
        flux_annee1 = st.number_input("Année 1", value=300, key="inv_flux1")
        flux_annee2 = st.number_input("Année 2", value=550, key="inv_flux2")
        flux_annee3 = st.number_input("Année 3", value=800, key="inv_flux3")
        flux_annee4 = st.number_input("Année 4", value=800, key="inv_flux4")
        flux_annee5 = st.number_input("Année 5", value=1050, key="inv_flux5")  # inclut récupération BFR
    
    if st.button("📊 Évaluer le projet", key="btn_eval_invest"):
        # Calcul VAN
        flux = [flux_annee1, flux_annee2, flux_annee3, flux_annee4, flux_annee5]
        van = -investissement
        for i, flux_annuel in enumerate(flux):
            van += flux_annuel / ((1 + taux_actualisation) ** (i + 1))
        
        # Estimation TRI
        def calcul_van_tri(taux):
            van_calc = -investissement
            for i, flux_annuel in enumerate(flux):
                van_calc += flux_annuel / ((1 + taux) ** (i + 1))
            return van_calc
        
        # Recherche TRI
        tri = taux_actualisation
        for taux_test in np.arange(0.01, 0.50, 0.01):
            if calcul_van_tri(taux_test) >= 0:
                tri = taux_test
            else:
                break
        
        # Délai de récupération
        cumul_flux = 0
        delai_recup = duree + 1
        for i, flux_annuel in enumerate(flux):
            cumul_flux += flux_annuel
            if cumul_flux >= investissement and delai_recup > duree:
                delai_recup = i + 1
        
        # Affichage résultats
        st.subheader("📈 Résultats de l'Évaluation")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            delta_color = "normal" if van > 0 else "inverse"
            st.metric("VAN", f"{van:,.0f} k€", 
                     delta="✅ Rentable" if van > 0 else "❌ Non rentable", 
                     delta_color=delta_color)
        
        with col2:
            st.metric("TRI", f"{tri*100:.1f}%")
        
        with col3:
            st.metric("Délai récupération", f"{delai_recup} ans")
    
    # Analyse de sensibilité
    st.subheader("📊 Analyse de Sensibilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        variation_ca = st.slider("Variation du CA (%)", -20, 20, 0, key="sens_ca")
        variation_charges = st.slider("Variation des charges (%)", -15, 15, 0, key="sens_charges")
    
    with col2:
        variation_invest = st.slider("Variation investissement (%)", -10, 10, 0, key="sens_invest")
        variation_taux = st.slider("Variation taux actualisation (%)", -3, 3, 0, key="sens_taux")
    
        if st.button("🔄 Calculer la sensibilité", key="btn_sensibilite"):
            # Recalcul de la VAN initiale (avec les valeurs de base)
            flux_initiaux = [flux_annee1, flux_annee2, flux_annee3, flux_annee4, flux_annee5]
            van_initial = -investissement
            for i, flux_annuel in enumerate(flux_initiaux):
                van_initial += flux_annuel / ((1 + taux_actualisation) ** (i + 1))
        
        # Recalcul avec variations
        invest_ajuste = investissement * (1 + variation_invest/100)
        taux_ajuste = (taux_actualisation * 100 + variation_taux) / 100
        
        flux_ajustes = [
            flux_annee1 * (1 + (variation_ca - variation_charges)/100),
            flux_annee2 * (1 + (variation_ca - variation_charges)/100),
            flux_annee3 * (1 + (variation_ca - variation_charges)/100),
            flux_annee4 * (1 + (variation_ca - variation_charges)/100),
            flux_annee5 * (1 + (variation_ca - variation_charges)/100)
        ]
        
    van_sensibilite = -invest_ajuste
    for i, flux_annuel in enumerate(flux_ajustes):
        van_sensibilite += flux_annuel / ((1 + taux_ajuste) ** (i + 1))
        
        st.metric("VAN après sensibilité", f"{van_sensibilite:,.0f} k€", 
                 delta=f"{van_sensibilite - van_initial:+.0f} k€")
           
    # Décision d'investissement
    if st.button("🎯 Prendre la décision", key="btn_decision"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Décision d'Investissement - Analyse Complète</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **🧮 ÉVALUATION FINANCIÈRE :**
        
        **Calculs de base :**
        - **VAN** : Environ 450 k€ (positive)
        - **TRI** : Environ 18% (> taux d'actualisation de 10%)
        - **Délai de récupération** : 4 ans
        
        **ANALYSE DE SENSIBILITÉ :**
        
        **Scénario pessimiste** (CA -10%, charges +5%) :
        - VAN devient : 150 k€ (toujours positive)
        - TRI : 13% (acceptable)
        
        **Scénario optimiste** (CA +10%, charges -5%) :
        - VAN devient : 750 k€ (très bonne)
        - TRI : 22% (excellent)
        
        **🎯 CRITÈRES DE DÉCISION :**
        
        **✅ ARGUMENTS POUR L'INVESTISSEMENT :**
        - VAN positive significative
        TRI supérieur au coût du capital
        - Délai de récupération acceptable
        - Potentiel de croissance important
        - Avantage concurrentiel durable
        
        **⚠️ RISQUES IDENTIFIÉS :**
        - Sensibilité aux variations du marché
        - Besoin en fonds de roulement important
        - Concurrence potentielle
        - Évolution des coûts énergétiques
        
        **📋 RECOMMANDATION :**
        
        **💡 DÉCISION : INVESTIR** 
        
        **Conditions :**
        1. Mise en place d'un plan de suivi rigoureux
        2. Définition d'indicateurs de performance
        3. Plan de contingence en cas de déviation
        4. Révision trimestrielle des hypothèses
        
        **Plan d'action :**
        - **Mois 1-3** : Négociation des équipements
        - **Mois 4-6** : Installation et formation
        - **Mois 7-9** : Démarrage progressif
        - **Mois 10-12** : Optimisation et montée en charge
        
        **Suivi post-investissement :**
        - Reporting mensuel des performances
        - Analyse trimestrielle de la rentabilité
        - Ajustement de la stratégie commerciale
        - Évaluation continue des risques
        """)

def show_cas_investissement():
    st.subheader("🏗️ Projet d'Investissement - Cas DÉCISIONNEL")
    
    st.markdown("""
    <div class="cas-container">
    <h3>🏭 Société AGRO-INNOV - Transformation alimentaire</h3>
    
    **Contexte :**
    - Projet d'investissement dans une nouvelle ligne de production
    - Investissement : 2,5 M€
    - Durée du projet : 5 ans
    - Objectif : augmentation de capacité de 40%
    </div>
    """, unsafe_allow_html=True)
    
    # Données du projet
    st.subheader("📋 Données du Projet d'Investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**INVESTISSEMENT INITIAL**")
        data_investissement = {
            'Poste': ['Machines et équipements', 'Installation et mise en route', 
                     'Frais d\'études', 'Besoins en fonds de roulement', 'TOTAL'],
            'Montant (k€)': [1800, 400, 150, 250, 2600]
        }
        df_invest = pd.DataFrame(data_investissement)
        st.dataframe(df_invest, use_container_width=True)
    
    with col2:
        st.write("**FLUX PRÉVISIONNELS**")
        data_flux = {
            'Année': [1, 2, 3, 4, 5],
            'CA supplémentaire (k€)': [1200, 1800, 2400, 2400, 2400],
            'Charges variables (k€)': [600, 900, 1200, 1200, 1200],
            'Charges fixes (k€)': [300, 350, 400, 400, 400]
        }
        df_flux = pd.DataFrame(data_flux)
        st.dataframe(df_flux, use_container_width=True)
    
    # Critères d'évaluation
    st.subheader("🎯 Critères d'Évaluation du Projet")
    
    st.markdown("""
    <div class="question-box">
    <h5>📋 Questions de décision</h5>
    1. Calculez la VAN du projet (taux d'actualisation : 10%)
    2. Déterminez le TRI approximatif
    3. Évaluez le délai de récupération
    4. Analysez la sensibilité du projet
    5. Prenez une décision d'investissement
    </div>
    """, unsafe_allow_html=True)
    
    # Calculateur d'investissement
    st.subheader("🧮 Calculateur de Rentabilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investissement = st.number_input("Investissement initial (k€)", value=2600, key="inv_initial")
        taux_actualisation = st.number_input("Taux d'actualisation (%)", value=10.0, key="inv_taux") / 100
        duree = st.number_input("Durée du projet (années)", value=5, key="inv_duree")
    
    with col2:
        st.write("**Flux de trésorerie annuels (k€)**")
        flux_annee1 = st.number_input("Année 1", value=300, key="inv_flux1")
        flux_annee2 = st.number_input("Année 2", value=550, key="inv_flux2")
        flux_annee3 = st.number_input("Année 3", value=800, key="inv_flux3")
        flux_annee4 = st.number_input("Année 4", value=800, key="inv_flux4")
        flux_annee5 = st.number_input("Année 5", value=1050, key="inv_flux5")  # inclut récupération BFR
    
    # Fonction pour calculer la VAN
    def calculer_van(invest, flux_list, taux):
        van_calc = -invest
        for i, flux_annuel in enumerate(flux_list):
            van_calc += flux_annuel / ((1 + taux) ** (i + 1))
        return van_calc
    
    # Fonction pour calculer le TRI
    def calculer_tri(invest, flux_list):
        def van_avec_taux(taux_test):
            van_calc = -invest
            for i, flux_annuel in enumerate(flux_list):
                van_calc += flux_annuel / ((1 + taux_test) ** (i + 1))
            return van_calc
        
        tri_calc = taux_actualisation
        for taux_test in np.arange(0.01, 0.50, 0.01):
            if van_avec_taux(taux_test) >= 0:
                tri_calc = taux_test
            else:
                break
        return tri_calc
    
    # Fonction pour calculer le délai de récupération
    def calculer_delai_recup(invest, flux_list):
        cumul_flux = 0
        delai_recup_calc = len(flux_list) + 1
        for i, flux_annuel in enumerate(flux_list):
            cumul_flux += flux_annuel
            if cumul_flux >= invest and delai_recup_calc > len(flux_list):
                delai_recup_calc = i + 1
        return delai_recup_calc
    
    # Initialiser les variables
    flux_courants = [flux_annee1, flux_annee2, flux_annee3, flux_annee4, flux_annee5]
    van_courante = calculer_van(investissement, flux_courants, taux_actualisation)
    tri_courant = calculer_tri(investissement, flux_courants)
    delai_recup_courant = calculer_delai_recup(investissement, flux_courants)
    
    if st.button("📊 Évaluer le projet", key="btn_eval_invest"):
        # Recalculer avec les valeurs actuelles
        flux_actuels = [flux_annee1, flux_annee2, flux_annee3, flux_annee4, flux_annee5]
        van_actuelle = calculer_van(investissement, flux_actuels, taux_actualisation)
        tri_actuel = calculer_tri(investissement, flux_actuels)
        delai_recup_actuel = calculer_delai_recup(investissement, flux_actuels)
        
        # Mettre à jour les variables courantes
        van_courante = van_actuelle
        tri_courant = tri_actuel
        delai_recup_courant = delai_recup_actuel
        
        # Affichage résultats
        st.subheader("📈 Résultats de l'Évaluation")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            delta_color = "normal" if van_actuelle > 0 else "inverse"
            st.metric("VAN", f"{van_actuelle:,.0f} k€", 
                     delta="✅ Rentable" if van_actuelle > 0 else "❌ Non rentable", 
                     delta_color=delta_color)
        
        with col2:
            st.metric("TRI", f"{tri_actuel*100:.1f}%")
        
        with col3:
            st.metric("Délai récupération", f"{delai_recup_actuel} ans")
    
    # Analyse de sensibilité
    st.subheader("📊 Analyse de Sensibilité")
    
    col1, col2 = st.columns(2)
    
    with col1:
        variation_ca = st.slider("Variation du CA (%)", -20, 20, 0, key="sens_ca")
        variation_charges = st.slider("Variation des charges (%)", -15, 15, 0, key="sens_charges")
    
    with col2:
        variation_invest = st.slider("Variation investissement (%)", -10, 10, 0, key="sens_invest")
        variation_taux = st.slider("Variation taux actualisation (%)", -3, 3, 0, key="sens_taux")
    
    if st.button("🔄 Calculer la sensibilité", key="btn_sensibilite"):
        # Calculer la VAN initiale (courante)
        van_initiale_courante = van_courante
        
        # Calculer les valeurs ajustées
        invest_ajuste = investissement * (1 + variation_invest/100)
        taux_ajuste = (taux_actualisation * 100 + variation_taux) / 100
        
        # Ajuster les flux selon les variations CA et charges
        flux_ajustes = [
            flux_annee1 * (1 + (variation_ca - variation_charges)/100),
            flux_annee2 * (1 + (variation_ca - variation_charges)/100),
            flux_annee3 * (1 + (variation_ca - variation_charges)/100),
            flux_annee4 * (1 + (variation_ca - variation_charges)/100),
            flux_annee5 * (1 + (variation_ca - variation_charges)/100)
        ]
        
        # Calculer la VAN avec sensibilité
        van_sensibilite = calculer_van(invest_ajuste, flux_ajustes, taux_ajuste)
        
        st.metric("VAN après sensibilité", f"{van_sensibilite:,.0f} k€", 
                 delta=f"{van_sensibilite - van_initiale_courante:+.0f} k€")
    
    # Décision d'investissement
    if st.button("🎯 Prendre la décision", key="btn_decision"):
        st.markdown("""
        <div class="solution-box">
        <h4>📝 Décision d'Investissement - Analyse Complète</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Utiliser les valeurs courantes pour l'analyse décisionnelle
        van_finale = van_courante
        tri_final = tri_courant
        delai_recup_final = delai_recup_courant
        
        st.write(f"""
        **🧮 ÉVALUATION FINANCIÈRE :**
        
        **Calculs de base :**
        - **VAN** : {van_finale:,.0f} k€ ({'✅ positive' if van_finale > 0 else '❌ négative'})
        - **TRI** : {tri_final*100:.1f}% ({"> taux d'actualisation de 10%" if tri_final > 0.1 else "≤ taux d'actualisation"})
        - **Délai de récupération** : {delai_recup_final} ans
        
        **ANALYSE DE SENSIBILITÉ :**
        
        **Scénario pessimiste** (CA -10%, charges +5%) :
        - VAN devient : ~{van_finale * 0.7:,.0f} k€ ({'toujours positive' if van_finale * 0.7 > 0 else 'devenue négative'})
        - TRI : ~{tri_final * 0.8:.1f}% ({'acceptable' if tri_final * 0.8 > 0.1 else 'insuffisant'})
        
        **Scénario optimiste** (CA +10%, charges -5%) :
        - VAN devient : ~{van_finale * 1.3:,.0f} k€ (très bonne)
        - TRI : ~{tri_final * 1.2:.1f}% (excellent)
        
        **🎯 CRITÈRES DE DÉCISION :**
        
        **✅ ARGUMENTS POUR L'INVESTISSEMENT :**
        - VAN {'positive' if van_finale > 0 else 'négative'} significative
        - TRI {'supérieur' if tri_final > 0.1 else 'inférieur'} au coût du capital
        - Délai de récupération {'acceptable' if delai_recup_final <= 4 else 'trop long'}
        - Potentiel de croissance important
        - Avantage concurrentiel durable
        
        **⚠️ RISQUES IDENTIFIÉS :**
        - Sensibilité aux variations du marché
        - Besoin en fonds de roulement important
        - Concurrence potentielle
        - Évolution des coûts énergétiques
        
        **📋 RECOMMANDATION :**
        
        **💡 DÉCISION : {'INVESTIR ✅' if van_finale > 0 and tri_final > 0.1 and delai_recup_final <= 5 else 'NE PAS INVESTIR ❌'}** 
        
        **Conditions :**
        1. Mise en place d'un plan de suivi rigoureux
        2. Définition d'indicateurs de performance
        3. Plan de contingence en cas de déviation
        4. Révision trimestrielle des hypothèses
        
        **Plan d'action :**
        - **Mois 1-3** : Négociation des équipements
        - **Mois 4-6** : Installation et formation
        - **Mois 7-9** : Démarrage progressif
        - **Mois 10-12** : Optimisation et montée en charge
        
        **Suivi post-investissement :**
        - Reporting mensuel des performances
        - Analyse trimestrielle de la rentabilité
        - Ajustement de la stratégie commerciale
        - Évaluation continue des risques
        """)

def show_ressources():
    st.markdown('<h2 class="section-header">📚 Ressources Pédagogiques</h2>', unsafe_allow_html=True)
    
    st.success("""
    **🎯 Comment utiliser cette section :**
    - **Visualisez** le contenu des fiches avant de les télécharger
    - **Testez** vos connaissances avec les quiz  
    - **Utilisez** les modèles pour vos propres analyses
    - **Progressez** à votre rythme
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📖 Fiches Mémo")
        
        # Contenu détaillé des fiches
        fiches_content = {
            "📄 Bilan": """
# FICHE MÉMO : BILAN COMPTABLE
## 📋 Définition
Le bilan est une photographie du patrimoine de l'entreprise à une date donnée.

## 🏗️ Structure
**ACTIF** (Ce que l'entreprise possède)
- Actif Immobilisé
  - Immobilisations incorporelles
  - Immobilisations corporelles
  - Immobilisations financières
- Actif Circulant
  - Stocks
  - Créances clients
  - Disponibilités

**PASSIF** (Ce que l'entreprise doit)
- Capitaux Propres
  - Capital social
  - Réserves
  - Résultat de l'exercice
- Dettes
  - Dettes financières
  - Dettes fournisseurs
  - Dettes fiscales et sociales

## ⚖️ Équilibre Fondamental
**ACTIF = PASSIF**

## 📊 Ratios Clés
- FRNG = Ressources stables - Emplois stables
- Taux d'endettement = Dettes financières / Capitaux propres
- Autonomie financière = Capitaux propres / Total passif

## 🎯 Points de Vigilance
- Vérifier l'équilibre Actif/Passif
- Analyser la structure des dettes
- Contrôler la qualité des actifs
            """,
            
            "📊 Compte de résultat": """
# FICHE MÉMO : COMPTE DE RÉSULTAT
## 📋 Définition
Le compte de résultat mesure la performance économique sur une période (généralement un an).

## 🏗️ Structure
**PRODUITS**
- Ventes de marchandises
- Production vendue
- Production stockée
- Subventions d'exploitation
- Produits financiers
- Produits exceptionnels

**CHARGES**
- Achats de marchandises
- Variation de stocks
- Charges externes
- Impôts et taxes
- Charges de personnel
- Dotations aux amortissements
- Charges financières
- Charges exceptionnelles

## 📈 Soldes Intermédiaires de Gestion
1. Marge commerciale
2. Valeur ajoutée
3. Excédent Brut d'Exploitation (EBE)
4. Résultat d'exploitation
5. Résultat courant
6. Résultat net

## 🎯 Ratios Clés
- Taux de marge = (Marge commerciale / CA) × 100
- Taux de VA = (Valeur ajoutée / CA) × 100
- Taux d'EBE = (EBE / CA) × 100
            """,
            
            "📐 Ratios financiers": """
# FICHE MÉMO : RATIOS FINANCIERS
## 📋 Classification des Ratios

## 💰 RENTABILITÉ
- Rentabilité économique = Résultat d'exploitation / Actif économique
- Rentabilité financière = Résultat net / Capitaux propres
- Taux de marge nette = (Résultat net / CA) × 100

## 🏗️ STRUCTURE
- Taux d'endettement = Dettes financières / Capitaux propres
- Autonomie financière = Capitaux propres / Total passif
- Ratio de solvabilité = Capitaux propres / Dettes totales

## 💧 LIQUIDITÉ
- Liquidité générale = Actif circulant / Dettes à court terme
- Liquidité réduite = (Actif circulant - Stocks) / Dettes à court terme
- Liquidité immédiate = Disponibilités / Dettes à court terme

## ⚙️ ACTIVITÉ
- Rotation des stocks = (Stocks moyens / Coût des ventes) × 360
- Crédit clients = (Clients moyens / CA TTC) × 360
- Crédit fournisseurs = (Fournisseurs moyens / Achats TTC) × 360

## 🎯 Normes Sectorielles
- Industrie : Rentabilité financière > 8%
- Commerce : Rotation stocks < 60 jours
- Services : Liquidité générale > 1,2
            """,
            
            "💧 Tableaux de flux": """
# FICHE MÉMO : TABLEAUX DE FLUX
## 📋 Définitions

## 💰 TABLEAU DES FLUX DE TRÉSORERIE (TFT)
**Flux d'Exploitation**
- Encaissements des clients
- Décaissements aux fournisseurs
- Charges de personnel
- Impôts payés

**Flux d'Investissement**
- Acquisitions d'immobilisations
- Cessions d'immobilisations
- Acquisitions de titres

**Flux de Financement**
- Augmentations de capital
- Emprunts contractés
- Remboursements d'emprunts
- Dividendes versés

## 🔄 MÉTHODE DE CONSTRUCTION
**Méthode Directe**
- Flux réels d'encaissements/décaissements
- Plus précise mais plus complexe

**Méthode Indirecte**
- Part du résultat net
- Ajustements des éléments non-monétaires
- Variation du BFR

## 📊 ÉQUILIBRE DES FLUX
Trésorerie nette = Flux exploitation + Flux investissement + Flux financement

## 🎯 ANALYSE
- Capacité à dégager de la trésorerie
- Politique d'investissement
- Stratégie de financement
- Équilibre global
            """,
            
            "🔍 Diagnostic financier": """
# FICHE MÉMO : DIAGNOSTIC FINANCIER
## 📋 Processus en 5 Étapes

## 1. COLLECTE DES INFORMATIONS
- Bilan
- Compte de résultat
- Annexes
- Données sectorielles

## 2. ANALYSE HORIZONTALE ET VERTICALE
- Évolution des postes
- Structure du bilan
- Soldes intermédiaires

## 3. CALCUL DES RATIOS
- Ratios de rentabilité
- Ratios de structure
- Ratios de liquidité
- Ratios d'activité

## 4. ANALYSE FONCTIONNELLE
- Fonds de Roulement Net Global (FRNG)
- Besoin en Fonds de Roulement (BFR)
- Trésorerie nette

## 5. SYNTHÈSE ET RECOMMANDATIONS
- Points forts/faibles
- Risques identifiés
- Plan d'action
- Suivi des indicateurs

## 🎯 GRILIE D'ANALYSE
✅ Rentabilité suffisante
✅ Équilibre financier
✅ Liquidité adéquate
✅ Croissance maîtrisée
            """
        }
        
        for ressource, content in fiches_content.items():
            with st.expander(f"{ressource}"):
                st.markdown(content)
                
                # Bouton de téléchargement avec contenu réel
                nom_fichier = f"fiche_{ressource.lower().replace('📄 ', '').replace('📊 ', '').replace('📐 ', '').replace('💧 ', '').replace('🔍 ', '').replace(' ', '_')}.txt"
                st.download_button(
                    f"📥 Télécharger {ressource}",
                    content,
                    file_name=nom_fichier,
                    key=f"dl_{ressource}"
                )
    
    with col2:
        st.subheader("🎓 Quiz d'auto-évaluation")
        
        quiz_choice = st.selectbox(
            "**Choisissez un quiz :**",
            ["🟢 Débutant - Fondamentaux", "🟡 Intermédiaire - Bilan", 
             "🟠 Avancé - Compte de résultat", "🔴 Expert - Ratios", "🏆 Master - Diagnostic global"],
            key="quiz_choice"
        )
        
        if "Débutant" in quiz_choice:
            show_quiz_fondamentaux()
        elif "Bilan" in quiz_choice:
            show_quiz_bilan()
        elif "Compte de résultat" in quiz_choice:
            show_quiz_compte_resultat()
        elif "Ratios" in quiz_choice:
            show_quiz_ratios()
        elif "Diagnostic" in quiz_choice:
            show_quiz_diagnostic()
    
    st.subheader("📊 Modèles et Templates")
    
    # Contenu des modèles Excel (simulé)
    modeles_content = {
        "modele_bilan": """
BILAN COMPTABLE - MODÈLE EXCEL
===============================

STRUCTURE DU FICHIER:

[ACTIF]
- Immobilisations
- Stocks
- Créances
- Disponibilités

[PASSIF]
- Capitaux propres
- Dettes LT
- Dettes CT

[ANALYSE]
- Ratios automatiques
- Équilibre financier
- Graphiques

FONCTIONNALITÉS:
- Calculs automatiques
- Mise en forme conditionnelle
- Graphiques de synthèse
""",
        "calculateur_ratios": """
CALCULATEUR DE RATIOS - MODÈLE EXCEL
=====================================

CATÉGORIES DE RATIOS:

1. RENTABILITÉ
   - Rentabilité économique
   - Rentabilité financière
   - Marge nette

2. LIQUIDITÉ
   - Liquidité générale
   - Liquidité réduite
   - Liquidité immédiate

3. STRUCTURE
   - Taux d'endettement
   - Autonomie financière
   - Solvabilité

FONCTIONNALITÉS:
- Tableaux de bord
- Analyses comparatives
- Seuils d'alerte
""",
        "tableau_flux_oec": """
TABLEAU DE FLUX OEC - MODÈLE EXCEL
===================================

SECTIONS PRINCIPALES:

[FLUX D'EXPLOITATION]
- Résultat net
- Dotations
- Variation BFR

[FLUX D'INVESTISSEMENT]
- Acquisitions
- Cessions

[FLUX DE FINANCEMENT]
- Augmentation capital
- Emprunts
- Dividendes

FONCTIONNALITÉS:
- Construction automatique
- Contrôle d'équilibre
- Analyse des variations
"""
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**📋 Modèle de bilan**")
        st.info("Structure complète avec analyse automatique")
        with st.expander("📋 Voir la description détaillée"):
            st.text(modeles_content["modele_bilan"])
        st.download_button(
            "📥 Télécharger le modèle",
            modeles_content["modele_bilan"],
            file_name="modele_bilan.xlsx",
            key="dl_bilan"
        )
    
    with col2:
        st.write("**📊 Modèle de ratios**")
        st.info("Calculateur automatique avec tableaux de bord")
        with st.expander("📊 Voir la description détaillée"):
            st.text(modeles_content["calculateur_ratios"])
        st.download_button(
            "📥 Télécharger le calculateur",
            modeles_content["calculateur_ratios"],
            file_name="calculateur_ratios.xlsx",
            key="dl_ratios"
        )
    
    with col3:
        st.write("**📈 Modèle de tableau de flux**")
        st.info("Template tableau de flux OEC complet")
        with st.expander("📈 Voir la description détaillée"):
            st.text(modeles_content["tableau_flux_oec"])
        st.download_button(
            "📥 Télécharger le template",
            modeles_content["tableau_flux_oec"],
            file_name="tableau_flux_oec.xlsx",
            key="dl_flux"
        )
    
    # Section des formules importantes
    st.subheader("🧮 Formules Clés")
    
    formules_content = """
FORMULES FINANCIÈRES ESSENTIELLES
==================================

📈 RENTABILITÉ
---------------
Rentabilité économique = Résultat d'exploitation / Actif économique
Rentabilité financière = Résultat net / Capitaux propres
Taux de marge nette = (Résultat net / CA) × 100

⚖️ ÉQUILIBRE FINANCIER
----------------------
FRNG = Ressources stables - Emplois stables
BFR = Actif circulant - Passif circulant
Trésorerie nette = FRNG - BFR

💰 CAPACITÉ D'AUTOFINANCEMENT
-----------------------------
CAF = Résultat net + Dotations - Reprises - Produits de cession

📊 SOLDES INTERMÉDIAIRES
------------------------
Marge commerciale = Ventes - Achats consommés
Valeur ajoutée = Marge commerciale + Production - Consommations
EBE = Valeur ajoutée - Charges de personnel

🎯 INVESTISSEMENT
-----------------
VAN = Σ(Flux / (1+t)ⁿ) - Investissement initial
TRI = Taux qui annule la VAN
Délai de récupération = Moment où les flux cumulés ≥ Investissement
"""
    
    with st.expander("🧮 Voir toutes les formules clés"):
        st.text(formules_content)
        st.download_button(
            "📥 Télécharger les formules",
            formules_content,
            file_name="formules_financieres.txt",
            key="dl_formules"
        )

def show_quiz_compte_resultat():
    st.write("**📊 Quiz sur le Compte de Résultat**")
    
    questions = [
        {
            "question": "Quel est le solde intermédiaire de gestion qui mesure la performance économique avant éléments financiers?",
            "options": [
                "Résultat net",
                "Excédent Brut d'Exploitation (EBE)", 
                "Valeur ajoutée",
                "Marge commerciale"
            ],
            "reponse": 1,
            "explication": "L'EBE (Excédent Brut d'Exploitation) mesure la performance économique avant prise en compte de la politique financière, des investissements et des éléments exceptionnels."
        },
        {
            "question": "Comment calcule-t-on la capacité d'autofinancement (CAF) à partir du résultat net?",
            "options": [
                "CAF = Résultat net - Dotations + Reprises",
                "CAF = Résultat net + Dotations - Reprises", 
                "CAF = Résultat net × 2",
                "CAF = Résultat net / Charges financières"
            ],
            "reponse": 1,
            "explication": "La CAF se calcule en ajoutant au résultat net les dotations aux amortissements et provisions, et en retranchant les reprises."
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        reponse = st.radio(f"Choisissez votre réponse:", q['options'], key=f"cr_q{i}")
        
        if st.button(f"Vérifier question {i+1}", key=f"cr_btn{i}"):
            if q['options'].index(reponse) == q['reponse']:
                st.success("✅ Bonne réponse!")
                st.info(f"**Explication :** {q['explication']}")
                score += 1
            else:
                st.error(f"❌ Mauvaise réponse. La bonne réponse était: {q['options'][q['reponse']]}")
                st.info(f"**Explication :** {q['explication']}")
    
    if st.button("🎯 Voir le score final", key="cr_final"):
        st.info(f"**Score: {score}/{len(questions)}**")
        if score == len(questions):
            st.balloons()
            st.success("🎉 Excellent! Maîtrise parfaite du compte de résultat!")
        elif score >= len(questions)/2:
            st.warning("📚 Bien! Continuez à étudier les soldes intermédiaires!")
        else:
            st.error("📖 Revoyez la structure du compte de résultat")

def show_quiz_ratios():
    st.write("**📐 Quiz sur les Ratios Financiers**")
    
    questions = [
        {
            "question": "Quel ratio mesure la capacité de l'entreprise à rembourser ses dettes à court terme avec ses actifs liquides?",
            "options": [
                "Ratio de liquidité générale",
                "Taux d'endettement", 
                "Rentabilité financière",
                "Rotation des stocks"
            ],
            "reponse": 0,
            "explication": "Le ratio de liquidité générale (Actif circulant / Dettes CT) mesure la capacité à honorer les dettes à court terme."
        },
        {
            "question": "Un taux d'endettement de 150% signifie que:",
            "options": [
                "L'entreprise est très solvable",
                "Les dettes représentent 1,5 fois les capitaux propres", 
                "La rentabilité est excellente",
                "L'entreprise n'a pas de dettes"
            ],
            "reponse": 1,
            "explication": "Un taux d'endettement de 150% signifie que les dettes financières sont 1,5 fois supérieures aux capitaux propres, ce qui peut indiquer un endettement élevé."
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        reponse = st.radio(f"Choisissez votre réponse:", q['options'], key=f"ratio_q{i}")
        
        if st.button(f"Vérifier question {i+1}", key=f"ratio_btn{i}"):
            if q['options'].index(reponse) == q['reponse']:
                st.success("✅ Bonne réponse!")
                st.info(f"**Explication :** {q['explication']}")
                score += 1
            else:
                st.error(f"❌ Mauvaise réponse. La bonne réponse était: {q['options'][q['reponse']]}")
                st.info(f"**Explication :** {q['explication']}")
    
    if st.button("🎯 Voir le score final", key="ratio_final"):
        st.info(f"**Score: {score}/{len(questions)}**")
        if score == len(questions):
            st.balloons()
            st.success("🎉 Excellent! Maîtrise parfaite des ratios financiers!")
        elif score >= len(questions)/2:
            st.warning("📚 Bien! Approfondissez vos connaissances sur les ratios!")
        else:
            st.error("📖 Revoyez la classification et le calcul des ratios")

def show_quiz_diagnostic():
    st.write("**🔍 Quiz sur le Diagnostic Financier**")
    
    questions = [
        {
            "question": "Quelle est la séquence correcte du processus de diagnostic financier?",
            "options": [
                "Ratios → Bilan → Recommandations",
                "Collecte → Analyse → Diagnostic → Recommandations", 
                "Recommandations → Diagnostic → Analyse",
                "Bilan → Compte de résultat → Ratios"
            ],
            "reponse": 1,
            "explication": "Le processus standard est : Collecte des informations → Analyse financière → Diagnostic → Recommandations."
        },
        {
            "question": "Un FRNG positif et un BFR négatif indiquent:",
            "options": [
                "Une situation de déséquilibre financier",
                "Une trésorerie excédentaire", 
                "Un besoin de financement urgent",
                "Une rentabilité insuffisante"
            ],
            "reponse": 1,
            "explication": "FRNG positif + BFR négatif = Trésorerie nette positive, ce qui indique une situation financière saine avec excédent de trésorerie."
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        reponse = st.radio(f"Choisissez votre réponse:", q['options'], key=f"diag_q{i}")
        
        if st.button(f"Vérifier question {i+1}", key=f"diag_btn{i}"):
            if q['options'].index(reponse) == q['reponse']:
                st.success("✅ Bonne réponse!")
                st.info(f"**Explication :** {q['explication']}")
                score += 1
            else:
                st.error(f"❌ Mauvaise réponse. La bonne réponse était: {q['options'][q['reponse']]}")
                st.info(f"**Explication :** {q['explication']}")
    
    if st.button("🎯 Voir le score final", key="diag_final"):
        st.info(f"**Score: {score}/{len(questions)}**")
        if score == len(questions):
            st.balloons()
            st.success("🎉 Excellent! Maîtrise parfaite du diagnostic financier!")
        elif score >= len(questions)/2:
            st.warning("📚 Bien! Approfondissez la méthodologie de diagnostic!")
        else:
            st.error("📖 Revoyez le processus complet de diagnostic financier")
            
def show_quiz_bilan():
    st.write("**Quiz sur le bilan comptable**")
    st.info("Ce quiz sera bientôt disponible...")
    

import io
import base64
from datetime import datetime

def show_ressources():
    st.markdown('<h2 class="section-header">📚 Ressources Pédagogiques</h2>', unsafe_allow_html=True)
    
    st.success("""
    **🎯 Comment utiliser cette section :**
    - **Téléchargez** des modèles Excel fonctionnels
    - **Analysez** vos propres états financiers  
    - **Testez** vos connaissances avec les quiz complets
    - **Progressez** avec des outils professionnels
    """)
    
    # Navigation dans les ressources
    resource_tabs = st.tabs(["📊 Analyse Personnalisée", "📁 Modèles Téléchargeables", "🎓 Quiz d'Évaluation"])
    
    with resource_tabs[0]:
        show_analyse_personnalisee()
    
    with resource_tabs[1]:
        show_modeles_telechargeables()
    
    with resource_tabs[2]:
        show_quiz_complets()

def show_analyse_personnalisee():
    st.subheader("🔍 Analyse Financière Personnalisée")
    
    st.info("""
    **Chargez vos états financiers pour obtenir une analyse automatique :**
    - Bilan comptable
    - Compte de résultat  
    - Tableaux de flux
    - Ou tous les états financiers
    """)
    
    # Sélection du type d'analyse
    analyse_type = st.radio(
        "**Sélectionnez le type d'analyse :**",
        ["📊 Analyse du Bilan", "📈 Analyse du Compte de Résultat", "💧 Analyse des Tableaux de Flux", "🔍 Analyse Complète"],
        horizontal=True
    )
    
    if "Bilan" in analyse_type:
        analyse_bilan_personnalise()
    elif "Compte" in analyse_type:
        analyse_compte_resultat_personnalise()
    elif "Tableaux" in analyse_type:
        analyse_flux_personnalise()
    else:
        analyse_complete_personnalise()

def analyse_bilan_personnalise():
    st.subheader("📊 Analyse Personnalisée du Bilan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Méthode 1 : Saisie manuelle**")
        with st.expander("📝 Saisir les données du bilan", expanded=True):
            st.write("**ACTIF**")
            immob_corporelles = st.number_input("Immobilisations corporelles (k€)", value=1500, key="pers_immob")
            stocks = st.number_input("Stocks (k€)", value=800, key="pers_stocks")
            clients = st.number_input("Créances clients (k€)", value=1200, key="pers_clients")
            disponibilites = st.number_input("Disponibilités (k€)", value=300, key="pers_dispo")
            
            st.write("**PASSIF**")
            capital = st.number_input("Capital social (k€)", value=1000, key="pers_capital")
            reserves = st.number_input("Réserves (k€)", value=800, key="pers_reserves")
            resultat = st.number_input("Résultat (k€)", value=200, key="pers_resultat")
            dettes_lt = st.number_input("Dettes long terme (k€)", value=1000, key="pers_dettes_lt")
            dettes_ct = st.number_input("Dettes court terme (k€)", value=800, key="pers_dettes_ct")
    
    with col2:
        st.write("**Méthode 2 : Charger un fichier Excel**")
        fichier_bilan = st.file_uploader("Télécharger votre bilan (format Excel)", type=['xlsx'], key="file_bilan")
        
        if fichier_bilan is not None:
            try:
                df_bilan = pd.read_excel(fichier_bilan)
                st.success("✅ Fichier chargé avec succès")
                st.dataframe(df_bilan)
            except Exception as e:
                st.error(f"❌ Erreur lors du chargement: {e}")
    
    if st.button("📈 Analyser le bilan", key="btn_analyse_bilan"):
        # Calculs d'analyse
        total_actif = immob_corporelles + stocks + clients + disponibilites
        total_passif = capital + reserves + resultat + dettes_lt + dettes_ct
        
        # Équilibre financier
        ressources_stables = capital + reserves + resultat + dettes_lt
        emplois_stables = immob_corporelles
        frng = ressources_stables - emplois_stables
        
        actif_circulant = stocks + clients + disponibilites
        passif_circulant = dettes_ct
        bfr = actif_circulant - passif_circulant
        tresorerie = frng - bfr
        
        # Ratios
        taux_endettement = (dettes_lt + dettes_ct) / (capital + reserves + resultat) * 100
        autonomie_financiere = (capital + reserves + resultat) / total_passif * 100
        liquidite_generale = actif_circulant / passif_circulant * 100
        
        # Affichage des résultats
        st.subheader("📊 Résultats de l'Analyse du Bilan")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Actif", f"{total_actif:,.0f} k€")
            st.metric("Total Passif", f"{total_passif:,.0f} k€")
            if abs(total_actif - total_passif) < 1:
                st.success("✅ Bilan équilibré")
            else:
                st.error(f"❌ Écart: {abs(total_actif - total_passif):.0f} k€")
        
        with col2:
            delta_color = "normal" if frng > 0 else "inverse"
            st.metric("FRNG", f"{frng:,.0f} k€", delta="✅ Bon" if frng > 0 else "❌ Risque", delta_color=delta_color)
            st.metric("BFR", f"{bfr:,.0f} k€", delta="📈 Besoin" if bfr > 0 else "📉 Ressource")
            delta_color = "normal" if tresorerie > 0 else "inverse"
            st.metric("Trésorerie", f"{tresorerie:,.0f} k€", delta="✅ Excédent" if tresorerie > 0 else "❌ Déficit", delta_color=delta_color)
        
        with col3:
            st.metric("Taux d'endettement", f"{taux_endettement:.1f}%")
            st.metric("Autonomie financière", f"{autonomie_financiere:.1f}%")
            st.metric("Liquidité générale", f"{liquidite_generale:.1f}%")
        
        # Diagnostic
        st.subheader("🔍 Diagnostic Financier")
        
        points_forts = []
        points_faibles = []
        
        if frng > 0:
            points_forts.append("FRNG positif - Bon équilibre financier")
        else:
            points_faibles.append("FRNG négatif - Risque de structure")
            
        if tresorerie > 0:
            points_forts.append("Trésorerie excédentaire")
        else:
            points_faibles.append("Trésorerie déficitaire")
            
        if taux_endettement < 100:
            points_forts.append("Endettement maîtrisé")
        else:
            points_faibles.append("Endettement élevé")
            
        if liquidite_generale > 100:
            points_forts.append("Bonne liquidité")
        else:
            points_faibles.append("Liquidité insuffisante")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if points_forts:
                st.success("**✅ Points Forts:**")
                for point in points_forts:
                    st.write(f"• {point}")
        
        with col2:
            if points_faibles:
                st.error("**⚠️ Points de Vigilance:**")
                for point in points_faibles:
                    st.write(f"• {point}")

def analyse_compte_resultat_personnalise():
    st.subheader("📈 Analyse Personnalisée du Compte de Résultat")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Saisie des données**")
        with st.expander("📝 Données du compte de résultat", expanded=True):
            ca = st.number_input("Chiffre d'affaires (k€)", value=5000, key="pers_ca")
            achats = st.number_input("Achats consommés (k€)", value=3000, key="pers_achats")
            charges_personnel = st.number_input("Charges de personnel (k€)", value=1200, key="pers_charges_pers")
            autres_charges = st.number_input("Autres charges (k€)", value=300, key="pers_autres_charges")
            dotations = st.number_input("Dotations aux amortissements (k€)", value=200, key="pers_dotations")
            charges_financieres = st.number_input("Charges financières (k€)", value=100, key="pers_charges_fin")
    
    with col2:
        st.write("**Chargement de fichier**")
        fichier_cr = st.file_uploader("Télécharger votre compte de résultat (Excel)", type=['xlsx'], key="file_cr")
        
        if fichier_cr is not None:
            try:
                df_cr = pd.read_excel(fichier_cr)
                st.success("✅ Fichier chargé avec succès")
                st.dataframe(df_cr)
            except Exception as e:
                st.error(f"❌ Erreur lors du chargement: {e}")
    
    if st.button("📊 Analyser la rentabilité", key="btn_analyse_cr"):
        # Calcul des SIG
        marge_commerciale = ca - achats
        valeur_ajoutee = marge_commerciale - autres_charges
        ebe = valeur_ajoutee - charges_personnel
        resultat_exploitation = ebe - dotations
        resultat_courant = resultat_exploitation - charges_financieres
        
        # Ratios de rentabilité
        taux_marge = (marge_commerciale / ca * 100) if ca > 0 else 0
        taux_ebe = (ebe / ca * 100) if ca > 0 else 0
        taux_resultat_exploitation = (resultat_exploitation / ca * 100) if ca > 0 else 0
        taux_resultat_courant = (resultat_courant / ca * 100) if ca > 0 else 0
        
        # Affichage des résultats
        st.subheader("📈 Soldes Intermédiaires de Gestion")
        
        sig_data = {
            'Solde': ['Marge commerciale', 'Valeur ajoutée', 'EBE', 'Résultat exploitation', 'Résultat courant'],
            'Montant (k€)': [marge_commerciale, valeur_ajoutee, ebe, resultat_exploitation, resultat_courant],
            'Taux (%)': [taux_marge, (valeur_ajoutee/ca*100) if ca>0 else 0, taux_ebe, taux_resultat_exploitation, taux_resultat_courant]
        }
        
        df_sig = pd.DataFrame(sig_data)
        st.dataframe(df_sig, use_container_width=True)
        
        # Graphique des SIG
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_sig['Solde'], y=df_sig['Montant (k€)'], name='Montant (k€)'))
        fig.update_layout(title='Pyramide des Soldes Intermédiaires de Gestion', xaxis_title='Soldes', yaxis_title='Montants (k€)')
        st.plotly_chart(fig)
        
        # Diagnostic de rentabilité
        st.subheader("🔍 Diagnostic de Rentabilité")
        
        normes_sectorielles = {
            'Taux de marge': {'min': 30, 'bon': 40},
            'Taux EBE': {'min': 10, 'bon': 15},
            'Taux résultat exploitation': {'min': 5, 'bon': 8}
        }
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if taux_marge >= normes_sectorielles['Taux de marge']['bon']:
                st.success(f"Taux de marge: {taux_marge:.1f}%")
            elif taux_marge >= normes_sectorielles['Taux de marge']['min']:
                st.warning(f"Taux de marge: {taux_marge:.1f}%")
            else:
                st.error(f"Taux de marge: {taux_marge:.1f}%")
        
        with col2:
            if taux_ebe >= normes_sectorielles['Taux EBE']['bon']:
                st.success(f"Taux EBE: {taux_ebe:.1f}%")
            elif taux_ebe >= normes_sectorielles['Taux EBE']['min']:
                st.warning(f"Taux EBE: {taux_ebe:.1f}%")
            else:
                st.error(f"Taux EBE: {taux_ebe:.1f}%")
        
        with col3:
            if taux_resultat_exploitation >= normes_sectorielles['Taux résultat exploitation']['bon']:
                st.success(f"Taux résultat exploitation: {taux_resultat_exploitation:.1f}%")
            elif taux_resultat_exploitation >= normes_sectorielles['Taux résultat exploitation']['min']:
                st.warning(f"Taux résultat exploitation: {taux_resultat_exploitation:.1f}%")
            else:
                st.error(f"Taux résultat exploitation: {taux_resultat_exploitation:.1f}%")

def analyse_flux_personnalise():
    st.subheader("💧 Analyse Personnalisée des Tableaux de Flux")
    
    st.info("Analysez vos flux de trésorerie : exploitation, investissement et financement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Flux d'Exploitation**")
        resultat_net = st.number_input("Résultat net (k€)", value=800, key="flux_rn")
        dotations = st.number_input("Dotations (k€)", value=300, key="flux_dot")
        variation_bfr = st.number_input("Δ BFR (k€)", value=-200, key="flux_bfr")
    
    with col2:
        st.write("**Flux d'Investissement et Financement**")
        acquisitions = st.number_input("Acquisitions (k€)", value=-1000, key="flux_acqu")
        emprunts = st.number_input("Nouveaux emprunts (k€)", value=500, key="flux_emp")
        remboursements = st.number_input("Remboursements (k€)", value=-300, key="flux_remb")
    
    if st.button("💰 Analyser les flux", key="btn_analyse_flux"):
        # Calcul des flux nets
        flux_exploitation = resultat_net + dotations + variation_bfr
        flux_investissement = acquisitions
        flux_financement = emprunts + remboursements
        variation_tresorerie = flux_exploitation + flux_investissement + flux_financement
        
        # Affichage des résultats
        st.subheader("📊 Synthèse des Flux de Trésorerie")
        
        flux_data = {
            'Catégorie': ['Exploitation', 'Investissement', 'Financement', 'Variation Trésorerie'],
            'Montant (k€)': [flux_exploitation, flux_investissement, flux_financement, variation_tresorerie],
            'Analyse': [
                "✅ Générateur" if flux_exploitation > 0 else "❌ Consommateur",
                "📈 Investisseur" if flux_investissement < 0 else "📉 Désinvestisseur",
                "💰 Apport net" if flux_financement > 0 else "💸 Sortie nette",
                "🔼 Augmentation" if variation_tresorerie > 0 else "🔽 Diminution"
            ]
        }
        
        df_flux = pd.DataFrame(flux_data)
        st.dataframe(df_flux, use_container_width=True)
        
        # Graphique en camembert
        fig = go.Figure(data=[go.Pie(
            labels=['Exploitation', 'Investissement', 'Financement'],
            values=[abs(flux_exploitation), abs(flux_investissement), abs(flux_financement)],
            hole=0.3
        )])
        fig.update_layout(title='Répartition des Flux de Trésorerie')
        st.plotly_chart(fig)

def analyse_complete_personnalise():
    st.subheader("🔍 Analyse Financière Complète")
    
    st.warning("Cette analyse nécessite tous les états financiers. Chargez vos fichiers ou utilisez les données par défaut.")
    
    # Chargement multiple de fichiers
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fichier_bilan = st.file_uploader("Bilan", type=['xlsx'], key="file_full_bilan")
    with col2:
        fichier_cr = st.file_uploader("Compte de résultat", type=['xlsx'], key="file_full_cr")
    with col3:
        fichier_flux = st.file_uploader("Tableaux de flux", type=['xlsx'], key="file_full_flux")
    
    if st.button("🚀 Lancer l'analyse complète", key="btn_analyse_complete"):
        # Analyse synthétique
        st.subheader("📋 Synthèse du Diagnostic Financier")
        
        # Tableau de bord
        indicateurs = {
            'Indicateur': ['Rentabilité financière', 'Taux d\'endettement', 'Liquidité générale', 'Couverture des frais financiers', 'Rotation du BFR'],
            'Valeur': ['15.2%', '65.8%', '1.8', '4.2', '45 jours'],
            'Seuil': ['>8%', '<100%', '>1.2', '>3', '<60 jours'],
            'Statut': ['✅ Bon', '✅ Acceptable', '✅ Bon', '✅ Bon', '✅ Bon']
        }
        
        df_indicateurs = pd.DataFrame(indicateurs)
        st.dataframe(df_indicateurs, use_container_width=True)
        
        # Recommandations stratégiques
        st.subheader("🎯 Recommandations Stratégiques")
        
        recom_cols = st.columns(2)
        
        with recom_cols[0]:
            st.success("**✅ Actions à Maintenir:**")
            st.write("• Politique d'investissement maîtrisée")
            st.write("• Bon contrôle des coûts d'exploitation")
            st.write("• Structure financière équilibrée")
            st.write("• Trésorerie suffisante")
        
        with recom_cols[1]:
            st.warning("**📈 Axes d'Amélioration:**")
            st.write("• Optimisation du BFR")
            st.write("• Diversification du financement")
            st.write("• Renforcement de la rentabilité")
            st.write("• Développement de nouveaux marchés")

def show_modeles_telechargeables():
    st.subheader("📁 Modèles Excel Professionnels")
    
    st.info("Téléchargez des modèles Excel fonctionnels pour vos analyses financières")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**📋 Modèle de Bilan**")
        st.markdown("""
        Structure complète avec :
        - Actif/Passif détaillé
        - Calculs automatiques
        - Ratios financiers
        - Graphiques de synthèse
        """)
        
        # Création d'un modèle Excel simple
        def create_bilan_template():
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                # Feuille Actif
                actif_data = {
                    'ACTIF': ['ACTIF IMMOBILISÉ', '', 'Immobilisations incorporelles', 'Immobilisations corporelles', 
                             'Immobilisations financières', 'TOTAL ACTIF IMMOBILISÉ', '',
                             'ACTIF CIRCULANT', '', 'Stocks', 'Créances clients', 'Disponibilités',
                             'TOTAL ACTIF CIRCULANT', '', 'TOTAL ACTIF'],
                    'Montant (k€)': ['', '', 500, 1500, 300, 2300, '', '', '', 800, 1200, 300, 2300, '', 4600]
                }
                df_actif = pd.DataFrame(actif_data)
                df_actif.to_excel(writer, sheet_name='Actif', index=False)
                
                # Feuille Passif
                passif_data = {
                    'PASSIF': ['CAPITAUX PROPRES', '', 'Capital social', 'Réserves', 'Résultat de l\'exercice',
                              'TOTAL CAPITAUX PROPRES', '', 'DETTES', '', 'Dettes financières LT', 'Dettes fournisseurs',
                              'Autres dettes', 'TOTAL DETTES', '', 'TOTAL PASSIF'],
                    'Montant (k€)': ['', '', 1000, 800, 200, 2000, '', '', '', 1000, 800, 800, 2600, '', 4600]
                }
                df_passif = pd.DataFrame(passif_data)
                df_passif.to_excel(writer, sheet_name='Passif', index=False)
                
                # Feuille Analyse
                analyse_data = {
                    'RATIOS FINANCIERS': ['FRNG', 'BFR', 'Trésorerie nette', 'Taux d\'endettement', 'Autonomie financière'],
                    'Valeur': ['700 k€', '500 k€', '200 k€', '65.8%', '43.5%'],
                    'Analyse': ['✅ Bon', '📈 À surveiller', '✅ Bon', '✅ Acceptable', '✅ Correct']
                }
                df_analyse = pd.DataFrame(analyse_data)
                df_analyse.to_excel(writer, sheet_name='Analyse', index=False)
            
            return output.getvalue()
        
        bilan_excel = create_bilan_template()
        st.download_button(
            label="📥 Télécharger le modèle Bilan",
            data=bilan_excel,
            file_name="modele_bilan_complet.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    with col2:
        st.write("**📊 Modèle Compte de Résultat**")
        st.markdown("""
        Structure complète avec :
        - Produits et charges détaillés
        - SIG automatiques
        - Ratios de rentabilité
        - Analyse horizontale/verticale
        """)
        
        def create_cr_template():
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                # Feuille Compte de résultat
                cr_data = {
                    'COMPTE DE RÉSULTAT': ['PRODUITS', '', 'Chiffre d\'affaires', 'Autres produits', 'TOTAL PRODUITS', '',
                                          'CHARGES', '', 'Achats consommés', 'Charges de personnel', 'Autres charges',
                                          'Dotations aux amortissements', 'Charges financières', 'TOTAL CHARGES', '',
                                          'RÉSULTAT NET'],
                    'Montant (k€)': ['', '', 5000, 200, 5200, '', '', '', 3000, 1200, 300, 200, 100, 4800, '', 400]
                }
                df_cr = pd.DataFrame(cr_data)
                df_cr.to_excel(writer, sheet_name='Compte de résultat', index=False)
                
                # Feuille SIG
                sig_data = {
                    'SOLDES INTERMÉDIAIRES': ['Marge commerciale', 'Valeur ajoutée', 'EBE', 'Résultat d\'exploitation', 'Résultat courant'],
                    'Montant (k€)': [2000, 1700, 500, 300, 200],
                    'Taux (%)': [40.0, 34.0, 10.0, 6.0, 4.0]
                }
                df_sig = pd.DataFrame(sig_data)
                df_sig.to_excel(writer, sheet_name='SIG', index=False)
            
            return output.getvalue()
        
        cr_excel = create_cr_template()
        st.download_button(
            label="📥 Télécharger modèle Compte de résultat",
            data=cr_excel,
            file_name="modele_compte_resultat.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    with col3:
        st.write("**📈 Modèle Tableaux de Flux**")
        st.markdown("""
        Structure complète avec :
        - Flux d'exploitation
        - Flux d'investissement  
        - Flux de financement
        - Synthèse automatique
        """)
        
        def create_flux_template():
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                # Feuille Flux
                flux_data = {
                    'TABLEAU DES FLUX': ['FLUX D\'EXPLOITATION', '', 'Résultat net', 'Dotations aux amortissements',
                                        'Variation du BFR', 'FLUX NET EXPLOITATION', '',
                                        'FLUX D\'INVESTISSEMENT', '', 'Acquisitions d\'immobilisations',
                                        'Cessions d\'immobilisations', 'FLUX NET INVESTISSEMENT', '',
                                        'FLUX DE FINANCEMENT', '', 'Augmentations de capital', 'Emprunts nouveaux',
                                        'Remboursements d\'emprunts', 'FLUX NET FINANCEMENT', '',
                                        'VARIATION DE TRÉSORERIE'],
                    'Montant (k€)': ['', '', 400, 200, -150, 450, '', '', '', -1000, 50, -950, '', '', '', 0, 500, -300, 200, '', -300]
                }
                df_flux = pd.DataFrame(flux_data)
                df_flux.to_excel(writer, sheet_name='Tableau des flux', index=False)
            
            return output.getvalue()
        
        flux_excel = create_flux_template()
        st.download_button(
            label="📥 Télécharger modèle Tableaux de flux",
            data=flux_excel,
            file_name="modele_tableaux_flux.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

def show_quiz_complets():
    st.subheader("🎓 Quiz d'Évaluation Complète")
    
    quiz_choice = st.selectbox(
        "**Sélectionnez votre niveau :**",
        ["🟢 Débutant - Fondamentaux", "🟡 Intermédiaire - Bilan", 
         "🟠 Avancé - Compte de résultat", "🔴 Expert - Ratios", "🏆 Master - Diagnostic global"],
        key="quiz_complet_choice"
    )
    
    if "Débutant" in quiz_choice:
        show_quiz_debutant()
    elif "Bilan" in quiz_choice:
        show_quiz_bilan_complet()
    elif "Compte" in quiz_choice:
        show_quiz_cr_complet()
    elif "Ratios" in quiz_choice:
        show_quiz_ratios_complet()
    elif "Diagnostic" in quiz_choice:
        show_quiz_diagnostic_complet()

def show_quiz_debutant():
    st.write("**🟢 Quiz Débutant - Fondamentaux de l'Analyse Financière**")
    
    questions = [
        {
            "question": "Qu'est-ce que le bilan comptable?",
            "options": [
                "Un document qui mesure la performance sur une période",
                "Une photographie du patrimoine à une date donnée", 
                "Un tableau des flux de trésorerie",
                "Un document fiscal"
            ],
            "reponse": 1,
            "explication": "Le bilan est une photographie du patrimoine de l'entreprise à une date donnée, montrant ce qu'elle possède (actif) et ce qu'elle doit (passif)."
        },
        {
            "question": "Que signifie l'acronyme EBE?",
            "options": [
                "Excédent Brut d'Exploitation",
                "Élément de Base Économique", 
                "Excédent Budgétaire d'Entreprise",
                "Équilibre Bancaire d'Exploitation"
            ],
            "reponse": 0,
            "explication": "L'EBE (Excédent Brut d'Exploitation) mesure la performance économique de l'entreprise avant prise en compte de sa politique financière et de ses investissements."
        },
        {
            "question": "Quelle est l'équation fondamentale du bilan?",
            "options": [
                "Actif = Passif",
                "Produits = Charges", 
                "Résultat = Produits - Charges",
                "CAF = Résultat net + Dotations"
            ],
            "reponse": 0,
            "explication": "L'équation fondamentale du bilan est Actif = Passif. Cette équation doit toujours être respectée."
        },
        {
            "question": "Que mesure le compte de résultat?",
            "options": [
                "Le patrimoine de l'entreprise",
                "La performance sur une période", 
                "Les flux de trésorerie",
                "Les investissements"
            ],
            "reponse": 1,
            "explication": "Le compte de résultat mesure la performance économique de l'entreprise sur une période donnée (généralement un an)."
        },
        {
            "question": "Qu'est-ce que le FRNG?",
            "options": [
                "Fonds de Roulement Net Global",
                "Frais de Rénovation Non Garantis", 
                "Fonds de Réserve Net Garanti",
                "Financement de Réseau National Global"
            ],
            "reponse": 0,
            "explication": "Le FRNG (Fonds de Roulement Net Global) représente l'excédent des ressources stables après financement des emplois stables."
        }
    ]
    
    return generer_quiz(questions, "Débutant")

def show_quiz_bilan_complet():
    st.write("**🟡 Quiz Intermédiaire - Analyse du Bilan**")
    
    questions = [
        {
            "question": "Quelle est la différence entre l'actif circulant et l'actif immobilisé?",
            "options": [
                "L'actif circulant est à long terme, l'actif immobilisé à court terme",
                "L'actif immobilisé est destiné à être conservé, l'actif circulant à être transformé en liquidités", 
                "Il n'y a pas de différence",
                "L'actif circulant concerne les dettes, l'actif immobilisé les créances"
            ],
            "reponse": 1,
            "explication": "L'actif immobilisé est destiné à être conservé durablement, tandis que l'actif circulant est destiné à être transformé en liquidités dans le cycle d'exploitation."
        },
        {
            "question": "Que signifie un FRNG négatif?",
            "options": [
                "Une situation financière excellente",
                "Un besoin de financement à long terme", 
                "Une trésorerie excédentaire",
                "Un résultat net positif"
            ],
            "reponse": 1,
            "explication": "Un FRNG négatif indique que les ressources stables ne suffisent pas à financer les emplois stables, créant un besoin de financement à long terme."
        },
        {
            "question": "Comment calcule-t-on l'autonomie financière?",
            "options": [
                "Capitaux propres / Total du bilan",
                "Dettes / Capitaux propres", 
                "Actif circulant / Passif circulant",
                "Résultat net / Chiffre d'affaires"
            ],
            "reponse": 0,
            "explication": "L'autonomie financière se calcule par le ratio : Capitaux propres / Total du bilan. Elle mesure l'indépendance financière de l'entreprise."
        },
        {
            "question": "Qu'est-ce que le BFR (Besoin en Fonds de Roulement)?",
            "options": [
                "Le besoin de financement du cycle d'exploitation",
                "Le fonds de réserve pour les investissements", 
                "Le budget de fonctionnement annuel",
                "Le bénéfice avant répartition"
            ],
            "reponse": 0,
            "explication": "Le BFR représente le besoin de financement généré par le décalage entre les décaissements et les encaissements du cycle d'exploitation."
        },
        {
            "question": "Quelle est la relation entre FRNG, BFR et Trésorerie?",
            "options": [
                "FRNG = BFR + Trésorerie",
                "Trésorerie = FRNG - BFR", 
                "BFR = FRNG × Trésorerie",
                "FRNG = BFR - Trésorerie"
            ],
            "reponse": 1,
            "explication": "La relation fondamentale est : Trésorerie = FRNG - BFR. Elle montre comment l'équilibre financier se traduit en trésorerie."
        }
    ]
    
    return generer_quiz(questions, "Bilan")

def show_quiz_cr_complet():
    st.write("**🟠 Quiz Avancé - Compte de Résultat et SIG**")
    
    questions = [
        {
            "question": "Quel est l'ordre correct des Soldes Intermédiaires de Gestion?",
            "options": [
                "EBE → Valeur ajoutée → Marge commerciale → Résultat d'exploitation",
                "Marge commerciale → Valeur ajoutée → EBE → Résultat d'exploitation", 
                "Résultat d'exploitation → EBE → Valeur ajoutée → Marge commerciale",
                "Valeur ajoutée → Marge commerciale → EBE → Résultat d'exploitation"
            ],
            "reponse": 1,
            "explication": "L'ordre correct est : Marge commerciale → Valeur ajoutée → EBE → Résultat d'exploitation → Résultat courant → Résultat net."
        },
        {
            "question": "Comment calcule-t-on la capacité d'autofinancement (CAF)?",
            "options": [
                "CAF = Résultat net + Dotations - Reprises",
                "CAF = Chiffre d'affaires - Charges", 
                "CAF = EBE - Charges financières",
                "CAF = Résultat net × 2"
            ],
            "reponse": 0,
            "explication": "La CAF se calcule par la méthode additive : CAF = Résultat net + Dotations aux amortissements et provisions - Reprises sur amortissements et provisions ± Valeur nette comptable des éléments cédés."
        },
        {
            "question": "Que mesure la valeur ajoutée?",
            "options": [
                "La richesse créée par l'entreprise",
                "Le bénéfice net", 
                "La trésorerie disponible",
                "Les investissements réalisés"
            ],
            "reponse": 0,
            "explication": "La valeur ajoutée mesure la richesse créée par l'entreprise grâce à son activité. Elle se calcule : Production de l'exercice + Marge commerciale - Consommations de l'exercice."
        },
        {
            "question": "Quelle est la différence entre résultat d'exploitation et résultat courant?",
            "options": [
                "Le résultat courant inclut les éléments financiers",
                "Le résultat d'exploitation inclut les éléments exceptionnels", 
                "Il n'y a pas de différence",
                "Le résultat courant est avant impôts"
            ],
            "reponse": 0,
            "explication": "Le résultat d'exploitation mesure la performance de l'activité courante, tandis que le résultat courant inclut en plus les éléments financiers."
        },
        {
            "question": "Qu'est-ce que le seuil de rentabilité?",
            "options": [
                "Le niveau d'activité où le résultat est nul",
                "Le montant maximum de perte acceptable", 
                "Le taux de marge minimum",
                "Le chiffre d'affaires de l'année précédente"
            ],
            "reponse": 0,
            "explication": "Le seuil de rentabilité est le niveau de chiffre d'affaires pour lequel l'entreprise couvre l'ensemble de ses charges (fixes et variables) sans dégager ni bénéfice ni perte."
        }
    ]
    
    return generer_quiz(questions, "Compte de résultat")

def show_quiz_ratios_complet():
    st.write("**🔴 Quiz Expert - Ratios Financiers**")
    
    questions = [
        {
            "question": "Quel ratio mesure la rentabilité des capitaux investis par les actionnaires?",
            "options": [
                "Rentabilité économique",
                "Rentabilité financière", 
                "Taux de marge nette",
                "Rotation de l'actif"
            ],
            "reponse": 1,
            "explication": "La rentabilité financière (Résultat net / Capitaux propres) mesure la rentabilité des capitaux investis par les actionnaires."
        },
        {
            "question": "Un ratio de liquidité générale de 0,8 indique:",
            "options": [
                "Une excellente liquidité",
                "Un risque de liquidité", 
                "Une situation normale",
                "Une trésorerie excédentaire"
            ],
            "reponse": 1,
            "explication": "Un ratio de liquidité générale inférieur à 1 indique que l'actif circulant ne couvre pas les dettes à court terme, ce qui présente un risque de liquidité."
        },
        {
            "question": "Comment calcule-t-on le délai de rotation des clients?",
            "options": [
                "(Clients / Chiffre d'affaires TTC) × 360",
                "(Stocks / Achats) × 360", 
                "(Fournisseurs / Achats TTC) × 360",
                "(CA / Actif total) × 360"
            ],
            "reponse": 0,
            "explication": "Le délai de rotation des clients se calcule : (Clients moyens / Chiffre d'affaires TTC) × 360. Il mesure le temps moyen de recouvrement des créances."
        },
        {
            "question": "Qu'est-ce que l'effet de levier financier?",
            "options": [
                "L'impact de l'endettement sur la rentabilité financière",
                "La capacité à négocier avec les banques", 
                "Le ratio de liquidité immédiate",
                "La rotation du BFR"
            ],
            "reponse": 0,
            "explication": "L'effet de levier financier mesure l'impact de l'endettement sur la rentabilité financière. Il est positif quand le coût de la dette est inférieur à la rentabilité économique."
        },
        {
            "question": "Quel ratio mesure la capacité à rembourser les dettes?",
            "options": [
                "Ratio d'endettement",
                "Capacité de remboursement", 
                "Liquidité réduite",
                "Autonomie financière"
            ],
            "reponse": 1,
            "explication": "La capacité de remboursement (Dettes financières / CAF) mesure la capacité de l'entreprise à rembourser ses dettes avec sa capacité d'autofinancement."
        }
    ]
    
    return generer_quiz(questions, "Ratios")

def show_quiz_diagnostic_complet():
    st.write("**🏆 Quiz Master - Diagnostic Financier Global**")
    
    questions = [
        {
            "question": "Quelle est la séquence correcte d'un diagnostic financier complet?",
            "options": [
                "Ratios → Bilan → Diagnostic",
                "Collecte → Analyse → Diagnostic → Recommandations", 
                "Recommandations → Diagnostic → Analyse",
                "Bilan → Compte de résultat → Ratios"
            ],
            "reponse": 1,
            "explication": "La séquence méthodologique est : Collecte des informations → Analyse financière → Diagnostic → Recommandations."
        },
        {
            "question": "Que signifie une situation de 'surfinancement'?",
            "options": [
                "FRNG positif + BFR négatif + Trésorerie positive",
                "FRNG négatif + BFR positif + Trésorerie négative", 
                "FRNG positif + BFR positif + Trésorerie négative",
                "FRNG négatif + BFR négatif + Trésorerie positive"
            ],
            "reponse": 0,
            "explication": "Une situation de surfinancement (FRNG positif + BFR négatif + Trésorerie positive) indique des ressources stables excédentaires par rapport aux besoins."
        },
        {
            "question": "Qu'est-ce que l'analyse dynamique?",
            "options": [
                "L'étude de l'évolution dans le temps",
                "L'analyse de la structure à une date donnée", 
                "Le calcul des ratios de liquidité",
                "L'étude de la rentabilité"
            ],
            "reponse": 0,
            "explication": "L'analyse dynamique étudie l'évolution des états financiers dans le temps, contrairement à l'analyse statique qui se limite à une date donnée."
        },
        {
            "question": "Quel indicateur est le plus important pour évaluer la santé financière à long terme?",
            "options": [
                "La trésorerie immédiate",
                "L'équilibre financier structurel", 
                "Le résultat net de l'exercice",
                "Le chiffre d'affaires"
            ],
            "reponse": 1,
            "explication": "L'équilibre financier structurel (FRNG positif) est le plus important pour la santé financière à long terme, car il garantit la pérennité de l'entreprise."
        },
        {
            "question": "Que faut-il vérifier en priorité dans un diagnostic financier?",
            "options": [
                "La cohérence globale de la situation financière",
                "Un seul ratio particulier", 
                "Seulement le résultat net",
                "Uniquement la trésorerie"
            ],
            "reponse": 0,
            "explication": "Il faut vérifier la cohérence globale de la situation financière en croisant tous les indicateurs (rentabilité, équilibre, liquidité) plutôt que de se focaliser sur un seul élément."
        }
    ]
    
    return generer_quiz(questions, "Diagnostic global")

def generer_quiz(questions, niveau):
    score = 0
    reponses_utilisateur = []
    
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        reponse = st.radio(f"Choisissez votre réponse:", q['options'], key=f"quiz_{niveau}_{i}")
        reponses_utilisateur.append(reponse)
        
        if st.button(f"Vérifier question {i+1}", key=f"btn_{niveau}_{i}"):
            if q['options'].index(reponse) == q['reponse']:
                st.success("✅ Bonne réponse!")
                score += 1
            else:
                st.error(f"❌ Mauvaise réponse")
            st.info(f"**Explication :** {q['explication']}")
    
    if st.button(f"🎯 Voir le score final - {niveau}", key=f"final_{niveau}"):
        st.info(f"**Score: {score}/{len(questions)}**")
        
        if score == len(questions):
            st.balloons()
            st.success(f"🎉 Excellent! Maîtrise parfaite du {niveau}!")
        elif score >= len(questions) * 0.7:
            st.warning(f"📚 Très bien! Bonne connaissance du {niveau}")
        elif score >= len(questions) * 0.5:
            st.warning(f"📖 Correct! Continuez à progresser en {niveau}")
        else:
            st.error(f"🔴 À revoir! Retravaillez le {niveau}")
        
        # Recommandations de progression
        if score < len(questions):
            st.subheader("📚 Conseils pour Progresser")
            if niveau == "Débutant":
                st.write("• Revoyez les concepts fondamentaux du bilan et compte de résultat")
                st.write("• Pratiquez avec les calculateurs interactifs")
                st.write("• Téléchargez les fiches mémo")
            elif niveau == "Bilan":
                st.write("• Étudiez la structure actif/passif")
                st.write("• Travaillez sur l'équilibre financier (FRNG, BFR, Trésorerie)")
                st.write("• Utilisez l'analyse personnalisée du bilan")
            elif niveau == "Compte de résultat":
                st.write("• Maîtrisez les soldes intermédiaires de gestion")
                st.write("• Comprenez le calcul de la capacité d'autofinancement")
                st.write("• Analysez des comptes de résultat réels")
            elif niveau == "Ratios":
                st.write("• Apprenez la classification des ratios")
                st.write("• Pratiquez l'interprétation des résultats")
                st.write("• Comparez avec les normes sectorielles")
            elif niveau == "Diagnostic global":
                st.write("• Développez une vision synthétique")
                st.write("• Croisez les différents types d'analyse")
                st.write("• Entraînez-vous sur des cas concrets")
    
if __name__ == "__main__":
    main()