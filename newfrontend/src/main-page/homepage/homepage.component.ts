import { Component, OnInit } from '@angular/core';
import { Observable, ObservedValueOf, throwError } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';
import { IUser } from '../user/iuser';
import { HttpClient, HttpHeaders, HttpErrorResponse } from "@angular/common/http";
import { ActivatedRoute, Router } from '@angular/router';
import { API_URL } from 'src/app/env';
@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
// @ts-ignore
  _user: IUser[];
  // @ts-ignore
  private userID: string | null;
  
  constructor(private http: HttpClient,
     private routerService : Router,
     private route: ActivatedRoute,
    ) { }

  ngOnInit(): void {
    this.userID = this.route.snapshot.paramMap.get('id');
    this._getUsers().subscribe({
      next: users => this._user = users
    }
    )
    
  }
  
  private _getUsers() : Observable<IUser[]>{

    return this.http.get<IUser[]>(`${API_URL}/user/${this.userID}`).pipe(
      tap(data => this._user = data),
      catchError(err => this.handleError(err))
    )
  }
  private handleError(error: Error) : Observable<any>{
    const errorMessage = 'An Error has occured';
    return throwError(errorMessage);

  }
}
