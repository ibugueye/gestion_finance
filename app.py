import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Configuration de la page
st.set_page_config(
    page_title="FinanceLab - Analyse Financière",
    page_icon="📊",
    layout="wide"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .concept-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown('<h1 class="main-header">🎯 FinanceLab - Maîtrisez l\'Analyse Financière</h1>', unsafe_allow_html=True)

# Sidebar pour la navigation
st.sidebar.title("📚 Modules d'Apprentissage")
section = st.sidebar.radio(
    "Choisissez un module:",
    ["🏠 Accueil", "📋 Fondamentaux", "💰 Performance", "⚖️ Équilibre Financier", "🎯 Évaluation d'Entreprise"]
)

if section == "📋 Fondamentaux":
    st.header("📋 Les Fondamentaux de l'Information Financière")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Principes Comptables", "🏦 Le Bilan", "📈 Compte de Résultat", "🧮 Soldes Intermédiaires"])
    
    with tab1:
        st.subheader("Les 10 Principes Comptables Fondamentaux")
        
        principles = {
            "Principe de prudence": "Anticiper les pertes, ne pas anticiper les gains",
            "Continuité d'exploitation": "L'entreprise continue son activité",
            "Coût historique": "Évaluation au prix d'acquisition",
            "Indépendance des exercices": "Rattacher charges et produits à la bonne période",
            "Permanence des méthodes": "Application constante des règles dans le temps",
            "Non-compensation": "Ne pas compenser actif/passif ou charges/produits",
            "Image fidèle": "Les comptes doivent refléter la réalité économique",
            "Primauté de la réalité économique": "La substance prime sur la forme",
            "Spécialisation des exercices": "Chaque exercice a sa propre détermination du résultat",
            "Juste valeur": "Évaluation à la valeur de marché quand elle est disponible"
        }
        
        col1, col2 = st.columns(2)
        with col1:
            for principle, description in list(principles.items())[:5]:
                with st.expander(f"✅ {principle}"):
                    st.write(description)
        
        with col2:
            for principle, description in list(principles.items())[5:]:
                with st.expander(f"✅ {principle}"):
                    st.write(description)
    
    with tab2:
        st.subheader("🔄 Reclassement du Bilan Interactif")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Bilan Comptable (Saisie)")
            
            # Actif
            st.markdown("**ACTIF**")
            immob_incorporelles = st.number_input("Immobilisations incorporelles", value=150000)
            immob_corporelles = st.number_input("Immobilisations corporelles", value=450000)
            immob_financieres = st.number_input("Immobilisations financières", value=200000)
            stocks = st.number_input("Stocks", value=120000)
            clients = st.number_input("Clients et comptes rattachés", value=180000)
            disponibilites = st.number_input("Disponibilités", value=50000)
            
            # Passif
            st.markdown("**PASSIF**")
            capital = st.number_input("Capital social", value=300000)
            reserves = st.number_input("Réserves", value=200000)
            resultat = st.number_input("Résultat de l'exercice", value=50000)
            emprunts_longs = st.number_input("Emprunts à long terme", value=250000)
            fournisseurs = st.number_input("Fournisseurs", value=150000)
            dettes_fiscales = st.number_input("Dettes fiscales et sociales", value=100000)
        
        with col2:
            st.markdown("#### Bilan Financier Reclassé")
            
            # Calculs pour le bilan financier
            actif_immobilise = immob_incorporelles + immob_corporelles + immob_financieres
            actif_circulant = stocks + clients
            tresorerie_actif = disponibilites
            
            capitaux_propres = capital + reserves + resultat
            dettes_financieres = emprunts_longs
            passif_circulant = fournisseurs + dettes_fiscales
            
            # Affichage du bilan financier
            st.markdown("**ACTIF**")
            st.write(f"Actif immobilisé: {actif_immobilise:,.0f} €")
            st.write(f"Actif circulant: {actif_circulant:,.0f} €")
            st.write(f"Trésorerie active: {tresorerie_actif:,.0f} €")
            st.write(f"**Total Actif: {actif_immobilise + actif_circulant + tresorerie_actif:,.0f} €**")
            
            st.markdown("**PASSIF**")
            st.write(f"Capitaux propres: {capitaux_propres:,.0f} €")
            st.write(f"Dettes financières: {dettes_financieres:,.0f} €")
            st.write(f"Passif circulant: {passif_circulant:,.0f} €")
            st.write(f"**Total Passif: {capitaux_propres + dettes_financieres + passif_circulant:,.0f} €**")
            
            # Vérification de l'équilibre
            total_actif = actif_immobilise + actif_circulant + tresorerie_actif
            total_passif = capitaux_propres + dettes_financieres + passif_circulant
            
            if abs(total_actif - total_passif) < 1:
                st.success("✅ Le bilan est équilibré !")
            else:
                st.error("❌ Le bilan n'est pas équilibré !")

elif section == "💰 Performance":
    st.header("💰 Diagnostic de la Performance et de la Rentabilité")
    
    tab1, tab2, tab3 = st.tabs(["📈 Création de Valeur (EVA)", "⚖️ Levier Financier", "🎯 Seuil de Rentabilité"])
    
    with tab1:
        st.subheader("📈 Simulateur de Création de Valeur (EVA)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            resultat_exploitation = st.slider("Résultat d'exploitation (k€)", 100, 5000, 1000, step=50)
            capital_investi = st.slider("Capital économique investi (k€)", 500, 20000, 5000, step=100)
            taux_imposition = st.slider("Taux d'imposition (%)", 15.0, 35.0, 25.0, step=0.5)
            cout_capital = st.slider("Coût du capital (%)", 5.0, 15.0, 8.0, step=0.5)
        
        with col2:
            # Calculs
            resultat_apres_impot = resultat_exploitation * (1 - taux_imposition/100)
            roic = (resultat_apres_impot / capital_investi) * 100
            eva = resultat_apres_impot - (capital_investi * cout_capital/100)
            
            # Affichage des résultats
            st.metric("Rentabilité (ROIC)", f"{roic:.1f}%")
            st.metric("Coût du Capital", f"{cout_capital:.1f}%")
            st.metric("Economic Value Added (EVA)", f"{eva:,.0f} k€")
            
            # Indicateur visuel
            if eva > 0:
                st.success("🎉 L'entreprise crée de la valeur !")
                st.balloons()
            else:
                st.error("⚠️ L'entreprise détruit de la valeur")
    
    with tab2:
        st.subheader("⚖️ Calculateur de Levier Financier")
        
        col1, col2 = st.columns(2)
        
        with col1:
            resultat_expl = st.number_input("Résultat d'exploitation (k€)", value=800)
            charges_financieres = st.number_input("Charges financières (k€)", value=100)
            capitaux_propres = st.number_input("Capitaux propres (k€)", value=2000)
            dette_financiere = st.number_input("Dettes financières (k€)", value=1000)
        
        with col2:
            # Calculs
            resultat_courant = resultat_expl - charges_financieres
            roe_avec_dette = (resultat_courant / capitaux_propres) * 100
            
            # Sans dette (pour comparaison)
            roe_sans_dette = (resultat_expl / (capitaux_propres + dette_financiere)) * 100
            
            # Effet de levier
            effet_levier = roe_avec_dette - roe_sans_dette
            
            st.metric("ROE avec endettement", f"{roe_avec_dette:.1f}%")
            st.metric("ROE sans endettement", f"{roe_sans_dette:.1f}%")
            st.metric("Effet de levier", f"{effet_levier:+.1f} points")
            
            if effet_levier > 0:
                st.success("✅ Le levier financier est positif")
            else:
                st.warning("📉 Le levier financier est négatif")
                
elif section == "⚖️ Équilibre Financier":
    st.header("⚖️ L'Équilibre Financier et la Trésorerie")
    
    st.subheader("🧊 Simulateur FR-BFR-TN")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Données d'entrée")
        capitaux_permanents = st.number_input("Capitaux permanents (k€)", value=800)
        actif_immobilise = st.number_input("Actif immobilisé (k€)", value=500)
        stocks = st.number_input("Stocks (k€)", value=150)
        clients = st.number_input("Créances clients (k€)", value=200)
        fournisseurs = st.number_input("Dettes fournisseurs (k€)", value=120)
    
    with col2:
        st.markdown("### Calculs")
        # Calcul des indicateurs
        fr = capitaux_permanents - actif_immobilise
        bfr = (stocks + clients) - fournisseurs
        tn = fr - bfr
        
        st.metric("Fonds de Roulement (FR)", f"{fr:,.0f} k€")
        st.metric("Besoin en Fonds de Roulement (BFR)", f"{bfr:,.0f} k€")
        st.metric("Trésorerie Nette (TN)", f"{tn:,.0f} k€")
    
    with col3:
        st.markdown("### Diagnostic")
        if tn > 0:
            st.success("""
            ✅ **Situation saine**
            - Trésorerie excédentaire
            - L'entreprise finance son BFR et dégage un excédent
            """)
        elif tn == 0:
            st.info("""
            ⚖️ **Situation équilibrée**
            - Le FR finance exactement le BFR
            - Trésorerie nulle
            """)
        else:
            st.error("""
            ❌ **Situation tendue**
            - Le FR ne couvre pas le BFR
            - Trésorerie négative → recours au découvert
            """)
    
    # Graphique de l'équilibre financier
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='FR',
        y=['Fonds de Roulement'],
        x=[fr],
        orientation='h',
        marker_color='green'
    ))
    
    fig.add_trace(go.Bar(
        name='BFR',
        y=['Besoin FR'],
        x=[bfr],
        orientation='h',
        marker_color='orange'
    ))
    
    fig.add_trace(go.Bar(
        name='TN',
        y=['Trésorerie Nette'],
        x=[tn],
        orientation='h',
        marker_color='blue'
    ))
    
    fig.update_layout(
        title="Représentation de l'Équilibre Financier",
        barmode='overlay',
        height=300
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
elif section == "🎯 Évaluation d'Entreprise":
    st.header("🎯 Évaluation d'Entreprise et Risque de Crédit")
    
    method = st.selectbox(
        "Choisissez la méthode d'évaluation:",
        ["Flux de Trésorerie Actualisés (DCF)", "Multiples de Marché", "Approche Patrimoniale"]
    )
    
    if method == "Flux de Trésorerie Actualisés (DCF)":
        st.subheader("💎 Calculateur DCF")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Hypothèses")
            fcf_actuel = st.number_input("Free Cash Flow actuel (k€)", value=500)
            croissance_5ans = st.slider("Croissance 5 premières années (%)", 1.0, 15.0, 5.0)
            croissance_perpetuite = st.slider("Croissance à perpétuité (%)", 0.0, 5.0, 2.0)
            wacc = st.slider("WACC (%)", 5.0, 15.0, 9.0)
        
        with col2:
            st.markdown("### Calcul de la Valeur")
            
            # Calcul DCF simplifié
            valeur_flux_explicites = 0
            fcf = fcf_actuel
            
            for annee in range(1, 6):
                fcf *= (1 + croissance_5ans/100)
                valeur_flux_explicites += fcf / ((1 + wacc/100) ** annee)
            
            # Valeur terminale
            fcf_annee5 = fcf_actuel * ((1 + croissance_5ans/100) ** 5)
            valeur_terminale = (fcf_annee5 * (1 + croissance_perpetuite/100)) / ((wacc/100) - (croissance_perpetuite/100))
            valeur_terminale_actualisee = valeur_terminale / ((1 + wacc/100) ** 5)
            
            valeur_entreprise = valeur_flux_explicites + valeur_terminale_actualisee
            
            st.metric("Valeur de l'entreprise", f"{valeur_entreprise:,.0f} k€")
            st.metric("Valeur des flux explicites", f"{valeur_flux_explicites:,.0f} k€")
            st.metric("Valeur terminale actualisée", f"{valeur_terminale_actualisee:,.0f} k€")
            
# Ajouter dans la navigation
# st.sidebar.radio(...) - ajouter "📊 Analyse par Ratios"

elif section == "📊 Analyse par Ratios":
    st.header("📊 Analyse Financière par les Ratios")
    
    tab1, tab2, tab3, tab4 = st.tabs(["💰 Rentabilité", "⚖️ Structure", "📈 Activité", "🧮 Liquidité"])
    
    with tab1:
        st.subheader("Ratios de Rentabilité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            ca = st.number_input("Chiffre d'affaires (k€)", value=2000)
            resultat_net = st.number_input("Résultat net (k€)", value=150)
            resultat_exploitation = st.number_input("Résultat d'exploitation (k€)", value=200)
            capitaux_propres = st.number_input("Capitaux propres (k€)", value=1000)
            actif_total = st.number_input("Actif total (k€)", value=2000)
        
        with col2:
            # Calcul des ratios
            roe = (resultat_net / capitaux_propres) * 100
            roa = (resultat_net / actif_total) * 100
            ros = (resultat_net / ca) * 100
            marge_ebit = (resultat_exploitation / ca) * 100
            
            st.metric("ROE (Return on Equity)", f"{roe:.1f}%")
            st.metric("ROA (Return on Assets)", f"{roa:.1f}%")
            st.metric("ROS (Return on Sales)", f"{ros:.1f}%")
            st.metric("Marge d'exploitation (EBIT)", f"{marge_ebit:.1f}%")
            
            # Benchmarking
            st.markdown("#### 📊 Référentiels")
            st.write("**ROE souhaitable**: > 8-10%")
            st.write("**ROA typique**: 3-8%")
            st.write("**ROS variable**: selon le secteur")
    
    with tab2:
        st.subheader("Ratios de Structure Financière")
        
        col1, col2 = st.columns(2)
        
        with col1:
            dette_financiere = st.number_input("Dettes financières (k€)", value=800)
            capitaux_propres_struct = st.number_input("Capitaux propres (k€)", value=1000)
            actif_immobilise = st.number_input("Actif immobilisé (k€)", value=1200)
            capitaux_permanents = st.number_input("Capitaux permanents (k€)", value=1800)
        
        with col2:
            # Calcul des ratios
            leverage = dette_financiere / capitaux_propres_struct
            autonomie_financiere = capitaux_propres_struct / (dette_financiere + capitaux_propres_struct) * 100
            couverture_immobilisation = capitaux_permanents / actif_immobilise
            
            st.metric("Ratio d'endettement", f"{leverage:.2f}")
            st.metric("Autonomie financière", f"{autonomie_financiere:.1f}%")
            st.metric("Couverture des immobilisations", f"{couverture_immobilisation:.2f}")
            
            # Interprétation
            if leverage < 1:
                st.success("✅ Structure financière saine")
            elif leverage < 2:
                st.warning("⚠️ Endettement modéré")
            else:
                st.error("❌ Endettement élevé")
    
    with tab3:
        st.subheader("Ratios d'Activité et d'Efficacité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            ca_activite = st.number_input("CA annuel (k€)", value=2000)
            clients_moyens = st.number_input("Créances clients moyennes (k€)", value=300)
            stocks_moyens = st.number_input("Stocks moyens (k€)", value=200)
            fournisseurs_moyens = st.number_input("Dettes fournisseurs moyennes (k€)", value=150)
        
        with col2:
            # Calcul des ratios
            dso = (clients_moyens / ca_activite) * 365  # Days Sales Outstanding
            dio = (stocks_moyens / ca_activite) * 365   # Days Inventory Outstanding
            dpo = (fournisseurs_moyens / ca_activite) * 365  # Days Payable Outstanding
            ccc = dso + dio - dpo  # Cash Conversion Cycle
            
            st.metric("Délai clients (jours)", f"{dso:.0f} j")
            st.metric("Délai stocks (jours)", f"{dio:.0f} j")
            st.metric("Délai fournisseurs (jours)", f"{dpo:.0f} j")
            st.metric("Cycle de trésorerie", f"{ccc:.0f} j")
            
            if ccc < 0:
                st.success("🎉 Trésorerie générée par le cycle d'exploitation")
            else:
                st.info("💡 BFR à financer")
    
    with tab4:
        st.subheader("Ratios de Liquidité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            actif_circulant = st.number_input("Actif circulant (k€)", value=800)
            stocks_liquidite = st.number_input("Stocks (k€)", value=200)
            disponibilites = st.number_input("Disponibilités (k€)", value=100)
            passif_courant = st.number_input("Passif courant (k€)", value=500)
        
        with col2:
            # Calcul des ratios
            liquidite_generale = actif_circulant / passif_courant
            liquidite_reduite = (actif_circulant - stocks_liquidite) / passif_courant
            liquidite_immediate = disponibilites / passif_courant
            
            st.metric("Liquidité générale", f"{liquidite_generale:.2f}")
            st.metric("Liquidité réduite", f"{liquidite_reduite:.2f}")
            st.metric("Liquidité immédiate", f"{liquidite_immediate:.2f}")
            
            # Seuils de référence
            st.markdown("#### 📈 Seuils de référence")
            st.write("**Liquidité générale > 1.2**")
            st.write("**Liquidité réduite > 0.8**")
            st.write("**Liquidité immédiate > 0.2**")
            
# Ajouter dans la navigation
# st.sidebar.radio(...) - ajouter "🏢 Cas Pratiques"

elif section == "🏢 Cas Pratiques":
    st.header("🏢 Études de Cas Complets")
    
    cas_choice = st.selectbox(
        "Choisissez un cas d'étude:",
        ["🚀 Startup Tech", "🏭 PMI Industrielle", "🛒 Commerce de Détail", "💻 ESI (Entreprise de Services Informatiques)"]
    )
    
    if cas_choice == "🚀 Startup Tech":
        st.subheader("🚀 Startup Technologique - Croissance Rapide")
        
        st.markdown("""
        **Contexte**: Une startup SaaS avec une croissance de 50% par an mais des pertes importantes.
        **Enjeu**: Évaluer la soutenabilité du modèle et les besoins de financement.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Données de la startup**")
            ca = st.slider("Chiffre d'affaires (k€)", 500, 5000, 1500)
            croissance = st.slider("Taux de croissance (%)", 10, 100, 50)
            marge_brute = st.slider("Marge brute (%)", 10, 90, 70)
            frais_fixes = st.slider("Frais fixes (k€)", 500, 3000, 1200)
            besoin_bfr = st.slider("BFR (mois de CA)", 1, 6, 3)
        
        with col2:
            # Calculs automatiques
            marge_absolue = ca * marge_brute / 100
            resultat_operationnel = marge_absolue - frais_fixes
            bfr_absolu = (ca * besoin_bfr) / 12
            ca_an_prochain = ca * (1 + croissance/100)
            
            st.metric("Résultat opérationnel", f"{resultat_operationnel:,.0f} k€")
            st.metric("BFR à financer", f"{bfr_absolu:,.0f} k€")
            st.metric("CA année N+1", f"{ca_an_prochain:,.0f} k€")
            
            # Diagnostic
            if resultat_operationnel < 0:
                st.error("**Problème**: Pertes opérationnelles")
                st.write("**Solution possible**: Lever des fonds ou réduire les coûts fixes")
            else:
                st.success("**Opportunité**: Rentabilité atteinte")
                
            if bfr_absolu > resultat_operationnel and resultat_operationnel > 0:
                st.warning("**Attention**: La croissance consomme plus de trésorerie qu'elle n'en génère")
    
    elif cas_choice == "🏭 PMI Industrielle":
        st.subheader("🏭 PMI Industrielle - Optimisation du BFR")
        
        st.markdown("""
        **Contexte**: Entreprise industrielle stable mais avec des tensions de trésorerie récurrentes.
        **Enjeu**: Améliorer la trésorerie sans impacter la croissance.
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Délais actuels**")
            delai_clients = st.slider("Délai clients (jours)", 30, 120, 75)
            delai_stocks = st.slider("Délai stocks (jours)", 15, 90, 45)
            delai_fournisseurs = st.slider("Délai fournisseurs (jours)", 20, 90, 30)
            ca_journalier = st.number_input("CA journalier (k€)", value=10.0)
        
        with col2:
            st.markdown("**Objectifs d'optimisation**")
            objectif_clients = st.slider("Objectif délai clients", 30, 120, 60)
            objectif_stocks = st.slider("Objectif délai stocks", 15, 90, 35)
            objectif_fournisseurs = st.slider("Objectif délai fournisseurs", 20, 90, 40)
        
        with col3:
            # Calcul des gains
            gain_clients = (delai_clients - objectif_clients) * ca_journalier
            gain_stocks = (delai_stocks - objectif_stocks) * ca_journalier * 0.6  # Coût des stocks
            gain_fournisseurs = (objectif_fournisseurs - delai_fournisseurs) * ca_journalier * 0.8  # Achats
            
            gain_total = gain_clients + gain_stocks + gain_fournisseurs
            
            st.metric("Gain sur clients", f"{gain_clients:,.0f} k€")
            st.metric("Gain sur stocks", f"{gain_stocks:,.0f} k€")
            st.metric("Gain sur fournisseurs", f"{gain_fournisseurs:,.0f} k€")
            st.metric("**GAIN TOTAL TRÉSORERIE**", f"{gain_total:,.0f} k€")
            
# Ajouter dans la navigation
# st.sidebar.radio(...) - ajouter "🎓 Quiz & Validation"

elif section == "🎓 Quiz & Validation":
    st.header("🎓 Validez Vos Connaissances")
    
    quiz_choice = st.selectbox(
        "Choisissez un quiz:",
        ["📋 Fondamentaux", "💰 Ratios", "⚖️ Équilibre Financier", "🎯 Évaluation"]
    )
    
    if quiz_choice == "📋 Fondamentaux":
        st.subheader("Quiz - Concepts Fondamentaux")
        
        questions = [
            {
                "question": "Qu'est-ce que le principe de prudence en comptabilité?",
                "options": [
                    "Anticiper les pertes mais pas les gains",
                    "Toujours être pessimiste",
                    "Ignorer les incertitudes",
                    "Valoriser au maximum les actifs"
                ],
                "reponse": 0
            },
            {
                "question": "Que représente le Fonds de Roulement?",
                "options": [
                    "La trésorerie disponible",
                    "Les ressources stables financées durablement",
                    "Le besoin en fonds de roulement",
                    "Le résultat de l'exercice"
                ],
                "reponse": 1
            },
            {
                "question": "Quelle est la formule du BFR?",
                "options": [
                    "Stocks + Créances - Dettes d'exploitation",
                    "Capitaux propres - Actif immobilisé",
                    "CA - Charges",
                    "Trésorerie active - Trésorerie passive"
                ],
                "reponse": 0
            }
        ]
        
        score = 0
        
        for i, q in enumerate(questions):
            st.markdown(f"**Question {i+1}**: {q['question']}")
            reponse_utilisateur = st.radio(
                f"Choisissez votre réponse:",
                q['options'],
                key=f"q{i}"
            )
            
            if st.button(f"Valider Q{i+1}", key=f"b{i}"):
                if reponse_utilisateur == q['options'][q['reponse']]:
                    st.success("✅ Bonne réponse !")
                    score += 1
                else:
                    st.error(f"❌ Mauvaise réponse. La bonne réponse était: {q['options'][q['reponse']]}")
        
        if st.button("📊 Voir mon score final"):
            st.metric("Score final", f"{score}/{len(questions)}")
            if score == len(questions):
                st.balloons()
                st.success("🎉 Excellent ! Vous maîtrisez les fondamentaux")
                
# Ajouter dans la navigation
# st.sidebar.radio(...) - ajouter "🎮 Simulations Stratégiques"

elif section == "🎮 Simulations Stratégiques":
    st.header("🎮 Simulateur de Décisions Stratégiques")
    
    st.subheader("Impact d'une décision d'investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📥 Données du projet")
        investissement_initial = st.number_input("Investissement initial (k€)", value=1000)
        duree_amortissement = st.slider("Durée d'amortissement (ans)", 3, 10, 5)
        ca_supplementaire = st.number_input("CA supplémentaire annuel (k€)", value=400)
        marge_supplementaire = st.slider("Marge supplémentaire (%)", 10, 50, 30)
        taux_actualisation = st.slider("Taux d'actualisation (%)", 5, 15, 10)
    
    with col2:
        st.markdown("### 📊 Résultats de l'analyse")
        
        # Calcul VAN
        marge_annuelle = ca_supplementaire * marge_supplementaire / 100
        amortissement_annuel = investissement_initial / duree_amortissement
        resultat_avant_impot = marge_annuelle - amortissement_annuel
        impot = resultat_avant_impot * 0.25  # Taux d'IS 25%
        flux_net = marge_annuelle - impot
        
        # Calcul VAN
        van = -investissement_initial
        for annee in range(1, duree_amortissement + 1):
            van += flux_net / ((1 + taux_actualisation/100) ** annee)
        
        # Calcul TRI (approximatif)
        tri = (flux_net / investissement_initial) * 100
        
        st.metric("VAN du projet", f"{van:,.0f} k€")
        st.metric("TRI approximatif", f"{tri:.1f}%")
        st.metric("Délai de récupération", f"{investissement_initial/flux_net:.1f} ans")
        
        # Recommandation
        if van > 0:
            st.success("✅ PROJET ACCEPTABLE - VAN positive")
        else:
            st.error("❌ PROJET À REJETER - VAN négative")
    
    # Graphique des flux
    annees = list(range(duree_amortissement + 1))
    flux = [-investissement_initial] + [flux_net] * duree_amortissement
    flux_cumules = np.cumsum(flux)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(x=annees, y=flux, name="Flux annuels", marker_color='blue'),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(x=annees, y=flux_cumules, name="Flux cumulés", line=dict(color='red', width=3)),
        secondary_y=True,
    )
    
    fig.update_layout(
        title="Flux de trésorerie du projet",
        xaxis_title="Années",
        showlegend=True
    )
    
    fig.update_yaxes(title_text="Flux annuels (k€)", secondary_y=False)
    fig.update_yaxes(title_text="Flux cumulés (k€)", secondary_y=True)
    
    st.plotly_chart(fig, use_container_width=True)
    
# Ajouter au début du fichier après les imports
if 'progression' not in st.session_state:
    st.session_state.progression = {
        'fondamentaux': False,
        'ratios': False,
        'equilibre': False,
        'evaluation': False,
        'cas_pratiques': False,
        'quiz': False
    }

# Ajouter dans la sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Ma Progression")

progression_totale = sum(st.session_state.progression.values()) / len(st.session_state.progression) * 100
st.sidebar.metric("Progression globale", f"{progression_totale:.0f}%")

if progression_totale == 100:
    st.sidebar.success("🎉 Formation terminée !")
    if st.sidebar.button("📜 Générer mon certificat"):
        st.sidebar.balloons()
        st.sidebar.markdown("""
        ## 📜 Certificat de Maîtrise
        **FinanceLab - Analyse Financière**
        
        Félicitations ! Vous avez complété avec succès 
        l'ensemble des modules de formation.
        
        *Certificat délivré le: {}*
        """.format(pd.Timestamp.now().strftime("%d/%m/%Y")))
        
# Fonction d'export à ajouter dans chaque section pertinente

def exporter_analyse(nom_analyse, données):
    """Fonction pour exporter les analyses en PDF ou Excel"""
    # Créer un DataFrame avec les résultats
    df = pd.DataFrame(données)
    
    # Afficher les options d'export
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(f"📊 Exporter {nom_analyse} en Excel"):
            # Créer le fichier Excel
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Analyse', index=False)
            st.download_button(
                label="📥 Télécharger Excel",
                data=output.getvalue(),
                file_name=f"analyse_{nom_analyse}_{pd.Timestamp.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.ms-excel"
            )
    
    with col2:
        if st.button(f"📄 Exporter {nom_analyse} en PDF"):
            st.info("Fonctionnalité PDF en développement...")

# Exemple d'utilisation dans une section
# exporter_analyse("Ratios", données_ratios)       





    

else:
    st.header("🏠 Bienvenue dans FinanceLab !")
    
    st.markdown("""
    ## 🎯 Votre Laboratoire d'Analyse Financière
    
    Cette application vous permet de:
    
    ✅ **Comprendre** les concepts fondamentaux de l'analyse financière
    ✅ **Pratiquer** avec des exemples concrets et interactifs
    ✅ **Visualiser** l'impact des décisions financières
    ✅ **Maîtriser** les outils d'évaluation et de diagnostic
    
    ### 📚 Modules disponibles:
    
    #### 📋 Fondamentaux
    - Principes comptables essentiels
    - Reclassement du bilan
    - Calcul des soldes intermédiaires de gestion
    
    #### 💰 Performance
    - Création de valeur (EVA)
    - Effet de levier financier
    - Seuil de rentabilité
    
    #### ⚖️ Équilibre Financier
    - Fonds de Roulement, BFR, Trésorerie Nette
    - Diagnostic de l'équilibre financier
    - Optimisation du BFR
    
    #### 🎯 Évaluation d'Entreprise
    - Méthode DCF (flux actualisés)
    - Calcul du coût du capital (WACC)
    - Analyse du risque de crédit
    """)
    
    # Quick start - exemple pratique
    st.markdown("---")
    st.subheader("🚀 Démarrage Rapide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Analyser un Bilan Simple"):
            st.session_state.section = "📋 Fondamentaux"
    
    with col2:
        if st.button("💰 Calculer la Création de Valeur"):
            st.session_state.section = "💰 Performance"
            
            

 
 
 
                