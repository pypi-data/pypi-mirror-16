
function polar_clock(config) {

  var w = config.width,
    h = config.height,
    r = Math.min(w, h) / 1.6,
    f = Math.floor(r / 25),
    s = .09,
    fsec = d3.time.format("%S s"),
    fmin = d3.time.format("%M m"),
    fhou = d3.time.format("%H h"),
    fwee = d3.time.format("%a"),
    fdat = d3.time.format("%d d"),
    fmon = d3.time.format("%b");

  var fill = d3.scale.linear()
    .range(["hsl(-180, 50%, 50%)", "hsl(180, 50%, 50%)"])
    .interpolate(interpolateHsl);

  var arc = d3.svg.arc()
    .startAngle(0)
    .endAngle(function(d) {
    return d.value * 2 * Math.PI;
  })
    .innerRadius(function(d) {
    return d.index * r;
  })
    .outerRadius(function(d) {
    return (d.index + s) * r;
  });

  var svg = d3.select(config.placeholder).append("svg")
    .attr("width", w)
    .attr("height", h)
    .append("g")
    .attr("transform", "translate(" + w / 2 + "," + h / 2 + ")");

  var div = d3.select(config.placeholder).append("div")
    .attr("class", "tooltip");

  var g = svg.selectAll("g")
    .data(fields)
    .enter().append("g");

  g.append("path")
    .style("fill", function(d) {
    return fill(d.value);
  })
    .attr("d", arc);

  g.append("text")
    .attr("text-anchor", "middle")
    .attr("dy", "1em")
    .attr("style", "font: " + f + "px sans-serif; font-weight: bold;")
    .text(function(d) {
    return d.text;
  });

  g.on("mousemove", function(d) {
    div.transition()
      .duration(200)
      .style("opacity", .9);
    div
    .text(d.text)
      .style("position", "absolute")
      .style("top", (d3.event.pageY)+"px");
      //.style("left", (d3.event.pageX / 2 - w)+"px");
  });
  g.on("mouseout", function(d) {
      div.transition()
          .duration(500)
          .style("opacity", 0);
  });

  // Update arcs.
  d3.timer(function() {
    var g = svg.selectAll("g")
      .data(fields);

    g.select("path")
      .style("fill", function(d) {
      return fill(d.value);
    })
      .attr("d", arc);

    g.select("text")
      .attr("dy", function(d) {
      return d.value < .5 ? "-.5em" : "1em";
    })
      .attr("transform", function(d) {
      return "rotate(" + 360 * d.value + ")" + "translate(0," + -(d.index + s / 2) * r + ")" + "rotate(" + (d.value < .5 ? -90 : 90) + ")"
    })
      .text(function(d) {
      return d.text;
    });
  });

  // Generate the fields for the current date/time.

  function fields() {
    var d = new Date;

    function days() {
      return 32 - new Date(d.getYear(), d.getMonth(), 32).getDate();
    }

    var second = (d.getSeconds() + d.getMilliseconds() / 1000) / 60,
      minute = (d.getMinutes() + second) / 60,
      hour = (d.getHours() + minute) / 24,
      weekday = (d.getDay() + hour) / 7,
      date = (d.getDate() - 1 + hour) / days(),
      month = (d.getMonth() + date) / 12;

    return [{
      value: second,
      index: .7,
      text: fsec(d)
    }, {
      value: minute,
      index: .6,
      text: fmin(d)
    }, {
      value: hour,
      index: .5,
      text: fhou(d)
    }, {
      value: weekday,
      index: .3,
      text: fwee(d)
    }, {
      value: date,
      index: .2,
      text: fdat(d)
    }, {
      value: month,
      index: .1,
      text: fmon(d)
    }, ];
  }

  // To avoid shortest-path interpolation.

  function interpolateHsl(a, b) {
    var i = d3.interpolateString(a, b);
    return function(t) {
      return d3.hsl(i(t));
    };
  }
}

