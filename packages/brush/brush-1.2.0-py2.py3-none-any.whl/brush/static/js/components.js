/** Handler for incoming EventSource data. */
var StreamHandler = function (callback) {
  this.stream = new EventSource('/stream');

  this.stream.onmessage = function (msg) {
    store.setData(JSON.parse(msg.data));
  };

  this.stream.onerror = function () {
    store.setServerState(false);
  };
};

/** Comb history chart. */
var CombChart = Vue.extend({
  template: "#chart-template",

  data: function () {
    return {
      chart: null
    };
  },

  props: {
    key: {
      type: String,
      required: true
    }
  },

  ready: function () {
    let canvas = this.$els.canvas;
    let ctx = canvas.getContext('2d');

    const chartOptions = {
      type: 'line',
      options: {
        responsive: true,
        legend: {
          display: false
        },
        tooltips: {
          enabled: true,
          callbacks: {
            title: function (item, data) {
              return moment(new Date(item[0].xLabel)).format('HH:mm:ss');
            }
          }
        },
        animation: {
          duration: 0
        },
        elements: {
          line: {
            tension: 0,
            fill: false
          },
          point: {
            radius: 2
          }
        },
        scales: {
          xAxes: [{
            type: 'linear',
            position: 'bottom',
            ticks: {
              callback: function (value, index, values) {
                return moment(new Date(value)).format('HH:mm:ss');
              }
            }
          }]
        }
      },
      data: {
        datasets: [{
          label: 'value',
          data: []
        }]
      }
    };

    this.chart = new Chart(ctx, chartOptions);
  },

  methods: {
    update: function (times) {
      const data = store.state.history[this.key];
      let datapoints = [];
      for (let i = 0; i < data.length; i++) {
        datapoints.push({x: times[i], y: data[i]});
      }
      this.chart.data.datasets[0].data = datapoints;
      this.chart.update(0);
    }
  }
});

/** Displays a current value from a counter. */
var CurrentValue = Vue.extend({
  template: "#current-value-template",
  props: {
    name: {
      type: String,
      required: true
    },
    value: {
      type: [String, Number],
      required: true
    },
    lockable: {
      type: Boolean,
      required: false,
      default: false
    },
    locked: {
      type: Boolean,
      required: false
    }
  }
});

/** Navigation between routes. */
var Navbar = Vue.extend({
  template: "#navbar-template",
  data: function () {
    return {
      activeRoute: store.state.activeRoute
    };
  },
  computed: {
    dashboardActive: function () {
      return this.activeRoute == 'dashboard';
    },
    statusActive: function () {
      return this.activeRoute == 'status';
    },
    historyActive: function () {
      return this.activeRoute == 'history';
    },
    downloadActive: function () {
      return this.activeRoute == 'download';
    }
  },
  ready: function () {
    store.on('new-route', () => {
      this.$set('activeRoute', store.state.activeRoute);
    });
  }
});

/** Primary app component. */
var App = Vue.extend({
  template: "#app-template",

  data: function () {
    return {
      serverUnreachable: false
    };
  },

  components: {
    "navbar": Navbar,
    "current-value": CurrentValue
  },

  methods: {
    handleServerStateChange: function (state) {
      this.serverUnreachable = !state;
    }
  },

  ready: function () {
    var dataHandler = new StreamHandler();
    store.on('server-state-change', this.handleServerStateChange);
  }
});
