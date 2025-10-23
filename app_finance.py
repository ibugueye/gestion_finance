import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import yfinance as yf
import requests
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pickle
from io import BytesIO

# Configuration de la page
st.set_page_config(
    page_title="FinanceLab - Analyse Financière",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
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
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Initialisation de l'état de session
if 'progression' not in st.session_state:
    st.session_state.progression = {
        'fondamentaux': False,
        'ratios': False,
        'equilibre': False,
        'evaluation': False,
        'cas_pratiques': False,
        'quiz': False
    }

if 'analyses_sauvegardees' not in st.session_state:
    st.session_state.analyses_sauvegardees = []

if 'watchlist' not in st.session_state:
    st.session_state.watchlist = []

if 'notifications' not in st.session_state:
    st.session_state.notifications = [
        {"type": "info", "message": "📚 Module Fondamentaux à compléter", "date": "2024-01-15"},
        {"type": "warning", "message": "⚡ Quiz Ratios à réviser", "date": "2024-01-14"},
        {"type": "success", "message": "🎉 Bienvenue dans FinanceLab !", "date": "2024-01-13"}
    ]

# Titre principal
st.markdown('<h1 class="main-header">🎯 FinanceLab - Maîtrisez l\'Analyse Financière</h1>', unsafe_allow_html=True)

# Sidebar pour la navigation
st.sidebar.title("📚 Modules d'Apprentissage")
section = st.sidebar.radio(
    "Choisissez un module:",
    ["🏠 Accueil", "📋 Fondamentaux", "💰 Performance", "⚖️ Équilibre Financier", "📊 Analyse par Ratios", 
     "🎯 Évaluation d'Entreprise", "🏢 Cas Pratiques", "🤖 Prévisions IA", "🌍 Données Réelles", 
     "💾 Mes Analyses", "📊 Mon Dashboard", "🔔 Alertes & Veille", "📑 Reporting", "❓ Aide & Support"]
)

# Fonction pour afficher les notifications
def afficher_notifications():
    if st.session_state.notifications:
        st.sidebar.markdown("---")
        st.sidebar.subheader("🔔 Notifications")
        
        for notif in st.session_state.notifications[:3]:
            if notif["type"] == "info":
                st.sidebar.info(notif["message"])
            elif notif["type"] == "warning":
                st.sidebar.warning(notif["message"])
            elif notif["type"] == "success":
                st.sidebar.success(notif["message"])

# Appel de la fonction notifications
afficher_notifications()

# Section Accueil
if section == "🏠 Accueil":
    st.header("🏠 Bienvenue dans FinanceLab !")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## 🎯 Votre Laboratoire d'Analyse Financière
        
        **FinanceLab** est une plateforme complète d'apprentissage interactif de l'analyse financière.
        Que vous soyez étudiant, professionnel ou entrepreneur, maîtrisez les concepts clés grâce à des outils pratiques et des cas concrets.
        
        ### 📚 Ce que vous allez apprendre:
        
        ✅ **Les fondamentaux** de l'information financière  
        ✅ **L'analyse des ratios** et indicateurs de performance  
        ✅ **L'équilibre financier** (FR, BFR, Trésorerie)  
        ✅ **Les méthodes d'évaluation** d'entreprise  
        ✅ **La prévision** avec l'intelligence artificielle  
        ✅ **L'analyse de données réelles** du marché  
        
        ### 🚀 Comment progresser:
        
        1. **Commencez** par les fondamentaux
        2. **Pratiquez** avec les calculateurs interactifs
        3. **Testez** vos connaissances avec les quiz
        4. **Appliquez** sur des cas concrets
        5. **Validez** votre progression avec le dashboard
        """)
    
    with col2:
        st.image("https://via.placeholder.com/300x400/1f77b4/ffffff?text=FinanceLab", use_column_width=True)
        
        # Quick start
        st.markdown("### 🚀 Démarrage Rapide")
        if st.button("📊 Commencer par les fondamentaux"):
            st.session_state.progression['fondamentaux'] = True
            st.rerun()
        
        if st.button("💰 Analyser la performance"):
            st.session_state.progression['ratios'] = True
            st.rerun()

    # Statistiques globales
    st.markdown("---")
    st.subheader("📈 Votre Progression Globale")
    
    modules_completes = sum(st.session_state.progression.values())
    progression_totale = (modules_completes / len(st.session_state.progression)) * 100
    
    col_met1, col_met2, col_met3, col_met4 = st.columns(4)
    
    with col_met1:
        st.metric("Modules Complétés", f"{modules_completes}/6")
    with col_met2:
        st.metric("Progression Globale", f"{progression_totale:.0f}%")
    with col_met3:
        st.metric("Analyses Sauvegardées", len(st.session_state.analyses_sauvegardees))
    with col_met4:
        st.metric("Entreprises Surveillées", len(st.session_state.watchlist))

# Section Fondamentaux
elif section == "📋 Fondamentaux":
    st.header("📋 Les Fondamentaux de l'Information Financière")
    
    # Marquer comme complété
    if not st.session_state.progression['fondamentaux']:
        if st.button("✅ Marquer ce module comme complété"):
            st.session_state.progression['fondamentaux'] = True
            st.session_state.notifications.append({
                "type": "success", 
                "message": "🎉 Module Fondamentaux complété !", 
                "date": datetime.now().strftime("%Y-%m-%d")
            })
            st.rerun()
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Principes Comptables", "🏦 Le Bilan", "📈 Compte de Résultat", "🧮 Soldes Intermédiaires"])
    
    with tab1:
        st.subheader("Les 10 Principes Comptables Fondamentaux")
        
        principles = {
            "Principe de prudence": "Anticiper les pertes, ne pas anticiper les gains. Se préparer aux difficultés sans compter sur les opportunités incertaines.",
            "Continuité d'exploitation": "L'entreprise continue son activité normalement. Les états financiers sont préparés dans cette perspective.",
            "Coût historique": "Évaluation des actifs à leur prix d'acquisition. Même si la valeur de marché a augmenté.",
            "Indépendance des exercices": "Rattacher charges et produits à la bonne période. Chaque exercice doit refléter sa propre performance.",
            "Permanence des méthodes": "Application constante des règles dans le temps. Permet la comparabilité des états financiers.",
            "Non-compensation": "Ne pas compenser actif/passif ou charges/produits. Chaque élément doit apparaître distinctement.",
            "Image fidèle": "Les comptes doivent refléter la réalité économique de l'entreprise, au-delà de la simple légalité.",
            "Primauté de la réalité économique": "La substance prime sur la forme. L'analyse économique prévaut sur l'apparence juridique.",
            "Spécialisation des exercices": "Chaque exercice a sa propre détermination du résultat. Pas de report de bénéfices ou pertes.",
            "Juste valeur": "Évaluation à la valeur de marché quand elle est disponible et fiable."
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
            
            # Explication pédagogique
            with st.expander("💡 Comprendre le reclassement"):
                st.markdown("""
                **Pourquoi reclasser le bilan ?**
                
                Le bilan comptable suit des règles précises, mais le bilan financier offre une vision plus opérationnelle:
                
                - **Actif immobilisé**: Investissements durables
                - **Actif circulant**: Cycle d'exploitation (stocks, créances)
                - **Trésorerie active**: Liquidités disponibles
                
                Cette vision facilite l'analyse de l'équilibre financier.
                """)

    with tab3:
        st.subheader("📈 Structure du Compte de Résultat")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Produits")
            ca = st.number_input("Chiffre d'affaires", value=1000000)
            prod_stockee = st.number_input("Production stockée", value=50000)
            subv_exploitation = st.number_input("Subventions d'exploitation", value=20000)
            produits_financiers = st.number_input("Produits financiers", value=30000)
            produits_exceptionnels = st.number_input("Produits exceptionnels", value=15000)
        
        with col2:
            st.markdown("#### Charges")
            achats_consommes = st.number_input("Achats consommés", value=600000)
            services_externes = st.number_input("Services externes", value=120000)
            charges_personnel = st.number_input("Charges de personnel", value=180000)
            dotations_amortissement = st.number_input("Dotations aux amortissements", value=80000)
            charges_financieres = st.number_input("Charges financières", value=25000)
            charges_exceptionnelles = st.number_input("Charges exceptionnelles", value=10000)
            impot_benefices = st.number_input("Impôt sur les bénéfices", value=35000)
        
        # Calcul des résultats intermédiaires
        marge_commerciale = ca - achats_consommes
        valeur_ajoutee = marge_commerciale - services_externes
        ebe = valeur_ajoutee - charges_personnel
        resultat_exploitation = ebe - dotations_amortissement
        resultat_courant = resultat_exploitation + produits_financiers - charges_financieres
        resultat_exceptionnel = produits_exceptionnels - charges_exceptionnelles
        resultat_net = resultat_courant + resultat_exceptionnel - impot_benefices
        
        # Affichage des soldes
        st.markdown("#### 📊 Soldes Intermédiaires de Gestion")
        
        soldes_data = {
            "Marge commerciale": marge_commerciale,
            "Valeur ajoutée": valeur_ajoutee,
            "Excédent Brut d'Exploitation (EBE)": ebe,
            "Résultat d'exploitation": resultat_exploitation,
            "Résultat courant": resultat_courant,
            "Résultat exceptionnel": resultat_exceptionnel,
            "Résultat net": resultat_net
        }
        
        for solde, valeur in soldes_data.items():
            col_s1, col_s2 = st.columns([2, 1])
            with col_s1:
                st.write(f"**{solde}**")
            with col_s2:
                st.write(f"{valeur:,.0f} €")
        
        # Graphique des soldes
        fig_soldes = go.Figure()
        fig_soldes.add_trace(go.Bar(
            x=list(soldes_data.keys()),
            y=list(soldes_data.values()),
            marker_color=['blue', 'green', 'orange', 'red', 'purple', 'brown', 'black']
        ))
        fig_soldes.update_layout(
            title="Évolution des Soldes Intermédiaires de Gestion",
            xaxis_tickangle=-45,
            height=400
        )
        st.plotly_chart(fig_soldes, use_container_width=True)

    with tab4:
        st.subheader("🧮 Calculateur de Soldes Intermédiaires de Gestion")
        
        st.markdown("""
        Les Soldes Intermédiaires de Gestion (SIG) permettent d'analyser la formation du résultat 
        et d'identifier les sources de performance ou de difficultés.
        """)
        
        # Calculateur interactif
        col_calc1, col_calc2 = st.columns(2)
        
        with col_calc1:
            st.markdown("**Données d'entrée**")
            ca_input = st.number_input("Chiffre d'affaires HT", value=500000, key="ca_sig")
            achats_consommes_input = st.number_input("Achats consommés", value=300000, key="achats_sig")
            variation_stocks = st.number_input("Variation des stocks", value=10000, key="var_stocks")
            production_immobilisee = st.number_input("Production immobilisée", value=20000, key="prod_immob")
            subventions_exploitation = st.number_input("Subventions d'exploitation", value=5000, key="subv_expl")
        
        with col_calc2:
            st.markdown("**Charges**")
            consommations_externes = st.number_input("Consommations externes", value=80000, key="cons_ext")
            impots_taxes = st.number_input("Impôts et taxes", value=15000, key="impots")
            charges_personnel_input = st.number_input("Charges de personnel", value=120000, key="charges_pers")
            dotations_input = st.number_input("Dotations aux amortissements", value=40000, key="dotations")
        
        # Calcul automatique des SIG
        marge_commerciale_calc = ca_input - achats_consommes_input + variation_stocks
        production_periode = ca_input + production_immobilisee
        valeur_ajoutee_calc = marge_commerciale_calc + production_periode - consommations_externes
        ebe_calc = valeur_ajoutee_calc - impots_taxes - charges_personnel_input + subventions_exploitation
        resultat_exploitation_calc = ebe_calc - dotations_input
        
        # Affichage des résultats
        st.markdown("### 📈 Résultats des SIG")
        
        sig_data = {
            "Marge commerciale": marge_commerciale_calc,
            "Production de l'exercice": production_periode,
            "Valeur ajoutée": valeur_ajoutee_calc,
            "Excédent Brut d'Exploitation (EBE)": ebe_calc,
            "Résultat d'exploitation": resultat_exploitation_calc
        }
        
        for sig, valeur in sig_data.items():
            percentage = (valeur / ca_input) * 100 if ca_input > 0 else 0
            st.metric(sig, f"{valeur:,.0f} €", f"{percentage:.1f}% du CA")
        
        # Interprétation automatique
        st.markdown("### 💡 Interprétation")
        
        if valeur_ajoutee_calc / ca_input > 0.4:
            st.success("**✅ Excellente valeur ajoutée**: L'entreprise transforme efficacement ses achats en valeur")
        elif valeur_ajoutee_calc / ca_input > 0.2:
            st.info("**📊 Valeur ajoutée correcte**: Niveau standard pour ce type d'activité")
        else:
            st.warning("**⚠️ Valeur ajoutée faible**: L'entreprise pourrait améliorer sa marge de transformation")
        
        if ebe_calc / ca_input > 0.1:
            st.success("**💰 Bon EBE**: L'entreprise dégage une marge d'exploitation saine")
        else:
            st.warning("**📉 EBE faible**: Risque sur la rentabilité opérationnelle")

# Section Performance et Rentabilité
elif section == "💰 Performance":
    st.header("💰 Diagnostic de la Performance et de la Rentabilité")
    
    if not st.session_state.progression['ratios']:
        if st.button("✅ Marquer ce module comme complété"):
            st.session_state.progression['ratios'] = True
            st.session_state.notifications.append({
                "type": "success", 
                "message": "🎉 Module Performance complété !", 
                "date": datetime.now().strftime("%Y-%m-%d")
            })
            st.rerun()
    
    tab1, tab2, tab3 = st.tabs(["📈 Création de Valeur (EVA)", "⚖️ Levier Financier", "🎯 Seuil de Rentabilité"])
    
    with tab1:
        st.subheader("📈 Simulateur de Création de Valeur (EVA)")
        
        st.markdown("""
        L'**Economic Value Added (EVA)** mesure la création de valeur économique réelle après rémunération 
        de tous les apporteurs de capitaux, y compris les actionnaires.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📥 Données d'entrée")
            resultat_exploitation = st.slider("Résultat d'exploitation (k€)", 100, 5000, 1000, step=50)
            capital_investi = st.slider("Capital économique investi (k€)", 500, 20000, 5000, step=100)
            taux_imposition = st.slider("Taux d'imposition (%)", 15.0, 35.0, 25.0, step=0.5)
            cout_capital = st.slider("Coût du capital (%)", 5.0, 15.0, 8.0, step=0.5)
        
        with col2:
            st.markdown("### 📊 Résultats")
            
            # Calculs EVA
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
            
            # Graphique de création de valeur
            fig_eva = go.Figure()
            fig_eva.add_trace(go.Indicator(
                mode = "number+delta",
                value = eva,
                delta = {'reference': 0, 'relative': False},
                title = {"text": "EVA (k€)"},
                domain = {'x': [0, 1], 'y': [0, 1]}
            ))
            fig_eva.update_layout(height=200)
            st.plotly_chart(fig_eva, use_container_width=True)
        
        # Explication pédagogique
        with st.expander("🧠 Comprendre l'EVA"):
            st.markdown("""
            **Formule de l'EVA:**
            ```
            EVA = Résultat d'exploitation après impôts - (Capital investi × Coût du capital)
            ```
            
            **Interprétation:**
            - **EVA > 0**: L'entreprise crée de la valeur économique
            - **EVA < 0**: L'entreprise détruit de la valeur
            - **EVA = 0**: L'entreprise rémunère juste le coût du capital
            
            L'EVA est un indicateur plus exigeant que le simple bénéfice comptable.
            """)
    
    with tab2:
        st.subheader("⚖️ Calculateur de Levier Financier")
        
        st.markdown("""
        Le **levier financier** mesure l'impact de l'endettement sur la rentabilité des capitaux propres.
        Il peut amplifier les gains... mais aussi les pertes !
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📥 Données financières")
            resultat_expl = st.number_input("Résultat d'exploitation (k€)", value=800, key="res_expl_levier")
            charges_financieres = st.number_input("Charges financières (k€)", value=100, key="charges_fin_levier")
            capitaux_propres = st.number_input("Capitaux propres (k€)", value=2000, key="cap_propres_levier")
            dette_financiere = st.number_input("Dettes financières (k€)", value=1000, key="dette_fin_levier")
            taux_imposition_levier = st.slider("Taux d'imposition (%)", 15.0, 35.0, 25.0, key="taux_imp_levier")
        
        with col2:
            st.markdown("### 📊 Impact du levier")
            
            # Calculs
            resultat_courant = resultat_expl - charges_financieres
            resultat_net = resultat_courant * (1 - taux_imposition_levier/100)
            roe_avec_dette = (resultat_net / capitaux_propres) * 100
            
            # Sans dette (pour comparaison)
            resultat_net_sans_dette = resultat_expl * (1 - taux_imposition_levier/100)
            roe_sans_dette = (resultat_net_sans_dette / (capitaux_propres + dette_financiere)) * 100
            
            # Effet de levier
            effet_levier = roe_avec_dette - roe_sans_dette
            
            st.metric("ROE avec endettement", f"{roe_avec_dette:.1f}%")
            st.metric("ROE sans endettement", f"{roe_sans_dette:.1f}%")
            st.metric("Effet de levier", f"{effet_levier:+.1f} points")
            
            if effet_levier > 0:
                st.success("✅ Le levier financier est positif")
            else:
                st.warning("📉 Le levier financier est négatif")
            
            # Graphique comparatif
            fig_levier = go.Figure()
            fig_levier.add_trace(go.Bar(
                name='Avec endettement',
                x=['ROE'],
                y=[roe_avec_dette],
                marker_color='blue'
            ))
            fig_levier.add_trace(go.Bar(
                name='Sans endettement',
                x=['ROE'],
                y=[roe_sans_dette],
                marker_color='lightblue'
            ))
            fig_levier.update_layout(
                title="Impact de l'endettement sur la rentabilité",
                barmode='group',
                height=300
            )
            st.plotly_chart(fig_levier, use_container_width=True)
        
        # Analyse de sensibilité
        st.markdown("### 🎚️ Analyse de Sensibilité")
        
        taux_interet = st.slider("Taux d'intérêt sur la dette (%)", 1.0, 10.0, 5.0)
        
        # Calcul du point d'équilibre
        roe_minimal = roe_sans_dette
        resultat_expl_minimal = (roe_minimal / 100) * (capitaux_propres + dette_financiere) / (1 - taux_imposition_levier/100)
        
        st.metric("Résultat d'exploitation minimum requis", f"{resultat_expl_minimal:,.0f} k€")
        
        if resultat_expl > resultat_expl_minimal:
            st.success("✅ Niveau de résultat suffisant pour un levier positif")
        else:
            st.warning("⚠️ Résultat d'exploitation insuffisant pour justifier l'endettement")
    
    with tab3:
        st.subheader("🎯 Calculateur de Seuil de Rentabilité")
        
        st.markdown("""
        Le **seuil de rentabilité** (ou point mort) est le niveau d'activité à partir duquel l'entreprise 
        commence à réaliser des bénéfices. Il se calcule en distinguant les coûts fixes et variables.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📥 Données de coûts")
            couts_fixes = st.number_input("Coûts fixes annuels (k€)", value=300)
            cout_variable_unitaire = st.number_input("Coût variable unitaire (€)", value=40)
            prix_vente_unitaire = st.number_input("Prix de vente unitaire (€)", value=100)
            capacite_production = st.number_input("Capacité de production (unités)", value=10000)
        
        with col2:
            st.markdown("### 📊 Résultats")
            
            # Calculs
            marge_unitaire = prix_vente_unitaire - cout_variable_unitaire
            taux_marge = (marge_unitaire / prix_vente_unitaire) * 100
            seuil_volume = couts_fixes * 1000 / marge_unitaire if marge_unitaire > 0 else 0
            seuil_ca = seuil_volume * prix_vente_unitaire / 1000  # en k€
            marge_securite = ((capacite_production - seuil_volume) / capacite_production) * 100
            
            st.metric("Seuil de rentabilité (volume)", f"{seuil_volume:,.0f} unités")
            st.metric("Seuil de rentabilité (CA)", f"{seuil_ca:,.1f} k€")
            st.metric("Taux de marge", f"{taux_marge:.1f}%")
            st.metric("Marge de sécurité", f"{marge_securite:.1f}%")
            
            if marge_securite > 20:
                st.success("✅ Bonne marge de sécurité")
            elif marge_securite > 10:
                st.warning("⚠️ Marge de sécurité modérée")
            else:
                st.error("❌ Marge de sécurité faible")
        
        # Graphique du seuil de rentabilité
        volumes = np.linspace(0, capacite_production * 1.2, 100)
        couts_totaux = couts_fixes * 1000 + cout_variable_unitaire * volumes
        chiffre_affaires = prix_vente_unitaire * volumes
        
        fig_seuil = go.Figure()
        
        fig_seuil.add_trace(go.Scatter(
            x=volumes, y=couts_totaux,
            mode='lines',
            name='Coûts totaux',
            line=dict(color='red', width=3)
        ))
        
        fig_seuil.add_trace(go.Scatter(
            x=volumes, y=chiffre_affaires,
            mode='lines',
            name='Chiffre d\'affaires',
            line=dict(color='green', width=3)
        ))
        
        # Point de seuil
        fig_seuil.add_trace(go.Scatter(
            x=[seuil_volume], y=[seuil_ca * 1000],
            mode='markers',
            name='Seuil de rentabilité',
            marker=dict(color='black', size=10, symbol='x')
        ))
        
        fig_seuil.update_layout(
            title="Graphique du Seuil de Rentabilité",
            xaxis_title="Volume (unités)",
            yaxis_title="Montant (€)",
            showlegend=True,
            height=400
        )
        
        st.plotly_chart(fig_seuil, use_container_width=True)
        
        # Analyse de sensibilité
        st.markdown("### 🎚️ Analyse de Sensibilité")
        
        col_sens1, col_sens2 = st.columns(2)
        
        with col_sens1:
            variation_prix = st.slider("Variation du prix de vente (%)", -20, 20, 0)
            nouveau_prix = prix_vente_unitaire * (1 + variation_prix/100)
            nouvelle_marge = nouveau_prix - cout_variable_unitaire
            nouveau_seuil = couts_fixes * 1000 / nouvelle_marge if nouvelle_marge > 0 else 0
            
            st.metric(f"Seuil avec prix {variation_prix:+}%", f"{nouveau_seuil:,.0f} unités")
        
        with col_sens2:
            variation_couts_fixes = st.slider("Variation des coûts fixes (%)", -20, 20, 0)
            nouveaux_couts_fixes = couts_fixes * (1 + variation_couts_fixes/100)
            nouveau_seuil_cf = nouveaux_couts_fixes * 1000 / marge_unitaire if marge_unitaire > 0 else 0
            
            st.metric(f"Seuil avec CF {variation_couts_fixes:+}%", f"{nouveau_seuil_cf:,.0f} unités")

# Section Équilibre Financier
elif section == "⚖️ Équilibre Financier":
    st.header("⚖️ L'Équilibre Financier et la Trésorerie")
    
    if not st.session_state.progression['equilibre']:
        if st.button("✅ Marquer ce module comme complété"):
            st.session_state.progression['equilibre'] = True
            st.session_state.notifications.append({
                "type": "success", 
                "message": "🎉 Module Équilibre Financier complété !", 
                "date": datetime.now().strftime("%Y-%m-%d")
            })
            st.rerun()
    
    st.subheader("🧊 Simulateur FR-BFR-TN")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📥 Données d'entrée")
        capitaux_permanents = st.number_input("Capitaux permanents (k€)", value=800, key="cap_permanents")
        actif_immobilise = st.number_input("Actif immobilisé (k€)", value=500, key="act_immobilise")
        stocks = st.number_input("Stocks (k€)", value=150, key="stocks_equilibre")
        clients = st.number_input("Créances clients (k€)", value=200, key="clients_equilibre")
        fournisseurs = st.number_input("Dettes fournisseurs (k€)", value=120, key="fournisseurs_equilibre")
        disponibilites = st.number_input("Disponibilités (k€)", value=80, key="dispo_equilibre")
        concours_bancaires = st.number_input("Concours bancaires (k€)", value=50, key="concours_equilibre")
    
    with col2:
        st.markdown("### 📊 Calculs")
        # Calcul des indicateurs
        fr = capitaux_permanents - actif_immobilise
        bfr = (stocks + clients) - fournisseurs
        tn = fr - bfr
        
        st.metric("Fonds de Roulement (FR)", f"{fr:,.0f} k€")
        st.metric("Besoin en Fonds de Roulement (BFR)", f"{bfr:,.0f} k€")
        st.metric("Trésorerie Nette (TN)", f"{tn:,.0f} k€")
        
        # Calcul de la trésorerie réelle
        tresorerie_reelle = disponibilites - concours_bancaires
        st.metric("Trésorerie réelle", f"{tresorerie_reelle:,.0f} k€")
    
    with col3:
        st.markdown("### 🩺 Diagnostic")
        if tn > 0:
            st.success("""
            ✅ **Situation saine**
            - Trésorerie excédentaire
            - L'entreprise finance son BFR et dégage un excédent
            - Bonne capacité d'autofinancement
            """)
        elif tn == 0:
            st.info("""
            ⚖️ **Situation équilibrée**
            - Le FR finance exactement le BFR
            - Trésorerie nulle
            - Situation stable mais peu de marge de manœuvre
            """)
        else:
            st.error("""
            ❌ **Situation tendue**
            - Le FR ne couvre pas le BFR
            - Trésorerie négative → recours au découvert
            - Risque de difficultés de trésorerie
            """)
        
        # Vérification cohérence
        if abs(tn - tresorerie_reelle) > 1:
            st.warning("⚠️ Écart entre TN théorique et trésorerie réelle")
    
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
        height=300,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Analyse des délais
    st.subheader("⏱️ Analyse des Délais d'Exploitation")
    
    col_del1, col_del2, col_del3 = st.columns(3)
    
    with col_del1:
        ca_annuel = st.number_input("CA annuel (k€)", value=1200, key="ca_delais")
        delai_clients = st.slider("Délai clients (jours)", 0, 120, 60)
    
    with col_del2:
        delai_stocks = st.slider("Délai stocks (jours)", 0, 90, 45)
    
    with col_del3:
        delai_fournisseurs = st.slider("Délai fournisseurs (jours)", 0, 90, 30)
    
    # Calcul du cycle de trésorerie
    cycle_exploitation = delai_stocks + delai_clients
    cycle_financement = delai_fournisseurs
    cycle_tresorerie = cycle_exploitation - cycle_financement
    
    st.metric("Cycle d'exploitation", f"{cycle_exploitation} jours")
    st.metric("Cycle de financement", f"{cycle_financement} jours")
    st.metric("Cycle de trésorerie", f"{cycle_tresorerie} jours")
    
    if cycle_tresorerie > 0:
        st.info("🔁 Cycle de trésorerie positif : besoin de financement du cycle d'exploitation")
    else:
        st.success("💰 Cycle de trésorerie négatif : l'exploitation génère de la trésorerie")
    
    # Recommandations d'optimisation
    st.subheader("💡 Recommandations d'Optimisation")
    
    if delai_clients > 60:
        st.warning("**⏳ Délai clients trop long**: Envisagez un relancement client ou un affacturage")
    
    if delai_stocks > 60:
        st.warning("**📦 Stocks élevés**: Optimisez la gestion des stocks et la rotation")
    
    if delai_fournisseurs < 30:
        st.info("**💳 Délai fournisseurs court**: Négociez de meilleurs délais de paiement")

# Section Analyse par Ratios
elif section == "📊 Analyse par Ratios":
    st.header("📊 Analyse Financière par les Ratios")
    
    tab1, tab2, tab3, tab4 = st.tabs(["💰 Rentabilité", "⚖️ Structure", "📈 Activité", "🧮 Liquidité"])
    
    with tab1:
        st.subheader("Ratios de Rentabilité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            ca = st.number_input("Chiffre d'affaires (k€)", value=2000, key="ca_ratios")
            resultat_net = st.number_input("Résultat net (k€)", value=150, key="res_net_ratios")
            resultat_exploitation = st.number_input("Résultat d'exploitation (k€)", value=200, key="res_expl_ratios")
            capitaux_propres = st.number_input("Capitaux propres (k€)", value=1000, key="cap_propres_ratios")
            actif_total = st.number_input("Actif total (k€)", value=2000, key="actif_total_ratios")
        
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
            
            # Diagnostic
            if roe > 15:
                st.success("✅ Excellente rentabilité des capitaux propres")
            elif roe > 8:
                st.info("📊 Rentabilité correcte")
            else:
                st.warning("⚠️ Rentabilité à améliorer")
    
    with tab2:
        st.subheader("Ratios de Structure Financière")
        
        col1, col2 = st.columns(2)
        
        with col1:
            dette_financiere = st.number_input("Dettes financières (k€)", value=800, key="dette_fin_struct")
            capitaux_propres_struct = st.number_input("Capitaux propres (k€)", value=1000, key="cap_propres_struct")
            actif_immobilise = st.number_input("Actif immobilisé (k€)", value=1200, key="act_immobilise_struct")
            capitaux_permanents = st.number_input("Capitaux permanents (k€)", value=1800, key="cap_permanents_struct")
        
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
                
            if autonomie_financiere > 33:
                st.success("✅ Bonne autonomie financière")
            else:
                st.warning("⚠️ Autonomie financière faible")
    
    with tab3:
        st.subheader("Ratios d'Activité et d'Efficacité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            ca_activite = st.number_input("CA annuel (k€)", value=2000, key="ca_activite")
            clients_moyens = st.number_input("Créances clients moyennes (k€)", value=300, key="clients_moyens")
            stocks_moyens = st.number_input("Stocks moyens (k€)", value=200, key="stocks_moyens")
            fournisseurs_moyens = st.number_input("Dettes fournisseurs moyennes (k€)", value=150, key="fournisseurs_moyens")
        
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
                
            # Cibles sectorielles
            st.markdown("#### 🎯 Cibles sectorielles typiques")
            st.write("**Délai clients**: 30-60 jours")
            st.write("**Délai stocks**: 30-90 jours")
            st.write("**Délai fournisseurs**: 30-60 jours")
    
    with tab4:
        st.subheader("Ratios de Liquidité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            actif_circulant = st.number_input("Actif circulant (k€)", value=800, key="actif_circulant")
            stocks_liquidite = st.number_input("Stocks (k€)", value=200, key="stocks_liquidite")
            disponibilites = st.number_input("Disponibilités (k€)", value=100, key="disponibilites")
            passif_courant = st.number_input("Passif courant (k€)", value=500, key="passif_courant")
        
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
            
            # Diagnostic
            if liquidite_generale > 1.2:
                st.success("✅ Bonne liquidité générale")
            else:
                st.warning("⚠️ Liquidité générale à surveiller")

# Section Évaluation d'Entreprise
elif section == "🎯 Évaluation d'Entreprise":
    st.header("🎯 Évaluation d'Entreprise et Risque de Crédit")
    
    if not st.session_state.progression['evaluation']:
        if st.button("✅ Marquer ce module comme complété"):
            st.session_state.progression['evaluation'] = True
            st.session_state.notifications.append({
                "type": "success", 
                "message": "🎉 Module Évaluation complété !", 
                "date": datetime.now().strftime("%Y-%m-%d")
            })
            st.rerun()
    
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
            dette_financiere = st.number_input("Dette financière nette (k€)", value=800)
        
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
            valeur_actions = valeur_entreprise - dette_financiere
            
            st.metric("Valeur de l'entreprise", f"{valeur_entreprise:,.0f} k€")
            st.metric("Valeur des flux explicites", f"{valeur_flux_explicites:,.0f} k€")
            st.metric("Valeur terminale actualisée", f"{valeur_terminale_actualisee:,.0f} k€")
            st.metric("Valeur des actions", f"{valeur_actions:,.0f} k€")
            
            # Sensibilité
            st.markdown("#### 🎚️ Analyse de Sensibilité")
            sensibilite_croissance = st.slider("Variation croissance (%)", -2.0, 2.0, 0.0)
            sensibilite_wacc = st.slider("Variation WACC (%)", -1.0, 1.0, 0.0)
            
            nouvelle_croissance = croissance_perpetuite + sensibilite_croissance
            nouveau_wacc = wacc + sensibilite_wacc
            
            if nouveau_wacc/100 > nouvelle_croissance/100:
                nouvelle_valeur_terminale = (fcf_annee5 * (1 + nouvelle_croissance/100)) / ((nouveau_wacc/100) - (nouvelle_croissance/100))
                nouvelle_valeur_entreprise = valeur_flux_explicites + (nouvelle_valeur_terminale / ((1 + nouveau_wacc/100) ** 5))
                variation = ((nouvelle_valeur_entreprise - valeur_entreprise) / valeur_entreprise) * 100
                
                st.metric("Nouvelle valeur entreprise", f"{nouvelle_valeur_entreprise:,.0f} k€", f"{variation:+.1f}%")
    
    elif method == "Multiples de Marché":
        st.subheader("📊 Évaluation par les Multiples")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Données de l'entreprise")
            ebitda = st.number_input("EBITDA (k€)", value=400)
            resultat_net = st.number_input("Résultat net (k€)", value=250)
            chiffre_affaires = st.number_input("Chiffre d'affaires (k€)", value=2000)
            dette_nette = st.number_input("Dette nette (k€)", value=800)
        
        with col2:
            st.markdown("### Multiples de référence")
            multiple_ebitda = st.slider("Multiple EBITDA", 4.0, 12.0, 8.0)
            multiple_resultat = st.slider("Multiple du résultat net", 8.0, 20.0, 12.0)
            multiple_ca = st.slider("Multiple du CA", 0.5, 3.0, 1.5)
            
            # Calculs
            valeur_ebitda = ebitda * multiple_ebitda
            valeur_resultat = resultat_net * multiple_resultat
            valeur_ca = chiffre_affaires * multiple_ca
            
            # Moyenne pondérée
            valeur_moyenne = (valeur_ebitda + valeur_resultat + valeur_ca) / 3
            valeur_entreprise = valeur_moyenne
            valeur_actions = valeur_entreprise - dette_nette
            
            st.metric("Valeur par EBITDA", f"{valeur_ebitda:,.0f} k€")
            st.metric("Valeur par résultat net", f"{valeur_resultat:,.0f} k€")
            st.metric("Valeur par CA", f"{valeur_ca:,.0f} k€")
            st.metric("Valeur moyenne entreprise", f"{valeur_entreprise:,.0f} k€")
            st.metric("Valeur des actions", f"{valeur_actions:,.0f} k€")
    
    else:  # Approche Patrimoniale
        st.subheader("🏛️ Approche Patrimoniale")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Actifs")
            actif_immobilise = st.number_input("Actif immobilisé (k€)", value=1500)
            actif_circulant = st.number_input("Actif circulant (k€)", value=800)
            plus_values_latentes = st.number_input("Plus-values latentes (k€)", value=200)
            actifs_incorporels = st.number_input("Actifs incorporels (k€)", value=300)
        
        with col2:
            st.markdown("### Passifs")
            dettes_financieres = st.number_input("Dettes financières (k€)", value=800)
            dettes_exploitation = st.number_input("Dettes d'exploitation (k€)", value=400)
            provisions = st.number_input("Provisions (k€)", value=100)
            moins_values_latentes = st.number_input("Moins-values latentes (k€)", value=50)
        
        # Calcul ANC
        actif_reel = actif_immobilise + actif_circulant + plus_values_latentes + actifs_incorporels
        passif_reel = dettes_financieres + dettes_exploitation + provisions + moins_values_latentes
        anc = actif_reel - passif_reel
        
        st.metric("Actif Net Comptable (ANC)", f"{anc:,.0f} k€")
        st.metric("Actif réel", f"{actif_reel:,.0f} k€")
        st.metric("Passif réel", f"{passif_reel:,.0f} k€")
        
        # Goodwill estimé
        st.markdown("### 🎯 Goodwill estimé")
        rentabilite_souhaitee = st.slider("Rentabilité souhaitée (%)", 8.0, 20.0, 12.0)
        resultat_net_recurrent = st.number_input("Résultat net récurrent (k€)", value=180)
        
        if rentabilite_souhaitee > 0:
            valeur_rentabilite = resultat_net_recurrent / (rentabilite_souhaitee/100)
            goodwill = valeur_rentabilite - anc
            valeur_totale = anc + max(0, goodwill)
            
            st.metric("Valeur de rentabilité", f"{valeur_rentabilite:,.0f} k€")
            st.metric("Goodwill estimé", f"{goodwill:,.0f} k€")
            st.metric("Valeur totale", f"{valeur_totale:,.0f} k€")

# Section Cas Pratiques
elif section == "🏢 Cas Pratiques":
    st.header("🏢 Études de Cas Complets")
    
    if not st.session_state.progression['cas_pratiques']:
        if st.button("✅ Marquer ce module comme complété"):
            st.session_state.progression['cas_pratiques'] = True
            st.session_state.notifications.append({
                "type": "success", 
                "message": "🎉 Module Cas Pratiques complété !", 
                "date": datetime.now().strftime("%Y-%m-%d")
            })
            st.rerun()
    
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
            
            # Graphique d'évolution
            annees = range(5)
            ca_projete = [ca * ((1 + croissance/100) ** i) for i in annees]
            
            fig_startup = go.Figure()
            fig_startup.add_trace(go.Scatter(
                x=list(annees),
                y=ca_projete,
                mode='lines+markers',
                name='CA projeté',
                line=dict(color='blue', width=3)
            ))
            fig_startup.update_layout(
                title="Projection de croissance du CA",
                xaxis_title="Années",
                yaxis_title="Chiffre d'affaires (k€)",
                height=300
            )
            st.plotly_chart(fig_startup, use_container_width=True)
    
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
            
            if gain_total > 0:
                st.success("✅ Optimisation possible")
            else:
                st.warning("⚠️ Revoir les objectifs")
        
        # Plan d'action
        st.markdown("### 🎯 Plan d'Action Recommandé")
        
        actions = [
            f"**Relance clients**: Réduire le délai de {delai_clients} à {objectif_clients} jours",
            f"**Optimisation stocks**: Passer de {delai_stocks} à {objectif_stocks} jours de stock",
            f"**Négociation fournisseurs**: Augmenter le délai de {delai_fournisseurs} à {objectif_fournisseurs} jours",
            f"**Gain total**: {gain_total:,.0f} k€ de trésorerie dégagée"
        ]
        
        for action in actions:
            st.write(f"• {action}")

# Section Prévisions IA (limité pour la démo)
elif section == "🤖 Prévisions IA":
    st.header("🤖 Prévisions Financières par Intelligence Artificielle")
    
    st.markdown("""
    Ce module utilise des algorithmes de machine learning pour prédire les tendances financières 
    basées sur des données historiques et des indicateurs économiques.
    """)
    
    tab1, tab2 = st.tabs(["📊 Prévision de CA", "🎯 Modèle Prédictif Avancé"])
    
    with tab1:
        st.subheader("Prévision de Chiffre d'Affaires par Régression")
        
        # Génération de données historiques simulées
        annees = list(range(2015, 2024))
        ca_historique = [1000, 1100, 1250, 1400, 1600, 1850, 2100, 2400, 2750]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Données Historiques**")
            df_historique = pd.DataFrame({
                'Année': annees,
                'CA (k€)': ca_historique
            })
            st.dataframe(df_historique, use_container_width=True)
            
            # Personnalisation
            croissance_moyenne = st.slider("Croissance moyenne attendue (%)", 1.0, 20.0, 12.0)
            volatilite = st.slider("Volatilité des prévisions", 1.0, 10.0, 3.0)
        
        with col2:
            # Préparation des données pour le modèle
            X = np.array(annees).reshape(-1, 1)
            y = np.array(ca_historique)
            
            # Entraînement du modèle
            model = LinearRegression()
            model.fit(X, y)
            
            # Prévisions
            annees_futures = list(range(2024, 2030))
            X_futur = np.array(annees_futures).reshape(-1, 1)
            predictions = model.predict(X_futur)
            
            # Ajout d'une composante aléatoire pour le réalisme
            np.random.seed(42)
            bruit = np.random.normal(0, volatilite/100 * predictions, predictions.shape)
            predictions_ajustees = predictions * (1 + croissance_moyenne/100) + bruit
            
            # Graphique des prévisions
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=annees, y=ca_historique,
                mode='lines+markers',
                name='Historique',
                line=dict(color='blue', width=3)
            ))
            
            fig.add_trace(go.Scatter(
                x=annees_futures, y=predictions_ajustees,
                mode='lines+markers',
                name='Prévisions IA',
                line=dict(color='red', width=3, dash='dash')
            ))
            
            fig.update_layout(
                title="Prévision de Chiffre d'Affaires par Intelligence Artificielle",
                xaxis_title="Année",
                yaxis_title="Chiffre d'Affaires (k€)",
                showlegend=True,
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Affichage des prévisions détaillées
            st.markdown("**Détail des Prévisions**")
            for annee, prediction in zip(annees_futures, predictions_ajustees):
                st.write(f"**{annee}**: {prediction:,.0f} k€")

# Section Données Réelles (limité pour la démo)
elif section == "🌍 Données Réelles":
    st.header("🌍 Analyse avec Données Réelles du Marché")
    
    tab1, tab2 = st.tabs(["📈 Actions Cotées", "📊 Benchmark Sectoriel"])
    
    with tab1:
        st.subheader("📈 Analyse d'Entreprises Cotées")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Sélection des entreprises
            entreprises = {
                "Apple": "AAPL",
                "Microsoft": "MSFT", 
                "Amazon": "AMZN",
                "Google": "GOOGL",
                "Tesla": "TSLA",
                "LVMH": "MC.PA",
                "L'Oréal": "OR.PA",
                "Airbus": "AIR.PA"
            }
            
            entreprise_choisie = st.selectbox("Choisissez une entreprise:", list(entreprises.keys()))
            ticker = entreprises[entreprise_choisie]
            periode = st.selectbox("Période d'analyse:", ["1mo", "3mo", "6mo", "1y", "2y", "5y"])
            
            if st.button("🔄 Charger les données"):
                with st.spinner("Chargement des données financières..."):
                    try:
                        # Récupération des données
                        stock = yf.Ticker(ticker)
                        historique = stock.history(period=periode)
                        info = stock.info
                        
                        # Sauvegarde dans la session
                        st.session_state.stock_data = {
                            'historique': historique,
                            'info': info,
                            'ticker': ticker
                        }
                        st.success("Données chargées avec succès !")
                        
                    except Exception as e:
                        st.error(f"Erreur lors du chargement: {e}")
        
        with col2:
            if 'stock_data' in st.session_state:
                data = st.session_state.stock_data
                historique = data['historique']
                info = data['info']
                
                # Affichage des indicateurs clés
                st.subheader(f"Indicateurs Clés - {ticker}")
                
                col_met1, col_met2, col_met3, col_met4 = st.columns(4)
                
                with col_met1:
                    prix_actuel = historique['Close'][-1]
                    variation = ((prix_actuel - historique['Close'][0]) / historique['Close'][0]) * 100
                    st.metric("Prix Actuel", f"{prix_actuel:.2f} $", f"{variation:+.2f}%")
                
                with col_met2:
                    per = info.get('trailingPE', 'N/A')
                    st.metric("P/E Ratio", f"{per if per != 'N/A' else 'N/A'}")
                
                with col_met3:
                    market_cap = info.get('marketCap', 0)
                    st.metric("Market Cap", f"{market_cap/1e9:.1f} B$")
                
                with col_met4:
                    dividend_yield = info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0
                    st.metric("Dividend Yield", f"{dividend_yield:.2f}%")
                
                # Graphique des prix
                fig = go.Figure()
                fig.add_trace(go.Candlestick(
                    x=historique.index,
                    open=historique['Open'],
                    high=historique['High'],
                    low=historique['Low'],
                    close=historique['Close'],
                    name='Prix'
                ))
                
                fig.update_layout(
                    title=f"Évolution du cours de {ticker}",
                    xaxis_title="Date",
                    yaxis_title="Prix ($)",
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)

# Section Mes Analyses
elif section == "💾 Mes Analyses":
    st.header("💾 Gestion de Mes Analyses")
    
    tab1, tab2, tab3 = st.tabs(["📁 Sauvegardes", "👥 Collaboration", "📤 Export"])
    
    with tab1:
        st.subheader("Sauvegarde des Analyses")
        
        # Formulaire de sauvegarde
        with st.form("sauvegarde_form"):
            nom_analyse = st.text_input("Nom de l'analyse", "Analyse Société X")
            description = st.text_area("Description", "Analyse complète des ratios et de la performance...")
            tags = st.text_input("Tags (séparés par des virgules)", "ratios, performance, valuation")
            
            if st.form_submit_button("💾 Sauvegarder l'analyse actuelle"):
                nouvelle_analyse = {
                    'id': len(st.session_state.analyses_sauvegardees) + 1,
                    'nom': nom_analyse,
                    'description': description,
                    'tags': tags,
                    'date': datetime.now().strftime("%d/%m/%Y %H:%M"),
                    'data': {
                        'ratios': {},
                        'equilibre': {}
                    }
                }
                st.session_state.analyses_sauvegardees.append(nouvelle_analyse)
                st.success("✅ Analyse sauvegardée avec succès !")
        
        # Liste des analyses sauvegardées
        st.subheader("Mes Analyses Sauvegardées")
        
        if st.session_state.analyses_sauvegardees:
            for analyse in st.session_state.analyses_sauvegardees:
                with st.expander(f"📊 {analyse['nom']} - {analyse['date']}"):
                    st.write(f"**Description**: {analyse['description']}")
                    st.write(f"**Tags**: {analyse['tags']}")
                    
                    col_act1, col_act2 = st.columns(2)
                    with col_act1:
                        if st.button(f"📖 Charger", key=f"load_{analyse['id']}"):
                            st.session_state.current_analysis = analyse
                            st.success("Analyse chargée !")
                    with col_act2:
                        if st.button(f"🗑️ Supprimer", key=f"del_{analyse['id']}"):
                            st.session_state.analyses_sauvegardees = [
                                a for a in st.session_state.analyses_sauvegardees 
                                if a['id'] != analyse['id']
                            ]
                            st.rerun()
        else:
            st.info("ℹ️ Aucune analyse sauvegardée pour le moment")

# Section Mon Dashboard
elif section == "📊 Mon Dashboard":
    st.header("📊 Mon Dashboard Personnel")
    
    # Calcul de la progression globale
    modules_completes = sum(st.session_state.progression.values())
    progression_totale = (modules_completes / len(st.session_state.progression)) * 100
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📚 Modules Complétés", f"{modules_completes}/6")
    with col2:
        st.metric("🎯 Progression Globale", f"{progression_totale:.0f}%")
    with col3:
        analyses_count = len(st.session_state.get('analyses_sauvegardees', []))
        st.metric("💾 Analyses Sauvegardées", analyses_count)
    with col4:
        quiz_score = st.session_state.get('quiz_score', 0)
        st.metric("🏆 Score Quiz", f"{quiz_score:.0f}%")
    
    # Graphique de progression
    st.subheader("📈 Ma Progression d'Apprentissage")
    
    modules = ['Fondamentaux', 'Ratios', 'Équilibre', 'Évaluation', 'Cas Pratiques', 'Quiz']
    progression_par_module = [
        st.session_state.progression.get('fondamentaux', False) * 100,
        st.session_state.progression.get('ratios', False) * 100,
        st.session_state.progression.get('equilibre', False) * 100,
        st.session_state.progression.get('evaluation', False) * 100,
        st.session_state.progression.get('cas_pratiques', False) * 100,
        st.session_state.progression.get('quiz', False) * 100
    ]
    
    fig_progression = go.Figure()
    fig_progression.add_trace(go.Bar(
        x=modules,
        y=progression_par_module,
        marker_color=['green' if p == 100 else 'orange' for p in progression_par_module]
    ))
    
    fig_progression.update_layout(
        title="Progression par Module",
        yaxis=dict(range=[0, 100]),
        height=300
    )
    
    st.plotly_chart(fig_progression, use_container_width=True)
    
    # Recommandations personnalisées
    st.subheader("🎯 Recommandations Personnalisées")
    
    col_rec1, col_rec2 = st.columns(2)
    
    with col_rec1:
        if not st.session_state.progression.get('fondamentaux', False):
            st.error("**📋 Priorité**: Commencez par les fondamentaux de l'analyse financière")
        elif not st.session_state.progression.get('ratios', False):
            st.warning("**⚡ Prochaine étape**: Maîtrisez l'analyse par les ratios")
        else:
            st.success("**🚀 Excellent**: Vous maîtrisez les bases ! Passez aux cas pratiques")
    
    with col_rec2:
        if analyses_count == 0:
            st.info("**💡 Astuce**: Sauvegardez vos premières analyses pour les retrouver plus tard")
        else:
            st.success(f"**📊 Actif**: Vous avez {analyses_count} analyses sauvegardées")

# Section Aide & Support
elif section == "❓ Aide & Support":
    st.header("❓ Centre d'Aide et Support")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Guide Utilisateur", "🎥 Tutoriels Vidéo", "❓ FAQ", "📞 Support"])
    
    with tab1:
        st.subheader("📖 Guide d'Utilisation Complet")
        
        with st.expander("🎯 Premiers Pas"):
            st.markdown("""
            **Bienvenue dans FinanceLab !**
            
            1. **Commencez** par le module "Fondamentaux" pour apprendre les bases
            2. **Pratiquez** avec les calculateurs interactifs
            3. **Testez** vos connaissances avec les quiz
            4. **Appliquez** vos compétences avec les cas pratiques
            """)
        
        with st.expander("📊 Comprendre les Ratios"):
            st.markdown("""
            **Les ratios clés à maîtriser:**
            
            - **ROE** (Return on Equity): Rentabilité des capitaux propres
            - **ROA** (Return on Assets): Efficacité de l'utilisation des actifs  
            - **Ratio d'endettement**: Niveau d'endettement de l'entreprise
            - **BFR** (Besoin en Fonds de Roulement): Besoin de financement du cycle d'exploitation
            """)
    
    with tab2:
        st.subheader("🎥 Tutoriels Vidéo")
        
        # Liens vers des tutoriels (simulés)
        tutoriels = [
            {"titre": "Maîtriser le BFR en 10 minutes", "duree": "10:15", "niveau": "Débutant"},
            {"titre": "Analyse DCF complète", "duree": "25:30", "niveau": "Avancé"},
            {"titre": "Ratios de rentabilité expliqués", "duree": "15:45", "niveau": "Intermédiaire"},
            {"titre": "Cas pratique PMI", "duree": "32:10", "niveau": "Expert"}
        ]
        
        for tuto in tutoriels:
            with st.expander(f"🎬 {tuto['titre']} ({tuto['duree']}) - {tuto['niveau']}"):
                st.write("**Description**: " + "Contenu du tutoriel détaillé...")
                st.info("🎥 Fonctionnalité vidéo à implémenter")
    
    with tab3:
        st.subheader("❓ Foire Aux Questions")
        
        faqs = [
            {
                "question": "Comment sauvegarder mes analyses ?",
                "reponse": "Utilisez le module 'Mes Analyses' et cliquez sur le bouton 'Sauvegarder' après chaque analyse."
            },
            {
                "question": "Puis-je utiliser l'application sur mobile ?",
                "reponse": "Oui ! FinanceLab est responsive et s'adapte à tous les appareils."
            },
            {
                "question": "Les données sont-elles sécurisées ?",
                "reponse": "Toutes vos données sont stockées localement dans votre navigateur. Nous ne collectons aucune donnée personnelle."
            }
        ]
        
        for faq in faqs:
            with st.expander(f"❔ {faq['question']}"):
                st.write(faq['reponse'])
    
    with tab4:
        st.subheader("📞 Support Technique")
        
        st.markdown("""
        **Besoin d'aide ? Contactez-nous :**
        
        📧 Email : ibugueye@ngorweb.com
        💬 Chat : Disponible 9h-18h
        📞 Téléphone : +33 7 81 53 62 33
        
        **Heures d'ouverture :**
        Lundi - Vendredi : 9h00 - 18h00
        Samedi : 10h00 - 16h00
        """)
        
        # Formulaire de contact
        with st.form("contact_form"):
            st.write("**Envoyez-nous un message**")
            nom = st.text_input("Votre nom")
            email = st.text_input("Votre email")
            message = st.text_area("Votre message")
            
            if st.form_submit_button("📤 Envoyer le message"):
                st.success("Message envoyé ! Nous vous répondrons dans les 24h.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "FinanceLab - Plateforme d'apprentissage de l'analyse financière • "
    "Développé par Amiharbi eyeug Xataxeli avec ❤️ et Streamlit"
    "</div>",
    unsafe_allow_html=True
)