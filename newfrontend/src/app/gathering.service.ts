import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { IGathering } from 'src/main-page/gathering/igathering';
import { API_URL } from './env';

@Injectable({
  providedIn: 'root'
})
export class GatheringService {

  //@ts-ignore
  _gathering: IGathering[];
  constructor(private http: HttpClient) { }
  _getGathering() : Observable<IGathering[]>{

    return this.http.get<IGathering[]>(`${API_URL}/gathering/0`).pipe(
      tap(data => this._gathering = data),
      catchError(err => this.handleError(err))
    )
  }
  private handleError(error: Error) : Observable<any>{
    const errorMessage = 'An Error has occured';
    return throwError(errorMessage);

  }
}
