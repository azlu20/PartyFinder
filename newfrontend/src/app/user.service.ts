import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { IUser } from 'src/main-page/user/iuser';
import { API_URL } from './env';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  //@ts-ignore
  _user: IUser[];
  constructor(private http: HttpClient,
) { }
   _getUsers(userID: string | null) : Observable<IUser[]>{

    return this.http.get<IUser[]>(`${API_URL}/user/${userID}`).pipe(
      tap(data => this._user = data),
      catchError(err => this.handleError(err))
    )
  }
  private handleError(error: Error) : Observable<any>{
    const errorMessage = 'An Error has occured';
    return throwError(errorMessage);

  }
}
