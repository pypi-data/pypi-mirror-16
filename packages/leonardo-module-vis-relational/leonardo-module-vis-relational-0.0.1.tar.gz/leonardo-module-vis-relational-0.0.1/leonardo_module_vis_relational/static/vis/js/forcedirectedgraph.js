function force_directed_graph(config) {

  var hash_lookup = [],
    width = config.width,
    height = config.height;

  var svg = d3.select(config.placeholder).append("svg")
    .attr("width", width)
    .attr("height", height);

  var force = d3.layout.force()
    .gravity(config.gravity)
    .distance(config.distance)
    .charge(config.charge)
    .size([width, height]);

  d3.json(config.data_source, function(error, json) {

    json.nodes.forEach(function(d, i) {
      hash_lookup[d.id] = d;
    });

    json.links.forEach(function(d, i) {
      d.source = hash_lookup[d.source];
      d.target = hash_lookup[d.target];
    });

    force
      .nodes(json.nodes)
      .links(json.links)
      .start();

    var link = svg.selectAll(".link")
        .data(json.links)
      .enter().append("line")
        .attr("class", "link");

    var node = svg.selectAll(".node")
        .data(json.nodes)
      .enter().append("g")
        .attr("class", "node")
        .call(force.drag);

    node.append("image")
      .attr("xlink:href", "https://github.com/favicon.ico")
      .attr("x", -8)
      .attr("y", -8)
      .attr("width", 16)
      .attr("height", 16);

    node.append("text")
      .attr("dx", 12)
      .attr("dy", ".35em")
      .text(function(d) { return d.name });

    force.on("tick", function() {
      link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

      node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    });

  });

}