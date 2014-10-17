var map = L.map('map');

L.tileLayer('https://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
    '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
    'Imagery © <a href="http://mapbox.com">Mapbox</a>',
  id: 'examples.map-i875mjb7'
}).addTo(map);

var defaultcenter = L.latLng(47.760, -122.1924);

map.setView(defaultcenter, 17);

var discoveryHallCoords = [
  L.latLng(47.7590377, -122.1924526),
  L.latLng(47.7592433, -122.1914825),
  L.latLng(47.7590333, -122.1913806),
  L.latLng(47.7589935, -122.1915516),
  L.latLng(47.759009, -122.1915581),
  L.latLng(47.7589736, -122.1917127),
  L.latLng(47.7589449, -122.1917028),
  L.latLng(47.7588034, -122.1923507)
];

var discoveryHall = L.polygon(discoveryHallCoords, {color: 'red'}).addTo(map);
