
function digital_clock(config) {

  var enableColor = "#2980b9";
  var disableColor = d3.hsl(enableColor).darker(4);
  var size = {
    width: config.width,
    height: config.height
  };
  var w = size.width / 28;
  var h = w * 2;
  var paths = [
    [
      [0, w * (1 / 4)],
      [0, w * (5 / 4) + h],
      [w / 2, w * (7 / 4) + h],
      [w, w * (5 / 4) + h],
      [w, w * (5 / 4)]
    ],
    [
      [0, w * (11 / 4) + h],
      [0, w * (15 / 4) + (h * 2)],
      [w, w * (11 / 4) + (h * 2)],
      [w, w * (11 / 4) + h],
      [w / 2, w * (9 / 4) + h]
    ],
    [
      [0, 0],
      [w, w],
      [w + h, w],
      [w * 2 + h, 0]
    ],
    [
      [w, w * (6 / 4) + h],
      [w / 2, w * (8 / 4) + h],
      [w, w * (10 / 4) + h],
      [w + h, w * (10 / 4) + h],
      [w + h + (w / 2), w * (8 / 4) + h],
      [w + h, w * (6 / 4) + h]
    ],
    [
      [w, w * (12 / 4) + (h * 2)],
      [0, w * (16 / 4) + (h * 2)],
      [w * 2 + h, w * (16 / 4) + (h * 2)],
      [w + h, w * (12 / 4) + (h * 2)]
    ],
    [
      [w + h, w * (5 / 4)],
      [w + h, w * (5 / 4) + h],
      [w + h + (w / 2), w * (7 / 4) + h],
      [w * 2 + h, w * (5 / 4) + h],
      [w * 2 + h, w * (5 / 4)],
      [w * 2 + h, w * (1 / 4)]
    ],
    [
      [w + h, w * (11 / 4) + h],
      [w + h, w * (11 / 4) + (h * 2)],
      [w * 2 + h, w * (15 / 4) + (h * 2)],
      [w * 2 + h,w * (11 / 4) + h],
      [w + h + (w / 2), w * (9 / 4) + h]
    ]
  ];
  var bits = [
    parseInt("1110111", 2),
    parseInt("1100000", 2),
    parseInt("0111110", 2),
    parseInt("1111100", 2),
    parseInt("1101001", 2),
    parseInt("1011101", 2),
    parseInt("1011111", 2),
    parseInt("1100101", 2),
    parseInt("1111111", 2),
    parseInt("1111101", 2)
  ];

  var svg = d3.select(config.placeholder).append("svg").attr(size);

  function left(digits, colons){
    return (digits || 0) * (w * (9 / 4) + h) + (colons || 0) * (w * (5 / 4));
  }
  function createDigit(pos){
    pos = pos || 0;
    svg
    .append("g")
    .attr("class", "digit")
    .selectAll("polygon")
    .data(paths)
    .enter()
    .append("polygon")
    .attr("points", function(d){
      return d.map(function(a){
        var b = a.concat();
        b[0] += pos;
        return b.join(",");
      }).join(" ");
    })
    .style("fill", enableColor);
  }
  function createColon(pos){
    var axis = [
      {x: pos, y: w * (3 / 4) + (h /2)},
      {x: pos, y: w * (13 / 4) + h}
    ];
    svg
    .append("g")
    .selectAll("rect")
    .data(axis)
    .enter()
    .append("rect")
    .attr({
      x: function(d){ return d.x; },
      y: function(d){ return d.y; },
      width: w,
      height: w
    })
    .style({
      fill: enableColor
    });
  }
  function updateDigit(index, num){
    var bit = bits[num];
    d3.select(
      svg.selectAll("g.digit")[0][index]
    )
    .selectAll("polygon")
    .each(function(d, i){
      d3.select(this).style("fill", (bit & 1 << i) ? enableColor : disableColor);
    });
  }

  createDigit();
  createDigit(left(1));
  createColon(left(2));
  createDigit(left(2, 1));
  createDigit(left(3, 1));
  createColon(left(4, 1));
  createDigit(left(4, 2));
  createDigit(left(5, 2));

  var f = function(n){
    return n > 9 ? "" + n : "0" + n;
  };
  (function loop(){
    var d = new Date;
    var h = f(d.getHours());
    var m = f(d.getMinutes());
    var s = f(d.getSeconds());
    [h[0], h[1], m[0], m[1], s[0], s[1]].forEach(function(n, i){
      updateDigit(i, n);
    });
    setTimeout(loop, 1000);
  })();

}
