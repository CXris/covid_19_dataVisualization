// 2019-情感分析
(function () {
  // 1实例化对象
  var myChart = echarts.init(document.querySelector(".bar .chart"));
  // 2. 指定配置项和数据

  var yearData = [
    {
      year: "2019", // 年份
      data: [
        [
          0.7871376811594203, 0.7212894560107455, 0.731572723689397,
          0.7067238912732475, 0.6970654627539503, 0.7848438690022849,
        ],
      ],
    },
  ];

  var option = {
    // 通过这个color修改两条线的颜色
    color: ["#00f2f1"],
    tooltip: {
      trigger: "axis",
    },
    legend: {
      // 如果series 对象有name 值，则 legend可以不用写data
      // 修改图例组件 文字颜色
      textStyle: {
        color: "#4c9bfd",
      },
      // 这个10% 必须加引号
      right: "10%",
    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
      show: true, // 显示边框
      borderColor: "#012f4a", // 边框颜色
      containLabel: true, // 包含刻度文字在内
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: ["1月", "2月", "3月", "4月", "5月", "6月"],
      axisTick: {
        show: false, // 去除刻度线
      },
      axisLabel: {
        color: "#4c9bfd", // 文本颜色
      },
      axisLine: {
        show: false, // 去除轴线
      },
    },
    yAxis: {
      type: "value",
      min: 0.55,
      max: 0.8,
      axisTick: {
        show: false, // 去除刻度线
      },
      axisLabel: {
        color: "#4c9bfd", // 文本颜色
      },
      axisLine: {
        show: false, // 去除轴线
      },
      splitLine: {
        lineStyle: {
          color: "#012f4a", // 分割线颜色
        },
      },
    },
    series: [
      {
        name: "积极情绪占比",
        type: "line",
        // true 可以让我们的折线显示带有弧度
        // smooth: true,
        data: yearData[0].data[0],
      },
    ],
  };
  // 3. 把配置项给实例对象
  myChart.setOption(option);
  // 4. 让图表跟随屏幕自动的去适应
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 2020-情感分析
(function () {
  // 1实例化对象
  var myChart = echarts.init(document.querySelector(".line .chart"));

  // 2. 指定配置项和数据

  var yearData = [
    {
      year: "2020", // 年份
      data: [
        [
          0.6556089044085552, 0.5851638458768456, 0.624033731553057,
          0.6787925696594427, 0.6883293637291595, 0.7339576829691293,
        ],
      ],
    },
  ];

  var option = {
    // 通过这个color修改两条线的颜色
    color: ["#ed3f35"],
    tooltip: {
      trigger: "axis",
    },
    legend: {
      // 如果series 对象有name 值，则 legend可以不用写data
      // 修改图例组件 文字颜色
      textStyle: {
        color: "#4c9bfd",
      },
      // 这个10% 必须加引号
      right: "10%",
    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
      show: true, // 显示边框
      borderColor: "#012f4a", // 边框颜色
      containLabel: true, // 包含刻度文字在内
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: ["1月", "2月", "3月", "4月", "5月", "6月"],
      axisTick: {
        show: false, // 去除刻度线
      },
      axisLabel: {
        color: "#4c9bfd", // 文本颜色
      },
      axisLine: {
        show: false, // 去除轴线
      },
    },
    yAxis: {
      type: "value",
      min: 0.55,
      max: 0.8,
      axisTick: {
        show: false, // 去除刻度线
      },
      axisLabel: {
        color: "#4c9bfd", // 文本颜色
      },
      axisLine: {
        show: false, // 去除轴线
      },
      splitLine: {
        lineStyle: {
          color: "#012f4a", // 分割线颜色
        },
      },
    },
    series: [
      {
        name: "积极情绪占比",
        type: "line",
        // true 可以让我们的折线显示带有弧度
        // smooth: true,
        data: yearData[0].data[0],
      },
    ],
  };
  // 3. 把配置项给实例对象
  myChart.setOption(option);
  // 4. 让图表跟随屏幕自动的去适应
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 2021-情感分析
(function () {
  // 1实例化对象
  var myChart = echarts.init(document.querySelector(".pie .chart"));

  // 2. 指定配置项和数据

  var yearData = [
    {
      year: "2021", // 年份
      data: [
        [
          0.7076023391812866, 0.693411420204978, 0.6740117130307467,
          0.7111273792093704, 0.6515373352855052, 0.6814708691499523,
        ],
      ],
    },
  ];

  var option = {
    // 通过这个color修改两条线的颜色
    color: ["#ffff00"],
    tooltip: {
      trigger: "axis",
    },
    legend: {
      // 如果series 对象有name 值，则 legend可以不用写data
      // 修改图例组件 文字颜色
      textStyle: {
        color: "#4c9bfd",
      },
      // 这个10% 必须加引号
      right: "10%",
    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
      show: true, // 显示边框
      borderColor: "#012f4a", // 边框颜色
      containLabel: true, // 包含刻度文字在内
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: ["1月", "2月", "3月", "4月", "5月", "6月"],
      axisTick: {
        show: false, // 去除刻度线
      },
      axisLabel: {
        color: "#4c9bfd", // 文本颜色
      },
      axisLine: {
        show: false, // 去除轴线
      },
    },
    yAxis: {
      type: "value",
      min: 0.55,
      max: 0.8,
      axisTick: {
        show: false, // 去除刻度线
      },
      axisLabel: {
        color: "#4c9bfd", // 文本颜色
      },
      axisLine: {
        show: false, // 去除轴线
      },
      splitLine: {
        lineStyle: {
          color: "#012f4a", // 分割线颜色
        },
      },
    },
    series: [
      {
        name: "积极情绪占比",
        type: "line",
        // true 可以让我们的折线显示带有弧度
        // smooth: true,
        data: yearData[0].data[0],
      },
    ],
  };
  // 3. 把配置项给实例对象
  myChart.setOption(option);
  // 4. 让图表跟随屏幕自动的去适应
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 2019-评论分布
(function () {
  var myChart = echarts.init(document.querySelector(".bar2 .chart"));
  var option = {
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff",
    ],
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)",
    },
    legend: {
      bottom: "0%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "6",
      },
    },
    series: [
      {
        name: "评论分布",
        type: "pie",
        radius: ["10%", "70%"],
        center: ["50%", "50%"],
        roseType: "radius",
        // 图形的文字标签
        label: {
          fontSize: 10,
        },
        // 链接图形和文字的线条
        labelLine: {
          // length 链接图形的线条
          length: 6,
          // length2 链接文字的线条
          length2: 8,
        },
        data: [
          { value: 204, name: "学习状态" },
          { value: 601, name: "学习形式" },
          { value: 464, name: "课程种类" },
          { value: 4549, name: "学习意愿" },
          { value: 6130, name: "教育现状" },
          { value: 503, name: "等级考试" },
          { value: 55, name: "娱乐学习" },
        ],
      },
    ],
  };
  myChart.setOption(option);
  // 监听浏览器缩放，图表对象调用缩放resize函数
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 2020-评论分布
(function () {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".line2 .chart"));
  var option = {
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff",
    ],
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)",
    },
    legend: {
      bottom: "0%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "6",
      },
    },
    series: [
      {
        name: "评论分布",
        type: "pie",
        radius: ["10%", "70%"],
        center: ["50%", "50%"],
        roseType: "radius",
        // 图形的文字标签
        label: {
          fontSize: 10,
        },
        // 链接图形和文字的线条
        labelLine: {
          // length 链接图形的线条
          length: 6,
          // length2 链接文字的线条
          length2: 8,
        },
        data: [
          { value: 1027, name: "上课形式" },
          { value: 1075, name: "课业任务" },
          { value: 308, name: "等级考试" },
          { value: 665, name: "学习记录" },
          { value: 819, name: "教育现状" },
          { value: 1969, name: "学习计划" },
          { value: 9623, name: "网课感受" },
        ],
      },
    ],
  };
  myChart.setOption(option);
  // 监听浏览器缩放，图表对象调用缩放resize函数
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 2021-评论分布
(function () {
  var myChart = echarts.init(document.querySelector(".pie2 .chart"));
  var option = {
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff",
    ],
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)",
    },
    legend: {
      bottom: "0%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "6",
      },
    },
    series: [
      {
        name: "评论分布",
        type: "pie",
        radius: ["10%", "70%"],
        center: ["50%", "50%"],
        roseType: "radius",
        // 图形的文字标签
        label: {
          fontSize: 10,
        },
        // 链接图形和文字的线条
        labelLine: {
          // length 链接图形的线条
          length: 6,
          // length2 链接文字的线条
          length2: 8,
        },
        data: [
          { value: 2198, name: "学习意愿" },
          { value: 8223, name: "教育现状" },
          { value: 771, name: "上课形式" },
          { value: 4099, name: "网课感受" },
          { value: 495, name: "等级考试" },
          { value: 761, name: "考研学习" },
          { value: 264, name: "课业任务" },
        ],
      },
    ],
  };
  myChart.setOption(option);
  // 监听浏览器缩放，图表对象调用缩放resize函数
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 混合图表
(function () {
  var myChart = echarts.init(document.querySelector(".bar1 .chart"));
  var option = {
    color: ["#00f2f1", "#ed3f35", "#ffff00"],
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
        crossStyle: {
          color: "#4c9bfd",
        },
      },
    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
      show: true, // 显示边框
      borderColor: "#012f4a", // 边框颜色
      containLabel: true, // 包含刻度文字在内
    },
    legend: {
      data: [
        "2019年微博数量",
        "2020年微博数量",
        "2021年微博数量",
        "2019年情绪分析值",
        "2020年情绪分析值",
        "2021年情绪分析值",
      ],
      textStyle: {
        color: "#4c9bfd",
        fontSize: "6",
      },
    },
    xAxis: [
      {
        type: "category",
        axisTick: {
          show: false, // 去除刻度线
        },
        axisLabel: {
          color: "#4c9bfd", // 文本颜色
        },
        axisLine: {
          show: false, // 去除轴线
        },
        data: ["1月", "2月", "3月", "4月", "5月", "6月"],
        axisPointer: {
          type: "shadow",
        },
      },
    ],
    yAxis: [
      {
        type: "value",
        axisTick: {
          show: false, // 去除刻度线
        },
        axisLine: {
          show: false, // 去除轴线
        },
        min: 0,
        max: 250,
        interval: 50,
        axisLabel: {
          formatter: "{value} 条",
          color: "#4c9bfd", // 文本颜色
        },
      },
      {
        type: "value",
        axisTick: {
          show: false, // 去除刻度线
        },
        axisLine: {
          show: false, // 去除轴线
        },
        min: 0.5,
        max: 0.8,
        interval: 1,
        axisLabel: {
          formatter: "{value}",
          color: "#4c9bfd", // 文本颜色
        },
      },
    ],
    series: [
      {
        name: "2019年微博数量",
        type: "bar",
        data: [5, 2, 4, 8, 5, 8],
      },
      {
        name: "2020年微博数量",
        type: "bar",
        data: [6, 34, 259, 82, 41, 42],
      },
      {
        name: "2021年微博数量",
        type: "bar",
        data: [19, 22, 27, 24, 11, 9],
      },
      {
        name: "2019年情绪分析值",
        type: "line",
        yAxisIndex: 1,
        smooth: true,
        data: [
          0.7871376811594203, 0.7212894560107455, 0.731572723689397,
          0.7067238912732475, 0.6970654627539503, 0.7848438690022849,
        ],
      },
      {
        name: "2020年情绪分析值",
        type: "line",
        yAxisIndex: 1,
        smooth: true,
        data: [
          0.6556089044085552, 0.5851638458768456, 0.624033731553057,
          0.6787925696594427, 0.6883293637291595, 0.7339576829691293,
        ],
      },
      {
        name: "2021年情绪分析值",
        type: "line",
        yAxisIndex: 1,
        smooth: true,
        data: [
          0.7076023391812866, 0.693411420204978, 0.6740117130307467,
          0.6811273792093704, 0.6515373352855052, 0.6814708691499523,
        ],
      },
    ],
  };
  myChart.setOption(option);
  // 监听浏览器缩放，图表对象调用缩放resize函数
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 词云
(function () {
  // 基于准备好的dom，初始化echarts实例
  var myChart = echarts.init(document.querySelector(".ciyun"));

  // 指定图表的配置项和数据
  let colorList = [
    "#CF4645",
    "#B580B2",
    "#29008A",
    "#146A90",
    "#8956FF",
    "#70C9A8",
    "#bfbfbf",
    "#595959",
    "#40a9ff",
    "#1890ff",
    "#ffd666",
    "#ffc53d",
    "#ffc53d",
    "#ffc069",
    "#ffa940",
    "#fa8c16",
    "#eccbd9",
    "#ffadad",
    "#ff6392",
    "#ffc09f",
    "#ffcb77",
    "#ffe066",
    "#ffd53e",
    "#ffda3d",
    "#adf7b6",
    "#a0e8af",
    "#80ed99",
    "#07beb8",
    "#17c3b2",
    "#48cae4",
    "#97d2fb",
    "#83bcff",
    "#91e5f6",
    "#9381ff",
  ];
  let colorListLen = colorList.length;
  var tempList = [
    "学习 6288",
    "老师 5861",
    "考研 4600",
    "professor 4343",
    "打卡 4141",
    "英语 4030",
    "courses 3959",
    "lecture 3705",
    "时间 2972",
    "作业 2834",
    "课程 2766",
    "考试 2644",
    "学校 2497",
    "烘焙 2207",
    "单词 2155",
    "techniques 2021",
    "感觉 2018",
    "复习 2008",
    "笔记 1993",
    "初级 1927",
    "学生 1897",
    "喜欢 1890",
    "蛋糕 1875",
    "努力 1801",
    "希望 1794",
    "interesting 1764",
    "小时 1713",
    "数学 1688",
    "加油 1658",
    "教育 1656",
    "今日 1646",
    "孩子 1610",
    "生活 1568",
    "机构 1523",
    "教师 1513",
    "阅读 1477",
    "information 1476",
    "手机 1394",
    "会计 1388",
    "下午 1299",
    "政治 1273",
    "开学 1261",
    "直播 1257",
    "朋友 1255",
    "美食 1220",
    "上课 1218",
    "同学 1217",
    "发现 1192",
    "面试 1169",
  ];

  var wordsList = [];

  for (let i = 0; i < tempList.length; i++) {
    str = tempList[i];
    arr = str.split(" ");
    wordsList.push(arr);
  }

  var num = 0;

  for (let i = 0; i < wordsList.length; i++) {
    let temp;
    temp = wordsList[i][1] - 0;
    num = num + temp;
  }

  let canDraggable = true;

  var tempData = [];

  for (let i = 0; i < wordsList.length; i++) {
    let temp1 = {};
    let temp2 = {};
    temp1.name = wordsList[i][0];
    temp1.value = wordsList[i][1] - 0;
    temp1.draggable = canDraggable;

    temp2.color = colorList[Math.floor(Math.random() * colorListLen)];
    temp2.fontSize = ((wordsList[i][1] - 0) / num) * 1100;

    temp1.label = temp2;

    tempData.push(temp1);
  }

  var option = {
    color: [],
    toolbox: {
      show: true,
      feature: {
        // dataView: {readOnly: false},
        // magicType: {type: ['line', 'bar']},
        restore: {},
        saveAsImage: {},
      },
    },
    series: [
      {
        type: "graph",
        layout: "force",
        force: {
          repulsion: 65,
          edgeLength: 10,
        },
        // roam: "scale",
        label: {
          show: true,
          color: "auto",
          fontSize: 14,
        },
      },
    ],
  };
  option.series[0].data = tempData;
  // 使用刚指定的配置项和数据显示图表。
  myChart.setOption(option);

  // 监听浏览器缩放，图表对象调用缩放resize函数
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();
