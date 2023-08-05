/** Global app data storage. */
var HISTORY_MAX_LENGTH = 60*60*1;

var store = new EventEmitter();

// For storing a timer to check if the server is reachable.
store.serverTimer = null;

store.state = {
  // General state
  serverReachable: false,
  activeRoute: 'dashboard',
  currentData: {},
  history: {},
  metadata: {},

  // DashboardView state
  selectedDisplayType: 'single',
  selectedDisplayOption: '3',

  // ChartsView state
  selectedChartKey: 'reprate_freq',
  chartKeys: ['reprate_freq', 'offset_freq']
};

// Routing
// ---------------------------------------------------------------------

store.setActiveRoute = function (route) {
  store.state.activeRoute = route;
  store.emit('new-route');
};

// Incoming data handling
// ---------------------------------------------------------------------

store.setData = function (newData) {
  store.setServerState(true);
  store.state.currentData = newData;

  if (Object.keys(store.state.history).length == 0) {
    for (let key in newData) {
      store.state.history[key] = [newData[key]];
    }
  } else {
    for (let key in newData) {
      store.state.history[key].push(newData[key]);
      if (store.state.history[key].length > HISTORY_MAX_LENGTH) {
        store.state.history[key].shift();
      }
    }
  }

  store.emit('new-data', newData);
};

store.clearHistory = function () {
  store.state.history = {};
};

store.setMetadata = function (newMetadata) {
  store.state.metadata = newMetadata;
  store.emit('new-metadata');
};

store.setServerState = function (state) {
  if (state) {
    window.clearTimeout(store.serverTimer);
    store.serverTimer = window.setTimeout(function () {
      store.setServerState(false);
    }, 5000);
  }

  store.serverReachable = state;
  store.emit('server-state-change', state);
};

function serverTimeoutCheck() {
  store.setServerState(false);
}

// DashboardView setters
// ---------------------------------------------------------------------

store.setDisplayType = function (type) {
  store.state.selectedDisplayType = type;
  store.emit('dashboard-update');
};

store.setDisplayOption = function (opt) {
  store.state.selectedDisplayOption = opt;
  store.emit('dashboard-update');
};

// ChartsView setters
// ---------------------------------------------------------------------

store.setSelectedChartKey = function (key) {
  store.state.selectedChartKey = key;
};
