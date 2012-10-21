

http://216.121.120.114/Project2


# Project 2: Foursquare - Stats for a City #
## Description ##
The objective of this project is to provide a general idea of a city or metropolitan area based on popular venues (as per Foursquare checkins) for a specific period of time

This project requires that you use reverse geocoding, either by writing your own program or using a web service (most of the free ones have limitations). Depending on the software tool you use, you might need to write a program to convert a Unix timestamp (Epoch Time) to a regular date and time.
## Metrics ##
All metrics are for the specified period and chosen city.

 1. Most popular Arts & Entertainment venues
  1. Present the top 5 most popular venues in this category
  1. Present the top 5 most popular venues in this category grouped by day of the week
  1. Present the top 5 most popular venues in this category grouped by day or night (day is from 6:01am to 6:00pm, night is 6:01pm to 6:00am)
 1. Most popular Food venues
  1. Present the top 3 most popular venues for breakfast (checkins from 6:00am to 10:59am)
  1. Present the top 5 most popular venues for brunch (checkins from 10:00am to 2:00pm, Sundays only)
  1. Present the top 5 most popular venues for lunch (checkins from 11:00am to 2:00pm)
  1. Present the top 10 most popular venues for dinner (checkins from 5:00pm to 10:00pm)
 1. Most popular Nightlife Spot venue
  1. Present the top 10 most popular venues for this category by day of week, gender and peak time
 1. Most popular Park & Outdoors venue
  1. Present the top 10 most popular venues for this category by day of week, gender and peak time
 1. Most popular Shops & Service venues
  1. For gender female, present the top 10 venues for weekdays and weekends
  1. For gender male, present the top 10 venues for weekdays and weekends
 1. Most popular Travel & Transport venue
  1. Present the peak usage hours by day of week for each of the following venues: Bus, Ferry, Light Rail, Subway, Taxi and Train
 1. Overall most popular venues
  1. Present the top 10 most popular venues for the selected city, broken down by gender and weekday/weekend
## Data ##
We have access to Foursquare data that is in JSON format. An example of a check-in:
{{{
{"checkin":{
  "venue":{
    "id":"4b0bd124f964a520e03323e3",
    "name":"Changi International Airport (SIN)"},
  "mayor":{"type":"nochange"},
  "user":{"gender":"none"},
  "badges":[],
  "created":1330207821,
  "geolat":1.354832916016495,
  "geolong":103.98797254038077,
  "timezone":"Asia\/Singapore",
  "primarycategory":{
    "id":"4bf58dd8d48988d1ed931735",
    "fullpathname":"Travel & Transport:Airports",
    "nodename":"Airports",
    "iconurl":"https:\/\/foursquare.com\/img\/categories\/travel\/airport.png"}
  }
}
}}}

Information on Foursquare categories can be found at http://aboutfoursquare.com/foursquare-categories/
## Deployment ##
### Splunk ###
Use one search head and two indexers.
### Hadoop ###
Use one master and two slaves. You can use HBase or Hive

