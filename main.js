// YOUR JAVASCRIPT CODE FOR INDEX.HTML GOES HERE
// sidebar toggle

var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");

function openSidebar(){
    if(!sidebarOpen){
        sidebar.classList.add("sidebar-responsive");
        sidebarOpen = true;
    }
}

function closeSidebar(){
    if(sidebarOpen){
        sidebar.classList.remove("sidebar-responsive");
        sidebarOpen = false;
    }
}


//--------Charts-------

//bar chart

 
      
var barChartOptions = {
    series: [{
    data: [10, 15,4,6,3]
  }],
    chart: {
    type: 'bar',
    height: 350,
    toolbar:{
        show:false
    },
  },
  colors:[
      "#246dec",
      "#cc3c43",
      "#367952",
      "#f5b74f",
      "#4f35a1",

  ],
  plotOptions: {
    bar: {
      distributed: true,
      borderRadius: 4,
      horizontal: false,
      columnWidth:'40%',
    }
  },
  dataLabels: {
    enabled: false
  },
  legend:{
     show:false
  },
  xaxis: {
    categories: ['South Korea', 'Canada', 'United Kingdom',  'Italy', 'France' ],
  },
  yaxis:{
    title:{
        text: "Count"
    }
  }
  };

  var barChart = new ApexCharts(document.querySelector("#bar-chart"), barChartOptions);
  barChart.render();

  //area chart
  var areaChartOptions = {
    series: [{
    name: 'purchase Orders',
    data: [44, 55, 31, 47, 31, 43, 26]
  }, {
    name: 'Sales Orders',
    data: [55, 69, 45, 61, 43, 54, 37]
  }],
    chart: {
    height: 350,
    type: 'area',
    toolbar:{
        show: false,
    },
  },
  colors:["#4f35a1","#246dec"],
  dataLabels:{
    enabled:false,
  },
  stroke: {
    curve: 'smooth'
  },
  labels: ['jan','feb','mar','apl','aug','oct','sep'],
  markers:{
    size: 0
  },
  yaxis: [
    {
      title: {
        text: 'Purchase orders',
      },
    },
    {
      opposite: true,
      title: {
        text: 'Sales Orders',
      },
    },
  ],
  tooltip: {
    shared: true,
    intersect: false,
  }
  };

  var areaChart = new ApexCharts(document.querySelector("#area-chart"), areaChartOptions);
  areaChart.render();
