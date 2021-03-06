import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { UserComponent } from './user/user.component';
import { HomepageComponent } from './homepage/homepage.component';
import { HttpClientModule } from '@angular/common/http';
import {AgmCoreModule} from '@agm/core'


@NgModule({
  declarations: [UserComponent, HomepageComponent],
  imports: [
    CommonModule, RouterModule.forChild([{
      path:'user/:id', 
      component: HomepageComponent
  }]), HttpClientModule, AgmCoreModule
  ]
})
export class MainPageModule { }
