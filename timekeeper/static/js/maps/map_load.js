/* define GLOBAL map_variable */
const labels = "C";
let label_index = 0;
let map;
let markers = [];
let marker


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
	
  add_marker(newCenter,map);
  populate_lat_lng(newCenter);
  
}

// Set the map sented depending on the Lat & Lng received
function populate_lat_lng(newCenter){
  $('#id_lat').val(newCenter['lat']).prop("readonly", true);
  $('#id_lng').val(newCenter['lng']).prop("readonly", true);  ;
}


// ADD MARKER to the map at the clicked location and push to the MARKER array
function add_marker(location,map){

      delete_markers();
      
      marker = new google.maps.Marker({
        position: location,
        label: labels[label_index++ % labels.length],
        map: map, 
        draggable: true,
      });
      
      markers.push(marker);
      var pos = marker.getPosition();
      console.log(pos);
      
      marker.addListener('drag',function(event) {
        populate_lat_lng(event.latLng);
      });
      
      marker.addListener('dragend',function(event) {
        populate_lat_lng(event.latLng);
      });
}



// adds all markers in the marker array to the map
function set_map_on_all(map){
  for (let i = 0; i < markers.length; i++){
    markers[i].setMap(map);
  }
}

// show any markers currently in the marker array
function show_markers(){
  set_map_on_all(map);
}
  

// remove the markers in the marker array from the map, but keep them in the array
function hide_markers(){
  set_map_on_all(null);
}


// Delete all markers from the marker array, which will remove them from teh map
function delete_markers(){
  hide_markers();
  markers = [];
}

/////////////////////////////////////////////////////////////////////////
//
//  MAP initialiser functions
//  
/////////////////////////////////////////////////////////////////////////

function init_expenses_map(){
    var selected_county = "";
    var selected_client = "";
    var selected_client_arr = [];
    //var lat = 0.0
    //var lng = 0.0
    var newCenter = [];
    
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 7,
        center: myCenter,
    });
    
    ////////////////////////////////////////////////////////////////////////////
    //  Detect when the user has changed the Client Select menu and retrieve
    //  details sp
    ////////////////////////////////////////////////////////////////////////////
    $('#company_name').change(function(){
     
        selected_client = $(this).find("option:selected").attr('value');
        console.log('selected_client:'+selected_client);
        
        ///////////////////////////////////////////////////
        //  split the selected_client string into an array
        //  as it contains the lat and lng for the map
        //////////////////////////////////////////////////
        selected_client_arr = selected_client.split("__");
        //for(var i=0; i< selected_client_arr.length; i++) {
        //    console.log(selected_client_arr[i]);
        //}
        selected_county = selected_client_arr[1];
        newCenter['lat'] = parseFloat(selected_client_arr[2]);
        newCenter['lng'] = parseFloat(selected_client_arr[3]);
        
        console.log('selected_county: '+selected_county);
        console.log('lat: '+newCenter['lat']);
        console.log('lng: '+ newCenter['lng']);
        ///////////////////////////////////////////////////
        //  Based on the client selected
        //  -   Recenter the map
        //  -   Add a Map Marker
        //  -   Populate the read only fields of the form
        ///////////////////////////////////////////////////
        re_center(map,selected_county);
        add_marker(newCenter,map);
        populate_lat_lng(newCenter);
    });
    
    
    
}


/* function to initialise and load the map to the ADD Client Page page */
function init_clients_map(){
    
    /**
     * Load the initial map with marker set to first County in menu ---Antrim
     */ 
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 7,
        center: myCenter,
    });
    
    add_marker(antrimCenter,map);
    populate_lat_lng(antrimCenter);

    
    /**
     *  Event Listener calls addMarker when the map is clicked
     *  Also retrieves the Latitured and Longitude of the marker
     */ 
    google.maps.event.addListener(map,"click",(event) => {
        add_marker(event.latLng, map);
        populate_lat_lng(event.latLng);
    });
    
    
    //  Select the county to focus on
    $("#id_county").change(function() {
        console.log('item changed');
        var selectedCounty = $('#id_county option:selected').text();
        console.log(selectedCounty);
        re_center(map,selectedCounty);
    });

}
