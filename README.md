ToolkitEarth
============

ToolkitEarth - connecting farmers to the latest satellite and weather data.

## Concept

This idea had a few key objectives that were partially fulfilled over the course of the day. The main ideas were:
* Making the latest satellite imagery available to farmers in a way that is easy to understand.
* Allowing farmers to select a bound around their properties so they can identify their property on the map
* Showing data such as precipitation and temperature on the farmer's properties

## Code

Subteams worked on:
* Creating a mongodb database that could be populated by cron job with information from BOM such as precipitation and user info

## Thoughts re. roadmap/wishlist

tl;dr: Draw a base map (OSM/MapBox/Leaflet?) with a LandSat option view mode, and then allow for weather input from both local-based weather stations (e.g. SmartCitizen.me/arduino)  and BOM/other upstream data sources. (If someone is super smart they can think about doing analysis of the local data and upstream data sources…)

Would be worth seeing if there are other existing projects in this space — many might appreciate these ideas and take them as extras/plugins/new features.
