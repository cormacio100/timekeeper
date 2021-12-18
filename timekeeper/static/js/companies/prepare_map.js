/* define GLOBAL map_variable */
const labels = "C";
let labelIndex = 0;
let map;
let markers = [];
let marker

const myCenter = {lat:53.423596, lng:-7.934211};
//  Republic
const clareCenter = {lat:52.897656, lng:-9.001446};
const corkCenter = {lat:51.888218, lng:-8.500987};
const cavanCenter = {lat:54.004074, lng:-7.414240};
const carlowCenter = {lat:52.835880, lng:-6.919208};
const donegalCenter = {lat:54.897377, lng:-7.998693};
const dublinCenter = {lat:53.347896, lng:-6.276414};
const galwayCenter = {lat:53.271637, lng:-9.060255};
const kildareCenter = {lat:53.161312, lng:-6.905107};
const kilkennyCenter = {lat:52.653602, lng:-7.245838};
const kerryCenter = {lat:52.014322, lng:-9.769697};
const longfordCenter = {lat:53.727550, lng:-7.795861};
const louthCenter = {lat:53.912289, lng:-6.471961};
const limerickCenter = {lat:52.659897, lng:-8.624132};
const leitrimCenter = {lat:54.185595, lng:-8.064960};
const laoisCenter = {lat:52.981514, lng:-7.371835};
const meathCenter = {lat:53.626562, lng:-6.764452};
const monaghanCenter = {lat:54.171889, lng:-6.910285};
const mayoCenter = {lat:53.949901, lng:-9.334534};
const offalyCenter = {lat:53.203317, lng:-7.658506};
const roscommonCenter = {lat:53.708854,lng:-8.230562};
const sligoCenter = {lat:54.273512, lng:-8.482532};
const tipperaryCenter = {lat:52.662315, lng:-7.961775};
const waterfordCenter = {lat:52.253049, lng:-7.113459};
const westmeathCenter = {lat:53.513374, lng:-7.483095};
const wicklowCenter = {lat:52.990023, lng:-6.360773};
const wexfordCenter = {lat:52.334171, lng:-6.474478};
//  North
const fermanaghCenter = {lat:54.34621017328863, lng:-7.6323280848920625}; 
const tyroneCenter = {lat:54.61492320729015, lng:-7.099613264345004};
const derryCenter = {lat:54.99995064883284, lng:-7.30684127517299};
const downCenter = {lat:54.4037063419809, lng:-5.897655996747719};
const antrimCenter = {lat:54.74406894258395, lng:-6.2148926143278125};
const armaghCenter = {lat:54.35231761428671, lng:-6.652675406799182};


function re_center(map,selectedCounty){
  var newCenter = myCenter;
  
  console.log('selectedCounty is '+selectedCounty);
  
  if("Clare"==selectedCounty){
    newCenter = clareCenter;
  }
    else if("Cork"==selectedCounty){
    newCenter=corkCenter;
  }
    else if("Cavan"==selectedCounty){
    newCenter=cavanCenter;
  }
    else if("Carlow"==selectedCounty){
    newCenter=carlowCenter;
  }
    else if("Donegal"==selectedCounty){
    newCenter=donegalCenter;
  }
    else if("Dublin"==selectedCounty){
    newCenter=dublinCenter;
  }
    else if("Galway"==selectedCounty){
    newCenter=galwayCenter;
  }
    else if("Kildare"==selectedCounty){
    newCenter=kildareCenter;
  }
    else if("Kilkenny"==selectedCounty){
    newCenter=kilkennyCenter;
  }
    else if("Kerry"==selectedCounty){
    newCenter=kerryCenter;
  }
    else if("Longford"==selectedCounty){
    newCenter=longfordCenter;
  }
    else if("Louth"==selectedCounty){
    newCenter=louthCenter;
  }
    else if("Limerick"==selectedCounty){
    newCenter=limerickCenter;
  }
    else if("Leitrim"==selectedCounty){
    newCenter=leitrimCenter;
  }
    else if("Laois"==selectedCounty){
    newCenter=laoisCenter;
  }
    else if("Meath"==selectedCounty){
    newCenter=meathCenter;
  }
    else if("Monaghan"==selectedCounty){
    newCenter=monaghanCenter;
  }
    else if("Mayo"==selectedCounty){
    newCenter=mayoCenter;
  }
    else if("Offaly"==selectedCounty){
    newCenter=offalyCenter;
  }
    else if("Roscommon"==selectedCounty){
    newCenter=roscommonCenter;
  }
    else if("Sligo"==selectedCounty){
    newCenter=sligoCenter;
  }
    else if("Tipperary"==selectedCounty){
    newCenter=tipperaryCenter;
  }
    else if("Waterford"==selectedCounty){
    newCenter=waterfordCenter;
  }
    else if("Westmeath"==selectedCounty){
    newCenter=westmeathCenter;
  }
    else if("Wicklow"==selectedCounty){
    newCenter=wicklowCenter;
  }
    else if("Wexford"==selectedCounty){
    newCenter=wexfordCenter;
  }
    else if("Fermanagh"==selectedCounty){
    newCenter=fermanaghCenter;
  }
    else if("Tyrone"==selectedCounty){
    newCenter=tyroneCenter;
  }
    else if("Derry"==selectedCounty){
    newCenter=derryCenter;
  }
    else if("Down"==selectedCounty){
    newCenter=downCenter;
  }
    else if("Antrim"==selectedCounty){
    newCenter=antrimCenter;
  }
    else if("Armagh"==selectedCounty){
    newCenter=armaghCenter;
  }
  
  console.log('recentering');
  
  map.setCenter(newCenter);
	map.setZoom(9);
  
}





// ADD MARKER to the map at the clicked location  and push to the array
function add_marker(location,map){

      delete_markers();
      
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
function set_map_on_all(map){
  for (let i = 0; i < markers.length; i++){
    markers[i].setMap(map);
  }
}

// show any markers currently in the array
function show_markers(){
  set_map_on_all(map);
}
  

// remove the markers from the map, but keep them in the array
function hide_markers(){
  set_map_on_all(null);
}


// Delete all markers from the array by removing references to them
function delete_markers(){
  hide_markers();
  markers = [];
}



/* function to initialise and load the map to the page */
function init_map(){
    
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 7,
        center: myCenter,
    });
    
    /**
     *  Event Listener calls addMarker when the map is clicked
     *  Also retrieves the Latitured and Longitude of the marker
     */ 
    google.maps.event.addListener(map,"click",(event) => {
        add_marker(event.latLng, map);
        $('#lat').val(event.latLng.lat())  ;
        $('#lng').val(event.latLng.lng())  ;
    });
    
    
    //  Select the county to focus on
    $("#id_county").change(function() {
        console.log('item changed');
        var selectedCounty = $('#id_county option:selected').text();
        console.log(selectedCounty);
        re_center(map,selectedCounty);
    });

    

    /*
    var myCenter=new google.maps.LatLng(53.423596, -7.934211);
    
    	// create an object for map properties
	var mapProp={
		center: myCenter,
		zoom:7,
		mapTypeId:google.maps.MapTypeId.ROADMAP
	};
	
	// create new google Maps object and pass in the location for where it will be displayed 
	// as well as the properties
	global_map = new google.maps.Map(document.getElementById("map"),mapProp);	
	
	console.log("map loaded...");
	*/
}



/**
 * When the Page Loads
 */ 
function prepare_map(){
    init_map();
}
