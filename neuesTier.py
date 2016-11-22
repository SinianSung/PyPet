import PyPet as pet
import json
import pickle

mypet =pet.PyPet('murksi')

print(mypet.__dict__)
mypet.setHappiness(5)
print(mypet.__dict__)

#speichern eines tieres
pickle.dump(mypet,open('meinTier.p','wb'))

# laden eines tieres aus der Datei
with open('meinTier.p','rb') as f:
    newpet = pickle.load(f)

newpet.name = 'hansli'
print(newpet.__dict__)

# speichern mit json
with open('meinTier.json','w') as f:
    json.dump(mypet.__dict__,f)
    
for item in mypet.happyMoments:
    print(mypet.happyMoments[item])

