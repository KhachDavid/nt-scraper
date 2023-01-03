# import faker
from faker import Faker
from unidecode import unidecode
from nations import nations_fifa
from translate import Translator
translator= Translator(to_lang="english")

# open a file to write the fake names
f = open("fake_names.txt", "w")

# Print the fake name
for i in range(1):
    # loop over nations_fifa
    for nation in nations_fifa:
        country_name = nation[0]
        continent = nation[1]
        population = nation[2]
        capital = nation[3]
        political_climate = nation[4]
        corruption_level = nation[5]
        fan_loyalty = nation[6]

        faker_locale_options = nation[7]

        # create a faker object

        if faker_locale_options[0] == 'name':
            fake = Faker(faker_locale_options[1])
            first_name = fake.first_name_male()
            
            fake = Faker(faker_locale_options[3])
            last_name = fake.last_name_male()

        else:
            # generate a fake name
            fake = Faker(faker_locale_options)
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()

        # convert name to english alphabet if it is not
        #first_name = unidecode(first_name)
        #last_name = unidecode(last_name)

        # translate the name to english
        first_name = translator.translate(first_name)
        last_name = translator.translate(last_name)

        # capitalize the first letter of the name
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()


        # print the name and the country name to the file
        f.write(first_name + " " + last_name + " : " + country_name)
         
        # write a new line
        f.write("\n")
