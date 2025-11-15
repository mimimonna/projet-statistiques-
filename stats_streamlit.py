import streamlit as st
import numpy as np

# Titre de l'application
st.title("Prédiction de la Qualité de l'Air (AQI)")

st.write("""
Cette application simule une prédiction de la qualité de l'air (AQI)
et affiche une alerte en fonction de la valeur prédite.
""")

# Simulation de la prédiction de l'AQI
# Pour cette démonstration, nous allons utiliser un slider pour simuler la moyenne des prédictions.
# En réalité, 'y_pred' proviendrait de votre modèle d'apprentissage automatique.

st.header("Saisir la Valeur AQI Prédite")
predicted_aqi = st.slider(
    "Déplacez le curseur pour simuler la moyenne des prédictions AQI :",
    min_value=0,
    max_value=250,
    value=75, # Valeur par défaut
    step=1
)

st.write(f"**AQI Prédit :** {predicted_aqi}")

# Système d'alerte basé sur la valeur prédite
st.header("Statut de la Qualité de l'Air")

if predicted_aqi > 150:
    st.error("🚨 Alerte pollution : qualité de l'air très mauvaise. Évitez toute activité extérieure.")
elif predicted_aqi > 100:
    st.warning("⚠️ Alerte modérée : la qualité de l'air est mauvaise. Évitez les activités sportives intenses en extérieur.")
else:
    st.success("✅ Qualité de l'air bonne. Profitez de l'extérieur !")

st.markdown("---")
st.info("Note : Ce n'est qu'une simulation. En production, 'predicted_aqi' serait le résultat de votre modèle.")

