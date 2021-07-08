import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { GatheringComponent } from './gathering/gathering.component';
import { HostComponent } from './host/host.component';



@NgModule({
  declarations: [
    GatheringComponent,
    HostComponent
  ],
  imports: [
    CommonModule
  ]
})
export class MainPageModule { }
