
function initialize_map() {

    var center = new google.maps.LatLng(0, 0);

    var maps_settings = {
        zoom: 4,
        center: center,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(document.getElementById("map"), maps_settings);

    google.maps.event.addDomListener(document.getElementById('map_form'), 'submit', function(e) {

        e.preventDefault();

        // Add the current location to the map 

        var lat = document.getElementById('lat').value;
        var lng = document.getElementById('lng').value;  
        var mapCenter = new google.maps.LatLng(lat, lng);

        new google.maps.Marker({
            position: mapCenter,
            title: 'Current location',
            map: map
        });


        // Center map
        map.setCenter(mapCenter);
    });

    fetchData(map);
}

// Get all the top five locations and add them to the map 
async function fetchData(map) {

    var lat = document.getElementById('lat').value;
    var lng = document.getElementById('lng').value; 

    console.log ("lat & lng: "+ lat+ lng)
    const response = await fetch('http://127.0.0.1:5000/fts/locator?lat='+lat+"&lng="+lng, { mode: 'cors'});
    const data = await response.json();


    console.log(data);

    const obj = JSON.parse(JSON.stringify(data));

    var list_size = Object.keys(obj.Longitude).length;

    for (let i = 0; i<list_size; i++){
    	
        var tmp_lng = obj.Longitude[i];
        var tmp_lat = obj.Latitude[i];

        console.log (tmp_lat + " " + tmp_lng);

        new google.maps.Marker({
            position: new google.maps.LatLng(tmp_lat, tmp_lng),
            title: 'closest location: '+i,
            map: map
        });
                
    }
}
