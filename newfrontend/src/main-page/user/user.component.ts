import { Component, Input, OnInit } from '@angular/core';
import { User } from './user';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit, User {

  constructor() { }
  userID: string | undefined;
  firstName: string | undefined;
  lastName: string | undefined;
  location: string | undefined;
  age: number | undefined;
  gender: string | undefined;
  phonenumber: number | undefined;
  partyFiendRating: number | undefined;

  ngOnInit(): void {
  }

}
