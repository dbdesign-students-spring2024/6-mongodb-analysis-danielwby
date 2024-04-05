# AirBnB MongoDB Analysis

[The origin of the data set. The format of the original data file is in CSV](/data/listings.csv)

[Click here to jump to the original dataset](https://data.insideairbnb.com/united-states/hi/hawaii/2024-03-22/data/listings.csv.gz)

| id      | listing_url                                | scrape_id      | last_scraped | source          | name                                            | description                                      | neighborhood_overview                          | picture_url                                     | host_id   | ... | reviews_per_month |
|---------|--------------------------------------------|----------------|--------------|-----------------|-------------------------------------------------|--------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-----------|-----|-------------------|
| 34421962| https://www.airbnb.com/rooms/34421962      | 20240322023526 | 2024-03-22   | city scrape     | Waipouli Beach Resort E106                      | Beautiful Luxury Inner Courtyard Garden View... | NaN                                             | https://a0.muscache.com/pictures/prohost-api... | 34386367  | ... | NaN               |
| 40707945| https://www.airbnb.com/rooms/40707945      | 20240322023526 | 2024-03-23   | city scrape     | DO NOT PUBLISH BEFORE MERGING 14891-HROV        | This is the description of this beautiful hot... | NaN                                             | https://a0.muscache.com/pictures/prohost-api... | 182704096 | ... | NaN               |
| 43656551| https://www.airbnb.com/rooms/43656551      | 20240322023526 | 2024-03-23   | city scrape     | Ilikai 1212 Ocean / Lagoon / King Bed, Sofa Bed | MEMORABLE OCEAN, LAGOON VIEWS! STEPS TO WAIKI... | NaN                                             | https://a0.muscache.com/pictures/prohost-api... | 347952914 | ... | 1.51              |


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
