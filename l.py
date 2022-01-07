s = """
Agricultural Produce
Books/Stationery
Catering/Restaurant
Chemicals/Paints
Courier/Logistics Service Provider / Packers and Movers
Electrical /Electronics / Home Appliances
Event Management
FMCG /Food Products /Grocery
Furniture / Home Furnishing /Decor
Hardware / Ceramics / Sanitary / Supplies / House Shifting
Machinery/Mechanical Equipment 
Paint
Paper/Packaging/Printed Material
Pharmacy/medical/Healthcare
Plastic/Rubber
Textile/Garments/Accessories to Clothes
Timber/Plywood/laminates
"""
s =  s.strip()
import pprint
l = []
c = 0
for i in s.split('\n'):
    l.append((i.strip(),c))
    c += 1
pprint.pprint(l)