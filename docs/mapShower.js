const maps = [
    "maps/map_conflict_feature_geojson.html",
    "maps/heatmap_w_time.html",
    "maps/map_conflict_feature_geojson_total_displacement.html",
    "maps/map_conflict_feature_geojson_gdp.html",
    "maps/map_conflict_feature_geojson_hdi.html",
    "viz_gexf/index.html"
];


function showMap(idx) {
    const i = parseInt(idx);
    d3.select(`#map${i}`)
        .append('object')
        .attr('data', maps[i])
        .attr('width', "60%")
        .attr('height', "900")
        .attr('class', 'center-block');

    d3.select(`#button${i}`)
        .remove();
}