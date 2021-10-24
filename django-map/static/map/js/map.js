(function () {
    window.addEventListener("map:init", function (e) {
        var markers = new L.FeatureGroup()
        var detail = e.detail
        var map = detail.map
        // Actuals should be declared as a global var
        actuals.forEach(element => {
          var marker = L.marker([element.fields.latitude, element.fields.longitude])
          markers.addLayer(marker)
        }, false);
        map.addLayer(markers)
      })
}) ()
