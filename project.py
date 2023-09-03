import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter


@st.cache_data
def load_data():
    food=pd.read_csv("datasets/africa_food_prices.csv")
    food.drop(columns=['Unnamed: 0','mp_commoditysource','currency_id','price','month_number'], inplace = True)
    food=food.rename(columns={'country_id':'Country_ID','country':'Country','state_id':'State_ID',
                    'state':'State','market_id':'Market_ID','market':'Market','produce_id':'Produce_ID',
                    'produce':'Produce', 'currency':'Currency',
                    'pt_id ':'PT_ID','market_type':'Market_Type','um_unit_id':'Um_Unit_ID',
                     'quantity':'Quantity','year':'Year','price_in_usd':'Price_in_usd','month_name':'Month_name'})
    

    food.loc[food['Market'] == 'National Average', 'State'] = food.loc[food['Market'] == 'National Average', 'State'].fillna(value='National Average')
    food.loc[food['Market'] == 'Nalut', 'State'] = food.loc[food['Market'] == 'Nalut', 'State'].fillna(value='Nalut')
    food.loc[food['Market'] == 'Azzintan', 'State'] = food.loc[food['Market'] == 'Azzintan', 'State'].fillna(value='Azzintan')
    food.loc[food['Market'] == 'Ghat', 'State'] = food.loc[food['Market'] == 'Ghat', 'State'].fillna(value='Ghat')
    food.loc[food['Market'] == 'AlMarj', 'State'] = food.loc[food['Market'] == 'AlMarj', 'State'].fillna(value='AlMarj')
    mozambique_fill = {
             'Nampula':'Nampula',                
             'Maputo':'Maputo',                 
             'Manica':'Manica',                 
             'Gorongoza':'Gorongoza',             
             'Chokwe':'Chokwe',                 
             'Angónia':'Angónia',                
             'Lichinga':'Lichinga',               
             'Beira':'Beira',                  
             'Pemba':'Pemba',                  
             'Maxixe':'Maxixe',                 
                    'Tete':'Tete',                   
                    'Mocuba':'Mocuba',                                  
                    'Montepuez':'Montepuez',              
                    'Chimoio':'Chimoio',                
                    'Quelimane':'Quelimane',              
                    'Massinga':'Massinga',               
                    'Inhambane':'Inhambane',              
                    'Alto Molócuè':'Alto Molócuè',           
                    'Ribaue':'Ribaue',                 
                    'Mutarara':'Mutarara',               
                    'Nhamatanda':'Nhamatanda',             
                    'Xai Xai':'Xai Xai',                
                    'Cuamba':'Cuamba',                  
                    'Milange':'Milange',                 
                    'Nacala':'Nacala',                  
                    'Govuro':'Govuro',                  
                    'Caia':'Caia',                    
                    'Panda':'Panda',                   
                    'Mandimba':'Mandimba',                
                    'Chibuto':'Chibuto',                 
                    'Namaacha':'Namaacha',                
                    'Gondola':'Gondola',                
                    'Vilanculos':'Vilanculos',              
                    'Morrumbene':'Morrumbene',             
                    'Inhassoro':'mozambique',               
                    'Mabote':'Mabote',              
                    'Balama':'Balama',                  
                    'Namuno':'Namuno',                  
                    'Murrupula':'Murrupula',              
                    'Inharrime':'Inharrime',              
                    'Funhalouro':'Funhalouro',              
                    'Macanga':'Macanga',               
                    'Changara':'Changara',                
                    'Báruè':'Báruè',                 
                    'Moamba':'Moamba',                
                    'Boane':'Boane',                   
                    'Malema':'Malema',                  
                    'Buzi':'Buzi',                    
                    'Manhica':'Manhica',                
                    'Chicualacuala Mapai':'Chicualacuala Mapai',   
                    'Bela Vista':'Bela Vista',            
                    'Cidade da Matola':'Cidade da Matola' }
    food['State'] = food.apply(lambda row: mozambique_fill.get(row['Market']) if pd.isna(row['State']) else row['State'], axis=1)
    libya_fill = {
    'Brak':'Brak',          
    'Sebha':'Sebha',             
    'Zliten':'Zliten',            
    'Ubari':'Ubari',             
    'Tobruk':'Tobruk',            
    'Algatroun':'Algatroun',         
    'Ghiryan':'Ghiryan',           
    'Albayda':'Albayda',           
    'Tarhuna':'Tarhuna',           
    'Bani Waleed':'Bani Waleed',       
    'Zwara':'Zwara',             
    'Benghazi':'Benghazi',          
    'Suq Aljumaa':'Suq Aljumaa',       
    'Abusliem':'Abusliem',          
    'Alkufra':'Alkufra',           
    'Aljufra':'Aljufra',           
    'Sabratha':'Sabratha',          
    'Derna':'Derna',             
    'Azzawya':'Azzawya',           
    'Misrata':'Misrata',           
    'Ghadamis':'Ghadamis',          
    'Sirt':'Sirt',              
    'Ejdabia':'Ejdabia',           
    'Al Aziziya':'Al Aziziya',        
    'Alkhums':'Alkhums',           
    'Tripoli center':'Tripoli center',     
    'Hai Alandalus':'Hai Alandalus',      
    'Yefren':'Yefren',             
    'Tajoura':'Tajoura',            
    'Msallata':'Msallata',           
    'Ashshgega':'Ashshgega',          
    'Ain Zara':'Ain Zara',           
    'Janzour':'Janzour',            
    'Murzuq':'Murzuq',             
    'Wadi Etba':'Wadi Etba' 
    }
    food['State'] = food.apply(lambda row: libya_fill.get(row['Market']) if pd.isna(row['State']) else row['State'], axis=1)
    south_sudan_fill = {
    'Konyokonyo':'Konyokonyo',   
    'Jau':'Jau',              
    'Aweil Town':'Aweil Town',       
    'Bor':'Bor',              
    'Rumbek':'Rumbek',           
    'Malakal':'Malakal',          
    'Bentiu':'Bentiu',           
    'Torit':'Torit',            
    'Kuajok':'Kuajok',           
    'Yida':'Yida',             
    'Minkaman':'Minkaman',         
    'Yambio':'Yambio',           
    'Aniet':'Aniet',            
    'Rubkona':'Rubkona',          
    'Bunj':'Bunj',             
    'Kapoeta South':'Kapoeta South',    
    'Makpandu':'Makpandu',         
    'Melut':'Melut',            
    'Suk Shabi':'Suk Shabi',        
    'Wunrok':'Wunrok',           
    'Akobo':'Akobo'
    } 
    food['State'] = food.apply(lambda row: south_sudan_fill.get(row['Market']) if pd.isna(row['State']) else row['State'], axis=1)
    chad_fill = {
        'Ndjamena':'Ndjamena',          
    'Moussoro':'Moussoro',              
    'Moundou':'Moundou',               
    'Abeche':'Abeche',                
    'Sarh':'Sarh',                  
    'Mongo':'Mongo',               
    'Mao':'Mao',                  
    'Am Timan':'Am Timan',             
    'Bol':'Bol',                  
    'Oum Hadjer':'Oum Hadjer',           
    'Aboudeia':'Aboudeia',             
    'Bousso':'Bousso',               
    'Abdi':'Abdi',                 
    'Gore':'Gore',                 
    'Bokoro':'Bokoro',               
    'Iriba':'Iriba',                
    'Goz Beida':'Goz Beida',            
    'Massakory':'Massakory',            
    'Amdam':'Amdam',                
    'Biltine':'Biltine',              
    'Laï':'Laï',                  
    'Mandelia':'Mandelia',             
    'Bongor':'Bongor',               
    'Kélo':'Kélo',                 
    'Ngouri':'Ngouri',               
    'Peni':'Peni',                 
    'Nokou':'Nokou',                 
    'Benoye':'Benoye',                
    'Kyabe':'Kyabe',                 
    'Mbaïbokoum':'Mbaïbokoum',            
    'Mbaïnamar':'Mbaïnamar',             
    'Gueledeng':'Gueledeng',             
    'Fianga':'Fianga',                
    'Maro':'Maro',                  
    'Moissala':'Moissala',              
    'Pala':'Pala',                  
    'Koumra':'Koumra',                
    'Doba':'Doba',                  
    'Beboto':'Beboto',                
    'Lere':'Lere',                  
    'Krim Krim':'Krim Krim',             
    'Ati':'Ati',                   
    'Bodo':'Bodo',                  
    'Bebedja':'Bebedja',               
    'Guereda':'Guereda',               
    'Massenya':'Massenya',              
    'Massaguet':'Massaguet',             
    'Am-Zoer':'Am-Zoer',               
    'Melfi':'Melfi',                 
    'Mondo':'Mondo',                  
    'Yao':'Yao',                    
    'Bitkine':'Bitkine',                
    'Mangalme':'Mangalme',               
    'Haraze Mangueigne':'Haraze Mangueigne',      
    'Oumhadjer':'Oumhadjer',               
    'Amdjarass':'Amdjarass',               
    'Faya':'Faya'
    }
    food['State'] = food.apply(lambda row: chad_fill.get(row['Market']) if pd.isna(row['State']) else row['State'], axis=1)
    swaziland_fill = {
        'Hhohho':'Hhohho',    
    'Shiselweni':'Shiselweni',    
    'Manzini':'Manzini',       
    'Lubombo':'Lubombo'
    }
    food['State'] = food.apply(lambda row: swaziland_fill.get(row['Market']) if pd.isna(row['State']) else row['State'], axis=1)
    sorted_food = food.sort_values('Price_in_usd', ascending=False)
    top10 = sorted_food.head(20)
    return food


