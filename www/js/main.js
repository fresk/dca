window.map;
var marker_sets = {};


function create_marker(mdata, template_name) {
    if (template_name == undefined){
    	template_name = "marker_tmpl";
    }

	var geo_point = new google.maps.LatLng(mdata.geo.lat, mdata.geo.lng)
	var marker = new google.maps.Marker({
		map: null,
		position: geo_point,
		title: mdata.title
	});


	google.maps.event.addListener(marker, 'click', function () {
		if (marker.info_window == undefined) {
			marker.info_window = new google.maps.InfoWindow({
				content: ich[template_name](mdata)[0],
				maxWidth: 430
			});
		}

		marker.info_window.open(map, marker);
		console.log(mdata);
	});

	return marker;
}

function show_marker_set(set_name) {
	$.each(marker_sets, function (key, val) {
		$.each(val, function (idx, marker) {
			if (set_name == key || set_name == 'all')
				//console.log(set_name, marker, new_map);
				marker.setMap(window.map);
			else
				marker.setMap(null);
		});
	});
}


function initialize() {
	window.map = new google.maps.Map(document.getElementById('map-canvas'), {
		zoom: 8,
		center: new google.maps.LatLng(41.6, -93.6),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});

	marker_sets.nrhp = []
	$.getJSON("data/nrhp.json", function (data) {
		$.each(data, function (key, val) {
			val.title = val['Property Name'];
			val.info = val['Address Description'];
			val.geo = val.geo[0].geometry.location;
			var m = create_marker(val);
			marker_sets.nrhp.push(m);
		});
	});

	marker_sets.barns = [];
	$.getJSON("data/barns.json", function (data) {
		$.each(data, function (key, val) {
			val.title = val['Property Name'];
			val.info = val['Address Description'];
			var m = create_marker(val);
			marker_sets.barns.push(m);
		});
	});

	marker_sets.landmarks = [];
	$.getJSON("data/landmarks.json", function (data) {
		$.each(data, function (key, val) {
			val.title = val['name'];
			var m = create_marker(val);
            console.log(val, m);
			marker_sets.landmarks.push(m);
		});
        show_marker_set('landmarks');
	});


}

google.maps.event.addDomListener(window, 'load', initialize);