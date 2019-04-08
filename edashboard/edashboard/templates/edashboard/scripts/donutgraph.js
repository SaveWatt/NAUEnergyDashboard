{% load staticfiles %}

var gaugeChart = AmCharts.makeChart("chartdiv", {
  "type": "gauge",
  "theme": "none",
  "axes": [{
    "axisAlpha": 0,
    "tickAlpha": 0,
    "labelsEnabled": false,
    "startValue": 0,
    "endValue": {{ elec_total|safe }} + {{ elec_total_yesterday|safe }},
    "startAngle": 0,
    "endAngle": 270,
    "bands": [{
      "color": "#eee",
      "startValue": 0,
      "endValue": {{ elec_total|safe }} + {{ elec_total_yesterday|safe }},
      "radius": "100%",
      "innerRadius": "85%"
    }, {
      "color": "#003467",
      "startValue": 0,
      "endValue": {{ elec_total|safe }},
      "radius": "100%",
      "innerRadius": "85%",
      "balloonText": "{{ elec_total|safe }} kW"

    }, {
      "color": "#eee",
      "startValue": 0,
      "endValue": {{ elec_total|safe }} + {{ elec_total_yesterday|safe }},
      "radius": "80%",
      "innerRadius": "65%"
    }, {
      "color": "#fdd400",
      "startValue": 0,
      "endValue": {{ elec_total_yesterday|safe }},
      "radius": "80%",
      "innerRadius": "65%",
      "balloonText": "{{ elec_total_yesterday|safe }} kW"
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
