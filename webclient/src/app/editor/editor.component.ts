import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent implements OnInit {
  textCode:string = "var j = 7; \n var l = 14;"
  constructor() { }

  ngOnInit() {
  }

}
