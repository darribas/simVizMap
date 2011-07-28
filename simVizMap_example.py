# Import class and functions required
from simVizMap import SimVizMap, set_h_tags, set_v_tags

# Set link to csv file
csv_link = 'rejRate_anselinRey.csv'

# Create graphical object for the map
plot_object = SimVizMap(csv_link, cb_orientation='vertical')

# Set labels
sizes = ['225', ' 169', '121', '81', '49', '25']
models = ['LM', 'Moran'] * 6
sp = ['-.8', '-.4', '0', '.4', '8'] * 2

# Plot the labels on the Map
set_v_tags(-0.15, sizes, plot_object.p, weight='bold', rotation=90, fontsize=15)
set_v_tags(-0.05, models, plot_object.p, fontsize=10)
set_h_tags(-0.075, ['Rho', 'Lambda'], plot_object.p, weight='bold', fontsize=15)
set_h_tags(-0.025, sp, plot_object.p, fontsize=10)
set_h_tags(1.05, ['Sp. Lag', 'Sp. Error'], plot_object.p, weight='bold', fontsize=15)

# Show the image on-the-fly
#plot_object.show()

# Alternatively, save to a file
output_png = 'simVizMap_example.png'
plot_object.save(output_png)
