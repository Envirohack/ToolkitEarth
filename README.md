ToolkitEarth
============

ToolkitEarth - connecting farmers to the latest satellite and weather data.

## Concept

Easy access for farmers to location-specific weather, current and historic satellite imagery

Currently a lot of data are (becoming) freely available, however it still requires substantial knowledge where these data are, how to download data in a usable format for the wanted area of interest only -- instead of full scenes -- and how to process them to obtain meaningful information. Most farmers struggle with the process. This project aims to give farmers easy access to information that is relevant and meaningful to the land in their care. We hope to assist them in informed decision making and to manage their resources in a sustainable manner.

## Storyboard/user features

- user arrives at a page (user agent agnostic) and is presented with:
	- map (w/ map layer and zooming controls)
	- search field to find locations of interest
	- locate me button (geo request to UA)
	- blurb of info
	- ‘edit’ function
- user enters edit function and is presented with:
	- polygon editing tools to draw multiple shapes to match paddock boundaries
	- labelling tools to add names to polygons/paddocks
	- info box/pane switches context to list drawn polygons/paddocks (inc. info like square km size of paddocks, name, and environmental conditions)
- user has drawn and labelled some paddocks and can now:
	- ‘save’ their changes (HTML5 local data w/ an ID to the server?)
	- sign up to receive email notifications for their selections

User should also:
- be able to view LandSat imagery (offer various map/satellite views?)
- easily see rain, wind, and frost conditions
- sign up for push notifications/warnings for selected variables?

## Code info

Our team divided itself to test a variety of ideas and data sources:

* Team 1: Creating a mongodb database that could be populated by cron job with information from BOM such as precipitation and user info. The data accessed is NetCDF from ACCESS OpenDAP (Numerical model from BoM): http://opendap.bom.gov.au:8080/thredds/catalogs/nmoc-catalogs/nmoc-access-catalog.html.
* Team 2: Extracting specific Landsat ‘tiles’ and building a viewer for these.
* Team 3: User interface prototyping and building an API to connect to the populated MonogDB.

### File listing

#### `ui.html`

This is a work in progress. Currently just puts a leaflet map and some buttons - needs more love.

#### `server.js` and `enviro.js`

These are files to run in node.js. These use express to make a Resful API for the MongoDB weather-by-location DB. Note: `enviro.js` needs to be under a `/routes/` folder. Will put a full working directory up after the hack session.

#### `landsat_viewer.html`

Scrapes from GA for a particular location and uses Leaflet for the view.

#### `weather_uploader.py`

Python scrapper that populates a MonogDB with data from the Bureau of Meteorology.

## Roadmap/other thoughts

tl;dr: Draw a base map (OSM/MapBox/Leaflet?) with a LandSat option view mode, and then allow for weather input from both local-based weather stations (e.g. SmartCitizen.me/arduino)  and BOM/other upstream data sources. (If someone is super smart they can think about doing analysis of the local data and upstream data sources.)

Would be worth seeing if there are other existing projects in this space — many might appreciate these ideas and take them as extras/plugins/new features. See the [SmartCitizen.me interface](https://github.com/fablabbcn/SmartCitizen.me).
