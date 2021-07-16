import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { MainPageModule } from 'src/main-page/main-page.module';


import { AppComponent } from './app.component';
import { GuesthomeComponent } from './guesthome/guesthome.component';
import { LoginComponent } from './login/login.component';
import { UserComponent } from '../main-page/user/user.component';
import { AgmCoreModule } from '@agm/core';
@NgModule({
  declarations: [
    AppComponent, GuesthomeComponent, LoginComponent
  ],
  imports: [
    BrowserModule, RouterModule.forRoot([
      {path: "guesthome", component: GuesthomeComponent},
      {path: "login", component: LoginComponent},
       {path: '**', redirectTo: 'guesthome', pathMatch: 'full'},
       {path: '', redirectTo: 'guesthome', pathMatch: 'full'}
      
      ]),
      MainPageModule,
      AgmCoreModule.forRoot({
        apiKey : 'AIzaSyB3p5nEkv0cxmNDp2uiOfN8V7VXjwWHhDw'
      }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
