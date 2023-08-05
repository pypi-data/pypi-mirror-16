var math = {
  mean: function (data) {
    var sum = 0;
    for (let i = 0; i < data.length; i++) {
      sum += data[i];
    }
    return sum / data.length;
  },
  std: function (data) {
    var result = 0;
    var mean = math.mean(data);
    for (let i = 0; i < data.length; i++) {
      let d = data[i] - mean;
      result += d*d;
    }
    return Math.sqrt(result/data.length);
  }
};
