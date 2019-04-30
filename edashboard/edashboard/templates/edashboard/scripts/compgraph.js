{% load staticfiles %}

  new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
  labels: [{% for datas in date%}
                "{{ datas|safe}}",
              {% endfor %}],
  fillOpacity: .3,
  datasets: [
    {% for data in content%}
    {% if forloop.last %}
    {
      data: {{data.0|safe}},
      label: "{{data.1|safe}}",
      borderColor: "{{ data.2|safe}}",
      fill: origin,
      backgroundColor: "{{ data.3|safe}}",
    }
    {% else %}
    {
      data: {{data.0|safe}},
      label: "{{data.1|safe}}",
      borderColor: "{{ data.2|safe}}",
      fill: origin,
      backgroundColor: "{{ data.3|safe}}",
    },
    {% endif %}
    {% endfor %}
  ]
  },
  options: {
  responsive: false,
  title: {
    display: true,
    text: "Comparison of {% for data in content%}{% if forloop.last %}{{data.1|safe}}{% else %}{{data.1|safe}}, {% endif %}{% endfor %} {{utilname|safe}}",
  },
  scales: {
  xAxes: [{
    scaleLabel: {
      display: true,
      labelString: 'Time'
    }
  }],
  yAxes: [{
    scaleLabel: {
      display: true,
      labelString: '{{utilname|safe}}'
    }}]}
  }});
