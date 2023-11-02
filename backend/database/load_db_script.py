import csv
import random
import pymongo

asian_cities = {
      "New Delhi": "The water bodies surrounding India comprise a diverse and vital ecosystem that plays a crucial role in the nation's environment and livelihoods. India is home to numerous rivers, lakes, and coastal areas, each with its unique characteristics and challenges.<br><br>The Ganges, Yamuna, Brahmaputra, and many other rivers are central to India's cultural and economic landscape, providing water for agriculture, industry, and domestic use. However, these water bodies face considerable challenges, including pollution from industrial and agricultural runoff, which has led to concerns about water quality and its impact on human health.<br><br>India's coastal regions are home to rich marine ecosystems, supporting fisheries and biodiversity. But these areas also confront issues like coastal erosion, rising sea levels, and overfishing, which threaten the delicate balance of these ecosystems.<br><br>Efforts are underway to address these challenges, with the government implementing various conservation and water quality improvement programs. International cooperation, sustainable practices, and community involvement are essential for safeguarding the water bodies surrounding India and ensuring a sustainable and healthy environment for future generations.", 
      "Beijing": "China boasts a vast and diverse network of water bodies, including rivers, lakes, and coastal regions, each with its unique ecological, economic, and cultural significance. The Yangtze and Yellow Rivers are prominent, serving as lifeblood for agriculture, industry, and transportation. However, these waterways grapple with issues such as pollution, over-extraction, and flood control.<br><br>China's extensive coastline encompasses the Bohai Sea, Yellow Sea, East China Sea, and South China Sea, fostering rich marine ecosystems and supporting vital fisheries. But coastal areas face challenges like rising sea levels, habitat degradation, and pollution from industrial activities.<br><br>Inland, China's numerous lakes, such as the vast Poyang and Dongting Lakes, play a pivotal role in regulating water resources and supporting biodiversity. However, they too confront pollution and habitat loss.<br><br>Efforts are ongoing to address these issues, including ambitious conservation programs and water quality improvement initiatives. Sustainable practices, cooperation with neighboring nations, and community engagement are crucial to ensure the well-being of China's water bodies and the ecological balance of these vital ecosystems.", 
      "Jakarta": "Indonesia, an archipelagic nation, is blessed with an abundance of water bodies, each contributing to its ecological and cultural diversity. The country's network of rivers, including the mighty Mekong, Kalimantan, and Barito, provides essential water resources for agriculture and transportation. However, these waterways are under pressure due to pollution, deforestation, and land-use changes.<br><br>Indonesia's vast expanse of coastline, stretching across the Indian and Pacific Oceans, supports thriving marine ecosystems and coastal communities. Coral reefs, mangroves, and seagrass beds are home to diverse marine life and offer livelihoods through fishing and tourism. Yet, these areas are threatened by issues like coral bleaching, illegal fishing, and plastic pollution.<br><br>Inland, the country's numerous lakes, such as Lake Toba and Lake Sentani, contribute to biodiversity and cultural heritage. However, they face challenges like pollution and overfishing.<br><br>Efforts are underway to protect and conserve these water bodies, including marine protected areas and reforestation programs. International collaboration, sustainable practices, and community involvement are vital to ensure the continued health and resilience of Indonesia's invaluable water ecosystems.", 
      "Dhaka": "Bangladesh, with its intricate network of rivers and deltaic landscapes, is defined by its water bodies, including the Ganges, Brahmaputra, and Meghna Rivers. These waterways are central to the nation's culture, agriculture, and transportation, serving as the lifeblood of the country. However, they face complex challenges, such as river erosion, flooding, and pollution from industrial and agricultural sources.<br><br>The extensive coastline along the Bay of Bengal supports rich marine biodiversity and sustains fisheries that are vital for the economy and livelihoods. Yet, coastal regions contend with rising sea levels, cyclones, and habitat degradation.<br><br>Bangladesh's numerous inland water bodies, including the Sundarbans mangrove forest, provide unique ecosystems and are home to iconic species like the Royal Bengal tiger. Nevertheless, these areas face threats from deforestation, overfishing, and pollution.<br><br>Efforts are ongoing to address these challenges, including disaster preparedness measures and conservation initiatives. Sustainable practices, international collaboration, and community engagement are key to preserving Bangladesh's water bodies and the well-being of its people and environment.", 
      "Tokyo": "Japan's water bodies offer a diverse and dynamic landscape, shaped by its geographical location and volcanic terrain. The country is blessed with a wealth of rivers, including the Shinano, Tone, and Kitakami Rivers, which provide freshwater resources, support agriculture, and are essential for hydroelectric power generation. Nevertheless, these waterways face challenges such as water pollution and flood control.<br><br>Japan's extensive coastline along the Pacific Ocean and the Sea of Japan sustains a vibrant marine environment and a rich tradition of fisheries. The seas surrounding Japan are home to an array of species, and the nation is renowned for its seafood. However, issues like overfishing, habitat destruction, and marine pollution demand careful management.<br><br>Inland, Japan boasts numerous lakes, like Lake Biwa and Lake Towada, contributing to the country's natural beauty and biodiversity. Despite their relative isolation, these lakes can experience water quality issues due to nutrient runoff and invasive species.<br><br>Japan is committed to preserving its water bodies through conservation efforts and water management practices, emphasizing sustainable fishing and environmental protection. International collaboration and ongoing research are essential to ensure the well-being of these crucial ecosystems.", 
      "Manila": "The Philippines, an archipelagic nation, is blessed with an abundance of water bodies that shape its environment and culture. The country's rivers, including the Cagayan and Agusan Rivers, play a vital role in irrigation, transportation, and energy production. However, these waterways face challenges such as pollution, deforestation, and soil erosion.<br><br>The extensive Philippine coastline, facing both the Pacific Ocean and the South China Sea, harbors diverse marine ecosystems and supports thriving fisheries. Coral reefs, seagrass beds, and mangroves are teeming with marine life, but they confront threats like coral bleaching, illegal fishing, and plastic pollution.<br><br>Inland, the country's lakes, such as Lake Lanao and Taal Lake, are not only sources of freshwater but also significant cultural landmarks. However, they are vulnerable to issues like sedimentation and pollution.<br><br>The Philippines is actively engaged in conservation efforts, establishing marine sanctuaries and watershed management programs. Sustainable practices, international cooperation, and community involvement are critical to preserving these invaluable water ecosystems and safeguarding the country's natural heritage.", 
      "Hanoi": "Vietnam's water bodies play a fundamental role in the nation's landscape, culture, and economy. The Mekong River, Red River, and numerous other waterways are essential for agriculture, transportation, and energy production. However, these rivers face complex challenges, including erosion, water pollution, and the impacts of hydropower dam construction upstream.<br><br>The extensive coastline along the South China Sea sustains rich marine ecosystems and supports vibrant fisheries, which are vital for the country's economy. Vietnam's coastal regions are renowned for their mangrove forests, coral reefs, and diverse marine life, but they are threatened by climate change, illegal fishing, and pollution.<br><br>Inland, Vietnam boasts a variety of lakes, such as Ba Be Lake and West Lake, each with its unique characteristics and cultural significance. These lakes face issues like water quality degradation and overfishing.<br><br>Vietnam is actively engaged in conservation and water resource management efforts, with a focus on sustainable agriculture and fisheries practices. International collaboration and community involvement are crucial to safeguard the nation's water ecosystems and ensure the well-being of its people and environment.", 
      "Bangkok": "Thailand's water bodies are a vital part of the country's geography and culture. Its network of rivers, including the Chao Phraya and Mekong Rivers, serves as a lifeline for agriculture, transportation, and energy production. These waterways, however, face challenges such as pollution, sedimentation, and the effects of dam construction.<br><br>Thailand's extensive coastline along the Andaman Sea and the Gulf of Thailand supports rich marine ecosystems, contributing to a thriving fishing industry and tourism. Coastal areas are known for their coral reefs, mangroves, and diverse marine life, but they are threatened by overfishing, illegal practices, and coastal development.<br><br>Inland, the nation has several lakes, such as Kwan Phayao and Songkhla Lake, which provide water resources and cultural value. However, these lakes encounter issues like water quality degradation and invasive species.<br><br>Thailand is actively involved in conservation efforts, promoting sustainable fishing and environmental protection. Collaboration with neighboring countries and community engagement is vital to safeguard Thailand's water ecosystems and ensure the well-being of its environment and people.", 
      "Naypyidaw": "Myanmar is characterized by its diverse water bodies, which are integral to the nation's environment and livelihoods. The Irrawaddy River, one of the country's primary rivers, plays a crucial role in agriculture, transportation, and culture. However, it faces issues like water pollution, deforestation, and land erosion.<br><br>The extensive coastline along the Andaman Sea in the west and the Bay of Bengal in the south sustains a rich marine environment and supports a significant fishing industry. Myanmar's coastal regions, with their mangroves, coral reefs, and diverse marine species, are vital for local economies. Nevertheless, they confront challenges such as illegal fishing, overexploitation, and habitat degradation.<br><br>Inland, Myanmar boasts a range of lakes, including Inle Lake and Indawgyi Lake, which contribute to the nation's natural beauty and biodiversity. These lakes face issues like sedimentation and water quality deterioration.<br><br>Myanmar is actively engaged in conservation and water resource management, emphasizing sustainable practices and community involvement. Collaboration with neighboring countries and international efforts are essential to safeguard these vital water ecosystems and ensure the well-being of the country's environment and people.", 
      "Seoul": "South Korea's water bodies, though relatively small in size compared to some neighboring nations, play a significant role in the country's landscape and culture. The Han River, Nakdong River, and a network of smaller rivers are essential for agriculture, transportation, and urban life. These waterways encounter challenges like pollution, dam construction, and water scarcity in some regions.<br><br>South Korea's coastline along the Yellow Sea and the Sea of Japan supports diverse marine ecosystems and a thriving fishing industry. Coastal areas are known for their tidal flats, seaweed farms, and abundant marine species. However, they face issues like coastal erosion, habitat loss, and marine pollution.<br><br>Inland, the country has numerous reservoirs and lakes, including Daecheong Lake and Soyang Lake, which provide water resources and recreational opportunities. These lakes can experience problems like water quality degradation and invasive species.<br><br>South Korea actively promotes water conservation and sustainable management practices, with a focus on mitigating water pollution and maintaining water availability. International collaboration and community participation are crucial to preserving the nation's valuable water ecosystems and ensuring the well-being of its environment and people.", 
      "Kuala Lumpur": "Malaysia is renowned for its abundant and diverse water bodies, which are integral to the nation's natural beauty, economy, and culture. The country's rivers, including the Rajang, Kinabatangan, and Pahang Rivers, play a vital role in agriculture, transportation, and biodiversity. However, they face challenges such as water pollution, deforestation, and habitat degradation.<br><br>Malaysia's extensive coastline along the South China Sea sustains rich marine ecosystems and supports a flourishing fishing industry. Coastal areas are known for their mangrove forests, coral reefs, and diverse marine life, but they are threatened by overfishing, illegal practices, and coastal development.<br><br>Inland, the nation has a range of lakes and reservoirs, such as Kenyir Lake and Tasik Bera, which provide water resources and recreational opportunities. These water bodies face issues like water quality deterioration and invasive species.<br><br>Malaysia is actively involved in conservation and sustainable water resource management, emphasizing the importance of protecting its ecosystems and ensuring the well-being of its environment and people. Collaboration with neighboring countries and international initiatives is essential to safeguard these invaluable water resources.", 
      "Kathmandu": "Nepal's water bodies, despite being a landlocked nation, are a vital part of its landscape, culture, and economy. The country's rivers, including the Ganges, Gandaki, and Koshi Rivers, are essential for agriculture, hydropower generation, and transportation. However, they face challenges like sedimentation, flooding, and water pollution.<br><br>Nepal's high-altitude geography also boasts numerous lakes, with Rara Lake and Phewa Lake being notable examples. These lakes serve as freshwater resources, tourist attractions, and support unique ecosystems. Nevertheless, they encounter threats like climate change impacts and water quality degradation.<br><br>Nepal's glacial meltwater and monsoon rains contribute to the Ganges and Brahmaputra River systems, affecting the water supply and livelihoods of millions downstream in India and Bangladesh.<br><br>The nation actively participates in conservation and sustainable water resource management, with an emphasis on protecting its fragile ecosystems and harnessing hydropower for economic development. Collaboration with neighboring countries and international support is crucial for the effective management and preservation of Nepal's water resources.", 
      "Pyongyang": "North Korea, a secretive and isolated nation, possesses a limited but strategically important network of water bodies. The Taedong River is one of its primary rivers, flowing through the capital city, Pyongyang. It serves as a vital water resource for the region, supporting agriculture and industry. However, water quality issues and pollution affect the river.<br><br>The nation's coastline along the Yellow Sea is relatively short, but it's essential for fishing and marine activities. Coastal areas include tidal flats, estuaries, and ports, supporting the livelihoods of coastal communities. These areas face challenges like overfishing and environmental degradation.<br><br>Inland, North Korea has several lakes and reservoirs, such as Lake Chon and Lake Samji, which contribute to water resources and irrigation. These water bodies also grapple with issues like water quality deterioration.<br><br>North Korea's water management and conservation efforts remain largely closed off to the international community. Limited access to information makes it challenging to assess the state of the nation's water bodies comprehensively. Collaborative efforts with neighboring countries and international organizations are essential to address water-related issues and improve the well-being of North Korea's environment and people.", 
      "Colombo": "Sri Lanka's water bodies are integral to the island nation's geography and culture. Its rivers, including the Mahaweli, Kelani, and Kalu Rivers, are crucial for agriculture, hydropower generation, and transportation. Sri Lanka's rivers often face issues such as pollution, sedimentation, and seasonal flooding.<br><br>The island is surrounded by the Indian Ocean, and its coastal areas are renowned for pristine beaches, coral reefs, and marine life. Coastal communities depend on fishing, and the tourism industry thrives on these coastal attractions. However, coastal erosion, pollution, and illegal fishing practices pose challenges.<br><br>Inland, Sri Lanka boasts a range of lakes and reservoirs like Kandy Lake and Victoria Reservoir, which contribute to irrigation and water supply. These water bodies confront issues such as water quality degradation and invasive species.<br><br>Sri Lanka actively promotes water conservation and sustainable management practices, with a focus on mitigating water pollution and maintaining water availability. Collaboration with neighboring countries and international initiatives is crucial to preserving the nation's invaluable water ecosystems and ensuring the well-being of its environment and people.", 
      "Phnom Penh": "Cambodia's water bodies are a defining feature of its landscape and are integral to the nation's culture, economy, and environment. The Mekong River, one of the world's great rivers, flows through the country, supporting agriculture, transportation, and fishing. Cambodia's unique and extensive floodplains, like the Tonle Sap, are a crucial part of its ecosystem, but they face challenges from climate change impacts and dam construction upstream.<br><br>The nation's coastal areas along the Gulf of Thailand are home to stunning beaches, mangrove forests, and vibrant marine life. Fishing is a vital industry for coastal communities, though overfishing and coastal development are concerns.<br><br>Inland, Cambodia has a wealth of lakes and reservoirs, such as the Boeung Kak and Yeak Laom Lakes, which provide water resources and support local communities. Water quality issues and deforestation affect these areas.<br><br>Cambodia is actively engaged in water resource management and conservation, emphasizing the importance of preserving its unique ecosystems and ensuring the well-being of its environment and people. Collaboration with neighboring countries and international initiatives is vital to safeguard these invaluable water resources.", 
      "Vientiane": "Laos, a landlocked country in Southeast Asia, is defined by its diverse and pristine water bodies. The Mekong River, one of the world's great rivers, flows through the nation, playing a central role in its culture and economy. Laos' stunning and ecologically rich floodplains, such as the Si Phan Don (Four Thousand Islands), are vital for agriculture and support unique ecosystems. These areas face challenges from dam construction and climate change.<br><br>Laos' mountainous terrain is home to numerous rivers, waterfalls, and lakes, including the Nam Ou River and Kuang Si Falls, which offer breathtaking landscapes and recreational opportunities. Despite their natural beauty, some of these areas encounter issues like deforestation and water quality degradation.<br><br>Laos is actively involved in water resource management and conservation, emphasizing sustainable practices and preservation of its rich ecosystems. Collaborative efforts with neighboring countries and international organizations are crucial to addressing challenges and maintaining the well-being of its environment and people.", 
      "Bishkek": "Kyrgyzstan, a mountainous country in Central Asia, boasts an array of pristine and high-altitude water bodies. The country's most prominent river is the Naryn, which flows through the country, merging with the Kara Darya to form the Syr Darya. These rivers are vital for agriculture and energy generation but face challenges from glacial melt due to climate change.<br><br>Kyrgyzstan's mountain lakes are renowned for their crystal-clear waters and stunning settings. Issyk-Kul, one of the world's largest alpine lakes, dominates the landscape. Other notable lakes include Song-Kol and Sary-Chelek, which offer recreational opportunities and biodiversity. However, water quality concerns and the risk of pollution are present.<br><br>The country actively engages in water resource management, focusing on sustainable practices and safeguarding its pristine ecosystems. Collaborative efforts with neighboring nations and international organizations are essential to addressing challenges and ensuring the well-being of Kyrgyzstan's environment and people.", 
      "Ashgabat": "Turkmenistan, a predominantly arid country in Central Asia, has limited water bodies compared to some of its neighbors. The Amu Darya River flows through its northeastern border, supplying water for irrigation and supporting agriculture. However, the river's water is heavily utilized upstream, which can lead to shortages downstream.<br><br>The Caspian Sea, the world's largest inland body of water, borders Turkmenistan to the west. The country has a short coastline along the Caspian, and the sea is a significant resource for fishing and potential oil and gas reserves beneath its seabed.<br><br>Inland, Turkmenistan has several small lakes, such as the Sarygamysh and Altyn Asyr Lakes, which serve as water reservoirs for irrigation and livestock. However, some of these lakes face issues related to water quality and salinity.<br><br>Turkmenistan actively engages in water resource management, focusing on efficient irrigation practices and sustainable water use in agriculture. Collaborative efforts with neighboring countries surrounding the Amu Darya and the Caspian Sea are crucial to address water-related challenges and ensure the well-being of Turkmenistan's environment and people.", 
      "Singapore": "Singapore, a small island nation in Southeast Asia, is surrounded by a network of water bodies that significantly influence its culture and development. The Singapore Strait to the south provides access to the global maritime trade routes and supports a bustling port, making Singapore a vital hub for international trade.<br><br>The island's reservoirs, like the MacRitchie and Upper Seletar Reservoirs, serve as sources of freshwater supply and offer recreational spaces with lush greenery. These reservoirs are essential for water security in a region with limited natural water resources.<br><br>Singapore's Marina Bay is a breathtaking example of coastal development, with its iconic skyline, waterfront promenades, and recreational areas. It combines urban living with sustainable water management through advanced drainage and wastewater systems.<br><br>Singapore actively engages in water resource management, focusing on water sustainability and innovative water technologies. These efforts are crucial for addressing water challenges in a densely populated urban environment and ensuring a sustainable future for Singapore's water needs and environment.", 
      "Ulaanbaatar": "Mongolia, a vast and landlocked country in East Asia, is characterized by its diverse but relatively sparse water bodies. The country's primary river is the Orkhon River, which flows through the central region, providing essential water resources for agriculture and livestock grazing. The Selenge River in the north is another significant watercourse, eventually joining Russia's Lake Baikal.<br><br>Mongolia boasts numerous pristine lakes, with Khövsgöl Nuur being the most famous. This stunning alpine lake is often referred to as the 'Blue Pearl' and is cherished for its unique biodiversity. However, some of Mongolia's lakes are increasingly threatened by pollution and overgrazing.<br><br>The Gobi Desert in the south contains occasional oases and underground water sources, vital for the region's nomadic communities and wildlife.<br><br>Water management is a critical issue in Mongolia, with a focus on sustainable practices, protecting fragile ecosystems, and ensuring adequate water access for the population. International cooperation is crucial to address water challenges and support the nation's economic and environmental well-being.", 
      "Dili": "Timor-Leste, a small island nation in Southeast Asia, is surrounded by water bodies that play a pivotal role in its geography and livelihood. The Timor Sea to the south provides access to the vast maritime resources of the Arafura and Timor Seas, supporting the nation's fishing industry.<br><br>The country's northern coastline boasts pristine beaches and coral reefs, making it an attractive destination for divers and tourists. The Ombai-Wetar Strait to the north separates Timor-Leste from neighboring Wetar Island and the eastern Indonesian archipelago.<br><br>Inland, the country has various rivers and streams, including the Lacló River, which is important for local agriculture and communities.<br><br>Access to clean and safe drinking water is a priority in Timor-Leste, with initiatives aimed at improving water quality and availability for the population.<br><br>Timor-Leste's future development hinges on sustainable water resource management, ensuring that water bodies remain a source of life and prosperity for its people while preserving the beauty and biodiversity of the surrounding marine environments.", 
      "Thimphu": "Bhutan, a landlocked country in the Eastern Himalayas, is surrounded by pristine water bodies that play a significant role in its unique environment and culture. The country's major river, the Drangme Chhu, flows through deep valleys and supports agriculture, providing livelihoods for many Bhutanese.<br><br>Bhutan's mountainous terrain is dotted with numerous glacial lakes, like the famous Paro Tsho and Thimphu Tsho. These lakes are not only scenic but also vital for the region's water supply and hydropower potential.<br><br>The Phobjikha Valley is home to the Gangtey Tsho, a natural habitat for the endangered black-necked crane, making it a site of international importance for conservation.<br><br>Water management in Bhutan focuses on harnessing the country's hydroelectric power potential, exporting electricity to neighboring countries, and fostering sustainability through initiatives like 'hydropower with a green conscience.'<br><br>Bhutan's water bodies are not only essential for the nation's energy and agriculture but also hold cultural significance, with reverence for the environment and the belief that spirits reside in these natural wonders. The Bhutanese government's emphasis on environmental conservation ensures that these water bodies continue to thrive, supporting both the ecosystem and the people.", 
      "Bandar Seri Begawan": "Brunei, a tiny sultanate on the island of Borneo, is graced with a network of water bodies that shape its landscape and culture. The South China Sea borders Brunei to the north, providing access to rich maritime resources and supporting the nation's fishing industry.<br><br>The Brunei River, the country's primary watercourse, flows through the capital city, Bandar Seri Begawan, and is integral to the nation's transportation and commerce. The Temburong River, which crosses into the Temburong District, boasts lush rainforest surroundings.<br><br>Brunei's numerous mangrove forests along its coastlines are ecologically important, providing habitat for diverse wildlife and acting as protective buffers against coastal erosion.<br><br>The Sultanate has a strong commitment to environmental preservation, with an emphasis on protecting its water bodies and rainforests. Conservation efforts aim to safeguard the nation's unique biodiversity and ensure sustainable management of its natural resources.<br><br>In summary, Brunei's water bodies, from its rivers to the South China Sea, are vital for both its economy and ecology. They play a pivotal role in sustaining the nation's biodiversity, culture, and economic activities."
}

sample_data = []

for city, context in asian_cities.items():
      water_history = context
      water_pH_level = round(random.uniform(6.0, 8.0), 2)
      sample_data.append([city, water_history, water_pH_level])

csv_file = 'database/water_data.csv'
with open(csv_file, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["city", "water history", "water pH level"])
      writer.writerows(sample_data)

client = pymongo.MongoClient("mongodb+srv://wad2g4t5:Fplyzk5st8wjMfFT@wad2-g4t5.saj8cns.mongodb.net/")
db = client["wad2-g4t5"]
collection = db["water_data"]

with open(csv_file, 'r') as file:
      csv_data = csv.DictReader(file)
      for row in csv_data:
            record = {
                  "city": row["city"],
                  "water_history": row["water history"],
                  "water_pH_level": float(row["water pH level"])
            }
            collection.insert_one(record)

print("Data imported into MongoDB.")