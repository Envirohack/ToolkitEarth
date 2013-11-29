ToolkitEarth
============

ToolkitEarth - connecting farmers to the latest satellite and weather data.

## Concept

Easy access for farmers to location-specific weather, current and historic satellite imagery

Currently a lot of data are (becoming) freely available, however it still requires substantial knowledge where these data are, how to download data in a usable format for the wanted area of interest only- instead of full scenes- and how to process them to obtain meaningful information. Most farmers struggle with the process. This project aims to give farmers easy access to information that is relevant and meaningful to the land in their care. We hope to assist them in informed decision making and to manage their resources in a sustainable manner.

## Code

Subteams worked on:
* Creating a mongodb database that could be populated by cron job with information from BOM such as precipitation and user info

## Thoughts re. roadmap/wishlist

tl;dr: Draw a base map (OSM/MapBox/Leaflet?) with a LandSat option view mode, and then allow for weather input from both local-based weather stations (e.g. SmartCitizen.me/arduino)  and BOM/other upstream data sources. (If someone is super smart they can think about doing analysis of the local data and upstream data sources…)

Would be worth seeing if there are other existing projects in this space — many might appreciate these ideas and take them as extras/plugins/new features.
