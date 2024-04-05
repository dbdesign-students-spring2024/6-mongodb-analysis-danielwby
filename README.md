# AirBnB MongoDB Analysis

[The origin of the data set. The format of the original data file is in CSV](/data/listings.csv)

[Click here to jump to the original dataset](https://data.insideairbnb.com/united-states/hi/hawaii/2024-03-22/data/listings.csv.gz)

```
csv
id,listing_url,scrape_id,last_scraped,name,description,neighborhood_overview,picture_url,host_id,host_url,host_name,host_since,host_location,host_about,host_response_time,host_response_rate,host_acceptance_rate,host_is_superhost,host_thumbnail_url,host_picture_url,host_neighbourhood,host_listings_count,host_total_listings_count,host_verifications,host_has_profile_pic,host_identity_verified,neighbourhood,neighbourhood_cleansed,neighbourhood_group_cleansed,latitude,longitude,property_type,room_type,accommodates,bathrooms,bathrooms_text,bedrooms,beds,amenities,price,minimum_nights,maximum_nights,minimum_minimum_nights,maximum_minimum_nights,minimum_maximum_nights,maximum_maximum_nights,minimum_nights_avg_ntm,maximum_nights_avg_ntm,calendar_updated,has_availability,availability_30,availability_60,availability_90,availability_365,calendar_last_scraped,number_of_reviews,number_of_reviews_ltm,number_of_reviews_l30d,first_review,last_review,review_scores_rating,review_scores_accuracy,review_scores_cleanliness,review_scores_checkin,review_scores_communication,review_scores_location,review_scores_value,license,instant_bookable,calculated_host_listings_count,calculated_host_listings_count_entire_homes,calculated_host_listings_count_private_rooms,calculated_host_listings_count_shared_rooms,reviews_per_month
18602,https://www.airbnb.com/rooms/18602,20240322023526,2024-03-22,artist apartment 4rent city scrape,Huge apartment in the heart of the city. Ideal for couples or artists. Close to bars, restaurants and public transportation. WiFi available.,"Huge apartment in the heart of the city. Ideal for couples or artists. Close to bars, restaurants and public transportation. WiFi available.",https://a0.muscache.com/pictures/781848/4b06645d_original.jpg,72014011,https://www.airbnb.com/users/show/72014011,Jani,2016-05-10,Helsinki, Finland,I am a professional musician and I rent out my apartment when I am on tour. I love meeting new people and sharing my love for Helsinki.,within a few hours,90%,50%,f,https://a0.muscache.com/im/users/72014011/profile_pic/1462882470/original.jpg?aki_policy=profile_small,https://a0.muscache.com/im/users/72014011/profile_pic/1462882470/original.jpg?aki_policy=profile_x_medium,Kallio,1.0,1.0,"['email', 'phone', 'reviews']",t,f,Kallio,Kallio,Helsinki,60.18267,24.94984,Entire rental unit,Entire home/apt,2,,1 bath,,1.0,"['Wifi', 'Kitchen', 'Heating', 'Washer', 'Smoke alarm', 'Carbon monoxide alarm', 'Fire extinguisher', 'Essentials', 'Shampoo', 'Hair dryer', 'Iron', 'Hangers']",€82.00,3,1125,3.0,3.0,1125.0,1125.0,3.0,1125.0,,t,0,0,0,0,2024-03-22,0,0,0,,,,,,,,,,f,2,2,0,0,
27223583,https://www.airbnb.com/rooms/27223583,20240322023526,2024-03-22,Heart of the City scrape,Newly renovated apartment in the city center. Perfect for couples or solo travelers. Walking distance to all major attractions.,"Newly renovated apartment in the city center. Perfect for couples or solo travelers. Walking distance to all major attractions.",https://a0.muscache.com/pictures/36325012/1b4c7a7e_original.jpg,202922944,https://www.airbnb.com/users/show/202922944,Mari,2018-05-01,Helsinki, Finland,I am a designer and I love to travel. I have renovated this apartment myself and I am excited to share it with guests.,within an hour,100%,100%,t,https://a0.muscache.com/im/users/202922944/profile_pic/1525136315/original.jpg?aki_policy=profile_small,https://a0.muscache.com/im/users/202922944/profile_pic/1525136315/original.jpg?aki_policy=profile_x_medium,Kamppi,1.0,1.0,"['email', 'phone', 'reviews', 'jumio']",t,t,Kamppi,Kamppi,Helsinki,60.16909,24.93258,Entire rental unit,Entire home/apt,2,,1 bath,,1.0,"['Wifi', 'Kitchen', 'Heating', 'Washer', 'Smoke alarm', 'Carbon monoxide alarm', 'Fire extinguisher', 'Essentials', 'Shampoo', 'Hair dryer', 'Iron', 'Hangers']",€89.00,2,30,2.0,2.0,30.0,30.0,2.0,30.0,,t,8,16,25,90,2024-03-22,4,0,0,2018-06-01,2024-02-14,,,,,,,,,,t,1,1,0,0,
40432211,https://www.airbnb.com/rooms/40432211,20240322023526,2024-03-22,Dreamy Attic Studio in Kallio city scrape,Cozy attic studio in the vibrant Kallio district. Perfect for solo travelers or couples. Close to bars, restaurants, and public transport.,"Cozy attic studio in the vibrant Kallio district. Perfect for solo travelers or couples. Close to bars, restaurants, and public transport.",https://a0.muscache.com/pictures/71421444/c1c4a8c2_original.jpg,309017221,https://www.airbnb.com/users/show/309017221,Liisa,2019-09-20,Helsinki, Finland,I am an artist and I love to create beautiful spaces. This attic studio is my latest project and I am excited to share it with you.,within an hour,100%,100%,t,https://a0.muscache.com/im/users/309017221/profile_pic/1568986357/original.jpg?aki_policy=profile_small,https://a0.muscache.com/im/users/309017221/profile_pic/1568986357/original.jpg?aki_policy=profile_x_medium,Kallio,2.0,2.0,"['email', 'phone', 'reviews', 'offline_government_id', 'selfie', 'government_id']",t,t,Kallio,Kallio,Helsinki,60.18788,24.95735,Entire rental unit,Entire home/apt,2,,1 bath,,1.0,"['Wifi', 'Kitchen', 'Heating', 'Smoke alarm', 'Carbon monoxide alarm', 'Fire extinguisher', 'Essentials', 'Shampoo', 'Hair dryer', 'Iron', 'Hangers']",€60.00,1,29,1.0,1.0,29.0,29.0,1.0,29.0,,t,3,7,11,34,2024-03-22,1,0,0,2020-01-02,2024-01-12,,,,,,,,,,t,1,1,0,0,
10988680,https://www.airbnb.com/rooms/10988680,20240322023526,2024-03-22,city scrape,Fully furnished apartment in the city center. Ideal for business travelers or couples. Close to shops, restaurants, and public transport.,"Fully furnished apartment in the city center. Ideal for business travelers or couples. Close to shops, restaurants, and public transport.",https://a0.muscache.com/pictures/92826326/4a9d5c5b_original.jpg,243675,https://www.airbnb.com/users/show/243675,Peter,2009-11-25,Helsinki, Finland,I am a business consultant and I travel frequently. I rent out my apartment when I am away. I hope you enjoy your stay in Helsinki.,within an hour,100%,100%,t,https://a0.muscache.com/im/pictures/243675-2c6f4c81_original.jpg?aki_policy=profile_small,https://a0.muscache.com/im/pictures/243675-2c6f4c81_original.jpg?aki_policy=profile_x_medium,Kamppi,1.0,1.0,"['email', 'phone', 'reviews', 'jumio']",t,t,Kamppi,Kamppi,Helsinki,60.16952,24.93545,Entire rental unit,Entire home/apt,2,,1 bath,,1.0,"['Wifi', 'Kitchen', 'Heating', 'Washer', 'Smoke alarm', 'Carbon monoxide alarm', 'Fire extinguisher', 'Essentials', 'Shampoo', 'Hair dryer', 'Iron', 'Hangers']",€95.00,3,60,3.0,3.0,60.0,60.0,3.0,60.0,,t,0,0,0,0,2024-03-22,0,0,0,,,,,,,,,,f,1,1,0,0,
23566446,https://www.airbnb.com/rooms/23566446,20240322023526,2024-03-22,Cozy City Center Apartment city scrape,Comfortable apartment in the city center. Great for business travelers or couples. Walking distance to shops, restaurants, and public transport.,"Comfortable apartment in the city center. Great for business travelers or couples. Walking distance to shops, restaurants, and public transport.",https://a0.muscache.com/pictures/29634889/6a9e4462_original.jpg,256003922,https://www.airbnb.com/users/show/256003922,Antti,2018-07-11,Helsinki, Finland,I am a software developer and I love to travel. I rent out my apartment to help fund my adventures.,within an hour,100%,100%,t,https://a0.muscache.com/im/users/256003922/profile_pic/1531332874/original.jpg?aki_policy=profile_small,https://a0.muscache.com/im/users/256003922/profile_pic/1531332874/original.jpg?aki_policy=profile_x_medium,Kamppi,1.0,1.0,"['email', 'phone', 'reviews', 'jumio']",t,t,Kamppi,Kamppi,Helsinki,60.16919,24.92941,Entire rental unit,Entire home/apt,2,,1 bath,,1.0,"['Wifi', 'Kitchen', 'Heating', 'Washer', 'Smoke alarm', 'Carbon monoxide alarm', 'Fire extinguisher', 'Essentials', 'Shampoo', 'Hair dryer', 'Iron', 'Hangers']",€85.00,2,60,2.0,2.0,60.0,60.0,2.0,60.0,,t,0,0,0,0,2024-03-22,0,0,0,,,,,,,,,,f,1,1,0,0,
```


| id      | listing_url                      | scrape_id     | last_scraped | name                       | description                                       | neighborhood_overview       | picture_url                                                                         | host_id    | host_url                          | host_name | host_since | host_location        | host_about          | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url                                                                   | host_picture_url                                                                    | host_neighbourhood | host_listings_count | host_total_listings_count | host_verifications         | host_has_profile_pic | host_identity_verified | street                          | neighbourhood | neighbourhood_cleansed | neighbourhood_group_cleansed | city            | state          | zipcode | market    | smart_location    | country_code | country        | latitude | longitude | is_location_exact | property_type            | room_type       | accommodates | bathrooms | bathroom_text     | bedrooms | beds | amenities                                                                                                                                                                                                                                             | price   | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review   | last_review    | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license                       | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
|---------|----------------------------------|--------------|--------------|----------------------------|---------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------|------------|----------------------------------|-----------|------------|----------------------|--------------------|---------------------|---------------------|----------------------|-------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|---------------------|---------------------|----------------------------|---------------------------|----------------------|------------------------|---------------------------------|---------------|------------------------|-----------------------------|-----------------|---------------|--------|-----------|-------------------|--------------|----------------|----------|-----------|--------------------|--------------------------|-----------------|--------------|-----------|------------------|----------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|----------------|----------------|------------------------|------------------------|------------------------|------------------------|-----------------------|-----------------------|-----------------|-----------------|----------------|----------------|----------------|-----------------|----------------------|------------------|-----------------------|------------------------|---------------|----------------|---------------------|------------------------|---------------------------|-----------------------|-----------------------------|-----------------------|----------------------|--------------------------------|------------------|---------------------------------|--------------------------------------------------|--------------------------------------------|--------------------------------------------|------------------|
| 1270056 | https://www.airbnb.com/rooms... | 202303292222 | 2023-03-30   | 27 S. Wildwood Blvd, Villas | "Whole house in Villas. Has 3 bedrooms, sleeps 10 | "Near the bay, peaceful and quiet." | "https://a0.muscache.com/pictures/miso/Hosting-1270056/original/e671c3b0-7b27-42e8-aee3-d84c48ef0a5c.jpeg" | 500671     | https://www.airbnb.com/users... | Jon        | 2013-08-16  | Villas, NJ, United States | "I love hosting and meeting new people!" | within an hour        | 100%                | 100%                   | t                | "https://a0.muscache.com/im/pictures/user/2306b453-f80d-4fd2-9ee0-55b7d0deed91.jpg?aki_policy=profile_small" | "https://a0.muscache.com/im/pictures/user/2306b453-f80d-4fd2-9ee0-55b7d0deed91.jpg?aki_policy=profile_x_medium" | Villas            | 3                  | 3                         | ['email', 'phone', 'reviews'] | t                     | t                       | "27 S. Wildwood Blvd, Villas, NJ 08251, United States" | Villas         | Villas                  | Cape May County           | Villas, NJ       | NJ             | 08251  | Cape May | Villas, NJ        | US           | United States   | 39.1419  | -74.9614  | t                  | Entire residential home    | Entire home/apt | 10           | 1.5       | 1.5 baths          | 3        | 6    | ["Kitchen", "Wifi", "Free parking on premises", "Pets allowed", "TV", "Washer", "Dryer", "Air conditioning", "Heating", "Smoke alarm"]                                                                                                        | $215.00 | 2              | 1125            | 2                      | 2                      | 1125                   | 1125                   | 2                     | 1125                   | 2 weeks ago       | t                | 0              | 0              | 0              | 0               | 2023-03-30            | 0                | 0                     | 0                      | 2023-03-05     | 2023-03-05      | nan                   | nan                      | nan                         | nan                     | nan                           | nan                     | nan                    | nan                          | t                | 3                               | 3                                                | 0                                              | 0                                              | nan              |
| 1358821 | https://www.airbnb.com/rooms... | 202303292222 | 2023-03-30   | Cozy Cottage on the Beac... | "Entire cottage in Villas. Has 2 bedrooms, sleeps 6 | "Beachfront with beautiful sunsets."             | "https://a0.muscache.com/pictures/miso/Hosting-1358821/original/31d93930-f1ed-42c3-9a76-24db1c452774.jpeg" | 1054201    | https://www.airbnb.com/users... | Emily      | 2014-06-05  | Villas, NJ, United States | "I love the beach and sharing my cozy cottage!" | within a few hours    | 90%                 | 95%                    | t                | "https://a0.muscache.com/im/pictures/user/8a4bfa20-8f97-4c07-9f6e-4b6e88591447.jpg?aki_policy=profile_small" | "https://a0.muscache.com/im/pictures/user/8a4bfa20-8f97-4c07-9f6e-4b6e88591447.jpg?aki_policy=profile_x_medium" | Villas            | 2                  | 2                         | ['email', 'phone', 'reviews', 'offline_government_id'] | t                     | t                       | "Cozy Cottage, Villas, NJ 08251, United States"      | Villas         | Villas                  | Cape May County           | Villas, NJ       | NJ             | 08251  | Cape May | Villas, NJ        | US           | United States   | 39.1325  | -74.953   | t                  | Entire residential home    | Entire home/apt | 6            | 1         | 1 bath             | 2        | 4    | ["Kitchen", "Wifi", "Free parking on premises", "Beachfront", "TV", "Washer", "Dryer", "Air conditioning", "Heating", "Smoke alarm"]                                                                                                           | $185.00 | 3              | 365             | 3                      | 3                      | 365                    | 365                    | 3                     | 365                    | a week ago        | t                | 10             | 40             | 70             | 345              | 2023-03-30            | 10               | 10                    | 0                      | 2023-03-05     | 2023-03-05      | nan                   | nan                      | nan                         | nan                     | nan                           | nan                     | nan                    | nan                          | t                | 2                               | 2                                                | 0                                              | 0                                              | 4.50            |
...


**On data cleaning: Remove duplicate values from the data. and then handle missing values, Remove columns with more than 50% missing values and fill missing values in numeric columns.Here is the code:**
```
import pandas as pd

# Load the CSV file
file_path = 'data/listings.csv'
df = pd.read_csv(file_path)

# 1. Remove duplicate rows
df_cleaned = df.drop_duplicates()

# 2. Handle missing values
# Remove columns with more than 50% missing values
missing_values = df_cleaned.isnull().mean().sort_values(ascending=False)
columns_to_drop = missing_values[missing_values > 0.5].index
df_cleaned = df_cleaned.drop(columns=columns_to_drop)

# Fill missing values in numeric columns
numeric_columns = ['review_scores_value', 'review_scores_checkin', 'review_scores_location',
'review_scores_communication', 'review_scores_cleanliness']

for col in numeric_columns:
median_value = df_cleaned[col].median()
df_cleaned[col] = df_cleaned[col].fillna(median_value)

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('data/listings_clean.csv', index=False)

```

## 1、show exactly two documents from the listings collection in any order
```
db.listings.find().limit(2);
```

```
{ "_id" : ObjectId("660d9c98b6515eb20576c9ba"), "id" : NumberLong("656863289181779136"), "listing_url" : "https://www.airbnb.com/rooms/656863289181779136", "scrape_id" : NumberLong("20240322023526"), "last_scraped" : "2024-03-23", "source" : "city scrape", "name" : "Ocean View Lanai W/Full-Kitchen–Waikiki Shore 506", "description" : "Once you open the condo door you'll be drawn to the floor-to-ceiling sliding glass doors and ocean views from your private lanai. This lovely one-bedroom one-bathroom suite is perfect for small families or friends. Get ready for Waikiki condo living at the only Oahu condominium directly on Waikiki Beach. Snap photos of the Pacific Ocean, iconic Diamond Head, and Fort DeRussy Park steps away from your condo. Sleeps four guests in two twin beds (can be converted into a king bed) and a sofa bed.", "neighborhood_overview" : "", "picture_url" : "https://a0.muscache.com/pictures/prohost-api/Hosting-656863289181779136/original/bfa14e93-fef0-4664-81cd-f0cbb9df81cf.jpeg", "host_id" : 116465695, "host_url" : "https://www.airbnb.com/users/show/116465695", "host_name" : "Castle Resorts And Hotels", "host_since" : "2017-02-15", "host_location" : "Hawaii, United States", "host_about" : "This exquisite condominium is located on Waikiki Beach just next door to Fort DeRussy Park and one block from bustling Kalakaua Avenue. Each studio, one- and two- bedroom suite features kitchenette or full kitchen, and in-room washer/dryer.\n\n\nSince 1993, Castle Resorts & Hotels has specialized in innovative hotel and resort management. We manage properties throughout the Hawaiian Islands, including Kauai, Oahu, Maui, Molokai, and Hawaii Island, as well as Auckland, New Zealand. Accommodations range from full-service hotels to resort condominiums and combines value, convenience, and authentic experiences.", "host_response_time" : "within an hour", "host_response_rate" : "86%", "host_acceptance_rate" : "100%", "host_is_superhost" : "f", "host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/2e385658-793a-439f-8218-91e18e471393.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/pictures/user/2e385658-793a-439f-8218-91e18e471393.jpg?aki_policy=profile_x_medium", "host_neighbourhood" : "Waikiki", "host_listings_count" : 60, "host_total_listings_count" : 65, "host_verifications" : "['email', 'phone']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood" : "", "neighbourhood_cleansed" : "Primary Urban Center", "neighbourhood_group_cleansed" : "Honolulu", "latitude" : 21.27764, "longitude" : -157.83182, "property_type" : "Entire condo", "room_type" : "Entire home/apt", "accommodates" : 4, "bathrooms" : 1, "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 3, "amenities" : "[\"Building staff\", \"Smoke alarm\", \"Iron\", \"Wifi\", \"Essentials\", \"Safe\", \"Stove\", \"Oven\", \"TV with standard cable\", \"Ceiling fan\", \"Fire extinguisher\", \"Refrigerator\", \"Air conditioning\", \"Washer\", \"Self check-in\", \"Hair dryer\", \"Dedicated workspace\", \"Beach access \\u2013 Beachfront\", \"Dishwasher\", \"Coffee maker\", \"Outdoor furniture\", \"Microwave\", \"Cooking basics\", \"Bathtub\"]", "price" : "$377.00", "minimum_nights" : 2, "maximum_nights" : 60, "minimum_minimum_nights" : 1, "maximum_minimum_nights" : 4, "minimum_maximum_nights" : 1, "maximum_maximum_nights" : 21, "minimum_nights_avg_ntm" : 2.1, "maximum_nights_avg_ntm" : 16.7, "has_availability" : "t", "availability_30" : 15, "availability_60" : 37, "availability_90" : 63, "availability_365" : 308, "calendar_last_scraped" : "2024-03-23", "number_of_reviews" : 1, "number_of_reviews_ltm" : 0, "number_of_reviews_l30d" : 0, "first_review" : "2022-07-20", "last_review" : "2022-07-20", "review_scores_rating" : 3, "review_scores_accuracy" : 1, "review_scores_cleanliness" : 3, "review_scores_checkin" : 5, "review_scores_communication" : 3, "review_scores_location" : 5, "review_scores_value" : 3, "license" : "260040120032, 506, TA-209-898-7008-01", "instant_bookable" : "t", "calculated_host_listings_count" : 59, "calculated_host_listings_count_entire_homes" : 59, "calculated_host_listings_count_private_rooms" : 0, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 0.05 }

{ "_id" : ObjectId("660d9c98b6515eb20576c9ab"), "id" : NumberLong("1111915930623153614"), "listing_url" : "https://www.airbnb.com/rooms/1111915930623153614", "scrape_id" : NumberLong("20240322023526"), "last_scraped" : "2024-03-22", "source" : "city scrape", "name" : "Hale Luna Mermadia", "description" : "A private and serene cabin located in the beautiful Kalapana Seaview Estates Neighborhood. Enjoy your own private entrance, parking and yard space in this lush jungle abode. Enjoy the fresh air and sunshine in this sweet space that connects you with nature and comfort. This Hale is equipped with all the necessities you'll need during your stay with us. Walking distance from Kehena Black sand beach or short drive. Home of Sunday Funday festival at our neighborhood park. Near the ecstatic dance.", "neighborhood_overview" : "", "picture_url" : "https://a0.muscache.com/pictures/hosting/Hosting-1111915930623153614/original/d5c5d9cd-f808-412b-b3b7-719c56d968ab.jpeg", "host_id" : 24272600, "host_url" : "https://www.airbnb.com/users/show/24272600", "host_name" : "Kanixa", "host_since" : "2014-11-28", "host_location" : "Hawaii, United States", "host_about" : "I am a yogi, artist, entrepreneur and graphic designer. I've been a host and traveler with Airbnb since 2014. I'm easy going and respectful to the space as a prior host I understand how important it is to have guests who appreciate the space. Thank you for hosting! \r", "host_response_time" : "within an hour", "host_response_rate" : "100%", "host_acceptance_rate" : "100%", "host_is_superhost" : "f", "host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/cac2aa84-28ad-44a5-b889-51d13954dcd6.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/pictures/user/cac2aa84-28ad-44a5-b889-51d13954dcd6.jpg?aki_policy=profile_x_medium", "host_neighbourhood" : "", "host_listings_count" : 1, "host_total_listings_count" : 4, "host_verifications" : "['email', 'phone']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood" : "", "neighbourhood_cleansed" : "Puna", "neighbourhood_group_cleansed" : "Hawaii", "latitude" : 19.405174, "longitude" : -154.9216383, "property_type" : "Entire cabin", "room_type" : "Entire home/apt", "accommodates" : 2, "bathrooms" : 1, "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 1, "amenities" : "[\"Dedicated workspace\", \"Hangers\", \"Wifi\", \"Private entrance\", \"Essentials\", \"Bed linens\", \"Beach access\", \"Clothing storage\", \"Kitchenette\", \"Long term stays allowed\", \"Free parking on premises\", \"Hammock\", \"Hot water\"]", "price" : "$64.00", "minimum_nights" : 1, "maximum_nights" : 365, "minimum_minimum_nights" : 1, "maximum_minimum_nights" : 1, "minimum_maximum_nights" : 365, "maximum_maximum_nights" : 365, "minimum_nights_avg_ntm" : 1, "maximum_nights_avg_ntm" : 365, "has_availability" : "t", "availability_30" : 4, "availability_60" : 23, "availability_90" : 53, "availability_365" : 232, "calendar_last_scraped" : "2024-03-22", "number_of_reviews" : 0, "number_of_reviews_ltm" : 0, "number_of_reviews_l30d" : 0, "first_review" : "", "last_review" : "", "review_scores_rating" : "", "review_scores_accuracy" : "", "review_scores_cleanliness" : 4.86, "review_scores_checkin" : 4.94, "review_scores_communication" : 4.94, "review_scores_location" : 4.93, "review_scores_value" : 4.76, "license" : "", "instant_bookable" : "t", "calculated_host_listings_count" : 1, "calculated_host_listings_count_entire_homes" : 1, "calculated_host_listings_count_private_rooms" : 0, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : "" }
```

## 2、show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function.
```
> db.listings.find().limit(10).pretty()
```

```
{
"_id" : ObjectId("660d9c98b6515eb20576c9ba"),
"id" : NumberLong("656863289181779136"),
"listing_url" : "https://www.airbnb.com/rooms/656863289181779136",
"scrape_id" : NumberLong("20240322023526"),
"last_scraped" : "2024-03-23",
"source" : "city scrape",
"name" : "Ocean View Lanai W/Full-Kitchen–Waikiki Shore 506",
"description" : "Once you open the condo door you'll be drawn to the floor-to-ceiling sliding glass doors and ocean views from your private lanai. This lovely one-bedroom one-bathroom suite is perfect for small families or friends. Get ready for Waikiki condo living at the only Oahu condominium directly on Waikiki Beach. Snap photos of the Pacific Ocean, iconic Diamond Head, and Fort DeRussy Park steps away from your condo. Sleeps four guests in two twin beds (can be converted into a king bed) and a sofa bed.",
"neighborhood_overview" : "",
"picture_url" : "https://a0.muscache.com/pictures/prohost-api/Hosting-656863289181779136/original/bfa14e93-fef0-4664-81cd-f0cbb9df81cf.jpeg",
"host_id" : 116465695,
"host_url" : "https://www.airbnb.com/users/show/116465695",
"host_name" : "Castle Resorts And Hotels",
"host_since" : "2017-02-15",
"host_location" : "Hawaii, United States",
"host_about" : "This exquisite condominium is located on Waikiki Beach just next door to Fort DeRussy Park and one block from bustling Kalakaua Avenue. Each studio, one- and two- bedroom suite features kitchenette or full kitchen, and in-room washer/dryer.\n\n\nSince 1993, Castle Resorts & Hotels has specialized in innovative hotel and resort management. We manage properties throughout the Hawaiian Islands, including Kauai, Oahu, Maui, Molokai, and Hawaii Island, as well as Auckland, New Zealand. Accommodations range from full-service hotels to resort condominiums and combines value, convenience, and authentic experiences.",
"host_response_time" : "within an hour",
"host_response_rate" : "86%",
"host_acceptance_rate" : "100%",
"host_is_superhost" : "f",
"host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/2e385658-793a-439f-8218-91e18e471393.jpg?aki_policy=profile_small",
"host_picture_url" : "https://a0.muscache.com/im/pictures/user/2e385658-793a-439f-8218-91e18e471393.jpg?aki_policy=profile_x_medium",
"host_neighbourhood" : "Waikiki",
"host_listings_count" : 60,
"host_total_listings_count" : 65,
"host_verifications" : "['email', 'phone']",
"host_has_profile_pic" : "t",
"host_identity_verified" : "t",
"neighbourhood" : "",
"neighbourhood_cleansed" : "Primary Urban Center",
"neighbourhood_group_cleansed" : "Honolulu",
"latitude" : 21.27764,
"longitude" : -157.83182,
"property_type" : "Entire condo",
"room_type" : "Entire home/apt",
"accommodates" : 4,
"bathrooms" : 1,
"bathrooms_text" : "1 bath",
"bedrooms" : 1,
"beds" : 3,
"amenities" : "[\"Building staff\", \"Smoke alarm\", \"Iron\", \"Wifi\", \"Essentials\", \"Safe\", \"Stove\", \"Oven\", \"TV with standard cable\", \"Ceiling fan\", \"Fire extinguisher\", \"Refrigerator\", \"Air conditioning\", \"Washer\", \"Self check-in\", \"Hair dryer\", \"Dedicated workspace\", \"Beach access \\u2013 Beachfront\", \"Dishwasher\", \"Coffee maker\", \"Outdoor furniture\", \"Microwave\", \"Cooking basics\", \"Bathtub\"]",
"price" : "$377.00",
"minimum_nights" : 2,
"maximum_nights" : 60,
"minimum_minimum_nights" : 1,
"maximum_minimum_nights" : 4,
"minimum_maximum_nights" : 1,
"maximum_maximum_nights" : 21,
"minimum_nights_avg_ntm" : 2.1,
"maximum_nights_avg_ntm" : 16.7,
"has_availability" : "t",
"availability_30" : 15,
"availability_60" : 37,
"availability_90" : 63,
"availability_365" : 308,
"calendar_last_scraped" : "2024-03-23",
"number_of_reviews" : 1,
"number_of_reviews_ltm" : 0,
"number_of_reviews_l30d" : 0,
"first_review" : "2022-07-20",
"last_review" : "2022-07-20",
"review_scores_rating" : 3,
"review_scores_accuracy" : 1,
"review_scores_cleanliness" : 3,
"review_scores_checkin" : 5,
"review_scores_communication" : 3,
"review_scores_location" : 5,
"review_scores_value" : 3,
"license" : "260040120032, 506, TA-209-898-7008-01",
"instant_bookable" : "t",
"calculated_host_listings_count" : 59,
"calculated_host_listings_count_entire_homes" : 59,
"calculated_host_listings_count_private_rooms" : 0,
"calculated_host_listings_count_shared_rooms" : 0,
"reviews_per_month" : 0.05
}
{
"_id" : ObjectId("660d9c98b6515eb20576c9ab"),
"id" : NumberLong("1111915930623153614"),
"listing_url" : "https://www.airbnb.com/rooms/1111915930623153614",
"scrape_id" : NumberLong("20240322023526"),
"last_scraped" : "2024-03-22",
"source" : "city scrape",
"name" : "Hale Luna Mermadia",
"description" : "A private and serene cabin located in the beautiful Kalapana Seaview Estates Neighborhood. Enjoy your own private entrance, parking and yard space in this lush jungle abode. Enjoy the fresh air and sunshine in this sweet space that connects you with nature and comfort. This Hale is equipped with all the necessities you'll need during your stay with us. Walking distance from Kehena Black sand beach or short drive. Home of Sunday Funday festival at our neighborhood park. Near the ecstatic dance.",
"neighborhood_overview" : "",
"picture_url" : "https://a0.muscache.com/pictures/hosting/Hosting-1111915930623153614/original/d5c5d9cd-f808-412b-b3b7-719c56d968ab.jpeg",
"host_id" : 24272600,
"host_url" : "https://www.airbnb.com/users/show/24272600",
"host_name" : "Kanixa",
"host_since" : "2014-11-28",
"host_location" : "Hawaii, United States",
"host_about" : "I am a yogi, artist, entrepreneur and graphic designer. I've been a host and traveler with Airbnb since 2014. I'm easy going and respectful to the space as a prior host I understand how important it is to have guests who appreciate the space. Thank you for hosting! \r",
"host_response_time" : "within an hour",
"host_response_rate" : "100%",
"host_acceptance_rate" : "100%",
"host_is_superhost" : "f",
"host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/cac2aa84-28ad-44a5-b889-51d13954dcd6.jpg?aki_policy=profile_small",
"host_picture_url" : "https://a0.muscache.com/im/pictures/user/cac2aa84-28ad-44a5-b889-51d13954dcd6.jpg?aki_policy=profile_x_medium",
"host_neighbourhood" : "",
"host_listings_count" : 1,
"host_total_listings_count" : 4,
"host_verifications" : "['email', 'phone']",
"host_has_profile_pic" : "t",
"host_identity_verified" : "t",
"neighbourhood" : "",
"neighbourhood_cleansed" : "Puna",
"neighbourhood_group_cleansed" : "Hawaii",
"latitude" : 19.405174,
"longitude" : -154.9216383,
"property_type" : "Entire cabin",
"room_type" : "Entire home/apt",
"accommodates" : 2,
"bathrooms" : 1,
"bathrooms_text" : "1 bath",
"bedrooms" : 1,
"beds" : 1,
"amenities" : "[\"Dedicated workspace\", \"Hangers\", \"Wifi\", \"Private entrance\", \"Essentials\", \"Bed linens\", \"Beach access\", \"Clothing storage\", \"Kitchenette\", \"Long term stays allowed\", \"Free parking on premises\", \"Hammock\", \"Hot water\"]",
"price" : "$64.00",
"minimum_nights" : 1,
"maximum_nights" : 365,
"minimum_minimum_nights" : 1,
"maximum_minimum_nights" : 1,
"minimum_maximum_nights" : 365,
"maximum_maximum_nights" : 365,
"minimum_nights_avg_ntm" : 1,
"maximum_nights_avg_ntm" : 365,
"has_availability" : "t",
"availability_30" : 4,
"availability_60" : 23,
"availability_90" : 53,
"availability_365" : 232,
"calendar_last_scraped" : "2024-03-22",
"number_of_reviews" : 0,
"number_of_reviews_ltm" : 0,
"number_of_reviews_l30d" : 0,
"first_review" : "",
"last_review" : "",
"review_scores_rating" : "",
"review_scores_accuracy" : "",
"review_scores_cleanliness" : 4.86,
"review_scores_checkin" : 4.94,
"review_scores_communication" : 4.94,
"review_scores_location" : 4.93,
"review_scores_value" : 4.76,
"license" : "",
"instant_bookable" : "t",
"calculated_host_listings_count" : 1,
"calculated_host_listings_count_entire_homes" : 1,
"calculated_host_listings_count_private_rooms" : 0,
"calculated_host_listings_count_shared_rooms" : 0,
"reviews_per_month" : ""
}
{
"_id" : ObjectId("660d9c98b6515eb20576c9ad"),
"id" : NumberLong("714439536697735942"),
"listing_url" : "https://www.airbnb.com/rooms/714439536697735942",
"scrape_id" : NumberLong("20240322023526"),
"last_scraped" : "2024-03-23",
"source" : "city scrape",
"name" : "Hokulani Waikiki Resort - 1 Bedroom Plus Dbl Beds",
"description" : "This one-bedroom suite features a primary bedroom with two double beds and a separate bath with a large soaker tub, shower room and an LCD-TV screen integrated with the vanity mirror. The casual living area has a cozy dining area, double sofa bed, flat screen TV featuring HGV's In-Room TV Experience",
"neighborhood_overview" : "Anchoring the northernmost stretch of the celebrated Waikiki Beach Walk entertainment district, Hokulani Waikiki by Hilton Grand Vacations Club offers ideal access to Waikiki’s most vibrant showcase for dining, shopping and entertainment.",
"picture_url" : "https://a0.muscache.com/pictures/prohost-api/Hosting-714439536697735942/original/f0101084-cb09-4e04-b248-55d54cdf3b89.jpeg",
"host_id" : 475676514,
"host_url" : "https://www.airbnb.com/users/show/475676514",
"host_name" : "Spencer",
"host_since" : "2022-08-18",
"host_location" : "",
"host_about" : "",
"host_response_time" : "within an hour",
"host_response_rate" : "100%",
"host_acceptance_rate" : "",
"host_is_superhost" : "f",
"host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/cf301ece-9157-4bc9-9960-25b5a57f22ea.jpg?aki_policy=profile_small",
"host_picture_url" : "https://a0.muscache.com/im/pictures/user/cf301ece-9157-4bc9-9960-25b5a57f22ea.jpg?aki_policy=profile_x_medium",
"host_neighbourhood" : "Waikiki",
"host_listings_count" : 5,
"host_total_listings_count" : 5,
"host_verifications" : "['email', 'phone']",
"host_has_profile_pic" : "t",
"host_identity_verified" : "f",
"neighbourhood" : "Honolulu, Hawaii, United States",
"neighbourhood_cleansed" : "Primary Urban Center",
"neighbourhood_group_cleansed" : "Honolulu",
"latitude" : 21.2799819577335,
"longitude" : -157.830374595451,
"property_type" : "Private room in resort",
"room_type" : "Private room",
"accommodates" : 4,
"bathrooms" : 1,
"bathrooms_text" : "1 private bath",
"bedrooms" : 1,
"beds" : 2,
"amenities" : "[\"Smoke alarm\", \"Iron\", \"Wifi\", \"Coffee\", \"Mini fridge\", \"Shampoo\", \"Essentials\", \"Safe\", \"Long term stays allowed\", \"Stove\", \"Game console\", \"Gym\", \"Extra pillows and blankets\", \"Body soap\", \"Ceiling fan\", \"Blender\", \"Fire extinguisher\", \"Resort access\", \"Pool\", \"Hot water\", \"Dishes and silverware\", \"Dining table\", \"Hangers\", \"Air conditioning\", \"Patio or balcony\", \"First aid kit\", \"Bed linens\", \"Beach access\", \"Washer\", \"Exercise equipment\", \"Elevator\", \"Hair dryer\", \"Room-darkening shades\", \"Dedicated workspace\", \"Dishwasher\", \"Paid parking on premises\", \"Dryer\", \"Kitchen\", \"Coffee maker\", \"Carbon monoxide alarm\", \"Clothing storage\", \"Heating\", \"Hot tub\", \"Outdoor furniture\", \"Microwave\", \"Cooking basics\", \"TV\", \"Bathtub\"]",
"price" : "$505.00",
"minimum_nights" : 1,
"maximum_nights" : 1125,
"minimum_minimum_nights" : 3,
"maximum_minimum_nights" : 3,
"minimum_maximum_nights" : 1125,
"maximum_maximum_nights" : 1125,
"minimum_nights_avg_ntm" : 3,
"maximum_nights_avg_ntm" : 1125,
"has_availability" : "t",
"availability_30" : 6,
"availability_60" : 19,
"availability_90" : 24,
"availability_365" : 289,
"calendar_last_scraped" : "2024-03-23",
"number_of_reviews" : 0,
"number_of_reviews_ltm" : 0,
"number_of_reviews_l30d" : 0,
"first_review" : "",
"last_review" : "",
"review_scores_rating" : "",
"review_scores_accuracy" : "",
"review_scores_cleanliness" : 4.86,
"review_scores_checkin" : 4.94,
"review_scores_communication" : 4.94,
"review_scores_location" : 4.93,
"review_scores_value" : 4.76,
"license" : "Exempt",
"instant_bookable" : "t",
"calculated_host_listings_count" : 5,
"calculated_host_listings_count_entire_homes" : 0,
"calculated_host_listings_count_private_rooms" : 5,
"calculated_host_listings_count_shared_rooms" : 0,
"reviews_per_month" : ""
}
```

## 3、choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts.only show the name, price, neighbourhood, host_name, and host_is_superhost for each result
```
> db.listings.find(
... {
... $or: [
... { host_id: 162307514, host_is_superhost: "t" },
... { host_id: 5042700, host_is_superhost: "t" }
... ]
... },
... {
... name: 1,
... price: 1,
... neighbourhood: 1,
... host_name: 1,
... host_is_superhost: 1
... }
... )
```

```
{ "_id" : ObjectId("660d9c96b6515eb205767823"), "name" : "Luxury Maui Camper AWD 2022 Airport Pick Up - Momi", "host_name" : "Chloe", "host_is_superhost" : "t", "neighbourhood" : "Kahului, Hawaii, United States", "price" : "$82.00" }
{ "_id" : ObjectId("660d9c96b6515eb2057680aa"), "name" : "Lux Maui Camper 2020 Airport Pick Up", "host_name" : "Chloe", "host_is_superhost" : "t", "neighbourhood" : "", "price" : "$76.00" }
{ "_id" : ObjectId("660d9c96b6515eb2057680e5"), "name" : "Lux Maui Camper 2020 Airport Pick Up - Kupanaha", "host_name" : "Chloe", "host_is_superhost" : "t", "neighbourhood" : "Kahului, Hawaii, United States", "price" : "$72.00" }
```

## 4 find all the unique host_name values
```
db.listings.distinct("host_name")
```

```
"(Super Host)Dennis"
"A"
"A & J"
```

## 5 find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as either the neighborhood or neighbourhood_group_cleansed fields in the data file), ordered by review_scores_rating descending
```
db.listings.find(
... {
... $and: [
... { $or: [{ neighbourhood_group_cleansed: "Kauai" }] },
... { beds: { $gt: 2 } },
... { review_scores_rating: { $ne: null } }
... ]
... },
... {
... name: 1,
... beds: 1,
... review_scores_rating: 1,
... price: 1
... }
... ).sort({ review_scores_rating: -1 })

```

```
{ "_id" : ObjectId("660d9c98b6515eb20576c8e4"), "name" : "Wyndham Bali Hai Resort 2 bedroom Villa", "beds" : 3, "price" : "$257.00", "review_scores_rating" : "" }
{ "_id" : ObjectId("660d9c98b6515eb20576c8b1"), "name" : "Club Wyndham Shearwater Princeville- 2bd Aloha", "beds" : 3, "price" : "$299.00", "review_scores_rating" : "" }
{ "_id" : ObjectId("660d9c98b6515eb20576c7a0"), "name" : "Private home. Access to Poi'pu Beach Athletic Club", "beds" : 5, "price" : "$400.00", "review_scores_rating" : "" }
```

## 6 show the number of listings per host
```
db.listings.aggregate([
... {
... $group: {
... _id: "$host_id",
... listingsCount: { $sum: 1 }
... }
... }
... ])
```

```
{ "_id" : 7532, "listingsCount" : 15 }
{ "_id" : 198079461, "listingsCount" : 1 }
{ "_id" : 159530852, "listingsCount" : 1 }
```

## 7 find the average review_scores_rating per neighborhood, and only show those that are 4 or above, sorted in descending order of rating 
```
db.listings.aggregate([
... {
... $match: {
... review_scores_rating: { $gte: 4 }
... }
... },
... {
... $group: {
... _id: "$neighbourhood",
... averageRating: { $avg: "$review_scores_rating" }
... }
... },
... {
... $match: {
... averageRating: { $gte: 4 }
... }
... },
... {
... $sort: { averageRating: -1 }
... }
... ])
```

```
{ "_id" : "Ka'anapali, Hawaii, United States", "averageRating" : 5 }
{ "_id" : "Poipu Beach, Hawaii, United States", "averageRating" : 5 }
{ "_id" : "Wahiawa, Hawaii, United States", "averageRating" : 5 }
```
