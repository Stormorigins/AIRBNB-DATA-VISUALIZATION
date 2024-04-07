import streamlit as st
from streamlit_option_menu import option_menu
import pymongo
import pandas as pd
pd.set_option("display.max_columns",None) #The maximum width in characters of a column in the repr of a pandas data structure
import warnings
warnings.filterwarnings("ignore")# To hide warnings
import plotly.express as px


# DATA= pd.read_csv("C:/Users/Aishwarya MMPL/Documents/GUVI_PYTHON/Projects/AIRBNB_DATA.csv")


#STREAMLIT PART

st.set_page_config(page_title="Airbnb",page_icon="🌍",layout="wide",initial_sidebar_state="expanded")

#Background image
page_bg_img='''<style>[data-testid="stAppViewContainer"]{background-color:#F5F5F5;}</style>'''
st.markdown(page_bg_img,unsafe_allow_html=True)

#Title
st.write("""<p style="font-family:Alegreya;font-size: 35px; text-align: center">
         AIRBNB DATA ANALYSIS</p>""", unsafe_allow_html=True)
st.text(" ")

#Set the background image
# bg_img = '''<style>[data-testid="stAppViewContainer"] {background-image: 
#                 url('https://img.freepik.com/premium-vector/grey-white-abstract-technology-background-hi-tech-digital-connect-communication-high-technology-concept-science-technology-background_262356-135.jpg?size=626&ext=jpg&ga=GA1.1.735520172.1710892800&semt=ais');
#                 background-size: cover;background-repeat: no-repeat;}</style>'''
# st.markdown(bg_img, unsafe_allow_html=True)

def dataframe():
    df= pd.read_csv("C:/Users/Aishwarya MMPL/Documents/GUVI_PYTHON/Projects/AIRBNB_DATA.csv")
    return df
df= dataframe()

#MENU BAR
SELECT = option_menu(menu_title=None,options = ["HOME","DATA VISUALIZATION","ABOUT"],icons =["house-heart","pie-chart","chat"],
    default_index=0,orientation="horizontal",styles={"icon": {"color": "black", "font-size": "20px"},"nav-link": {"font-size": "15px","font-family":"PhonePeSans,sans-serif,Helvetica,Arial", 
    "text-align": "center", "margin": "0px", "--hover-color": "#FF7F50"},
    "nav-link-selected": {"background-color": "#7FD8BE"}})

if SELECT == "HOME":
    
    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')

if SELECT == "DATA VISUALIZATION":
    st.text(" ")
    select = option_menu(menu_title=None,options = ["PRICE ANALYSIS","AVAILABILITY ANALYSIS","LOCATION BASED","GEOSPATIAL VISUALIZATION","TOP CHARTS"],icons =["coin","bag-heart","compass","geo-alt","diagram-3-fill"],
    default_index=0,orientation="horizontal",styles={"icon": {"color": "black", "font-size": "15px"},"nav-link": {"font-size": "11px","font-family":"PhonePeSans,sans-serif,Helvetica,Arial", 
    "text-align": "center", "margin": "0px", "--hover-color": "#FFE4C4"},
    "nav-link-selected": {"background-color": "#90EE90"}})

    if select == "PRICE ANALYSIS":
        st.write("""<p style="font-family:Alegreya;font-size: 20px; text-align: center">PRICE DIFFERENCE</p>""", unsafe_allow_html=True)

        col1,col2,col3= st.columns(3)
        with col1:
            country= st.selectbox("Select the Country for price analysis",df["country"].unique())
            df1= df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

        with col2:
            room_ty= st.selectbox("Select the Room Type for price analysis",df1["room_type"].unique())
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

        with col3:
            proper_ty= st.selectbox("Select the Property type for price analysis",df2["property_type"].unique())
#pie chart   
        col1,col2= st.columns(2)
        with col1:
            df4= df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_pi= px.pie(df_pie, values="price", names= "host_response_time",hole=0.5,hover_data=["bedrooms"],color_discrete_sequence=px.colors.qualitative.T10,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME")
            fig_pi.update_traces(textfont=dict(color='#fff'))
            fig_pi.update_layout(autosize=True, height=500, width=1000,
                            margin=dict(t=80, b=30, l=70, r=40),
                            title_font=dict(size=20, family="Muli, sans-serif"),
                            font=dict(color='#8a8d93'),
                            legend=dict(orientation="v", yanchor="bottom", y=0.5, xanchor="right", x=1.4)
                            )

            st.plotly_chart(fig_pi)
#bar chart
        df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
        df_bar.reset_index(inplace= True)

        fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Emrld_r,height=500, width= 1100)
        fig_bar.update_layout(title_font=dict(size=20, family="Muli, sans-serif"),
                                font=dict(color='#8a8d93'))
        st.plotly_chart(fig_bar)

        col1,col2,col3,col4,col5= st.columns(5)
        with col3:
            host_time= st.selectbox("Select the type of host response",df4["host_response_time"].unique())

        col1,col2= st.columns(2)
        with col1:
            df5= df4[df4["host_response_time"]==host_time]
            df_bar=pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_bar.reset_index(inplace= True)
