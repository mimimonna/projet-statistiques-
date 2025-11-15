import streamlit as st
import numpy as np
import random

#titre de l'application
st.set_page_config(page_title="Qualité de l'Air en Direct", layout="centered")

st.title(" la qualité de l'air de ta ville en Direct")
st.write("""
Cette application vous informe sur la qualité de l'air dans différentes villes
et vous fournit des conseils pratiques pour les habitants et les pouvoirs publics.
""")

#liste des villes pour le sélecteur
cities = [
    'Brasilia',
    'Cairo',
    'Dubai',
    'London',
    'Sydney',
    'New York', ]

#sélection une ville
selected_city = st.selectbox(
    "Sélectionnez une ville :",
    cities
)

#une fonction pour simuler l'AQI en fonction de la ville sélectionnée
#dans application réelle la fonction ferait un appel API pour obtenir des données 
def simulate_aqi(city):
    """
    Simule une valeur d'AQI basée sur la ville.
    Les valeurs sont aléatoires pour la démonstration.
    """
    if city == 'Dubai':
        #simule un AQI plus varié pour une capitale
        aqi = random.randint(40, 180)
    elif city == 'New York':
        aqi = random.randint(30, 160)
    elif city == 'London':
        aqi = random.randint(20, 140)
    else:
        #AQI plus bas pour les autres villes dans cette simulation
        aqi = random.randint(10, 120)
    return aqi

#simuler l'AQI actuel pour une ville sélectionné
current_aqi = simulate_aqi(selected_city)

#on détermine le niveau d'alerte le message et les conseils sur l'AQI
def get_aqi_status(aqi):
    """
    Retourne le statut, la couleur et les conseils en fonction de la valeur AQI.
    """
    status = {
        "message": "",
        "color": "",  #couleur pour l'affichage
        "advice_habitants": [],
        "advice_pouvoirs_publics": []
    }

    if aqi > 150:
        status["message"] = "Alerte pollution : Qualité de l'air très mauvaise !"
        status["color"] = "red"
        status["advice_habitants"] = [
            "Évitez de sortir, surtout les personnes sensibles (enfants, seniors, asthmatiques).",
            "Si vous devez sortir, portez un masque de protection.",
            "Reportez les activités sportives en extérieur."
        ]
        status["advice_pouvoirs_publics"] = [
            "Déclencher le plan d'action anti-pollution (alerte rouge).",
            "Mettre en place la circulation alternée ou restreindre l'accès aux véhicules les plus polluants.",
            "Renforcer les messages de prévention et d'information du public."
        ]
    elif aqi > 100:
        status["message"] = "Alerte modérée : Qualité de l'air mauvaise."
        status["color"] = "orange"
        status["advice_habitants"] = [
            "Réduisez les activités physiques intenses en extérieur.",
            "Pour les personnes sensibles, évitez les sorties prolongées.",
            "Aérez votre logement aux heures les moins polluées (tôt le matin ou tard le soir)."
        ]
        status["advice_pouvoirs_publics"] = [
            "Déclencher le plan d'action anti-pollution (alerte orange).",
            "Recommander la réduction de vitesse sur les axes routiers.",
            "Sensibiliser les entreprises à réduire leurs émissions."
        ]
    elif aqi > 50:
        status["message"] = "Qualité de l'air moyenne."
        status["color"] = "yellow"
        status["advice_habitants"] = [
            "Aucune restriction majeure mais les personnes très sensibles peuvent ressentir une gêne.",
            "Continuez à aérer votre logement régulièrement."
        ]
        status["advice_pouvoirs_publics"] = [
            "Maintenir la vigilance et surveiller l'évolution.",
            "Poursuivre les actions de fond pour améliorer la qualité de l'air."
        ]
    else:
        status["message"] = "Qualité de l'air bonne. Vous pouvez profitez de l'extérieur !"
        status["color"] = "green"
        status["advice_habitants"] = [
            "Profitez pleinement des activités extérieures.",
            "Aérez votre logement sans restriction."
        ]
        status["advice_pouvoirs_publics"] = [
            "Continuer les efforts pour maintenir une bonne qualité de l'air.",
            "Communiquer sur les bénéfices d'un air sain."
        ]
    return status

#pour obtenir le statut actuel de l'AQI
aqi_status = get_aqi_status(current_aqi)

#affichage de l'AQI actuel avec un style
st.markdown(f"""
<div style="
    background-color: {'#ef4444' if aqi_status['color'] == 'red' else '#f97316' if aqi_status['color'] == 'orange' else '#eab308' if aqi_status['color'] == 'yellow' else '#22c55e'};
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 20px;
    color: white;
">
    <p style="font-size: 1.25rem; font-weight: 600;">Qualité de l'air actuelle à {selected_city} :</p>
    <p style="font-size: 3.75rem; font-weight: 800; margin: 10px 0;">{current_aqi}</p>
    <p style="font-size: 1.875rem; font-weight: 700;">{aqi_status['message']}</p>
</div>
""", unsafe_allow_html=True)

#section des conseils pour les habitants
st.subheader("Pour les habitants :")
for advice in aqi_status["advice_habitants"]:
    st.markdown(f"- {advice}")

#section des conseils pour les pouvoirs publics
st.subheader("Pour les pouvoirs publics et des actions :")
for advice in aqi_status["advice_pouvoirs_publics"]:
    st.markdown(f"- {advice}")

# Section de partage social (simulée)
st.markdown("### Partagez l'information :")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Partager sur Twitter"):
        st.info("Partage sur Twitter !")
with col2:
    if st.button("Partager par message"):
        st.info("Partage par message!")
with col3:
    if st.button("Partager par Email"):
        st.info("Partage par Email !")

st.markdown("---")
st.info("Note :Les données AQI sont simulées pour cette démonstration..")
