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
</style>
""", unsafe_allow_html=True)

def main():
    # Header principal
    st.markdown('<h1 class="main-header">📊 Maîtrise de l\'Analyse Financière</h1>', unsafe_allow_html=True)
    
    # Navigation par onglets
    tabs = st.tabs([
        "🏠 Accueil",
        "📈 Concepts Fondamentaux",
        "🧮 Calculateurs",
        "💼 Études de Cas",
        "📚 Ressources"
    ])
    
    with tabs[0]:
        show_accueil()
    
    with tabs[1]:
        show_concepts_fondamentaux()
    
    with tabs[2]:
        show_calculateurs()
    
    with tabs[3]:
        show_etudes_cas()
    
    with tabs[4]:
        show_ressources()

def show_accueil():
    st.markdown('<h2 class="section-header">Bienvenue dans l\'application d\'analyse financière</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        Cette application vous permet de maîtriser tous les aspects de l'analyse financière d'entreprise 
        à travers des concepts théoriques, des calculateurs interactifs et des études de cas pratiques.
        
        ### Objectifs pédagogiques :
        - Comprendre les principes fondamentaux de la gestion financière
        - Maîtriser les outils d'analyse financière
        - Apprendre à interpréter les états financiers
        - Développer des compétences en diagnostic financier
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400", caption="Analyse Financière")
    
    # Statistiques d'apprentissage
    st.subheader("🎯 Progression recommandée")
    
    progress_data = {
        "Module": ["Fondamentaux", "Bilan & Compte de résultat", "Ratios & SIG", "Analyse fonctionnelle", "Tableaux de flux", "Diagnostic avancé"],
        "Durée estimée": ["2 semaines", "3 semaines", "2 semaines", "2 semaines", "3 semaines", "2 semaines"],
        "Difficulté": ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]
    }
    
    df_progress = pd.DataFrame(progress_data)
    st.dataframe(df_progress, use_container_width=True)

def show_concepts_fondamentaux():
    st.markdown('<h2 class="section-header">Concepts Fondamentaux</h2>', unsafe_allow_html=True)
    
    concept_choice = st.selectbox(
        "Choisissez un concept à explorer :",
        [
            "Diagnostic Financier",
            "Bilan Comptable", 
            "Compte de Résultat",
            "Soldes Intermédiaires de Gestion",
            "Seuil de Rentabilité",
            "Fonds de Roulement",
            "Ratios Financiers"
        ]
    )
    
    if concept_choice == "Diagnostic Financier":
        show_diagnostic_financier()
    elif concept_choice == "Bilan Comptable":
        show_bilan_comptable()
    elif concept_choice == "Compte de Résultat":
        show_compte_resultat()
    elif concept_choice == "Soldes Intermédiaires de Gestion":
        show_soldes_gestion()
    elif concept_choice == "Seuil de Rentabilité":
        show_seuil_rentabilite()
    elif concept_choice == "Fonds de Roulement":
        show_fonds_roulement()
    elif concept_choice == "Ratios Financiers":
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
        **Définition :**
        Le diagnostic financier est une démarche qui vise à :
        - Identifier les causes de difficultés présentes ou futures
        - Mettre en lumière les dysfonctionnements
        - Présenter les perspectives d'évolution
        - Proposer des actions correctives
        
        **États financiers analysés :**
        - Bilan (patrimoine à une date donnée)
        - Compte de résultat (performance sur une période)
        - Annexe (informations complémentaires)
        """)
    
    with col2:
        st.write("""
        **Méthodologie :**
        1. Analyse de la rentabilité
        2. Analyse de la liquidité
        3. Analyse de la structure financière
        4. Analyse économique complémentaire
        
        **Outils :**
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
    **Définition :** Photographie du patrimoine de l'entreprise à une date donnée.
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
    st.subheader("🧮 Calculateur de Bilan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Actif**")
        immob_corporelles = st.number_input("Immobilisations corporelles", value=500000)
        stocks = st.number_input("Stocks", value=200000)
        clients = st.number_input("Créances clients", value=300000)
        disponibilites = st.number_input("Disponibilités", value=100000)
        
        total_actif = immob_corporelles + stocks + clients + disponibilites
        
    with col2:
        st.write("**Passif**")
        capital = st.number_input("Capital social", value=400000)
        reserves = st.number_input("Réserves", value=300000)
        resultat = st.number_input("Résultat", value=100000)
        emprunts = st.number_input("Emprunts", value=200000)
        fournisseurs = st.number_input("Dettes fournisseurs", value=100000)
        
        total_passif = capital + reserves + resultat + emprunts + fournisseurs
    
    # Vérification équilibre
    if abs(total_actif - total_passif) > 1:
        st.error(f"⚠️ Le bilan n'est pas équilibré ! Actif: {total_actif:,.0f} € vs Passif: {total_passif:,.0f} €")
    else:
        st.success(f"✅ Bilan équilibré : {total_actif:,.0f} €")

def show_compte_resultat():
    st.markdown("""
    <div class="concept-card">
    <h3>📊 Compte de Résultat</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Définition :** Mesure la performance économique sur une période (généralement un an).
    """)
    
    # Structure du compte de résultat
    st.subheader("Structure du Compte de Résultat")
    
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
    st.subheader("🧮 Calculateur de Résultat")
    
    ca = st.number_input("Chiffre d'affaires HT (€)", value=1000000)
    achats = st.number_input("Achats consommés (€)", value=400000)
    charges_personnel = st.number_input("Charges de personnel (€)", value=300000)
    dotations_amort = st.number_input("Dotations aux amortissements (€)", value=50000)
    charges_financieres = st.number_input("Charges financières (€)", value=20000)
    
    resultat_exploitation = ca - achats - charges_personnel - dotations_amort
    resultat_courant = resultat_exploitation - charges_financieres
    
    st.metric("Résultat d'Exploitation", f"{resultat_exploitation:,.0f} €")
    st.metric("Résultat Courant", f"{resultat_courant:,.0f} €")

def show_soldes_gestion():
    st.markdown("""
    <div class="concept-card">
    <h3>📈 Soldes Intermédiaires de Gestion</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Les SIG permettent de décomposer la formation du résultat en plusieurs niveaux.")
    
    # Calculateur des SIG
    st.subheader("Calculateur des SIG")
    
    ca = st.number_input("Chiffre d'affaires", value=1000000, key="sig_ca")
    achats_marches = st.number_input("Achats de marchandises", value=300000)
    prod_vendue = st.number_input("Production vendue", value=800000)
    consommations = st.number_input("Consommations externes", value=200000)
    charges_personnel = st.number_input("Charges de personnel", value=350000, key="sig_personnel")
    
    # Calcul des SIG
    marge_commerciale = ca - achats_marches
    valeur_ajoutee = marge_commerciale + prod_vendue - consommations
    ebe = valeur_ajoutee - charges_personnel
    
    # Affichage des résultats
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
    **Définition :** Niveau de chiffre d'affaires pour lequel le résultat est nul.
    
    **Formule :** SR = Charges Fixes / Taux de Marge sur Coût Variable
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
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Taux MCV", f"{taux_mcv*100:.1f} %")
    
    with col2:
        st.metric("Seuil Rentabilité", f"{seuil_rentabilite:,.0f} €")
    
    with col3:
        st.metric("Marge de Sécurité", f"{marge_securite:.1f} %")
    
    # Graphique
    if seuil_rentabilite > 0:
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
    **FRNG = Ressources Stables - Emplois Stables**
    **BFR = Actif Circulant - Passif Circulant**
    **Trésorerie = FRNG - BFR**
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
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("FRNG", f"{frng:,.0f} €", delta="✅ Bon" if frng > 0 else "❌ Risque")
    
    with col2:
        st.metric("BFR", f"{bfr:,.0f} €", delta="📈 Besoin" if bfr > 0 else "📉 Ressource")
    
    with col3:
        st.metric("Trésorerie", f"{tresorerie:,.0f} €", delta="✅ Excédent" if tresorerie > 0 else "❌ Déficit")

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
    st.subheader("📊 Résultats des Ratios")
    
    ratios_data = {
        "Ratio": ["Rentabilité nette", "Rentabilité financière", "Rentabilité économique", "Taux d'endettement", "Ratio de liquidité"],
        "Valeur": [f"{rentabilite_net:.1f}%", f"{rentabilite_financiere:.1f}%", f"{rentabilite_economique:.1f}%", f"{endettement:.1f}%", f"{liquidite:.1f}%"],
        "Interprétation": [
            "> 2% bon" if rentabilite_net > 2 else "À améliorer",
            "> 8% bon" if rentabilite_financiere > 8 else "À améliorer", 
            "> 10% bon" if rentabilite_economique > 10 else "À améliorer",
            "< 100% bon" if endettement < 100 else "Trop élevé",
            "> 100% bon" if liquidite > 100 else "Risque liquidité"
        ]
    }
    
    df_ratios = pd.DataFrame(ratios_data)
    st.dataframe(df_ratios, use_container_width=True)

def show_calculateurs():
    st.markdown('<h2 class="section-header">Calculateurs Interactifs</h2>', unsafe_allow_html=True)
    
    calc_choice = st.selectbox(
        "Choisissez un calculateur :",
        [
            "Amortissements",
            "Capacité d'Autofinancement", 
            "Effet de Levier",
            "VAN et TIR",
            "Score Financier"
        ]
    )
    
    if calc_choice == "Amortissements":
        show_calculateur_amortissements()
    elif calc_choice == "Capacité d'Autofinancement":
        show_calculateur_caf()
    elif calc_choice == "Effet de Levier":
        show_calculateur_levier()
    elif calc_choice == "VAN et TIR":
        show_calculateur_van_tir()
    elif calc_choice == "Score Financier":
        show_calculateur_score()

def show_calculateur_amortissements():
    st.subheader("📉 Calculateur d'Amortissements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        valeur_origine = st.number_input("Valeur d'origine (€)", value=100000)
        duree = st.number_input("Durée d'amortissement (années)", value=5, min_value=1)
        mode = st.radio("Mode d'amortissement", ["Linéaire", "Dégressif"])
    
    with col2:
        date_acquisition = st.date_input("Date d'acquisition", value=datetime(2023, 1, 1))
        coefficient = st.selectbox("Coefficient dégressif", [1.25, 1.75, 2.25]) if mode == "Dégressif" else 0
    
    # Calcul du plan d'amortissement
    if st.button("Calculer le plan d'amortissement"):
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

def show_calculateur_caf():
    st.subheader("💸 Calculateur de Capacité d'Autofinancement")
    
    st.write("**Méthode additive : CAF = Résultat net + Dotations - Reprises - Produits de cession**")
    
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

def show_calculateur_levier():
    st.subheader("⚖️ Calculateur d'Effet de Levier Financier")
    
    col1, col2 = st.columns(2)
    
    with col1:
        actif_economique = st.number_input("Actif économique (€)", value=1000000)
        resultat_exploitation = st.number_input("Résultat d'exploitation (€)", value=120000)
        capitaux_propres = st.number_input("Capitaux propres (€)", value=600000)
    
    with col2:
        dettes_financieres = st.number_input("Dettes financières (€)", value=400000)
        taux_impot = st.number_input("Taux d'impôt (%)", value=25.0) / 100
        taux_interet = st.number_input("Taux d'intérêt (%)", value=4.0) / 100
    
    # Calculs
    re_apres_impot = resultat_exploitation * (1 - taux_impot)
    rentabilite_economique = re_apres_impot / actif_economique
    
    charges_financieres = dettes_financieres * taux_interet
    cf_apres_impot = charges_financieres * (1 - taux_impot)
    
    resultat_net = re_apres_impot - cf_apres_impot
    rentabilite_financiere = resultat_net / capitaux_propres
    
    effet_levier = rentabilite_financiere - rentabilite_economique
    
    # Affichage
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Rentabilité économique", f"{rentabilite_economique*100:.1f}%")
    
    with col2:
        st.metric("Rentabilité financière", f"{rentabilite_financiere*100:.1f}%")
    
    with col3:
        st.metric("Effet de levier", f"{effet_levier*100:.1f}%", 
                 delta="✅ Positif" if effet_levier > 0 else "❌ Négatif")

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
    
    if st.button("Calculer VAN et TIR"):
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
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("VAN", f"{van:,.0f} €", delta="✅ Projet rentable" if van > 0 else "❌ Projet non rentable")
        with col2:
            st.metric("TIR approximatif", f"{tir*100:.1f}%")

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
        st.error("❌ Situation risquée")

def show_etudes_cas():
    st.markdown('<h2 class="section-header">Études de Cas Pratiques</h2>', unsafe_allow_html=True)
    
    cas_choice = st.selectbox(
        "Choisissez une étude de cas :",
        [
            "Diagnostic PME industrielle",
            "Analyur de rentabilité", 
            "Équilibre financier",
            "Tableau de flux",
            "Projet d'investissement"
        ]
    )
    
    if cas_choice == "Diagnostic PME industrielle":
        show_cas_pme()
    elif cas_choice == "Analyse de rentabilité":
        show_cas_rentabilite()
    elif cas_choice == "Équilibre financier":
        show_cas_equilibre()
    elif cas_choice == "Tableau de flux":
        show_cas_flux()
    elif cas_choice == "Projet d'investissement":
        show_cas_investissement()

def show_cas_pme():
    st.subheader("🏭 Diagnostic d'une PME Industrielle")
    
    st.write("""
    **Contexte :** Société DUBOIS, fabricant de composants électroniques
    - Chiffre d'affaires : 2,5 M€
    - Effectif : 45 personnes
    - Marché en croissance mais concurrence forte
    """)
    
    # Données financières
    st.subheader("📋 Données financières")
    
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
        "Sélectionnez l'analyse à effectuer :",
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
    **Calcul des ratios de rentabilité :**
    
    1. Taux de marge commerciale = Marge commerciale / CA
    2. Taux de valeur ajoutée = VA / CA  
    3. Taux d'EBE = EBE / CA
    4. Rentabilité économique = RE / Actif économique
    5. Rentabilité financière = RN / Capitaux propres
    """)
    
    # Réponse guidée
    with st.expander("📝 Réponse détaillée"):
        st.write("""
        **Calculs :**
        - Taux de marge : 52% (N) vs 50% (N-1) → Amélioration
        - Taux EBE : 20% (N) vs 17.4% (N-1) → Bonne progression
        - Rentabilité économique : 8.7% → Correcte
        - Rentabilité financière : 12.5% → Bonne
        
        **Conclusion :** Rentabilité en amélioration, bonne performance économique.
        """)

def show_analyse_structure_cas():
    st.write("""
    **Analyse de la structure financière :**
    
    - FRNG = Ressources stables - Emplois stables
    - BFR = Actif circulant - Passif circulant  
    - Taux d'endettement = Dettes financières / Capitaux propres
    - Autonomie financière = Capitaux propres / Total passif
    """)
    
    with st.expander("📝 Réponse détaillée"):
        st.write("""
        **Calculs :**
        - FRNG = 1,200 + 800 - 1,800 = 200 k€ → Positif
        - BFR = (450 + 600) - 1,000 = 50 k€ → Faible besoin
        - Taux d'endettement = 800/1,200 = 67% → Acceptable
        - Autonomie = 1,200/3,000 = 40% → Correct
        
        **Conclusion :** Structure financière équilibrée.
        """)

def show_analyse_liquidite_cas():
    st.write("""
    **Analyse de la liquidité :**
    
    - Ratio de liquidité générale = Actif circulant / Dettes CT
    - Ratio de liquidité réduite = (Actif circulant - Stocks) / Dettes CT  
    - Ratio de liquidité immédiate = Disponibilités / Dettes CT
    - Trésorerie nette = FRNG - BFR
    """)
    
    with st.expander("📝 Réponse détaillée"):
        st.write("""
        **Calculs :**
        - Liquidité générale = 1,200/1,000 = 1.2 → Correct
        - Liquidité réduite = 750/1,000 = 0.75 → À surveiller
        - Trésorerie nette = 200 - 50 = 150 k€ → Excédentaire
        
        **Conclusion :** Liquidité globalement satisfaisante.
        """)

def show_diagnostic_global_cas():
    st.write("""
    **Diagnostic global :**
    
    **Points forts :**
    ✅ Rentabilité en amélioration
    ✅ Structure financière équilibrée  
    ✅ Trésorerie excédentaire
    ✅ Croissance du CA
    
    **Points de vigilance :**
    ⚠️ Liquidité réduite un peu faible
    ⚠️ BFR à surveiller
    ⚠️ Investissements importants
    
    **Recommandations :**
    📈 Optimiser la gestion du BFR
    📈 Renforcer la trésorerie
    📈 Poursuivre les investissements maîtrisés
    """)

def show_cas_rentabilite():
    st.subheader("📈 Analyse de Rentabilité - Cas PRATIQUE")
    # Implémenter un cas pratique complet d'analyse de rentabilité
    pass

def show_cas_equilibre():
    st.subheader("⚖️ Équilibre Financier - Cas CONCRET")
    # Implémenter un cas pratique d'analyse d'équilibre financier
    pass

def show_cas_flux():
    st.subheader("💧 Tableaux de Flux - Cas APPLICATIF")
    # Implémenter un cas pratique de construction de tableaux de flux
    pass

def show_cas_investissement():
    st.subheader("🏗️ Projet d'Investissement - Cas DÉCISIONNEL")
    # Implémenter un cas pratique d'évaluation de projet d'investissement
    pass

def show_ressources():
    st.markdown('<h2 class="section-header">Ressources Pédagogiques</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📖 Fiches Mémo")
        
        ressources = {
            "Bilan": "Structure actif/passif, équilibre, analyse",
            "Compte de résultat": "Soldes, SIG, rentabilité", 
            "Ratios financiers": "Calcul, interprétation, normes",
            "Tableaux de flux": "Construction, analyse, OEC vs CDB",
            "Diagnostic financier": "Méthodologie, outils, reporting"
        }
        
        for ressource, description in ressources.items():
            with st.expander(f"📄 {ressource}"):
                st.write(description)
                st.download_button(
                    f"Télécharger fiche {ressource}",
                    f"Contenu de la fiche {ressource}",
                    file_name=f"fiche_{ressource.lower().replace(' ', '_')}.txt"
                )
    
    with col2:
        st.subheader("🎓 Quiz d'auto-évaluation")
        
        quiz_choice = st.selectbox(
            "Choisissez un quiz :",
            ["Fondamentaux", "Bilan", "Compte de résultat", "Ratios", "Expert"]
        )
        
        if quiz_choice == "Fondamentaux":
            show_quiz_fondamentaux()
        elif quiz_choice == "Bilan":
            show_quiz_bilan()
        # Ajouter les autres quiz...
    
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
    st.write("Testez vos connaissances sur les fondamentaux de l'analyse financière")
    
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
    
    if st.button("Voir le score final"):
        st.info(f"Score: {score}/{len(questions)}")
        if score == len(questions):
            st.balloons()

def show_quiz_bilan():
    st.write("Quiz sur le bilan comptable")
    # Implémenter le quiz sur le bilan
    pass

if __name__ == "__main__":
    main()