import React from 'react';
import ReactApexChart from 'react-apexcharts';

const TreeMap = (props) => {
  const { data } = props;

  const state = {
    treeVisibility: false,
    options: {
      tooltip: {
        enabled: true,
        theme: 'dark', //dark theme for the tooltip

        //custom tooltip
        custom: function ({ data, seriesIndex, dataPointIndex, w }) {
          var data = w.globals.initialSeries[seriesIndex].data[dataPointIndex];

          //returning the x value from the data array
          return (
            '<div style="width: 180px; height: 40px;text-align: center;margin-top: 25px;">' +
            data.x +
            '</div>'
          );
        },
      },

      plotOptions: {
        treemap: {
          distributed: true, //distributed multicolour treemap
        },
      },

      // colors: ['#05B8CC'],

      states: {
        hover: {
          filter: {
            type: 'darken', //Hovering boxes of the treemap with the dark theme
            value: 0.55,
          },
        },
      },
    },
  };

  return (
    <div>
      <ReactApexChart options={state.options} series={data} type="treemap" />
    </div>
  );
};
export default TreeMap;
