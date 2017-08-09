import folium
import pandas

data = pandas.read_csv("ballparkLocation.csv")
lat = list(data["lat"])
lng = list(data["lng"])
teamname = list(data["teamname"])
ballpark = list(data["ballpark"])
address = list(data["address"])
location = list(data["location"])

info = pandas.read_csv("BallparkInfo.csv")

def number_seat(seats):
    num = info.loc[info["Team"] == seats]["Seating capacity"].tolist()
    nums = 0
    for x in num[0]:
        if x != ',':
            nums = nums*10 + int(x)
    return nums

def color_producer(value):
    if value < 40000:
        return 'green'
    elif 40000 <= value < 45000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[40.829167, -73.926389], zoom_start=5, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Stadiums")

for lt, ln, name, park, add, loc in zip(lat, lng, teamname, ballpark, address, location):
    seat = number_seat(name);
    html = ("<div style=\"font-size:13px\"><p><strong>"+str(name)+ "</strong></p><p><strong>"+str(park)+"</strong></p><p>"
    +str(add)+"</p><p>"+str(loc)+"</p><p><strong>"+"Seating capacity: "+str(seat)+"</strong></p></div>")
    iframe = folium.IFrame(html = html, width=180, height=180)
    popup = folium.Popup(iframe, max_width=200)

    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=popup,
    radius=10, fill_color=color_producer(seat), color='grey', fill_opacity=0.7))

map.add_child(fgv)

map.save("Map1.html")
