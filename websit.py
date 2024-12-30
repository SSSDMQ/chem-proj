import streamlit as st
st.title("Thermochemistry Solver")
st.subheader('Developed by Saud Al-Qahtani', divider=("red"))

def page_1():
    st.header("Calculate the total energy of a thermochemical reaction", divider=("grey"))
    m = st.number_input("Insert the total mass of the substance (in grams)")
    h_in = st.number_input("What was the initial enthlapy (heat) of the substance (in Celsius)")
    h_f = st.number_input("What was the final enthlapy (heat) of the reaction (in Celsius)")
    c = st.number_input("What is the specific heat of the subsrance?")
    hdelta = h_f - h_in
    # num_inputs = st.number_input("How many unique elements does this substance have?", min_value=1, step=1)

    # inputs = {}

   #  for i in range(num_inputs):
     #    var_name = f"value_{i+1}"
      #  inputs[var_name] = st.number_input("Insert the molar mass of element no. " + str(i+1), step=1)

    if st.button("Calculate Total Energy"):
   
        #st.write("The total energy is:")
       # molarm = 0  
    
        # for var_name, value in inputs.items():
            # st.write(f"{var_name}: {value}")
     #      molarm += value
        q = m * c * hdelta
        if q < 0:
            a = " and the reaction is **exothermic**."
        elif q > 0:
            a = " and the reaction is **endothermic**."
        else:
            a = " and the reaction is **athermic**."
        st.write("The total energy is: " + f"**{q}**" + " J," + str(a))


def page_2():
    st.title("Coming Soon...")
    

def page_3():
     st.title("Coming Soon...")


page_options = ["Energy Calculator", "TBD", "TBD2"]
selected_page = st.sidebar.radio("Select a Page", page_options)


if selected_page == "Energy Calculator":
    page_1()
elif selected_page == "TBD":
    page_2()
elif selected_page == "TBD2":
    page_3()



#  c = st.number_input("What is the specific heat of the subsrance?") c = st.number_input("What is the specific heat of the subsrance?")
    
