var router = new VueRouter();

router.map({
  '/dashboard': {
    component: DashboardRoute
  },
  '/status': {
    component: StatusRoute
  },
  '/history': {
    component: ChartsRoute
  },
  '/download': {
    component: DownloadRoute
  }
});

router.redirect({
  '/': '/dashboard'
});

router.beforeEach(function (transition) {
  store.setActiveRoute(transition.to.path.substr(1));
  store.removeAllListeners('new-data');
  transition.next();
});

router.start(App, '#app');

window.onload = function () {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/data/metadata');
  xhr.setRequestHeader('accept', 'application/json');
  xhr.onload = function () {
    var metadata = JSON.parse(xhr.response);
    store.setMetadata(metadata);
  };
  xhr.send();
};
