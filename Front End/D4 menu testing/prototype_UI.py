# imports
import streamlit as st

st.title = 'Interface Prototype'

# sidebar
select_topic = []
select_subtopic = []
selected = -1
sub_selected = 0

# menu and submenu
menu_button1 = ('Fuel Utilization', ('New Plants', 'Usage', 'Growth'))
menu_button2 = ('CO2 Emissions', ('Trends', 'Maps', 'Renewable'))
menu_button3 = ('Grid Reliability', ('Trends', 'Maps'))
menu_button4 = ('Sector Cost', ())
menu_button5 = ('Fossil Fuel Efficiency', ('Fuel Type', 'Plant Age'))
menu_buttons = (menu_button1, menu_button2, menu_button3, menu_button4, menu_button5)

@st.cache
# create menu and radio buttons
for index_x, x in enumerate(menu_buttons):
    # get the parent topic from the first part of the menu_button 1-5 tuple
    new_topic = st.sidebar.button(x[0])
    if new_topic:
        selected = index_x
        st.write(x)
    select_topic.append(new_topic)
    sub_selected = 0
    if index_x == selected:
        # get the sub topics from the embedded tuple, can pass directly
        new_radio = st.sidebar.radio('Select a subgroup', x[1])
        for index_y, y in enumerate(x[1]):
            if new_radio == y:
                sub_selected = index_y
                st.write(y)
            select_subtopic.append(new_radio)
