# Compare 2 files that list all of the unique proteins found to see which ones are cell type specific
inCell1 = open('HS_CB660_unique.txt')
outCell1 = open('HS_CB660_only.txt', 'w')
for line1 in inCell1:
  unique = True
  inCell2 = open('HS_G166_1105_unique.txt')
  for line2 in inCell2:
    if line1 == line2:
      unique = False
  if unique == True:
    outCell1.write(line1)
  inCell2.close()
outCell1.close()
inCell1.close()

inCell2 = open('HS_G166_1105_unique.txt')
outCell2 = open('HS_G166_1105_only.txt', 'w')
for line2 in inCell2:
  unique = True
  inCell1 = open('HS_CB660_unique.txt')
  for line1 in inCell1:
    if line2 == line1:
      unique = False
  if unique == True:
    outCell2.write(line2)
  inCell1.close()
outCell2.close()
inCell2.close()

inCell1.close()
inCell2.close()
outCell2.close()
