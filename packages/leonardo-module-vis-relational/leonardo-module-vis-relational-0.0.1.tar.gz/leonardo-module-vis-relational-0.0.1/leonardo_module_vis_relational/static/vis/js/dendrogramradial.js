
function dendrogram_radial(config) {

  var width = config.width,
    height = config.height;

  var radius = height / 2;

  var cluster = d3.layout.cluster()
    .size([360, radius - 120]);

  var diagonal = d3.svg.diagonal.radial()
    .projection(function(d) { return [d.y, d.x / 180 * Math.PI]; });

  var svg = d3.select(config.placeholder).append("svg")
    .attr("width", radius * 2)
    .attr("height", radius * 2)
    .append("g")
      .attr("transform", "translate(" + radius + "," + radius + ")");

  d3.json(config.data_source, function(error, root) {
    var nodes = cluster.nodes(root);

    var link = svg.selectAll("path.link")
      .data(cluster.links(nodes))
      .enter().append("path")
        .attr("class", "link")
        .attr("d", diagonal);

    var node = svg.selectAll("g.node")
      .data(nodes)
      .enter().append("g")
        .attr("class", "node")
        .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + d.y + ")"; });

    node.append("circle")
      .attr("r", 4.5);

    node.append("text")
      .attr("dy", ".31em")
      .attr("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
      .attr("transform", function(d) { return d.x < 180 ? "translate(8)" : "rotate(180)translate(-8)"; })
      .text(function(d) { return d.name; });
  });

//  d3.select(self.frameElement).style("height", radius * 2 + "px");

}
