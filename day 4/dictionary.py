capitals={'usa':'washington','india':'delhi','china':'beijing','russia':'moscow'}
hello={12:12,'india':'mumbai'}
print(hello.items())
print(capitals['russia'])
print(capitals.get('germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'germany':'berlin'})
capitals.update({'usa':'las vegas'})
capitals.pop('india')
#capitals.clear()

for key,values in capitals.items():
    print(key,values)