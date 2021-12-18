const labels = "C";
let labelIndex = 0;
let map;
let markers = [];
let marker


// ADD MARKER to the map at the clicked location  and push to the array
function addMarker(location,map){

      deleteMarkers();
      
      marker = new google.maps.Marker({
        position: location,
        label: labels[labelIndex++ % labels.length],
        map: map, 
        draggable: true,
      });
      
      markers.push(marker);
      var pos = marker.getPosition();
      console.log(pos);
      
      marker.addListener('drag',function(event) {
        $('#lat').val(event.latLng.lat());
        $('#lng').val(event.latLng.lng());
      });
      
      marker.addListener('dragend',function(event) {
        $('#lat').val(event.latLng.lat())  ;
        $('#lng').val(event.latLng.lng())  ;
      });

}

// Sets the map on all markers in the array
function setMapOnall(map){
  for (let i = 0; i < markers.length; i++){
    markers[i].setMap(map);
  }
}
  
// remove the markers from the map, but keep them in the array
function hideMarkers(){
  setMapOnall(null);
}

// show any markers currently in the array
function showMarkers(){
  setMapOnall(map);
}

// Delete all markers from the array by removing references to them
function deleteMarkers(){
  hideMarkers();
  markers = [];
}