st.title("Africa_food_price Dashboard")

try:
    food = load_data()
    Produce = food.Produce.unique()
    Produce_selection = st.multiselect('Choose Produce', Produce, [Produce[0], Produce[1]])
    Produce_selected = food[food["Produce"].isin(Produce_selection)]
    
    # table
    st.write("""### Top 20 rows of Produce selected""")
    st.write(Produce_selected.head(20)) 
    
    #bar chat
    st.write("""### Sum of price by Selected Product(s)""")
    bar1 =  Produce_selected.groupby(['Produce'])['Price_in_usd'].sum().sort_values(ascending=True)
    st.bar_chart(bar1)
except ValueError as e:
    st.error("""
            Error
    """ %e.reason)

def main():
    st.write("""### Sum of Price by Selected Years""")
   
    # Load the data
    food = load_data()

    # Create a multiselect widget for selecting years
    all_years = sorted(food['Year'].unique())
    years_selected = st.multiselect('Select Year(s)', all_years, default=all_years)
    

    if not years_selected:
        st.warning('Please select at least one year.')
        return

    # Filter the data for selected years
    selected_data = food[food['Year'].isin(years_selected)]
    
    def format_Millions(x, pos):
        return f"${x / 1e6:.2f}M"
    formatter = FuncFormatter(format_Millions)

    # Create a line plot for sum of price vs. year
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
    sns.lineplot(x='Year', y='Price_in_usd', data=selected_data, estimator='sum', ci=None, palette='viridis')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.xlabel('Year')
    plt.ylabel('Sum of Price in USD')
    plt.title('Sum of Price vs. Year')
    plt.grid(True)
    st.pyplot(fig)
    
    
    
    st.write("""### Sum of Price by Selected Countires""")
    Country = food.Country.unique()
    Country_selection = st.multiselect('Select Countries', Country, [Country[0], Country[1]])
    if not Country_selection:
        st.warning('Please select at least one Country.')
        return

    # Filter the dataset based on selected countries
    filtered_Country = food[food["Country"].isin( Country_selection)]
    def format_Millions(x, pos):
        return f"${x / 1e6:.2f}M"
    formatter = FuncFormatter(format_Millions)

    # Create a Seaborn plot for the sum of prices by country
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(x="Country", y="Price_in_usd", data= filtered_Country, estimator=sum, ci=None)
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45)
    plt.xlabel("Country")
    plt.ylabel("Sum Price (USD)")
    st.pyplot(fig3)
   
    
    st.write("""### Sum of Price by Selected Months""")

    # Create a multiselect widget for selecting years
    all_months = sorted(food['Month_name'].unique())
    months_selected = st.multiselect('Select Months(s)', all_months, default=all_months)
    

    if not months_selected:
        st.warning('Please select at least one year.')
        return

    # Filter the data for selected years
    selected_months = food[food['Year'].isin(months_selected)]
    
    def format_Millions(x, pos):
        return f"${x / 1e6:.2f}M"
    formatter = FuncFormatter(format_Millions)

    # Create a line plot for sum of price vs. year
    fig2, ax2 = plt.subplots(figsize=(13, 13))
    sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
    sns.lineplot(x='Month_name', y='Price_in_usd', data=selected_data, estimator='sum', ci=None, palette='viridis')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.xlabel('Year')
    plt.ylabel('Sum of Price in USD')
    plt.title('Sum of Price vs. Months')
    plt.grid(True)
    st.pyplot(fig2)
    
    
    
    
               
if __name__ == "__main__":
    main()
