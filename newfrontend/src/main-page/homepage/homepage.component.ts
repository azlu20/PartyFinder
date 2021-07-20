import { Component, OnInit } from '@angular/core';
import { Observable, ObservedValueOf, of, throwError } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';
import { IUser } from '../user/iuser';
import { HttpClient, HttpHeaders, HttpErrorResponse } from "@angular/common/http";
import { ActivatedRoute, Router } from '@angular/router';
import { API_URL } from 'src/app/env';
import { UserService } from 'src/app/user.service';
import { GatheringService } from 'src/app/gathering.service';
import { IGathering } from '../gathering/igathering';
@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
  lat = 42.05624429682688;
  lng = -87.67500950992316;
  color = "white"
// @ts-ignore
  _user: IUser[];
//@ts-ignore
  _gathering: IGathering[];
  // @ts-ignore
  private userID: string | null;
  
  constructor(
    private userservice: UserService,
     private routerService : Router,
    private route: ActivatedRoute,
    private gatheringservice: GatheringService
    ) {
     }

  ngOnInit(): void {
    this.userID = this.route.snapshot.paramMap.get('id');
    this.userservice._getUsers(this.userID).subscribe({
      next: users => this._user = users
    }
    )
    this.gatheringservice._getGathering().subscribe({
      next: gatherings => this._gathering = gatherings
    })
   console.log(this._gathering) 
   console.log(this._user)
  }
}
