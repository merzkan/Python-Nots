import pandas as pd

data = pd.read_csv("pandas\\datasets\\nba.csv")
data.dropna(inplace=True)#NAN değerlerini silip göster
#print(data.columns)
#Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight','College', 'Salary'],dtype='object')

#data["Name"] = data["Name"].str.upper() #namedeki sütundakileri büyük harf yap
#            Name            Team  Number Position   Age Height  Weight        College     Salary
#0  AVERY BRADLEY  Boston Celtics     0.0       PG  25.0    6-2   180.0          Texas  7730337.0
#1    JAE CROWDER  Boston Celtics    99.0       SF  25.0    6-6   235.0      Marquette  6796117.0
#3    R.J. HUNTER  Boston Celtics    28.0       SG  22.0    6-5   185.0  Georgia State  1148640.0
#6  JORDAN MICKEY  Boston Celtics    55.0       PF  21.0    6-8   235.0            LSU  1170960.0
#7   KELLY OLYNYK  Boston Celtics    41.0        C  25.0    7-0   238.0        Gonzaga  2165160.0

#data["Team"] = data["Team"].str.lower() #team sütunundakileri hepsini küçük harf yap
#            Name            Team  Number Position   Age Height  Weight        College     Salary
#0  Avery Bradley  boston celtics     0.0       PG  25.0    6-2   180.0          Texas  7730337.0
#1    Jae Crowder  boston celtics    99.0       SF  25.0    6-6   235.0      Marquette  6796117.0
#3    R.J. Hunter  boston celtics    28.0       SG  22.0    6-5   185.0  Georgia State  1148640.0
#6  Jordan Mickey  boston celtics    55.0       PF  21.0    6-8   235.0            LSU  1170960.0
#7   Kelly Olynyk  boston celtics    41.0        C  25.0    7-0   238.0        Gonzaga  2165160.0

#data["index"] = data["Name"].str.find('a') # Namede a geçen isimlere a'nın indexsini yeni sütunda yaz
#            Name            Team  Number  ...        College     Salary index 
#0  Avery Bradley  Boston Celtics     0.0  ...          Texas  7730337.0     8 
#1    Jae Crowder  Boston Celtics    99.0  ...      Marquette  6796117.0     1 
#3    R.J. Hunter  Boston Celtics    28.0  ...  Georgia State  1148640.0    -1 
#6  Jordan Mickey  Boston Celtics    55.0  ...            LSU  1170960.0     4 
#7   Kelly Olynyk  Boston Celtics    41.0  ...        Gonzaga  2165160.0    -1

#data = data[data.Name.str.contains("Jordan")]
#6      Jordan Mickey        Boston Celtics  ...        LSU   1170960.0
#98    DeAndre Jordan  Los Angeles Clippers  ...  Texas A&M  19689000.0
#110  Jordan Clarkson    Los Angeles Lakers  ...   Missouri    845059.0
#175     Jordan McRae   Cleveland Cavaliers  ...  Tennessee    111196.0
#201      Jordan Hill        Indiana Pacers  ...    Arizona   4000000.0
#257     Jordan Adams     Memphis Grizzlies  ...       UCLA   1404600.0        
#289  Jordan Hamilton  New Orleans Pelicans  ...      Texas   1015421.0 

#data = data.Team.str.replace(' ','-').str.replace('*','') #bosluk kısmını - yapar \\ yıldız buldugu yeri siler
#0     Boston-Celtics
#1     Boston-Celtics
#3     Boston-Celtics
#6     Boston-Celtics
#7     Boston-Celtics
#8     Boston-Celtics
#9     Boston-Celtics
#10    Boston-Celtics
#11    Boston-Celtics
#12    Boston-Celtics

#name sütununu isim ve soy isim olarak ikiye ayırmak istiyoruz
#data[["FirstName","LastName"]] = data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)
#           Name            Team  Number  ...     Salary  FirstName   LastName
#0     Avery Bradley  Boston Celtics     0.0  ...  7730337.0      Avery    Bradley
#1       Jae Crowder  Boston Celtics    99.0  ...  6796117.0        Jae    Crowder
#3       R.J. Hunter  Boston Celtics    28.0  ...  1148640.0       R.J.     Hunter
#6     Jordan Mickey  Boston Celtics    55.0  ...  1170960.0     Jordan     Mickey
#7      Kelly Olynyk  Boston Celtics    41.0  ...  2165160.0      Kelly     Olynyk
#8      Terry Rozier  Boston Celtics    12.0  ...  1824360.0      Terry     Rozier
#9      Marcus Smart  Boston Celtics    36.0  ...  3431040.0     Marcus      Smart
#10  Jared Sullinger  Boston Celtics     7.0  ...  2569260.0      Jared  Sullinger
#11    Isaiah Thomas  Boston Celtics     4.0  ...  6912869.0     Isaiah     Thomas
#12      Evan Turner  Boston Celtics    11.0  ...  3425510.0       Evan     Turner
#
#[10 rows x 11 columns]



print(data.head(10)) 