import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/banana")
streamlit.text(fruityvice_response)

# New section to display fruityvice api response

streamlit.header("Fruityvice Fruit Advice!")


# for adding banana
# fruityvice_response_banana = requests.get("https://fruityvice.com/api/fruit/banana")
# streamlit.text(fruityvice_response_banana)

# streamlit.header("Fruityvice Fruit Advice! banana added")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

# create therepeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information") 
    # streamlit.write('The user entered ', fruit_choice)
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
# import snowflake.connector
streamlit.header("The fruit load list contains:")
# snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall();


# def insert_row_snowflake(new_fruit):
#     with my_cnx.cursor() as my_cur:
#         my_cur.execute("insert into fruit_load_list values ( 'from streamlit')")
#         return "Thanks for adding" + new_fruit

def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values (' " +  + " ')")
        return "Thanks for adding" + new_fruit


add_my_fruit = streamlit.text_input('what fruit would you like to add?')
# add a button to load the fruit
# if streamlit.button('Add a Fruit to the List'):
#     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     back_from_function = insert_row_snowflake(add_my_fruit)
#     streamlit.text(back_from_function) 

# *************************************************************
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
  


# if streamlit.button('Get Fruit Load List'):

#     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     # my_cur = my_cnx.cursor()
#     my_data_rows = get_fruit_load_list()
#     streamlit.dataframe(my_data_rows)
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

# my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# my_data_row = my_cur.fetchall()

# streamlit.text("the fruit load list contains:")
# streamlit.text(my_data_row)

# my_data_row = my_cur.fetchone()

# my_cur.execute("select * from fruit_load_list")
# my_data_rows = my_cur.fetchall()


# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_row)



fruit_choice_two = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('The user entered ', fruit_choice_two)