#barchart1
            fig= px.bar(df_bar,x='bed_type', y=['minimum_nights', 'maximum_nights'],barmode='group',title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
                color_discrete_sequence=px.colors.sequential.Viridis_r, width=600, height=500)
            fig.update_layout(title_font=dict(size=17, family="Muli, sans-serif"),
                                font=dict(color='#8a8d93'),
                                legend=dict(orientation="v"))
            st.plotly_chart(fig)
        with col2:
            df5= df4[df4["host_response_time"]==host_time]
            df_bar=pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_bar.reset_index(inplace= True)
#barchart2
            fig= px.bar(df_bar,x='bed_type', y=["bedrooms","beds","accommodates","price"],barmode='group',title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
                color_discrete_sequence=px.colors.sequential.Blackbody_r, width=600, height=500)
            fig.update_layout(title_font=dict(size=17, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="v"))
            st.plotly_chart(fig)
    
    if select == "AVAILABILITY ANALYSIS":
        def datafr():
            df_a= pd.read_csv("C:/Users/Aishwarya MMPL/Documents/GUVI_PYTHON/Projects/AIRBNB_DATA.csv")
            return df_a
        df_a= datafr()

        st.write("""<p style="font-family:Alegreya;font-size: 20px; text-align: center">AVAILABILITY ANALYSIS</p>""", unsafe_allow_html=True)
        col1,col2= st.columns(2)
        with col1:
            country_a= st.selectbox("Select the Country for availability analysis",df_a["country"].unique())
            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)
        with col2:
            property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)
