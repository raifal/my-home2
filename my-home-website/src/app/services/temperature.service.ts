import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { HttpErrorHandler, HandleError } from '../../http-error-handler.service';
import { Temperature } from './temperature';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    Authorization: 'my-auth-token'
  })
};

@Injectable({
  providedIn: 'root'
})
export class TemperatureService {
  url = 'https://ywpr9tv915.execute-api.eu-central-1.amazonaws.com/dev?date=2022-11-27';
  private handleError: HandleError;

  constructor(
    private http: HttpClient,
    httpErrorHandler: HttpErrorHandler) {
    this.handleError = httpErrorHandler.createHandleError('HeroesService');
  }

  getTemperatures(){

    //let httpHeaders = new HttpHeaders().set('x-api-key', 'ryhIUCkPWH4cwGUcUT1nR6RDH85Wo2lo7KRs4cd8');

    //return this.httpClient.get(this.url, { headers: httpHeaders });

  }
}