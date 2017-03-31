import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'PasteCode';
  menu = [
    {name: 'Editor', route: '/editor'},
    {name: 'Home', route: '/'}
  ];
}
