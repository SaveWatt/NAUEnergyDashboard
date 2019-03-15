{% load staticfiles %}

var gaugeChart = AmCharts.makeChart("chartdiv", {
  "type": "gauge",
  "theme": "none",
  "axes": [{
    "axisAlpha": 0,
    "tickAlpha": 0,
    "labelsEnabled": false,
    "startValue": 0,
    "endValue": 100,
    "startAngle": 0,
    "endAngle": 270,
    "bands": [{
      "color": "#eee",
      "startValue": 0,
      "endValue": 100,
      "radius": "100%",
      "innerRadius": "85%"
    }, {
      "color": "#003467",
      "startValue": 0,
      "endValue": 72,
      "radius": "100%",
      "innerRadius": "85%",
      "balloonText": "72%"

    }, {
      "color": "#eee",
      "startValue": 0,
      "endValue": 100,
      "radius": "80%",
      "innerRadius": "65%"
    }, {
      "color": "#fdd400",
      "startValue": 0,
      "endValue": 96,
      "radius": "80%",
      "innerRadius": "65%",
      "balloonText": "96%"
    }]
  }],
  "allLabels": [{
    "text": "Today",
    "x": "49%",
    "y": "5%",
    "size": 15,
    "bold": true,
    "color": "#003467",
    "align": "right"
  }, {
    "text": "Yesterday",
    "x": "49%",
    "y": "15%",
    "size": 15,
    "bold": true,
    "color": "#fdd400",
    "align": "right"
  }],
  "export": {
    "enabled": true
  }
});
