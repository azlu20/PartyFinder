import { Component, Host, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-gathering',
  templateUrl: './gathering.component.html',
  styleUrls: ['./gathering.component.css']
})
export class GatheringComponent implements OnInit {
  @Input() hostdetails: Host | undefined;
  constructor() { }

  ngOnInit(): void {
  }

}