#availabilty plot
        fig_30= px.bar(df2_a, x="availability_30",y= ["room_type","bed_type","is_location_exact"],title="AVAILABILITY 30",color_discrete_sequence=px.colors.sequential.Peach_r,height=500, width= 1100)
        fig_30.update_layout(title_font=dict(size=17, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="h", yanchor="top", y=1.15, xanchor="right", x=1.25))
        st.plotly_chart(fig_30)

        fig_60= px.bar(df2_a, x="availability_60",y= ["room_type","bed_type","is_location_exact"],title="AVAILABILITY 60",color_discrete_sequence=px.colors.sequential.Blues_r,height=500, width= 1100)
        fig_60.update_layout(title_font=dict(size=17, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="h", yanchor="top", y=1.15, xanchor="right", x=1.25))
        st.plotly_chart(fig_60)

        fig_90= px.bar(df2_a, x="availability_90",y= ["room_type","bed_type","is_location_exact"],title="AVAILABILITY 60",color_discrete_sequence=px.colors.sequential.Aggrnyl_r,height=500, width= 1100)
        fig_90.update_layout(title_font=dict(size=17, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="h", yanchor="top", y=1.15, xanchor="right", x=1.25))
        st.plotly_chart(fig_90)

        fig_365= px.bar(df2_a, x="availability_365",y= ["room_type","bed_type","is_location_exact"],title="AVAILABILITY 60",color_discrete_sequence=px.colors.sequential.Greens_r,height=500, width= 1100)
        fig_365.update_layout(title_font=dict(size=17, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="h", yanchor="top", y=1.15, xanchor="right", x=1.25))
        st.plotly_chart(fig_365)

        col1,col2,col3,col4,col5= st.columns(5)
        with col3:
            roomtype_a= st.selectbox("Select the Room Type of Availability", df2_a["room_type"].unique())
            room= df2_a[df2_a["room_type"] == roomtype_a]

        df= pd.DataFrame(room.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df.reset_index(inplace= True)
#Barchart
        fig= px.bar(df, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
            title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",color_discrete_sequence=px.colors.sequential.Sunset_r,width=1200,height=700)
        
        fig.update_layout(title_font=dict(size=17, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="v", yanchor="top", y=0.7, xanchor="right", x=1.35))
        st.plotly_chart(fig)

    if select == "LOCATION BASED":

        def datafr():
            df= pd.read_csv("C:/Users/Aishwarya MMPL/Documents/GUVI_PYTHON/Projects/AIRBNB_DATA.csv")
            return df

        df_l= datafr()

        st.write("""<p style="font-family:Alegreya;font-size: 20px; text-align: center">LOCATION ANALYSIS</p>""", unsafe_allow_html=True)

        col1,col2= st.columns(2)
        with col1:
            country_l= st.selectbox("Select the Country",df_l["country"].unique())
            df1_l= df_l[df_l["country"] == country_l]
            df1_l.reset_index(drop= True, inplace= True)
        
        with col2:
            proper_ty_l= st.selectbox("Select the Property type",df1_l["property_type"].unique())
            df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
            df2_l.reset_index(drop= True, inplace= True)

        differ_max_min= df2_l['price'].max()-df2_l['price'].min()

        val_sel= st.radio("Select the Price Range",[str("(0% to 25% of the Value)"),str("(25% to 50% of the Value)"),str("(50% to 75% of the Value)"),str("(75% to 100% of the Value)")],index=0,horizontal=True)
        st.write("")
        
        def select_the_df(sel_val):
            if sel_val == str("(0% to 25% of the Value)"):
                st.write(str('Minimum value ')+str(df2_l['price'].min())+' '+str('to Maximum value')+' '+str(differ_max_min*0.25 + df2_l['price'].min()))   
                df_val_25= df2_l[df2_l["price"] <= differ_max_min*0.25 + df2_l['price'].min()]
                df_val_25.reset_index(drop= True, inplace= True)
                return df_val_25
            
            elif sel_val == str("(25% to 50% of the Value)"):
                st.write(str('Minimum value ')+str(differ_max_min*0.25 + df2_l['price'].min())+' '+str('to Maximum value')+' '+str(differ_max_min*0.50 + df2_l['price'].min()))
                df_val_50= df2_l[df2_l["price"] >= differ_max_min*0.25 + df2_l['price'].min()]
                df_val_50= df_val_50[df_val_50["price"] <= differ_max_min*0.50 + df2_l['price'].min()]
                df_val_50.reset_index(drop= True, inplace= True)
                return df_val_50 
            
            elif sel_val == str("(50% to 75% of the Value)"):
                st.write(str('Minimum value ')+str(differ_max_min*0.50 + df2_l['price'].min())+' '+str('to Maximum value')+' '+str(differ_max_min*0.75 + df2_l['price'].min()))
                df_val_75= df2_l[df2_l["price"] >= differ_max_min*0.50 + df2_l['price'].min()]
                df_val_75= df_val_75[df_val_75["price"] <= differ_max_min*0.75 + df2_l['price'].min()]
                df_val_75.reset_index(drop= True, inplace= True)
                return df_val_75 
            
            elif sel_val == str("(75% to 100% of the Value)"):
                st.write(str('Minimum value ')+str(differ_max_min*0.75 + df2_l['price'].min())+' '+str('to Maximum value')+' '+str(differ_max_min*1 + df2_l['price'].min()))
                df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.75 + df2_l['price'].min()]
                df_val_100= df_val_100[df_val_100["price"] <= differ_max_min*1.00 + df2_l['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100 
            
        df_val_sel= select_the_df(val_sel)
        st.write("")
        st.dataframe(df_val_sel)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)
#barchart
        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', color_continuous_midpoint=px.colors.sequential.Agsunset_r,width=1000,orientation="v")
        fig_1.update_layout(title_font=dict(size=20, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="v", yanchor="top", y=0.7, xanchor="right", x=1.35))
        st.plotly_chart(fig_1)

        col1,col2,col3,col4,col5= st.columns(5)
        with col3:
            room_rty_l= st.selectbox("Select the Room Type", df_val_sel["room_type"].unique())
#barchart
        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_rty_l]
        fig_2= px.bar(df_val_sel_rt, y= ["street","host_location","host_neighbourhood"],x="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='v', color_discrete_sequence=px.colors.plotlyjs.Earth,width=1000)
        fig_2.update_layout(title_font=dict(size=20, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="v", yanchor="top", y=0.7, xanchor="right", x=1.35))
        st.plotly_chart(fig_2)
#barchart
        fig_4= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        fig_4.update_layout(title_font=dict(size=20, family="Muli, sans-serif"),font=dict(color='#8a8d93'),legend=dict(orientation="v", yanchor="top", y=0.7, xanchor="right", x=1.35))
        st.plotly_chart(fig_4)

    if select == "GEOSPATIAL VISUALIZATION":
        st.write("""<p style="font-family:Alegreya;font-size: 20px; text-align: center">GEO VISUALIZATION</p>""", unsafe_allow_html=True)

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='accommodates',size="price",
                        color_continuous_scale=px.colors.cyclical.IceFire,hover_name='name',range_color=(0,20), mapbox_style="open-street-map",
                        zoom=1,title='Geospatial Distribution of Listings',width=1450,height=700)
        fig_4.update_layout(title_font=dict(size=20, family="Muli, sans-serif"),font=dict(color='#8a8d93'))
        st.plotly_chart(fig_4)

    if select == "TOP CHARTS":
        col1, col2= st.columns(2)
        with col1:
            country_t= st.selectbox("Select the Country_t",df["country"].unique())

        df1_t= df[df["country"] == country_t]

        with col2:
            property_ty_t= st.selectbox("Select the Property_type_t",df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)
        with col1:
            
            fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                            title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room_Type_t",df2_t_sorted["room_type"].unique())

        df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

        df3_t_sorted_price= df3_t.sort_values(by= "price")

        df3_t_sorted_price.reset_index(drop= True, inplace = True)

        df3_top_50_price= df3_t_sorted_price.head(100)

        fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,df3_top_50_price["price"].max()),
                                title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "greens",
                                 title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                range_color=(0,df3_top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)

if SELECT == "ABOUT":

    st.header("ABOUT THIS PROJECT")

    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')
 

   



        
