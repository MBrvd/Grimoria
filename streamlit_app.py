import streamlit as st


st.markdown("## 🔥💧GRIMORIA 🌪️🌱")
st.markdown("### Le grimoire en ligne des animaux élémentaires")

c1 = st.container(border=True)
element = c1.selectbox(
    "Choisis ton élément", 
    options=["","🔥 Feu", "💧 Eau", "🌪️ Vent", "🌱 Terre"]
)

text = "TRLVRVWNOECZGUDEQFSSOUMEJDTNSSMRWESVWUGEIMFAWE"

def get_text_from_animal(offset:int):
    output = ""
    for i in range(offset,len(text), 4):
        output += text[i]
    return output

if element:
    c2 = st.container(border=True)
    animal = c2.text_input("Rentre ton animal élémentaire")
    validated = c2.button("Valider")
    output = ""
    if validated :
        if element == "🔥 Feu" and animal.upper() == "SALAMANDRE":
            output = get_text_from_animal(0)
            color = "red"
        elif element == "💧 Eau" and animal.upper() == "HIPPOCAMPE":
            output = get_text_from_animal(1)
            color = "blue"
        elif element == "🌪️ Vent" and animal.upper() == "HIRONDELLE":
            output = get_text_from_animal(2)
            color = "green"
        elif element == "🌱 Terre" and animal.upper() == "PHACOCHERE":
            output = get_text_from_animal(3)
            color = "grey"
        elif len(animal) != 10 and len(animal) != 0 :
            c2.error("Nombre de lettres invalide")
        else:
            c2.error("Code incorrect")

    if output : 
        c3 = st.container(border=True)
        c3.write("Code correct ! Voici ta récompense :")
        c3.write(f":{color}[{output}]")
        c3.write("Combine la avec les 3 autres éléments pendant l'épreuve commune")