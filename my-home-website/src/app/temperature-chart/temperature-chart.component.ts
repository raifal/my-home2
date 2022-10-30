import { Component, OnInit } from "@angular/core";
import { BarChart } from "echarts/charts";
import { EChartsOption } from 'echarts';
import { TemperatureService } from '../services/temperature.service';

@Component({
  selector: 'app-temperature-chart',
  templateUrl: './temperature-chart.component.html',
  styleUrls: ['./temperature-chart.component.scss']
})
export class TemperatureChartComponent implements OnInit {
  echartsOptions: EChartsOption = {};

  constructor(private temperatureService: TemperatureService) { }

  posts: any;

  ngOnInit(): void {
    this.temperatureService.getTemperatures()
      .subscribe(response => {
        this.posts = response;
      });


    this.echartsOptions = {
      legend: {},
      tooltip: {
        trigger: 'axis',
      },
      dataset: {
        source: [
          ['2018-04-10T19:40:33', 10, 5],
          ['2018-04-10T20:40:53', 20, 3],
          ['2018-04-10T21:41:03', 40, 2],
          ['2018-04-10T22:42:03', 25, 4],
          ['2018-04-10T23:43:03', 35, 3]
        ],
        dimensions: ['timestamp', 'sensor1', 'sensor2'],
      },
      xAxis: { type: 'time' },
      yAxis: { name: '°C' },
      series: [
        {
          name: 'sensor1',
          type: 'line',
          encode: {
            x: 'timestamp',
            y: 'sensor1' // refer sensor 1 value 
          }
        }, {
          name: 'sensor2',
          type: 'line',
          encode: {
            x: 'timestamp',
            y: 'sensor2'
          }
        }]
    };
  }
}