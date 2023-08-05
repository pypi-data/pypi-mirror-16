/**
 * Dashboard route providing an overview of current counter readings.
 */
var DashboardRoute = Vue.extend({
  template: "#dashboard-route-template",
  name: 'Dashboard',
  components: { CurrentValue },
  data: function () {
    return {
      displayType: store.state.selectedDisplayType,
      displayTypes: [
        {text: 'Single', value: 'single'},
        {text: 'Mean', value: 'mean'},
        {text: 'Std Dev', value: 'std'}
      ],

      displayOption: store.state.selectedDisplayOption,
      displayOptions: [
        {text: '3', value: '3'},
        {text: '5', value: '5'},
        {text: '10', value: '10'},
        {text: '20', value: '20'},
        {text: '100', value: '100'}
      ],

      counters: 2,
      offsetLocked: false,
      reprateLocked: false,
      offsetFreqs: [],
      reprateFreqs: [],
      counterFreqs: [[], []]
    };
  },

  computed: {
    offsetFreq: function () {
      return this.getDisplayValue(this.offsetFreqs);
    },
    reprateFreq: function () {
      return this.getDisplayValue(this.reprateFreqs);
    }
  },

  methods: {
    appendFrequency: function (array, frequency) {
      array.unshift(frequency);
      if (array.length > 100) {
        array.pop();
      }
      return array;
    },

    getDisplayValue: function (array) {
      let result;
      const option = Number(this.displayOption);
      switch (this.displayType) {
      case 'single':
        result = array[0];
        break;
      case 'mean':
        result = math.mean(array.slice(0, option));
        break;
      case 'std':
        result = math.std(array.slice(0, option));
        break;
      }

      result = result || '---';
      if (typeof result != "string") {
        result = result.toFixed(4);
      }

      return result;
    },

    counterFreq: function (n) {
      let array = this.counterFreqs[n];
      return this.getDisplayValue(array);
    },

    handleData: function (newData) {
      this.offsetLocked = newData.lb2_status === 2;
      this.reprateLocked = newData.lb1_status === 2;

      this.appendFrequency(this.offsetFreqs, newData.offset_freq);
      this.appendFrequency(this.reprateFreqs, newData.reprate_freq);

      this.counters = newData.counter_channels;
      for (let i = 0; i < newData.counter_channels; i++) {
        while (this.counterFreqs.length < this.counters) {
          this.counterFreqs.push([]);
        }
        this.appendFrequency(this.counterFreqs[i], newData[`counter${i}_freq`]);
      }
    },

    setDisplayType: function () {
      store.setDisplayType(this.displayType);
    },

    setDisplayOption: function () {
      store.setDisplayOption(this.displayOption);
    }
  },

  created: function () {
    store.on('new-data', this.handleData);
  },

  destroyed: function () {
    store.removeListener('new-data', this.handleData);
  }
});

/** Display of all data values in a sorted table. */
var StatusRoute = Vue.extend({
  template: "#status-route-template",
  name: 'Status',
  data: function () {
    return {
      keys: [],
      values: []
    };
  },
  methods: {
    handleData: function (newData) {
      this.keys = Object.keys(newData).sort();
      let values = [];
      for (let key of this.keys) {
        values.push(newData[key]);
      }
      this.values = values;
    }
  },
  created: function () {
    store.on('new-data', this.handleData);
  },
  destroyed: function () {
    // Why doesn't this work?
    store.removeListener('new-data', this.handleData);
  }
});

/** History (chart) route. */
var ChartsRoute = Vue.extend({
  template: "#charts-route-template",
  name: 'Charts',

  components: {
    "comb-chart": CombChart
  },

  data: function () {
    return {
      selectedKey: store.state.selectedChartKey,
      metadata: store.state.metadata,
      keys: store.state.chartKeys,
      chartUpdatesEnabled: true
    };
  },

  methods: {
    toggleUpdates: function () {
      this.chartUpdatesEnabled = !this.chartUpdatesEnabled;
      console.debug('Chart updates ' + (this.chartUpdatesEnabled ? 'enabled' : 'disabled'));
    },

    clearHistory: function () {
      store.clearHistory();
      console.debug('Clearing history');
    },

    setSelectedChartKey: function () {
      store.setSelectedChartKey(this.selectedKey);
    }
  },

  // TODO: de-ES6ify
  ready: function () {
    store.on('new-data', (newData) => {
      if (this.chartUpdatesEnabled) {
        let times = [];
        store.state.history.timestamp.forEach((value) => {
          times.push(new Date(value*1000));
        });

        for (let n = 0; n < store.state.currentData.counter_channels; n++) {
          const key = `counter${n}_freq`;
          if (this.keys.indexOf(key) < 0) {
            this.keys.push(`counter${n}_freq`);
          }
        }

        for (let chart of this.$children) {
          chart.update(times);
        }
      }
    });
  }
});

/** Route for downloading data via HTTP. */
var DownloadRoute = Vue.extend({
  template: "#download-route-template",
  data: function () {
    return {
      start: '',
      end: moment().toISOString(),
      availableKeys: [],
      keys: [],
      selectedKeys: []
    };
  },

  computed: {
    keys: function () {
      let keys = new Set();
      for (let key in this.availableKeys) {
        if (key != 'timestamp') {
          keys.add(key);
        }
      }
      return Array.from(keys).sort();
    },

    downloadDisabled: function () {
      if (this.start == '' || this.selectedKeys.length == 0) {
        return true;
      } else {
        return false;
      }
    }
  },

  methods: {
    download: function () {
      let start = moment(this.start).unix();
      let end = moment(this.end).unix();
      console.debug(start);
      console.debug(end);
      let keys = Array.from(this.selectedKeys);
      keys.push('timestamp');
      let url = `/data?start=${start}&end=${end}&keys=${keys.join(',')}`;
      window.open(url);
    }
  },

  ready: function () {
    // Enable datetime pickers
    $("#datetime-start").datetimepicker();
    $("#datetime-end").datetimepicker();

    // Get available datatypes for download
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/data/keys');
    xhr.setRequestHeader('accept', 'application/json');
    xhr.onload = function () {
      let res = JSON.parse(xhr.response);
      let keys = [];
      for (let key of res.keys) {
        keys.push(key);
      }
      this.availableKeys = keys;
    }.bind(this);
    xhr.send();
  }
});
