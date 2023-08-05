
function arc_diagram(config) {

      var width  = config.width;           // width of svg image
      var height = config.width/2;           // height of svg image
      var margin = 20;            // amount of margin around plot area
      var pad = margin / 2;       // actual padding amount
      var radius = 4;             // fixed node radius
      var yfixed = pad + radius;  // y position for all nodes

    d3.json(config.data_source, function(error, graph) {
      arcDiagram(graph);
    });

    /* HELPER FUNCTIONS */

    // Generates a tooltip for a SVG circle element based on its ID
    function addTooltip(circle) {
        var x = parseFloat(circle.attr("cx"));
        var y = parseFloat(circle.attr("cy"));
        var r = parseFloat(circle.attr("r"));
        var text = circle.attr("id");

        var tooltip = d3.select(config.placeholder+" g")
            .append("text")
            .text(text)
            .attr("x", x)
            .attr("y", y)
            .attr("dy", -r * 2)
            .attr("id", config.placeholder+"tooltip");
//            .attr("class", "tooltip");

        var offset = tooltip.node().getBBox().width / 2;

        if ((x - offset) < 0) {
            tooltip.attr("text-anchor", "start");
            tooltip.attr("dx", -r);
        }
        else if ((x + offset) > (width - margin)) {
            tooltip.attr("text-anchor", "end");
            tooltip.attr("dx", r);
        }
        else {
            tooltip.attr("text-anchor", "middle");
            tooltip.attr("dx", 0);
        }
    }

    /* MAIN DRAW METHOD */

    // Draws an arc diagram for the provided undirected graph
    function arcDiagram(graph) {
        // create svg image

        var svg  = d3.select(config.placeholder)
            .append("svg")
            .attr("class", "arc")
            .attr("width", config.width)
            .attr("height", config.height);

        // create plot area within svg image
        var plot = svg.append("g")
            .attr("class", "plot")
            .attr("transform", "translate(" + pad + ", " + pad + ")");

        // fix graph links to map to objects instead of indices
        graph.links.forEach(function(d, i) {
            d.source = isNaN(d.source) ? d.source : graph.nodes[d.source];
            d.target = isNaN(d.target) ? d.target : graph.nodes[d.target];
        });

        // must be done AFTER links are fixed
        linearLayout(graph.nodes);

        // draw links first, so nodes appear on top
        drawLinks(graph.links);

        // draw nodes last
        drawNodes(graph.nodes);
    }

    // Layout nodes linearly, sorted by group
    function linearLayout(nodes) {
        // sort nodes by group
        nodes.sort(function(a, b) {
            return a.group - b.group;
        })

        // used to scale node index to x position
        var xscale = d3.scale.linear()
            .domain([0, nodes.length - 1])
            .range([radius, width - margin - radius]);

        // calculate pixel location for each node
        nodes.forEach(function(d, i) {
            d.x = xscale(i);
            d.y = yfixed;
        });
    }

    // Draws nodes on plot
    function drawNodes(nodes) {
        // used to assign nodes color by group
        var color = d3.scale.category20();

        d3.select(config.placeholder+' svg').selectAll(".node")
            .data(nodes)
            .enter()
            .append("circle")
            .attr("class", "node")
            .attr("id", function(d, i) { return d.name; })
            .attr("cx", function(d, i) { return d.x; })
            .attr("cy", function(d, i) { return d.y; })
            .attr("r",  function(d, i) { return radius; })
            .style("fill",   function(d, i) { return color(d.group); })
            .on("mouseover", function(d, i) { addTooltip(d3.select(this)); })
            .on("mouseout",  function(d, i) { d3.select("#"+config.placeholder+" .tooltip").remove(); });
    }

    // Draws nice arcs for each link on plot
    function drawLinks(links) {
        // scale to generate radians (just for lower-half of circle)
        var radians = d3.scale.linear()
            .range([Math.PI / 2, 3 * Math.PI / 2]);

        // path generator for arcs (uses polar coordinates)
        var arc = d3.svg.line.radial()
            .interpolate("basis")
            .tension(0)
            .angle(function(d) { return radians(d); });

        // add links
        d3.select(config.placeholder+' g').selectAll(".link")
            .data(links)
            .enter()
            .append("path")
            .attr("class", "link")
            .attr("transform", function(d, i) {
                // arc will always be drawn around (0, 0)
                // shift so (0, 0) will be between source and target
                var xshift = d.source.x + (d.target.x - d.source.x) / 2;
                var yshift = yfixed;
                return "translate(" + xshift + ", " + yshift + ")";
            })
            .attr("d", function(d, i) {
                // get x distance between source and target
                var xdist = Math.abs(d.source.x - d.target.x);

                // set arc radius based on x distance
                arc.radius(xdist / 2);

                // want to generate 1/3 as many points per pixel in x direction
                var points = d3.range(0, Math.ceil(xdist / 3));

                // set radian scale domain
                radians.domain([0, points.length - 1]);

                // return path for arc
                return arc(points);
            });
    }

}