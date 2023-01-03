function createMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: {lat: -0.4347, lng: 36.9634},
      });
      var marker = new google.maps.Marker({
        position: {lat: -0.4347, lng: 36.9634},
        map: map,
        title: 'Hello map'
      });
}
// Wait for the Google Maps API to finish loading
google.maps.event.addDomListener(window, 'load', createMap);
  