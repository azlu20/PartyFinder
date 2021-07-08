import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';


import { AppComponent } from './app.component';
import { GuesthomeComponent } from './guesthome/guesthome.component';
import { LoginComponent } from './login/login.component';
import { UserComponent } from './user/user.component';

@NgModule({
  declarations: [
    AppComponent, GuesthomeComponent, LoginComponent, UserComponent
  ],
  imports: [
    BrowserModule, RouterModule.forRoot([
      {path: "guesthome", component: GuesthomeComponent},
      {path: "login", component: LoginComponent},
       {path: '**', redirectTo: 'guesthome', pathMatch: 'full'},
       
      
      ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
