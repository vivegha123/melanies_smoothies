# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: customize your smoothie! : cup_with_straw:")
st.write(
    """Orders that need to filled.""") 

cnx= st.connection("snowflake")
session =cnx.session()
my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()
editable_df = st.experimental_data_editor(my_dataframe)

cnx= st.connection("snowflake")
session =cnx.session()


ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:'
    , my_dataframe
)

if ingredients_list:
    ingredients_string = '' 

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    # st.write(ingredients_string)    

    my_insert_stmt = """insert into smoothies.public.orders(ingredients)
                        values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    st.write(my_insert_stmt)
    st.stop()


   time_to_insert = st.button('submit order')
   
   if time_to_insert:
       session.sql(my_insert_stmt).collect()

       st.success('Your Smoothie is ordered!', icon="✅")

