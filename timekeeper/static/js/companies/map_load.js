function initMap() {
    console.log('loading Map');
    
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 7,
        center: myCenter,
    });
  
      //  Event Listener calls addMarker when the map is clicked
  //  Also retrieves the Latitured and Longitude of the marker
  google.maps.event.addListener(map,"click",(event) => {
    addMarker(event.latLng, map);
    $('#lat').val(event.latLng.lat())  ;
    $('#lng').val(event.latLng.lng())  ;
  });
  
  //  add event listeners for the buttons
  document
    .getElementById("show-markers")
    .addEventListener("click", showMarkers);
  document
    .getElementById("hide-markers")
    .addEventListener("click", hideMarkers);
  document
    .getElementById("delete-markers")
    .addEventListener("click", deleteMarkers);
  
  //  Select the county to focus on
  $("#countySelect").change(function() {
      console.log('item changed');
      var selectedCounty = $('#countySelect option:selected').text();
      console.log(selectedCounty);
      reCenter(map,selectedCounty);
  });
    
}