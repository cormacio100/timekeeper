/* define GLOBAL map_variable */
var global_map;
var pageLoaded=0;

/* function to initialise and load the map to the page */
function initialise_map(){
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
}

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}



/**
 * When the Page Loads
 */ 
function prepare_map(){

        initialise_map();


}
