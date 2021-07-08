import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { UserComponent } from './user/user.component';


@NgModule({
  declarations: [UserComponent],
  imports: [
    CommonModule, RouterModule.forChild([])
  ]
})
export class MainPageModule { }
