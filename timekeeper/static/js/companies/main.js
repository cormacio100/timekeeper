/*  When the listing page loads */

let map;
const myCenter = {lat:53.423596, lng:-7.934211};

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: myCenter,
    zoom: 8,
  });
  
  
  console.log('map loaded');
  console.log('myCenter: lat:'+myCenter['lat']+' lng:'+myCenter['lng']);
}

function main(){
    initMap();
}


