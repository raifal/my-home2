import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NgxEchartsModule } from 'ngx-echarts';

import { AppComponent } from './app.component';
import { TemperatureChartComponent } from './temperature-chart/temperature-chart.component';

import { HttpClientModule } from '@angular/common/http';
import { HttpErrorHandler } from './http-error-handler.service';

@NgModule({
  declarations: [
    AppComponent,
    TemperatureChartComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    NgxEchartsModule.forRoot({
      echarts: () => import('echarts')
    })
  ],
  providers: [HttpErrorHandler],
  bootstrap: [AppComponent]
})
export class AppModule { }
